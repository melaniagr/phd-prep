# Computational Neuroscience – Synapses, Neurons & Brains

8‑week course notes covering neuron doctrine, biophysics, synapses, plasticity, dendrites, brain simulation projects and perception.

Handwritten notes on folder, here summary / synthesis:

## Neurons & doctrine

- Neuron doctrine (Cajal 1887): nervous system made of discrete cells; dynamic polarization – dendrites input, axons output.
- Neuron types: principal (excitatory, projecting) vs interneurons (inhibitory, local); classified by anatomy, function, spiking, chemistry, genes; ~100 billion neurons.
- Axon features: myelin (oligodendrocytes central, Schwann peripheral), nodes of Ranvier, axon initial segment (AIS) as spike initiation zone.
- Dendrites: diverse morphologies (e.g. Purkinje flat, pyramidal spiny); spines (~10k/cell) as main synapse sites.

## Biophysics & PSPs

- Passive neuron as RC circuit: \(\tau_m = RC \approx 20\) ms (temporal summation); \(V(t) = IR(1 - e^{-t/\tau})\).
- PSP equation: \(0 = C \frac{dV}{dt} + g_r(V - E_r) + g_s(V - E_s)\); steady state \(V = \frac{g_r E_r + g_s E_s}{g_r + g_s}\).
- EPSP (excitatory, e.g. Na⁺ battery ~0 mV) vs IPSP (inhibitory, e.g. Cl⁻ ~‑70 mV).

## Action potentials (Hodgkin‑Huxley)

- All‑or‑none spikes via voltage clamp experiments (space/voltage clamp).
- Currents: fast inward Na⁺ (blocked by TTX), slow outward K⁺ (TEA); leak.
- HH model: \(I = C \frac{dV}{dt} + g_{Na} m^3 h (V - E_{Na}) + g_K n^4 (V - E_K) + g_L (V - E_L)\).
- Gating: \(g_n = \bar{g}_n \cdot n^k\) (time/V‑dependent, 0–1 open probability); explains refractory period.

## Dendritic computation & cable theory

- Brain as computer: encode/decode info; regions with specific roles (e.g. Hubel–Wiesel V1 orientation selectivity).
- Cable theory (Rall): dendrites as non‑isopotential cables; axial/membrane currents; \(\lambda = \sqrt{r_m / r_i}\).
- Distal synapses broader/delayed; enables local computation (e.g. directional selectivity via dendrite geometry).
- M&P point neuron (1943): logical gates via E/I inputs.

## Plasticity & learning

- Hebb: “fire together, wire together”; STDP – LTP (pre before post), LTD (post before pre).
- Structural: activity drives spine formation (learning/enriched env); neurogenesis (hippocampus, e.g. taxi drivers).

## Brain projects & frontiers

- BMI (deep brain stim for Parkinson, closed‑loop).
- Optogenetics (light‑gated channels), connectomics (EM 3D), Brainbow staining.
- Projects: Allen Brain Atlas, Janelia, Human Brain Project (Markram), Blue Brain (1 mm² = 30k cells).
- Clay Reid columns; Hodgkin–Huxley extensions for cell types.

## Perception

- Sensation → neural activity → perception (Marr).
- Audition: hair cells → basilar membrane motion → mechano‑sensitive channels (cochlea, Helmholtz tonotopy).
- Plasticity: barn owl prism shifts map axons.

