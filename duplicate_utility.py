import os;

print(
    "Remove File Duplicates Utility"
)

directory = input("ABSOLUTE path to check for duplicate files: ")
directory = directory.strip()
identifier = input("File name identifier for duplicate files: ")
length = int(input("Identifier full length: "))
position = input("Identifier at the (S)tart or (E)nd of the file name?: ")

for subdir, dirs, files in os.walk(directory):
    for file in files:
        filePath = subdir + os.sep + file
        if (identifier in file):
            fileName, fileType = os.path.splitext(filePath) # get name and file extension of offending file
            origFilePath = fileName[:len(fileName) - length] + fileType

            if (position.lower() == 'S'):
                origFilePath = fileName[length + 1:] + fileType
            
            print("REMOVING DUPLICATE OF " + filePath + " -> " + origFilePath)
            if (os.path.getmtime(filePath) > os.path.getmtime(origFilePath)):
                os.remove(origFilePath)
                os.rename(filePath, origFilePath)
            else:
                os.remove(filePath)