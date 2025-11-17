#compress_image.py

from PIL import Image
import os

# folder path
# folder_path = 'large_image'
# folder_path = 'Batch 3/Batch 3'
# folder_path = 'Batch4/Batch4'
folder_path = 'Batch10/Batch10'


# output_folder = 'jpg_img_compressed_images_70'
# output_folder = 'batch3_compressed'
# output_folder = 'batch4_compressed'
output_folder = 'batch10_compressed'


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(folder_path):
    print(f'\nProcessing {filename}...')

    if filename.endswith('.jpg'):
        img = Image.open(os.path.join(folder_path, filename))
        img.save(os.path.join(output_folder, filename.replace(' .','.')), optimize=True, quality=70)
        print(f'Compressed {filename} and saved to {output_folder}')

    elif filename.endswith('.png'):
        img = Image.open(os.path.join(folder_path, filename))
        img = img.convert('P', palette=Image.ADAPTIVE)
        img.save(os.path.join(output_folder, filename.replace(' .','.')), optimize=True)
        print(f'Compressed {filename} and saved to {output_folder}')
        
    else:
        print(f'Skipping {filename}, not a supported image format.')    