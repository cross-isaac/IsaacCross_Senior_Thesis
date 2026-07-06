# 05_Broadening_Simulation — Dipole-dipole inhomogeneous broadening Monte Carlo (thesis Ch. 6)

Monte Carlo model of spin-spin (magnetic dipole-dipole) interactions between dopants:
Poisson-distributed neighbors in a box, optional pumping/alignment efficiencies, dipolar
field summed at a central test spin → Zeeman shift distribution → Lorentzian fit → Γ and
T2* = 1/(πΓ). Verified against the Kittel-Abrahams analytic limit (agreement within ~2×).

**Conclusion:** dipolar broadening matches experiment within ~1 order of magnitude at high
densities (≳10^17 cm^-3, alkalis in parahydrogen) but under-predicts by ~100× at typical
densities (Rb:Ne, Na:Ne at ~10^16 cm^-3) → structural disorder dominates T2*. Growing at
ρ ~ 10^15 cm^-3 in improved crystals would keep dipolar-limited T2* at the ms level.

## Files

- **`broadening_sim.py`** — the full simulation (same code as thesis Appendix D).
  Originally the ES_APPM 421 final project (Dec 2025).
- **`ICross_421_Final_Report.pdf`** — the 421 course report on this simulation
  (identical copy also in `08_.../Reports/ICross_421_Final_Report_BroadeningSim.pdf`).
- **`FCC.png`** — FCC lattice figure (solid Ar host, 4 atoms/unit cell — Eq. 6.19 context).
- **`mF_eff=0.png`, `mF_eff=1.png`** — simulation outputs for different mF/pumping settings.

Related: the 421 poster is in `07_Talks_and_Posters/ICross_421_Poster.{pptx,pdf}`;
the Upadhyay thesis used for comparison data is in `01_References/`.
