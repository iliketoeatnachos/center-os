import os

def create(type, directory):
    if type == "file":
        try:
            open(directory, "x")
        except:
            print("An error occurred while creating file.")
    
    if type == "folder":
        try:
            os.mkdir(directory)
        else:
            print("An error occurred while creating folder.")

def delete(directory):
    try:
        os.remove(direcotry)
    except:
        print("An error occurred while deleting file/folder.")