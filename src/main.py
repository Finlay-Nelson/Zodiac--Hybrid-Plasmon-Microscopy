"""
main.py

Thin wrapper that defaults to CLI entry point.
Switch this to gui_main.main() if you want GUI as the default.
"""

from cli_main import main as cli_main

if __name__ == "__main__":
    cli_main()
