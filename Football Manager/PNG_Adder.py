import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image  # If you need to manipulate images
import shutil

def on_open_file():
    global config_path
    filepath = filedialog.askopenfilename(
        title="Open XML File",
        filetypes=(("XML files", "*.xml"), ("All files", "*.*"))
    )
    if filepath:
        config_path = filepath
        messagebox.showinfo("File Loaded", "XML file loaded successfully!")

def on_drop(event):
    if event.data:
        files = root.tk.splitlist(event.data)
        for f in files:
            if f.lower().endswith('.png'):
                save_image(f, config_path)

def save_image(image_path, config_path):
    if config_path:
        directory = os.path.join(os.path.dirname(config_path), 'faces')
        if not os.path.exists(directory):
            os.makedirs(directory)
        shutil.copy(image_path, directory)
        messagebox.showinfo("Success", f"Image {os.path.basename(image_path)} saved successfully in faces folder.")
    else:
        messagebox.showerror("Error", "Load the config file first to determine the save directory.")

root = tk.Tk()
root.title("Football Manager Graphics Faces Configurator")
root.geometry("500x300")

open_file_button = ttk.Button(root, text="Open XML File", command=on_open_file)
open_file_button.pack(pady=10, padx=10)

# Configure the window to accept drag and drop
root.drop_target_register(tk.DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
