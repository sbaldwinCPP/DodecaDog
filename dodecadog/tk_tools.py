import os
import tkinter as tk
from tkinter import filedialog, messagebox


def file_browse(file_types=[]):
    app_path = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(app_path, "assets", "icons", "file.ico")
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


if __name__ == "__main__":
    print(file_browse())
