import os
# READ THE "readme" FILE FIRST
command_words = ["register","add","out"]
# creates the memeroy lists
memory = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
# checks for any keywords
def check_word(word, address, value):
    o = 0
    if address < 100:
        try:
            if word == "register" and memory[address] == 0:
                memory[address] = int(value)
            elif word == "register" and memory[address] != 0:
                return False
            elif word == "out":
                o = memory[address]
                return o
        except:
            return "why"
def my_lang(code):
    # get the lines into words in sublists in one line
    code_lines =[]
    counter=0
    # gets all the lines in the program into a list with a sublist :(
    with open(code, "r")as program:
        for line in program:
            line = line.split("\n")
            if len(line)>0:
                code_lines.append(line)
        # removes the "" from the list so I can now create the code to put it into the words
        for lines in code_lines:
            for letter in lines:
                if letter == "":
                    lines.remove(letter)
        #get all the lines converted to words
        for lines in code_lines:
            for words in lines:
                code_lines[counter]=words.split(" ")
            counter +=1
        # ints the numbers
        counter_outer = 0
        for tests in code_lines:
            counter_inner = 0
            for words in tests:
                if len(words)<3 and words not in command_words and words != "":
                    code_lines[counter_outer][counter_inner]=int(words)
                    counter_inner+=1
                elif words in command_words:
                    counter_inner+=1
            counter_outer+=1
    # gets the command word
    do_words = []
    address = []
    values = []
    counter_outer = 0
    counter = 0
    for coword in code_lines:
        do_words.append(code_lines[counter_outer][0])
        counter_outer+=1
    counter_outer = 0
    # get the adresses of where to register
    for reg in code_lines:
        address.append(code_lines[counter_outer][1])
        counter_outer+=1
    counter_outer = 0
    for val in code_lines:
        values.append(code_lines[counter_outer][2])
        counter_outer +=1
    #RUNNING THE FINAL PRODUCT
    counter=0
    for command_word in do_words:
        output =check_word(command_word, address[counter],values[counter])
        counter+=1
    if __name__=="__main__":
        return output

print(my_lang("program.txt"))
