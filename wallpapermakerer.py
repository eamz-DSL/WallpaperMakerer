import os
import random
from PIL import Image, ImageDraw

def generate_collage(input_folder, output_file):
    # List all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    if not image_files:
        print("No image files found in the input folder.")
        return

    # Initialize the final collage image
    collage = Image.new('RGB', (1920, 1080), color='white')
    draw = ImageDraw.Draw(collage)

    # Loop through each image file
    for image_file in image_files:
        # Open the image
        img = Image.open(os.path.join(input_folder, image_file))
        
        # Randomize size and position
        width, height = img.size
        max_resize_factor = min(1920 / width, 1080 / height, 1)  # Calculate max resize factor
        resize_factor = random.uniform(0.01, max_resize_factor)  # Random resize factor between 0.01 and max_resize_factor
        new_width = int(width * resize_factor)
        new_height = int(height * resize_factor)
        
        # Calculate the maximum position where the image can be placed to extend beyond the edges
        max_x_pos = collage.width - new_width + int(0.1 * new_width)  # Allow 10% of the image width to extend beyond the right edge
        max_y_pos = collage.height - new_height + int(0.1 * new_height)  # Allow 10% of the image height to extend beyond the bottom edge
        
        x_pos = random.randint(-int(0.1 * new_width), max_x_pos)  # Allow negative x_pos to extend beyond the left edge
        y_pos = random.randint(-int(0.1 * new_height), max_y_pos)  # Allow negative y_pos to extend beyond the top edge

        # Resize the image
        img = img.resize((new_width, new_height))

        # Paste the image onto the collage
        collage.paste(img, (x_pos, y_pos))

        # Draw a border around the pasted image
        draw.rectangle([x_pos, y_pos, x_pos + new_width, y_pos + new_height], outline='black')

    # Save the collage to the desktop
    collage.save(output_file)
    print(f"Collage saved as {output_file}")

if __name__ == "__main__":
    input_folder = "INPUT HERE"  # Change this to the path of your input folder
    output_file = os.path.expanduser("OUPUT HERE .png")  # Output file will be saved on the desktop

    generate_collage(input_folder, output_file)
