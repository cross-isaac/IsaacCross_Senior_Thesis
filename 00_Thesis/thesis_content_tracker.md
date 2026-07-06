# Thesis Content Tracker
**Isaac Cross — Odom Lab, Northwestern University**
**Last updated: April 2026**

---

## CONFIRMED CONTENT (include for sure)

### Physics Background
- BSM physics, matter-antimatter asymmetry, CP violation
- EDM searches and sensitivity scaling (σ ∝ 1/T₂*√N)
- Doped cryogenic noble gas crystals as a platform; comparison to beams/traps
- Prior work: Cs/He, Rb/Ne, Rb/parahydrogen T₂* values
- Coherence times: T₁, T₂, T₂* hierarchy; sources of inhomogeneous broadening
- Argon as host: isotope structure, optical transparency, van der Waals bonding
- Rb as dopant: hyperfine structure, D₂ line, electron spin
- Single crystal vs. polycrystalline; trapping site inhomogeneity argument

### Effusive Beam Theory
- Maxwell-Boltzmann distribution; effusive flux formula
- Knudsen number and flow regimes (molecular, transitional, viscous)
- Capillary collimation: geometric half-angle from aspect ratio
- Molecular flow conductance per capillary
- Dual-species beam: why Rb divergence upper-bounds Ar divergence
- Mean free path of Rb in Ar background

### Crystal Growth Chamber (context/constraints, not Isaac's primary work)
- Bridgman-Stockbarger method for single-crystal Ar seeds
- Dual-chamber design (IVC, outer jacket); cryogenic constraints
- X-ray compatibility: PEEK IVC, Kapton windows, APS 28-ID beamline
- Optical access requirements
- Space constraints → collimation requirements (~0.5 m nozzle to substrate)
- Growth rate, dopant density, substrate temperature as key parameters

### Beam Source Design
- 231-microcapillary nozzle, 100 µm ID, ~0.3 in length, triangular CF flange
- Original design from Sawaoka et al.; modifications for dual-species
- Nichrome-mica heater design (originated at Kovachy lab for Sr cell)
- Temperature sensors; thermal isolation stages
- Achieved ~400°C sustained in UHV; week-long bake without clogging
- Ar gas handling system; flow controller; steady-state flux assumption
- UHV chamber: base pressure 7.5×10⁻¹⁰ Torr
- Beam pipe; copper heat shield; two interrogation zones + translation stages
- EDM machining at NU machine shop for nozzle fabrication

### 780 nm Optical System (deserves substantial section/possibly own chapter)
- ECDL recommissioning (Toptica DL Pro)
- Full optics chain: Faraday isolator, mode shaper, collimation, PBS,
  PM single-mode fiber coupling, reference Rb cell
- Beam profiling: software to image 780 beam, verify Gaussian profile,
  measure beam waist
- Saturation intensity characterization
- Early 780 beam divergence measurement (lower precision; useful for
  future lab members even if not state-of-the-art)
- FM spectroscopy setup; balanced photodetection

### Signal Conditioning Circuit
- RC high-pass filter: R=1MΩ, C=10nF, fc≈15.9 Hz
- Non-inverting op-amp amplifier: Rf=100kΩ, Rg=1.5kΩ, G≈67.7×
- Why degree-2 polynomial baseline: filter-induced curvature on triangle wave
- Signal levels: ~1V DC offset, ~5mV ramp, ~0.4mV absorption dip at center

### Characterization Methods
- Absorption spectroscopy pipeline (master_document.ipynb)
- Lorentzian fitting; degree-2 baseline subtraction
- Two divergence measurement methods (Method A vs. Method B); why B is preferred
- Method B result: α₁/ₑ = 0.48 ± 0.1° (pure Rb, two-zone)
- Method A result: ~0.74–1.0° (inflated; Rb-Ar beam, single zone)
- Capture efficiency ~68% at growth substrate
- Rb flux ~1.78×10¹⁰ atoms/s; Ar flux ~5×10¹⁵ atoms/s
- Vertical translation stages for PD and probe beam (periscope setup)

### Procedures (for future lab members)
- Toptica laser operating procedure
- Rb loading procedure
- Microcapillary loading/placement into nozzle/CF flange
- Opening chamber with Rb still inside; Ar backfilling
- General UHV baking and cleaning procedures
- Vacuum cleaning procedures

### Broadening Simulation
- Monte Carlo model of magnetic dipole-dipole interactions
- Poisson-distributed neighbors; uniform positions in cell
- Lorentzian fit to Δν distribution → T₂*
- Results: spin-spin subdominant below ~10¹⁸ atoms/cm³ for Rb
- Comparison to K-39, Rb-85/87, Cs-133, Na-23 experimental data
- Conclusion: crystal quality is dominant bottleneck at lab-relevant densities

---

## THINGS TRIED / MOVED AWAY FROM (include with honest discussion)
- **Fiber coupling:** attempted, challenges encountered — document what
  was tried and why moved away or what issues arose
- **Beam expanding:** attempted — note approach and outcome
- **Lock-in amplification:** tried as alternative to filter-amplifier
  circuit — note why the filter-amplifier approach was chosen instead

---

## THINGS IN PROGRESS (include results when available)
- Two-zone divergence measurement for Rb-Ar beam (in progress)
- Crystal growth run with beam source connected to growth chamber
  (coming weeks-months); growth rate as Ar flux cross-check

---

## THINGS NOT INCLUDED
- Beam velocity measurement (not planned before thesis submission)
- Crystal growth chamber detailed design (PhD student Daniel Lutes' work;
  mention constraints only)

---

## APPENDICES PLANNED
- A: Rb spectroscopy reference data (Steck)
- B: Signal conditioning circuit schematic and analysis
- C: Python analysis pipeline documentation (master_document.ipynb)
- D: Monte Carlo simulation details and parameter tables

---

## OPEN QUESTIONS / THINGS STILL BEING WORKED OUT
- Two-zone divergence for Rb-Ar beam
- Exact Ar oven pressure (currently estimated from flow rate + conductance;
  uncertain whether fully in molecular or transitional regime)
- Reconciling Method A vs. Method B divergence numbers fully
- Ar flux: flow-rate estimate (~5×10¹⁵/s) vs. pressure-based estimate
  (tension; flow rate is more reliable)
