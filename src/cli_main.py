#!/usr/bin/env python3
import sys

def run_experiment():
    print("Running experiment... (placeholder)")

def process_data():
    print("Processing data... (placeholder)")

def launch_gui():
    print("Launching GUI... (placeholder)")

def show_help():
    print("""
Microscopy Assembly CLI
======================

Available commands:
  run_experiment    Run a placeholder experiment
  process_data      Process placeholder data
  gui               Launch a placeholder GUI
  help              Show this help message
""")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    cmd = sys.argv[1].lower()

    if cmd == "run_experiment":
        run_experiment()
    elif cmd == "process_data":
        process_data()
    elif cmd == "gui":
        launch_gui()
    elif cmd == "help":
        show_help()
    else:
        print(f"Unknown command: {cmd}")
        show_help()

if __name__ == "__main__":
    main()
