# Strings can use "" or ''
name = "Jacques"
name2 = 'Jacques'

print(name, name2)

#Double quotes
print("#Double quotes")
msg = "he said: 'Hello there'"
print(msg)

#Escape Seqeunces/Characters
print("Escape Seqeunces/Characters")


#\n
new_line = "hello \n world"
print(new_line)

#\\
string = "this is a backslash: \\"
print(string)

mountains = "/\\/\\/\\"
print(mountains)

quotation = "he said \"Hello There\""
print(quotation)


#Concatenation
print("#Concatenation")

str_one = "your"
str_two = " face"
print(str_one + str_two)

user_name = "Jacques"
print("Welcome to the game, " + user_name)


str_one = "ice"
str_one += " cream"
print(str_one)

#Formatting String with F-STRINGS
print("#Formatting String with F-STRINGS")

x = 10
print(f"you guess of {x} was not correct")
print(f"you guess of {x + 5} was not correct")
print("you guess of {} was not correct".format(x))


#String Indexes
print("#String Indexes")

name = "Jacques"
print(name[3])
print(name[-3]) #starts from the end



#Converting Data Types
print("#Converting Data Types")

decimal = 12.45645
integer = int(decimal) #converts the float in to an int
print(integer)

