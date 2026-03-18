import os
import shutil

# get the desktop path
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# folder where everything will go
everything_folder = os.path.join(desktop, "Everything")

# create the folder if it doesnt exist
if not os.path.exists(everything_folder):
    os.mkdir(everything_folder)

# go through everything on the desktop
for item in os.listdir(desktop):
    # skip the Everything folder itself
    if item == "Everything":
        continue

    old_path = os.path.join(desktop, item)
    new_path = os.path.join(everything_folder, item)

    # try to move the file or folder
    try:
        shutil.move(old_path, new_path)
        print("Moved: " + item)
    except:
        print("Skipped (file might be in use): " + item)

print("Done! Thank you for using! github.com/han-dsd")
