import os
from PIL import Image

def scale_images(input_dir, output_dir, new_size):
    # Check if the output directory exists; if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            file_path = os.path.join(input_dir, filename)
            img = Image.open(file_path)
            
            # Resize the image to the new specified size
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
       
            # Save the resized image to the output directory
            resized_img.save(os.path.join(output_dir, filename))
         

if __name__ == '__main__':
    input_directory = 'PNG-cards-1.3'
    output_directory = 'cards'
    new_size = (77, 111)  # Set the new dimensions

    scale_images(input_directory, output_directory, new_size)
