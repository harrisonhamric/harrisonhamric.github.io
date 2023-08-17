import os

path = 'path/to/your/images/'

# Get all the .jpg files in the directory
images = [f for f in os.listdir(path) if f.endswith('.jpg')]

# Sort the files (optional, depending on how you want to order them)
images.sort()

# Rename each file
for i, image in enumerate(images, start=1):
    old_path = os.path.join(path, image)
    new_path = os.path.join(path, f'image{i}.jpg')
    os.rename(old_path, new_path)

print("Renaming completed!")
