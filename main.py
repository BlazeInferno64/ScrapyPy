# Copyright 2024 (c) BlazeInferno64 --> https://github.com/blazeinferno64
import src.app

"""
This is the main entry point of the ScrappPy web scrapper application.
It imports the 'src.app' module, which contains the main application logic.
Check './src/app.py' for the source code
"""

if __name__ == "__main__":
    try:
        # Run the main application
        src.app.main()
    except KeyboardInterrupt:
        src.app.time.sleep(1)
        print(f"\n\nError: Keyboard interrupt error occured!\n")