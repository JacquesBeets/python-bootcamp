# ===============================================
# OBJECTIVES
# ===============================================

# Read text files in Python
# Write text files in Python
# Use "with" blocks when reading / writing files
# Describe the different ways to open a file
# Read CSV files in Python
# Write CSV files in Python

# ===============================================
# OPEN AND CLOSE A FILE
# ===============================================

# You can read a file with the open function

# open returns a file object to you

# You can read a file object with the read method

# f = open('story.txt')

# print(f.read())

# f.seek(0) # will move cursor to the beginning.

# f.readline() # will read 1 line at a time.

# f.readlines() # will return a list with all all the lines seperated.

# f.close() # closes the file after it is read.


# ===============================================
# THE "WITH" STATEMENT
# ===============================================


# # Option 1
# file = open("story.txt")
# file.read()
# file.close()

# file.closed # True

# Option 2
with open("story.txt") as file: # closes file automatically
    file.read()

#file.closed # True


# ===============================================
# WRITING TO FILES
# ===============================================

# You can also use open to write to a file
# Need to specify the "w" flag as the second argument

# Option 1
# file.open("haiku.txt")
#   file.write("Writing files is great\n")
#   file.write("Here's another line of text\n")
#   file.write("Closing now, goodbye!")
# file.close()

# Option 2
with open("haiku.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!\n")

with open("lol.txt", "w") as file:
    file.write("haha" * 10000)


# ===============================================
# Modes for Opening Files
# ===============================================   

# r - Read a file (no writing) - this is the default
# w - Write to a file (previous contents removed)
# a - Append to a file (previous contents not removed)
# r+ - Read and write to a file (writing based on cursor)(only works with existing file. will not create a new file)

with open("haiku.txt", "r+") as file:
    file.write("Using r+\n")


# ===============================================
# EXCERSIZES
# =============================================== 

# 1
def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)

# 2
def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
 
    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])

# 3
def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }

# 4
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()