import os

# os.mkdir("folder")

if os.path.exists("folder"):
    with open("folder/file.txt", "w") as file:
        pass

if os.path.isfile("folder"):
    print('file')
else:
    print('no file')

dogs_images = []
print(os.listdir("folder"))