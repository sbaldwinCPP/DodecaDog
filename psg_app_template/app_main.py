# %% imports

import PySimpleGUI as sg

import app_module as mod
import app_package.pgk_module as pkg


# %% functions
def make_window(theme):
    sg.theme(theme)

    tab_one = [
        [sg.Text("Set theme here:")],
        [
            sg.Listbox(
                values=sg.theme_list(),
                size=(20, 12),
                key="-THEME LISTBOX-",
                enable_events=True,
            )
        ],
        [sg.Button("Set Theme")],
    ]

    tab_two = [
        [
            sg.Text(
                "Template Program",
                # size=(38, 1),
                justification="center",
                # font=("Cascadia Code", 16),
                font=("Century Gothic", 16),
                # font=("Comic Sans MS", 16),
                relief=sg.RELIEF_RIDGE,
                k="-TEXT HEADING-",
                # enable_events=True,
            )
        ],
        [sg.Text("Popup Testing")],
        [sg.Button("Open Folder")],
        [sg.Button("Open File")],
    ]

    tab_three = [
        [sg.Text("3")],
    ]

    tab_group = sg.TabGroup(
        [
            [
                sg.Tab("1", tab_one),
                sg.Tab("2", tab_two),
                sg.Tab("3", tab_three),
                # sg.Tab("Popups", popup_layout),
                # sg.Tab("Theming", theme_layout),
                # sg.Tab("Output", logging_layout),
            ]
        ],
        key="-TAB GROUP-",
        expand_x=True,
        expand_y=True,
    )

    layout = [[tab_group]]

    window = sg.Window(
        "Template",
        layout,
        # right_click_menu=right_click_menu_def,
        # right_click_menu_tearoff=True,
        # grab_anywhere=True,
        resizable=True,
        # margins=(0, 0),
        # use_custom_titlebar=True,
        finalize=True,
        # keep_on_top=True,
    )
    window.set_min_size(window.size)
    return window


def main():
    # imported from module file
    mod.foo("do the thing!")

    # imported from package folder
    pkg.baz("do another thing")

    window = make_window(sg.theme())

    while True:
        event, values = window.read(timeout=100)
        # keep an animation running so show things are happening
        # window['-GIF-IMAGE-'].update_animation(sg.DEFAULT_BASE64_LOADING_GIF, time_between_frames=100)
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print("============ Event = ", event, " ==============")
            print("-------- Values Dictionary (key=value) --------")
            for key in values:
                print(key, " = ", values[key])
        if event in (None, "Exit"):
            print("[LOG] Clicked Exit!")
            break
        elif event == "Open Folder":
            print("[LOG] Clicked Open Folder!")
            folder_or_file = sg.popup_get_folder("Choose your folder", keep_on_top=True)
            sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
            print("[LOG] User chose folder: " + str(folder_or_file))
        elif event == "Open File":
            print("[LOG] Clicked Open File!")
            folder_or_file = sg.popup_get_file("Choose your file", keep_on_top=True)
            sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
            print("[LOG] User chose file: " + str(folder_or_file))
        elif event == "Set Theme":
            print("[LOG] Clicked Set Theme!")
            theme_chosen = values["-THEME LISTBOX-"][0]
            print("[LOG] User Chose Theme: " + str(theme_chosen))
            window.close()
            window = make_window(theme_chosen)


# %% run
if __name__ == "__main__":
    main()
