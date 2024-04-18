# Football Manager Graphics Faces Configurator

This Python application provides a simple graphical user interface (GUI) for
dynamically adding player ID values to the `config.xml` file used for managing
graphics faces in Football Manager. The tool allows users to easily specify
new player IDs and append them to the XML file directly after a specified comment marker,
ensuring that the game correctly recognizes and applies new face graphics.

## Features

- **Load XML Configuration File**: Users can select and load their `config.xml` file through a file dialog.
- **Add New Player IDs**: Through a user-friendly interface, player ID values can be added. These entries are directly inserted into the XML, maintaining the file's integrity and structure.
- **Save Updated Configurations**: After modifications, the updated XML file can be saved immediately, making the changes persistent and ready for use in Football Manager.

## Requirements

- Python 3.x
- `lxml` library for XML processing
- `tkinter` for the GUI

## Installation

To set up the application on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BarkevK/Personal-Projects.git

2. **Install Dependencies**:
Ensure Python is installed, then run:
   ```bash
   pip install lxml

## Usage

1. Run the script

2. Use the **Open XML File** button to load your `config.xml` file.

3. Enter a player ID when prompted after clicking the **Add Record** button. This ID is then inserted into the XML configuration file/

4. Save the file using the GUI, which will reflect changes immediately in the XML document.


## Contact

Your Name - [@BarkevKS](https://twitter.com/BarkevKS)  
Project Link: [https://github.com/BarkevK/Personal-Projects](https://github.com/BarkevK/Personal-Projects/blob/main/Football%20Manager/FM_XML_adder.py)

  
   