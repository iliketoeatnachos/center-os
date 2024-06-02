import os
import requests

try:
    fileutility = requests.get("https://raw.githubusercontent.com/iliketoeatnachos/center-os/main/libraries/fileutility/fileutility.py").content
    exec(fileutility)
except:
    print("An error occurred while getting temporary script.")

def get(type, name):
    if type == "package":
        try:
            installscript = requests.get(f"https://raw.githubusercontent.com/iliketoeatnachos/center-os/main/packages/{name}/install.py")
            exec(installscript)
        except:
            print("An error occurred while installing package.")
    
    if type == "library":
        try:
            libraryscript = requests.get(f"https://raw.githubusercontent.com/iliketoeatnachos/center-os/main/libraries/{name}/{name}.py")
            libraryversion = requests.get(f"https://raw.githubusercontent.com/iliketoeatnachos/center-os/main/libraries/{name}/version")
            create("folder", f"libraries/{name}")
            create("file", f"libraries/{name}/{name}.py")
            create("file", f"libraries/{name}/version")
            write(f"libraries/{name}/{name}.py", libraryscript)
            write(f"libraries/{name}/version", libraryversion)
        except:
            print("An error occurred while installing library.")

        