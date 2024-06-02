while True:
    prompt = input("~> ")
    
    if prompt == "python":
        print("Welcome to pyshell.")
        print("Version: 1.0.0")
        while True:
            try:
                pyshellprompt = input("Python~> ")
                exec(pyshellprompt)
            except Exception as error:
                print(f"Error: {error}.")
    else:
        print("Unknown command.")
