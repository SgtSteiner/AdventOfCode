"""_summary_: https://adventofcode.com/2022/day/7

"""

import os

subdirs = {}
direct_directory_size = {}

# Lee archivo de entrada
def read_input():
    with open("input.txt", 'r') as f:
        return f.read().strip().split('\n')
    
# size calculation function
def compute_dirsize(dirname: str):
    dirsize = direct_directory_size[dirname] # initialise the size by the size of the directory excluding the subdirectories
    for ii in subdirs[dirname]: # go through all the subdirectories
        if ii in subdirs:
            dirsize += compute_dirsize(ii) # looping the subdirectory size addition until we no longer find the subdirectories
    return dirsize
    
if __name__ == "__main__":
    data  = read_input()
    
    for item in data:
        if item[0] == "$":
            ds, cmd, *ddir = item.split()
            if cmd == "cd":
                path = ddir[0]
                if path == "/":
                    curdir = path
                else:
                    curdir = os.path.normpath(os.path.join(curdir, path))
                if curdir not in subdirs:
                    subdirs[curdir] = []
                    direct_directory_size[curdir] = 0
                    
        else:
            fsize, fname = item.split()
            if fsize != 'dir': 
                direct_directory_size[curdir] += int(fsize)
            else:
                subdirs[curdir].append(os.path.normpath(os.path.join(curdir, fname)))
                
    # Part 1: Sum of all the directories with a total size of at most 100000.
    part_one = 0
    for ii in subdirs:
        dirsize = compute_dirsize(ii)
        if dirsize <= 100000:
            part_one += dirsize
    print(f"Part one: {part_one}")
    
    # Part 2: The smallest possible file to delete to free up the required space.
    total_space = 70000000
    space_required = 30000000
    space_used = compute_dirsize('/')

    delete_this_directory = total_space
    for ii in direct_directory_size:
        dirsize = compute_dirsize(ii)
        if dirsize >= space_required - (total_space - space_used) and dirsize <= delete_this_directory:
            delete_this_directory = dirsize
    print(f"Part two: {delete_this_directory}")