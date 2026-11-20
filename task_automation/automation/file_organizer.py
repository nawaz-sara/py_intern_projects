
import shutil
from pathlib import Path


def get_unique_path(destination):
    """
    Prevent overwriting an existing file.
    """

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem} ({counter})"
            f"{destination.suffix}"
        )

        new_path = destination.with_name(new_name)

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder_path):

    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        raise ValueError("Please select a valid folder.")

    moved = []
    errors = []

    for file in folder.iterdir():

        # Skip folders
        if not file.is_file():
            continue

        # Extract extension
        extension = file.suffix.lower().lstrip(".")

        # Files without extensions go into Others
        folder_name = extension.upper() if extension else "OTHERS"

        # Create destination folder
        destination_folder = folder / folder_name
        destination_folder.mkdir(exist_ok=True)

        # Avoid overwriting files
        destination = get_unique_path(
            destination_folder / file.name
        )

        try:
            shutil.move(str(file), str(destination))
            moved.append(file.name)

        except OSError as error:
            errors.append(f"{file.name}: {error}")

    return {
        "moved": moved,
        "errors": errors
    }
