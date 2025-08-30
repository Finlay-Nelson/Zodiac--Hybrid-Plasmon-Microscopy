"""
experiments.py

Defines experiment orchestration logic.
Experiments should call into hardware control and data processing modules.
"""

from . import control

def run_experiment(name="test"):
    """Run an experiment workflow (placeholder)."""
    print(f"[Placeholder] Running experiment: {name}")
    control.initialize_camera()
    control.capture_image(f"{name}_output.png")
    print("[Placeholder] Experiment complete")
