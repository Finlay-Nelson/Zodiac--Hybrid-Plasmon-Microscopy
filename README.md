# Microscopy Assembly Platform

This repository contains software for controlling microscopy experiments,
running automated workflows, and processing experimental data.

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

