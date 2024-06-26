import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from lxml import etree
import os
from PIL import Image 
import shutil
from tkinterdnd2 import DND_FILES, TkinterDnD

def load_xml(file_path):
    try:
        return etree.parse(file_path)
    except etree.XMLSyntaxError as e:
        messagebox.showerror("XML Syntax Error", f"Error in XML syntax: {e}")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None

# Function to save the XML tree back to a file
def save_xml(tree, file_path):
    try:
        tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="UTF-8")
        messagebox.showinfo("Success", "File saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save the file: {e}")

# Function to add a record element to the XML tree
def add_record(tree, num):
    if tree is not None:
        root = tree.getroot()
        # Find the specific comment
        target_comment = next((node for node in root.iter(etree.Comment) if "Auto generated by fmXML" in node.text), None)
        if target_comment is not None:
            new_record = etree.Element("record", from_=str(num), to=f"graphics/pictures/person/{num}/portrait")
            # Insert the new element after the comment
            parent = target_comment.getparent()  # Get parent of the comment
            index = parent.index(target_comment)  # Get index of the comment within its parent
            parent.insert(index + 1, new_record)  # Insert the new element after the comment
            save_xml(tree, file_path.get())  # Save to the specified file path
        else:
            messagebox.showerror("Error", "The specific comment 'Auto generated by fmXML' was not found in the XML file.")

# Handler for button click to add new record
def on_add():
    num = simpledialog.askstring("Input", "Enter the number:", parent=root)
    if num and num.isdigit():
        add_record(xml_tree, num)
    else:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

# Handler to open file dialog and load file
def on_open_file():
    filepath = filedialog.askopenfilename(
        title="Open XML File",
        filetypes=(("XML files", "*.xml"), ("All files", "*.*"))
    )
    if filepath:
        file_path.set(filepath)
        global xml_tree
        xml_tree = load_xml(filepath)
        if xml_tree is not None:
            messagebox.showinfo("File Loaded", "XML file loaded successfully!")

image_save_directory = None

def set_save_directory():
    global image_save_directory
    directory = filedialog.askdirectory(title="Select Faces Directory")
    if directory:
        image_save_directory = directory
        messagebox.showinfo("Directory Set", f"Images will be saved to: {directory}")

def save_image(image_path):
    if image_save_directory and os.path.exists(image_save_directory):
        shutil.copy(image_path, image_save_directory)
        messagebox.showinfo("Success", f"Image {os.path.basename(image_path)} saved successfully in faces folder.")
    else:
        messagebox.showerror("Error", "Please set a valid save directory first.")

def on_drop(event):
    files = root.tk.splitlist(event.data)
    for f in files:
        if f.lower().endswith('.png'):
            save_image(f)

def on_select_image():
    file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("PNG images", "*.png")])
    if file_path:
        save_image(file_path)

# GUI 

def on_exit():
    root.quit()  

root = TkinterDnD.Tk()
root.title("Football Manager Graphics Faces Configurator")
root.geometry("500x300")  # You can adjust the size as needed


style = ttk.Style()
style.theme_use('clam') 

open_file_button = ttk.Button(root, text="Open XML File", command=on_open_file)
open_file_button.pack(pady=10, padx=10)

add_button = ttk.Button(root, text="Add Record", command=on_add)
add_button.pack(pady=20, padx=10)

exit_button = ttk.Button(root, text="Exit", command=on_exit)
exit_button.pack(pady=10, padx=10, side=tk.BOTTOM)

signature_label = ttk.Label(root, text="Made by BarkevKS", font=("Helvetica", 8))
signature_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

set_directory_button = ttk.Button(root, text="Set Faces Directory", command=set_save_directory)
set_directory_button.pack(pady=10)

add_image_button = ttk.Button(root, text="Add Image", command=on_select_image)
add_image_button.pack(pady=10)

root.mainloop()
