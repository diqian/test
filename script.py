# This chunk of code took me around 30 mins to complete.
# I wrote this file for the purpose of facilitating 
# my process of practicing my coding skills on 
# online coding platforms such as hackerrank and poj

# I would like to showcase this becuase
# 1. It's easy to understand becuase I always make my code 
# in an organized and easily readible fashion
# 2. It shows that I always look for ways to automate things
# to save time 

import os

"""
################################################
            Helper function
################################################
"""
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def ConvertProblemName(s, level_of_difficulty):
    t = {1: "E", 2: "M", 3: "H"}
    return t[level_of_difficulty]+"_"+s.replace(". ", '_').replace(" ", '_')

"""
################################################
            Set up
################################################
"""
path = os.getcwd()
ignoredFiles = ["script.py", "template.java", "playground.py", ".DS_Store", ".git", "junit-4.10.jar", ".gitignore", "readme.txt"]
dirList = [item for item in os.listdir(path) if item not in ignoredFiles]
dic = { idx: item for idx, item in enumerate(dirList)}
"""
################################################
            Getting User Innput
################################################
"""
print("========================================")
print("======      Starting Script  ===========")
print("========================================")
print("")
print("Here is a list of your existing folders:")
print("")
print(dic)
print("")
print("========================================")
print("")
print("Enter the folder index or a new folder name:")
folder = input("Enter here: ")
print("Enter the level of difficuly of ur problem: {1: easy, 2: medium, 3: hard}")
problem_difficuly_level = int(input("Enter here: "))
print("Enter the leetcode question name: ")
problem_name = ConvertProblemName(input("Enter here: "), problem_difficuly_level);
"""
################################################
            Creating folders and files
################################################
"""

#           Create Category folder
folderToEnter = dic[int(folder)] if RepresentsInt(folder) else folder
categoryFolderPath = os.path.join(path, folderToEnter)

if(not os.path.isdir(categoryFolderPath)): # if folder does not exist, create one
    os.mkdir(categoryFolderPath)

# Create a sub folder under this category folder based on the name of the problem
problemNameAbsPath = os.path.join(categoryFolderPath, problem_name)
if(not os.path.isdir(problemNameAbsPath)):
    os.mkdir(problemNameAbsPath)

# Create a Solution file under this folder
targetFile = open(os.path.join(problemNameAbsPath, "DQFramework.java"), 'w')

# Write the template file into Solution.py
templateFile = open(os.path.join(path, "template.java"), 'r')
content = templateFile.read()
targetFile.write(content);

"""
################################################
            Clean up
################################################
"""
templateFile.close()
targetFile.close()

print("Generating file successful")

