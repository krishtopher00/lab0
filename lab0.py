print("Welcome to my Caesar Cipher Decoder!")

fileName = raw_input("Which file would you like to open to decode (encrypted.txt is preferred)? ")

if ".txt" not in fileName:
    fileName += ".txt"
    
shift = 0


f = open(fileName,"r")
message = f.read()
f.close

decodedFileName = raw_input("Name a file that you want to create for the possibilities of the decoded message (decrypt.txt is preferred): ")
if ".txt" not in decodedFileName:
    decodedFileName += ".txt"

f = open(decodedFileName, "w") 

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
    f.write("Shift {}. {}\n\n".format(shift,output))
    shift += 1

f.close()
