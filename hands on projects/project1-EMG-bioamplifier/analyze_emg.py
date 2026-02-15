import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import pandas as pd
import os

# ============================================================================
# EMG SIGNAL ANALYSIS SCRIPT - WITH DEBUG OUTPUT
# ============================================================================

SAMPLING_RATE = 100  # Hz
CSV_FILES = {
    'rest': 'rest.csv',
    'gentle': 'gentle.csv',
    'strong': 'strong.csv'
}

# ============================================================================
# 1. DEBUG: CHECK IF FILES EXIST
# ============================================================================
print("Checking for files...")
for condition, filename in CSV_FILES.items():
    exists = os.path.exists(filename)
    print(f"  {'✓' if exists else '✗'} {filename}")

# ============================================================================
# 2. LOAD DATA - CONVERTS ADC (0-1023) TO VOLTAGE (0-5V)
# ============================================================================
def load_emg_data(filename):
    """Load CSV, convert strings to numbers, then ADC to voltage"""
    try:
        df = pd.read_csv(filename)
        voltage_col = df.columns[0]
        
        # Convert strings to numbers, drop any NaN
        signal = pd.to_numeric(df[voltage_col], errors='coerce').dropna().values.astype(float)
        
        # Convert ADC (0-1023) to voltage (0-5V)
        signal = signal * (5.0 / 1023.0)
        
        print(f"✓ Loaded {filename}: {len(signal)} samples")
        return signal
    except FileNotFoundError:
        print(f"✗ File not found: {filename}")
        return None
    except Exception as e:
        print(f"✗ Error loading {filename}: {e}")
        return None

print("\nLoading EMG data...")
data = {}
for condition, filename in CSV_FILES.items():
    data[condition] = load_emg_data(filename)

# Check which files loaded
missing = [k for k, v in data.items() if v is None]
if missing:
    print(f"\n⚠️  Missing: {missing}")

# ============================================================================
# 3. CALCULATE STATISTICS
# ============================================================================
def calculate_stats(signal):
    """Calculate RMS, mean, max, min, std dev"""
    if signal is None or len(signal) == 0:
        return None
    rms = np.sqrt(np.mean(signal**2))
    return {
        'RMS': rms,
        'Mean': np.mean(signal),
        'Max': np.max(signal),
        'Min': np.min(signal),
        'Std Dev': np.std(signal)
    }

print("\n" + "="*60)
print("STATISTICS")
print("="*60)

stats = {}
for condition in ['rest', 'gentle', 'strong']:
    stats[condition] = calculate_stats(data[condition])
    if stats[condition]:
        print(f"\n{condition.upper()}:")
        for key, value in stats[condition].items():
            print(f"  {key:12s}: {value:.4f} V")
    else:
        print(f"\n{condition.upper()}: NO DATA")

# ============================================================================
# 4. CREATE FIGURE WITH 4 SUBPLOTS
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('EMG Signal Analysis: Rest vs Gentle Flex vs Strong Flex', 
             fontsize=16, fontweight='bold', y=0.995)

# Plot 1: Raw signals (time domain)
ax = axes[0, 0]
time_rest = np.arange(len(data['rest'])) / SAMPLING_RATE if data['rest'] is not None else []
time_gentle = np.arange(len(data['gentle'])) / SAMPLING_RATE if data['gentle'] is not None else []
time_strong = np.arange(len(data['strong'])) / SAMPLING_RATE if data['strong'] is not None else []

if data['rest'] is not None:
    ax.plot(time_rest, data['rest'], label='Rest', linewidth=0.8, alpha=0.8)
if data['gentle'] is not None:
    ax.plot(time_gentle, data['gentle'], label='Gentle Flex', linewidth=0.8, alpha=0.8)
if data['strong'] is not None:
    ax.plot(time_strong, data['strong'], label='Strong Flex', linewidth=0.8, alpha=0.8)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_title('Raw EMG Signals (Time Domain)')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 2: RMS Amplitude Comparison (Bar chart)
ax = axes[0, 1]
conditions = []
rms_values = []
for condition in ['rest', 'gentle', 'strong']:
    if stats[condition]:
        conditions.append(condition.capitalize())
        rms_values.append(stats[condition]['RMS'])

colors = ['#32b8c6', '#e68161', '#c01537']
ax.bar(conditions, rms_values, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
ax.set_ylabel('RMS Amplitude (V)')
ax.set_title('RMS Amplitude Comparison')
ax.grid(True, alpha=0.3, axis='y')

for i, v in enumerate(rms_values):
    ax.text(i, v + 0.05, f'{v:.3f}V', ha='center', va='bottom', fontweight='bold')

# Plot 3: FFT Frequency Spectrum
ax = axes[1, 0]
if data['strong'] is not None and len(data['strong']) > 0:
    signal = data['strong']
    N = len(signal)
    freqs = fftfreq(N, 1/SAMPLING_RATE)[:N//2]
    fft_vals = np.abs(fft(signal))[:N//2]
    
    ax.semilogy(freqs, fft_vals, linewidth=1, color='#208080')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Magnitude')
    ax.set_title('Frequency Spectrum (Strong Flex, FFT)')
    ax.set_xlim([0, 50])
    ax.grid(True, alpha=0.3)
    ax.axvline(x=50, color='red', linestyle='--', alpha=0.5, label='50 Hz (line noise)')
    ax.legend()

# Plot 4: Statistics Table
ax = axes[1, 1]
ax.axis('tight')
ax.axis('off')

table_data = []
table_data.append(['Metric', 'Rest', 'Gentle', 'Strong'])

metrics = ['RMS', 'Mean', 'Max', 'Min', 'Std Dev']
for metric in metrics:
    row = [metric]
    for condition in ['rest', 'gentle', 'strong']:
        if stats[condition]:
            row.append(f"{stats[condition][metric]:.4f}")
        else:
            row.append("—")
    table_data.append(row)

table = ax.table(cellText=table_data, cellLoc='center', loc='center',
                colWidths=[0.15, 0.25, 0.25, 0.25])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

for i in range(4):
    table[(0, i)].set_facecolor('#208080')
    table[(0, i)].set_text_props(weight='bold', color='white')

for i in range(1, len(table_data)):
    for j in range(4):
        if i % 2 == 0:
            table[(i, j)].set_facecolor('#f0f0f0')

plt.tight_layout()

# Save figure
plt.savefig('emg_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Figure saved as 'emg_analysis.png'")

plt.show()

# ============================================================================
# 5. EXPORT RESULTS TO CSV
# ============================================================================
results_df = pd.DataFrame(stats).T
results_df.to_csv('emg_analysis_results.csv')
print("✓ Results saved as 'emg_analysis_results.csv'")

print("\n" + "="*60)
print("ANALYSIS COMPLETE")
print("="*60)
if stats['rest'] and stats['rest']['RMS'] > 0:
    print(f"Rest RMS: {stats['rest']['RMS']:.3f}V (baseline)")
if stats['gentle'] and stats['gentle']['RMS'] > 0:
    print(f"Gentle/Rest ratio: {stats['gentle']['RMS']/stats['rest']['RMS']:.1f}x")
if stats['strong'] and stats['strong']['RMS'] > 0:
    print(f"Strong/Rest ratio: {stats['strong']['RMS']/stats['rest']['RMS']:.1f}x")
print("\nExpected results:")
print("  Rest RMS:    ~0.1–0.2V")
print("  Gentle RMS:  ~0.5V")
print("  Strong RMS:  ~1–2V")
print("  Ratio: 3–10x amplitude increase from rest to max flex")
