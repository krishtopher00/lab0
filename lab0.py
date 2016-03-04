#Author: Krish Bhavnani
#Date: March 4,2016


print("Welcome to my Caesar Cipher Decoder!")

fileName = raw_input("Which file would you like to open to decode (encrypted.txt is preferred)? ")

# User does not have to put .txt in the name
if ".txt" not in fileName:
    fileName += ".txt"
    
shift = 0

# Read file into a string
f = open(fileName,"r")
message = f.read()
f.close

# Create an output file
decodedFileName = raw_input("Name a file that you want to create for the possibilities of the decoded message (decrypt.txt is preferred): ")
if ".txt" not in decodedFileName:
    decodedFileName += ".txt"

f = open(decodedFileName, "w") 

# Take each character of string message and switch
# Shift cannot be 95 because it is the same as the original
while shift < 95:
    output = ""
    for character in message:
        character = ord(character)
        character += shift
        if character > 126:
            character -= 95
        character = chr(character)
        output += character
    if "Krish" in output:
        print("This is your message at Shift {}: {}".format(shift,output))
    # New line for readability
    f.write("Shift {}. {}\n\n".format(shift,output))
    shift += 1

#Close the file
f.close()
