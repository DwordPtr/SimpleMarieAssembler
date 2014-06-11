def parseInstruction(word):
    """This method takes a string as an argument and parses it to the write op-code
    This is a staging area so we can write the proper op-code to the heigh order byte """
    if word == "load":
        return "01"
    elif word == "store":
        return "02"
    elif word == "add":
        return "03"
    elif word == "sub":
        return "04"
    elif word == "input":
        return "05"
    elif word == "output":
        return "06"
    elif word == "halt":
        return "07"
    elif word == "skipcond":
        return "08"
    else:
        print("Error: Invalid Instruction"+"\n"+ "Now exiting program") #on error we simply exit in the future I want to wipe the programh and programl files
        exit()

#case insensitivity added!
#Marie partial solution
#take the filename of our program as input
inputFileName = input("enterFile name to be assembled")  #we take a string argumetn searching for matching filenames in the same folder
f = open(inputFileName,'r') 
fileIn = f.read()  #put the entire file into fileIn
f.close() #read file as string
high = open("programh.txt",'w')  #high order bytes (op-codes) go in this file
low = open("programl.txt",'w')  #low order  (data) bytes in here
lines = fileIn.split('\n') # makes a list of the lines
words = [] # a for loop makes a multidimmensional array where words is a 2d array [line][word]
for i in range(len(lines)-1 ): #we divide the list of lines into a list of "words" these words should either be opcodes or data The "-1" keeps us from appending garbage that .split tacks on 
    temp = lines[i].split(' ') #this phrase makes a temp list that parses each lines "words" into a list
    words.append(temp) # we append this list onto works making words a list of lists [line][word]

for i in range(len(lines)-1): # we need nested for loops to iterate over this list of lists
    for j in range(len(words[i])):
        if j==0: # because each line should be instruction, data we can (hopefully) assume everything follows this pattern so j=0 is instruction and other is data
                instruction = parseInstruction(words[i][j].lower()) #if j=0 we're dealing with an instruction so we feed this "word" to the parser function to get the write opCode
                high.write(instruction) #once we get the parsed instruction we want to write it
                high.write("\n") #we need to put the next opcode on the next line
                if(instruction != "sub" or instruction != "add"):
                    continue #some instructions don't have data....I'm not too sure about this line but its a simple fix (hopefully) if anything's amiss
        else:
            data = words[i][j]  #if its not an insturction its data
            output = str(hex(int(data))[2:]) #we take the string and make it an int then we make the int a hex num and cut off the obnoxious 0x with [2:]
            if((int(data))<=15): # if the data is smaller than 10 in hex or 16 we need to add a leading zero so the low order byte is proper
                output = "0"+str(hex(int(data))[2:]) #add a low order zero if and only if its needed
            low.write(output) #write the data to the low order byte file
            low.write("\n") #write a newline


high.close() #when the loop is done the files will be parsed out and our work will be done
low.close()
print("Success: No Errors!") # a notificiation
exit()




