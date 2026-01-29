# EMG Bioamplifier

Engineered differential amplifier circuit for real-time EMG acquisition. Developed Python signal-processing pipeline (filtering, feature extraction, statistical analysis) with AI assistance (Perplexity); independently designed architecture, integrated components, and validated outputs. Demonstrated competency in hardware design, signal processing workflows, and real-time data systems.

## why i'm doing this

**Goal:** Start building hands-on projects in order to understand the theory differently, more in-depth. I will understand motor unit recruitment by measuring electromyographic signals across three muscle states (rest, light contraction, maximal effort).

**why:** EMG amplitude scales with muscle force through motor unit recruitment—early contractions recruit slow-twitch fibers (low force), maximal effort recruits fast-twitch fibers (high force). This project tests whether a low-cost bioamplifier can detect this 3-10× signal increase.

**scientific value:** Validates that Arduino + op-amp bioamplification is sufficient for muscle activation studies, making EMG accessible for biomechanics research without expensive clinical equipment.

## Current Status
- ✅ Arduino data acquisition functional 
- 🟠 Python analysis pipeline working - except one dataset 
- ⚠️ **V1.0 beta:** Hardware to be improved; Rest/Gentle ratio only 1.009× (target: >3×)

## Methods

### Hardware
- **Microcontroller:** Arduino Uno (10-bit ADC, 100 Hz sampling @ 10ms intervals)
- **Amplifier:** LM324 non-inverting configuration (R_feedback = 100kΩ, R_input = 1MΩ, Gain = 1.1×)
- **Electrodes:** Bipolar Ag/AgCl surface electrodes on flexor carpi radialis
- **Reference:** Bony prominence (wrist)
- **ADC range:** 0-1023 counts → 0-5V output

### Data Acquisition
1. Record 20 seconds per condition (rest, gentle flex, strong flex)
2. Serial transmission at 115200 baud to computer
3. Save as CSV: timestamp (implied) + ADC count

### Analysis
- **RMS amplitude:** $\sqrt{\frac{1}{N}\sum_{i=1}^{N} x_i^2}$ on 0-5V converted signal
- **Frequency spectrum:** FFT to identify dominant muscle activation frequencies (expected: 20-150 Hz)
- **Signal comparison:** RMS ratio (Gentle/Rest, Strong/Rest) to quantify recruitment

### Why These Methods
- **RMS over raw amplitude:** Better captures EMG energy since signals are biphasic (positive + negative)
- **ADC conversion:** Arduino reads 0-1023; multiply by 5V/1023 to get meaningful voltage for comparison to literature
- **30-second trials:** Long enough for statistical stability, short enough to avoid fatigue artifact
- **FFT analysis:** Confirms signal is in expected EMG bandwidth (20-500 Hz); detects 50Hz line noise

## Current Results

| Condition | RMS (V) | Mean (V) | Max (V) | Samples |
|-----------|---------|---------|---------|---------|
| Rest      | 1.909   | 1.441   | 4.194   | 2300    |
| Gentle    | 1.920   | 1.404   | 4.174   | 2300    |
| Strong    | —       | —       | —       | —       |

**Gentle/Rest ratio:** 1.009× ❌ (Expected: 3-10×)

**Interpretation:** Signals are nearly identical. This indicates **hardware saturation**, not measurement failure. The ~1.9V baseline is from DC offset (electrode polarization + op-amp offset) rather than muscle signal. The ~0.5V EMG signal is swamped and invisible.

## Known Issues & Next Steps

### Issue: 

Seems to be missing AC coupling capacitor + insufficient gain (1.1×) + the electrodes didnot seem to work well. 
I will review the theory to come up with solutions for the hardware, get better electrodes and the python code.
In parallel, I will get better pictures next time I work on the circuit, do a drawing of the circuit (ASCII schematic example), expand on argument. Review and improve methods, analysis.

### Timeline
Review theory and new concepts.
Work on python code.
After circuit modifications:
- Recollect 3× rest, 3× gentle, 3× strong trials
- Expected result: Gentle/Rest = 3-5×, Strong/Rest = 8-15×
- Ready for publication + PhD applications

## Files
- `analyze_emg.py` – Python analysis (RMS, FFT, visualization)
- `rest.csv`, `gentle.csv`, `strong.csv` – Current raw ADC data (0-1023 counts)
- `emg_analysis.png` – 4-panel output (raw signals, RMS bar chart, FFT spectrum, statistics table)
- `requirements.txt` – Python dependencies

## Quick Start
```bash
pip install -r requirements.txt
python analyze_emg.py
```

Outputs: `emg_analysis.png` + `emg_analysis_results.csv`

## References
- **Neuroscience:** Enoka, R. (2015). Neuromechanics of Human Movement.
- **EMG Standards:** SENIAM guidelines (http://www.seniam.org/)
- **Bioamplifier Design:** Merletti & Farina (2016). Surface Electromyography.
- **HTM Workshop https://www.youtube.com/@HTMWorkshop**
- **Perplexity AI**
