import os
import shutil

# Pasta que será organizada
SOURCE_FOLDER = "."

# Tipos de arquivos
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt"],
}

def organize_files():
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    os.makedirs(folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder, file))
                    moved = True
                    break

            if not moved:
                os.makedirs("Others", exist_ok=True)
                shutil.move(file_path, os.path.join("Others", file))

if __name__ == "__main__":
    organize_files()
