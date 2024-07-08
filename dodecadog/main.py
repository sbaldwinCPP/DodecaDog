"""
This is a launcher that 'anchors' the location to the root folder.
Helps keep imports and paths to data files consistent when 'frozen' to .exe format
"""

# custom import
from . import gui

# global constants
APP_VERSION = "0.0.0.0"
APP_NAME = "App Template"


def main():
    gui.run(
        # file=__file__,
        name=APP_NAME,
        version=APP_VERSION,
    )


if __name__ == "__main__":
    main()
#     gui.AppClass(
#         file=__file__,
#         name=APP_NAME,
#         version=APP_VERSION,
#     ).run()
