# A High Resolution Plasmonic Sensing Microscopy Platform

Electrical impedance imaging is a burgeoning field in electrochemistry, materials, and electrophysiology. Given here is an account of a high-resolution hybrid sensing / imaging platform from which maps of electrical impedance can be constructed with resolutions < 500nm, with samples ranging from simple polymers and coatings, to complex biological systems.

Within this repository:
- An account of the optical configuration and assembly of the microscopy platform
- An overview (and demonstration) of its veraious modalities
- All necessary softwares for high-level integrated control of the microscope and its constituent parts (stages, detectors, sources, etc.)
- Descriptions of experimental workflows and their automation
- Experimental data / imaging processing software and examples

(Repo updates to follow conclusion of discussion re: IP)

<p align="center">
  <img src="images/Zodiac Full Lo Res.png", height="400" alt="Zodiac Full Lo Res">
</p>

## Current Status
This is an early skeleton version with placeholder functions.
- CLI works: `python src/cli_main.py --experiment test`
- GUI stub works: `python src/gui_main.py` (requires PySide6)
- Core logic modules are defined but not yet implemented.

## Installation (Developer Mode)
```bash
git clone https://github.com/<YourUsername>/microscopy-assembly.git
cd microscopy-assembly
conda env create -f environment.yml
conda activate microscopy
python src/cli_main.py --help

