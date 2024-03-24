# WallpaperMakerer
Easily take a folder of images and collage them for sleek and fun desktop wallpapers

Certainly! Here's a modern and sleek README for your Python script:

---

# Wallpaper Maker

## Overview

Wallpaper Maker is a Python script that generates a collage from a collection of images. It randomly arranges the images, resizes them, and pastes them onto a 1920x1080 canvas to create a unique wallpaper.

## Features

- Randomly arranges images to create a visually appealing collage.
- Resizes images to fit within the collage while maintaining aspect ratio.
- Supports various image formats such as JPEG, PNG, etc.
- Sleek and minimalistic design.

## Installation

1. Clone the repository or download the script file (`wallpapermaker.py`).

    
    git clone https://github.com/yourusername/wallpaper-maker.git
    

2. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. Install the required dependencies using pip:


    pip install Pillow


## Usage

1. Place your desired images in a folder.

2. Open the `wallpapermaker.py` script in a text editor.

3. Modify the `input_folder` variable to specify the path to your image folder.

  
    input_folder = "path/to/your/image/folder"
  

4. Set the `output_file` variable to define where you want to save the generated collage.

    
    output_file = "path/to/output/collage.png"
    

5. Run the script using Python:

    
    python wallpapermaker.py
    

6. Check the specified output path for the generated collage.

## Example


input_folder = "C:/Users/username/Pictures/wallpaper_images"
output_file = "C:/Users/username/Desktop/collage.png"
generate_collage(input_folder, output_file)


## Credits

WallpaperMakerer is created by EAMZ @ DARKSTONE LABS
