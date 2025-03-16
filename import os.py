import os
import shutil

def organize_files(directory):
    # Create a dictionary to map file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.tar.gz'],
    }

    # Create folders if they don't exist
    for folder_name in file_types.keys():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(directory, folder_name, filename))
                    break

if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)
    print("Files organized successfully!")