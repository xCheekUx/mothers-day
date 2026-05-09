import os

# specify the path (use "." for current directory)
path = "."

# list all files and directories
contents = os.listdir(path)

# print the contents
for item in contents:
    print(item)
