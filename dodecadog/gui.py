import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

from . import core


def callback_check(sender, app_data, user_data):
    print(sender, app_data, user_data)


def basic():
    app = core.AppClass()
    dpg.create_context()
    dpg.create_viewport(title="Custom Title", width=600, height=300)

    with dpg.window(label="Example Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Test", callback=app.add)
        dpg.add_button(
            label="EVENT", tag="check", callback=callback_check, user_data="test"
        )
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(
            label="float",
            default_value=0.273,
            max_value=1,
            callback=callback_check,
            user_data="test",
        )
        dpg.add_input_int(
            label="int",
            tag="int",
            default_value=273,
            max_value=1,
            callback=callback_check,
            user_data="adsklf;sakjf",
        )

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def dpg_demo():
    dpg.create_context()
    dpg.create_viewport(title="Custom Title", width=600, height=600)

    demo.show_demo()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
