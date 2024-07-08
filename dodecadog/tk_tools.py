from os.path import dirname, abspath, join
import tkinter as tk
from tkinter import filedialog, messagebox


def file_browse():
    file_types = []
    app_path = dirname(abspath(__file__))
    icon_path = join(app_path, "assets", "icons", "file.ico")
    file_types.append(("All Files", "*"))
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(icon_path)
    file_path = filedialog.askopenfilename(
        parent=root,
        title="Select a file",
        filetypes=file_types,
    )
    root.destroy()
    return file_path


def msg_box():
    title = "INFO"
    message = "Good Dog!"
    app_path = dirname(abspath(__file__))
    icon_path = join(app_path, "assets", "icons", "dog.ico")
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(icon_path)
    messagebox.showinfo(title=title, message=message, parent=root)
    root.destroy()


if __name__ == "__main__":
    print(file_browse())
    # msg_box()
