import os
import shutil
import argparse

def organize_files(target_folder):
    # Finds the extensions of the files 
    extensions = {item.split('.')[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}

    # Create folder based on extension type
    for extension in extensions:
        if not os.path.exists(os.path.join(target_folder, extension)):
            os.mkdir(os.path.join(target_folder, extension))

    # move files to target folder
    for item in os.listdir(target_folder):
        if os.path.isfile(os.path.join(target_folder, item)):
            try:
                file_extension = item.split('.')[-1]
                shutil.move(os.path.join(target_folder, item), os.path.join(target_folder, file_extension, item ))
            except PermissionError as e:
                print(f"PermissionError: {item} is being used by another process, skipping.")
            except FileNotFoundError as e: 
                print(f"FileNotFoundError: Could not find the file or path {item}, skipping.")

def main(): 
    #Sets up the command line parsing change parameter in expanduser for default location
    parser = argparse.ArgumentParser(description= 'Organizes the files based on extension of file')
    parser.add_argument('path', type=str, nargs='?', default=os.path.expanduser('../../Downloads'), help='Default path ~/Downloads' )

    args = parser.parse_args()

    organize_files(args.path)

if __name__ == "__main__":
    main()