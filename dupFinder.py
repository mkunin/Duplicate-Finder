import os, sys
import hashlib

def generateMap(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
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
    return removeNonDuplicates(generateMap(pathName))

print(getDups("/Users/mkunin/Desktop/test"))
