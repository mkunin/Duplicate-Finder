import os, sys
import hashlib

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return file_paths

def generateMap(file_paths):
    # Dups in format {hash:[names]}
    dups = {}
    for file_path in file_paths:
        # Calculate hash
        file_hash = hashfile(file_path)
        # Add or append the file path
        if file_hash in dups:
            dups[file_hash].append(file_path)
        else:
            dups[file_hash] = [file_path]
    return dups

def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def removeNonDuplicates(myMap):
    dups = {}
    dupsFinalResult = []
    for key, values in myMap.iteritems():
        if len(values) > 1:
            dups[key] = values

    for key, values in dups.iteritems():
        dupsFinalResult.append(values)

    return dupsFinalResult

def getDups(pathName):
    return removeNonDuplicates(generateMap(get_filepaths(pathName)))

print(getDups("/Users/mkunin/Desktop/test"))
