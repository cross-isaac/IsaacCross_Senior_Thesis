# Isaac Cross — Senior Honors Thesis (Physics, Northwestern University, 2026)

**"A Tunable Dual-Species Rubidium-Argon Beam Source for Controlled Doped Cryogenic Crystal Growth"**
Advisor: Prof. Brian C. Odom (Odom Lab)

This repository contains all source material for the thesis: the document itself, the
reference library, design calculations and CAD, raw and analyzed characterization data,
simulation code, figures, and related talks/proposals.

## Project in one paragraph

Doped cryogenic noble-gas crystals are a promising precision-measurement platform
(~10^16 dopants/cm^3 interrogated simultaneously, potential eEDM sensitivity), but their
ensemble coherence time T2* (~10–100 µs) is 10^3–10^4 times shorter than the homogeneous
T2 (~0.1 s). To enable systematic studies of how growth conditions affect crystal quality
and coherence, this thesis (1) develops and characterizes a tunable dual-species Rb-Ar
effusive beam source built around a 231-microcapillary nozzle array (ID 100 µm, L 7.62 mm)
with independent Rb and Ar flux control, characterized via 780 nm absorption spectroscopy
of the 85Rb D2 line (θ½ ≈ 1.4 ± 0.6°, Rb flux ~2.5–3×10^10 atoms/s, capture efficiency
23–41%, inferred dopant density ~10^17 cm^-3, ~2 µm/hr growth); and (2) presents a Monte
Carlo simulation of dipole-dipole inhomogeneous broadening showing dipolar interactions
are ~100× too weak to explain observed linewidths at typical densities — implicating
structural disorder as the dominant decoherence mechanism — and that ρ ~ 10^15 cm^-3
would suffice for millisecond dipolar-limited T2* in improved crystals.

## Repository structure

| Folder | Contents |
|---|---|
| `00_Thesis` | Final thesis PDF, LaTeX source archive, content tracker |
| `01_References` | All papers, textbooks, theses, datasheets, and equipment manuals |
| `02_Beam_Source_Design` | Design calculations (Mathematica) and all CAD (nozzle, oven, chambers) — thesis Ch. 3 |
| `03_Heaters_and_Monitoring` | Nichrome heater test data + ESP32 temperature logger — thesis Sec. 3.5 |
| `04_Beam_Characterization` | 780 nm probe system, raw absorption data, analysis code, results — thesis Ch. 4–5 |
| `05_Broadening_Simulation` | Dipole-dipole Monte Carlo simulation — thesis Ch. 6 |
| `06_Figures_and_Media` | Thesis figures (by chapter), lab photos/videos, Blender renders |
| `07_Talks_and_Posters` | Conference posters and talk slides |
| `08_Proposals_and_Applications` | Research grants, GRFP, grad-school applications, CV |
| `09_Kovachy_Lab` | Prior training work in the Kovachy lab (heaters, MOT CAD) — predates this project |
| `99_Archive` | Byte-identical duplicates (preserved, not deleted) and AI-generated drafts |

Each folder has its own `README.md` with details.

## Notes on git tracking

Some content is intentionally **on disk but not in git** (see `.gitignore`):
raw absorption CSVs (`04_.../absorption_data/`, several GB), the bulk `Lab Photos`
dump, video files, the archived duplicates, the large Kovachy MOT CAD assembly, and
PlatformIO vendored libraries. Code, documents, curated figures, and results are tracked.

## Provenance

Reorganized July 2026 from the original working folders. Byte-identical duplicate files
were either removed (published papers only, where a copy remains in `01_References`) or
moved to `99_Archive/duplicates` (everything else). No data files were modified.
