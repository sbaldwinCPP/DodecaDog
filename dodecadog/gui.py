import os.path

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

import core, fonts


# %% main
def run(name=core.NAME, version=core.VERSION):
    # create app instance
    app = core.AppClass()

    app_path = os.path.dirname(os.path.abspath(__file__))
    icon = os.path.join(app_path, "assets", "icons", "dog.ico")

    # boilerplate
    dpg.create_context()
    dpg.create_viewport(
        title="Custom Title", width=200, height=200, small_icon=icon, large_icon=icon
    )

    # add custom font
    fonts.set_default(i=1, s=16)

    # layout
    with dpg.window(tag="main"):
        dpg.add_text(f"{name} v{version}")

        dpg.add_slider_float(
            label="a",
            default_value=app.a,
            max_value=1,
            callback=callback_a,
            user_data=app,
        )

        dpg.add_input_int(
            label="b", default_value=app.b, callback=callback_b, user_data=app
        )
        with dpg.group(horizontal=True):
            dpg.add_text("a * b =")
            dpg.add_text("0.00", tag="display")

    # more boilerplate
    dpg.setup_dearpygui()
    dpg.show_viewport()

    # set main window
    dpg.set_primary_window("main", True)

    # more boilerplate
    dpg.start_dearpygui()
    dpg.destroy_context()


# %% callbacks
def callback_a(sender, app_data, app):
    app.set_a(app_data)
    update_display(sender, app_data, app)


def callback_b(sender, app_data, app):
    app.set_b(app_data)
    update_display(sender, app_data, app)


# %% helpers
def update_display(sender, app_data, app):
    dpg.set_value("display", app.go())


def callback_check(sender, app_data, user_data):
    print(f"sender: {sender}\napp_data: {app_data}\nuser_data{user_data}")


# %% extras
def dpg_demo():
    dpg.create_context()
    dpg.create_viewport(title="Custom Title", width=600, height=600)

    demo.show_demo()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    run()
