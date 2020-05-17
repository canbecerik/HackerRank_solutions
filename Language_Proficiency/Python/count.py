import os, sys

def file_count(extension, count):
    """Count no of files under current folder with given extension"""
    for root, dir, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.'+extension):
                count += 1
    return count

def main():
    """Get optional extension from call argument, default to py"""
    count = 0
    if len(sys.argv) != 2:
        extension = "py"
    else:
        extension = sys.argv[1]
    if extension == "py":
        count = -3 # Ignore events.py, watcher.py and count.py
    number = file_count(extension, count)
    print(f"There are {number} {extension} files.")

main()