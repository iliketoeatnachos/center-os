import os

def create(type, directory):
    if type == "file":
        try:
            open(directory, "x")
        except:
            print("An error occurred while creating file.")
    
    elif type == "folder":
        try:
            os.mkdir(directory)
        except:
            print("An error occurred while creating folder.")
    else:
        print('"{type}" not a type that can be created.')

def delete(directory):
    try:
        os.remove(direcotry)
    except:
        print("An error occurred while deleting file/folder.")