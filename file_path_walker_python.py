import os
import sys

""""
A command-line program that takes input xxx in form of "%python problem4.py xxx"
where xxx is a file path such as "/Users/name/Documents", must be a valid file path, optimized for MacOS for now

first maps files by recursion, reformats this as a list, then prints it in a tree-like structure with indents

glob module has print directories as tree in its methods: glob.glob()
Unix can use the tree command, or ls with different flags: $ tree -R

""""

#mapping files by recursion, keeping path and file name separate
def map_files(path):
    ttz = sorted(os.listdir(path))
    for i in ttz:
        zz = os.path.join(path,i)
        
        if os.path.isdir(zz) == True:
            map_files(os.path.normpath(zz))
            continue
    
        if os.path.isdir(zz) == False:
            xyz.append([path, [], [i]])
            continue

#printing path function
def print_path(y):

    global indents

    if bool(y) == False:
        return None

    if y[0] == "":
        return print_path(y[1:])
    
    if y[0] != "":
        print(" "*indents, end="")
        print(y[0])
        indents += 1
        return print_path(y[1:])

#reformating the list structure, from string to list, for easier printing/handling
def parse_tings(aa):

    global zz

    if bool(aa) == False:
        return None
    
    if bool(aa[0][1]) == True:
        return parse_tings(aa[1:])
    
    if bool(aa[0][1]) == False:
        zz.append(aa[0])
        return parse_tings(aa[1:])

#used slash to separate into list, so here add slash back to folders/dirs
#adds to a new list
def add_slash(y):

    global zzyz
    if bool(y) == False:
        return None
    
    if y[0] == "":
        return add_slash(y[1:])

    t = y[0] + "/"
    zzyz.append(t)
    return add_slash(y[1:])

#reformating path from string to list for easier handling
def reformating_path(y):
    if bool(y) == False:
        return None
    
    z = list(y[0])
    a = z[0]
    b = a.split("/")
    add_slash(b)
    q = [zzyz.copy(), y[0][2]]
    reformat_struct.append(q)
    zzyz.clear()
    return reformating_path(y[1:])

#printing the path, keeping track of indents with global variable, uses recursion
def print_path(y):

    global indents

    if bool(y) == False:
        return None

    if y[0] == "":
        return print_path(y[1:])
    
    if y[0] != "":
        print(" "*indents, end="")
        print(y[0])
        indents += 1
        return print_path(y[1:])

#prining the files, also uses global bariable indents, recursion
def print_files(y):
    global indents

    if bool(y) == False:
        return None

    if y[0] != "":
        print(" "*indents, end = "")
        print(y[0])
        return print_files(y[1:])


#function that compares a global variabl last_path to current path
#this determins number of indents, and what parts of a path to omit
def compare_path(y):

    global position
    global indents
    global last_path

    if position == len(y):
        return 0
    
    if last_path == []:
        return 0

    try:
        if last_path[position] == y[position]:
            position += 1
            return compare_path(y)
    except IndexError:
        return 0
    
    if last_path[position] != y[position]:
        t = len(last_path) - position
        indents -= t
        return 0


#function that calls print_path and print_file, recursion
def print_tree(y):

    if bool(y) == False:
        return None
    
    global indents
    global position
    global last_path

    #compare to last path
    compare_path(y[0][0])


    #print(indent)
    print_path(y[0][0][position:])
    a = sorted(y[0][1])

    print_files(a)

    position = 0

    last_path = y[0][0]

    return print_tree(y[1:])


#takes input from command line
#initiates global variables, calls above functions 
def main():
    if len(sys.argv) != 2:
        print("Please provide 1 file path")
        exit()
    

    try:
        str(sys.argv)
    except (ValueError, TypeError):
        print("Please provide valid file path.")
        exit()

    #cheking path exists
    try:
        os.path.exists(os.path.normpath(input1))
    except FileNotFoundError:
        print("Please provide path that exists.")
        exit()

    if len(sys.argv) == 2:
        input1 = sys.argv[1]

        #note that these are intermediate data structures
        global xyz
        xyz =[]
        global zz 
        zz = []
        global reformat_struct
        reformat_struct = []
        global zzyz
        zzyz = []
        global last_path
        last_path = []
        #global variables initialized
        global position
        position = 0
        global indents
        indents = 0
        #getting the file paths
        map_files(os.path.normpath(input1))
        y = sorted(list(xyz)) #sorting list for easier handling
        #more reformating
        z = parse_tings(y)
        reformating_path(zz)
        #the main call for printing
        print_tree(reformat_struct)


if __name__ == '__main__':
    main()

