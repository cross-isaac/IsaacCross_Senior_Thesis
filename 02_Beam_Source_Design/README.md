# 02_Beam_Source_Design — Design calculations and CAD (thesis Ch. 3)

Design work for the dual-species Rb-Ar beam source: 231-microcapillary nozzle
(ID 100 µm, OD 200 µm, L 7.62 mm, 21-row triangular array in a modified 2.75" CF flange),
heated Rb bellows reservoir + variable leak valve, Ar gas handling line.

## Mathematica notebooks

- **`Nozzle Geometry to Expected Results.nb`** — main design notebook: nozzle geometry →
  conductance, throughput, growth-rate heat maps (source of thesis Figs. 3.3–3.4).
- **`Oven Calculations 2.5.nb`** — oven pressure/temperature/flow design calculations.
- **`Divergence Stuff.nb`** — beam divergence estimates (geometric vs. 1.68·ID/L).
- **`Impurity Stuff.nb`** — impurity/Rb-depletion estimates (thesis Sec. 3.6.1).
- **`MeanFreePath_FlowConversions_scratch.nb`** — scratch calcs: Ar/Rb mean free paths,
  SCCM→pressure conversion, solid-Ar densities at 5–20 K, dopant density.
  (Formerly `Untitled-1.nb`.)
- **`TiltTolerances/`** — nozzle tilt/misalignment tolerance calculations with annotated
  geometry sketches.

## CAD/

- **`Oven_SW_Models/`** — SolidWorks models of the beam source itself: the `Nozzle/`
  subfolder has the modified CF flange, clamp, and microcapillary models plus the
  machining `Sketches/` sent to the NU Research Shop (wire-EDM parts); `Oven/` has the
  full oven/mixing-chamber assembly (`Oven.SLDASM`, `OvenWithCross.SLDASM`).
- **`Chamber_SW_Models/`** — characterization chamber block diagrams and vendor part
  models (CF flanges, leak valve, Ar line); source of the beam-source CAD renders in
  thesis Figs. 3.16–3.17.
- **`Crystal_Growth_Chamber/`** — growth-chamber CAD (CHEX apparatus, cryostat, local
  chamber). Primarily PhD student Daniel Lutes' design; kept here because the beam source
  was designed against its constraints (~0.5 m flight path, ~1 cm tube, X-ray
  diffractometer compatibility at Argonne).
