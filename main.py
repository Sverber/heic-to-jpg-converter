import os
import shutil

from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

# Get list of HEIF and HEIC files in directory
input_directory = 'input'
output_directory = 'output'
failed_directory = 'failed'

# Create the output and failed directories if they don't exist
os.makedirs(output_directory, exist_ok=True)
os.makedirs(failed_directory, exist_ok=True)

# Convert each file to JPEG
for input_filename in os.listdir(input_directory):
    if input_filename.endswith('.heic') or input_filename.endswith('.heif'):
        input_path = os.path.join(input_directory, input_filename)
        try:
            image = Image.open(input_path)
            image.load()
            output_filename = os.path.splitext(input_filename)[0] + '.jpg'
            output_path = os.path.join(output_directory, output_filename)
            image.save(output_path, 'JPEG')
            print(f'Converted {input_filename} to {output_path}')
        except Exception as e:
            print(f'Conversion of {input_filename} failed: {str(e)}')
            # Copy the failed image to the "failed" directory
            failed_path = os.path.join(failed_directory, input_filename)
            shutil.copy(input_path, failed_path)
            print(f'Copied {input_filename} to {failed_path}')
