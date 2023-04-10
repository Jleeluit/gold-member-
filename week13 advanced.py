import os

def get_file_info(path=None):
    """
    """
    
    if path is None:
        path = os.getcwd()  # Set default path to current working directory

    file_list = []  # List to store file information

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_stat = os.stat(file_path)

            # Create a dictionary with file information
            file_info = {
                'filename': filename,
                'path': file_path,
                'size': file_stat.st_size,
            }

            file_list.append(file_info)  # Append the file information to the list

    return file_list


# Get file information for current working directory
files = get_file_info()
print(files, '\n')

