# 03_Heaters_and_Monitoring — Custom Nichrome heaters + temperature logging (thesis Sec. 3.5)

Custom Nichrome-mica resistive heaters (22 AWG bare Nichrome, mica insulation, high-temp
crimps, Variac-driven) used on the nozzle (~230 °C operating, >400 °C during bakes),
Rb reservoir, reservoir valve, and bellows.

## Data and analysis

- **`HeaterStuff.ipynb`** — analysis of heater characterization data.
- **`ss_air_temp_vs_time.csv`, `ss_heater_T_vs_t.png/.pdf`** — stainless-steel test
  reservoir heater tests (5–13 Nichrome turns at 5 A → 320–580 °C equilibrium);
  source of thesis Figs. 3.10–3.11.
- **`Nozzle Temp 092025.csv`, `Rb Temp 092025.csv`, `Bellow temp 092025.csv`** —
  September 2025 temperature logs of the assembled beam source heaters.
- **`MAX-*-20251011-*.csv`** — October 2025 logs from MAX31865/thermocouple readout
  (RTD vs. TC channels).

## TempReading/

PlatformIO (ESP32) firmware + Python serial loggers (`temp_logger*.py`) used to read
thermocouples/RTDs and produce the CSV logs above. `test*.csv` are logger test outputs.
The vendored `.pio/` library tree is git-ignored.
