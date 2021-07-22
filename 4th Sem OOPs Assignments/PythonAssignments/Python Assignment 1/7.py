
#Write a function findfiles that recursively descends the directory 
# tree for the specified diectory and generates paths of all the files in the tree 
import os
d=input("Enter the directory: ")

command="tree "+d
os.system(command)