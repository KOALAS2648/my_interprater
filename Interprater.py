import os
import time
import webbrowser
command_words = ["register","add","out","inc",";","rprint","add","mul","exit"]
more_info_command_words = ["register"]
# creates the memeroy lists
memory = []
for _ in range(0, 100):
    memory.append(0)
# checks for any keywords
def check_word(word, address, value):
    o = 0   
    if address < 100:
        try:
            # puts what ever the value is into the address
            if word == "register" and memory[address] == 0:
                memory[address] = int(value)
            elif word == "register" and memory[address] != 0:
                return False
            elif word == "inc":
                memory[address]=memory[address]+1
            elif word == "rprint":
                return memory
            elif word == "add":
                memory[address] = memory[address]+value
            elif word == "mul":
                memory[address] = memory[address]*value
            elif word == "out":
                o = memory[address]
                if o != None:
                    print(o)
            elif word =="exit":
                exit
        except:
            raise Exception("command: {} : not found".format(word)")
def my_lang(code):
    # get the lines into words in sublists in one line
    code_lines =[]
    counter=0
    # gets all the lines in the program into a list with a sublist :(
    with open(code, "r")as program:
        for line in program:
            line = line.split("\n")
            if len(line)>1:
                code_lines.append(line)
            if line[counter][0]==";":
                code_lines.remove(line)
                counter +=1
        # removes the "" from the list so I can now create the code to put it into the words
        for lines in code_lines:
            for letter in lines:
                if letter == "":
                    lines.remove(letter)
        #get all the lines converted to words
        counter = 0
        for lines in code_lines:
            for words in lines:
                code_lines[counter]=words.split(" ")
            counter +=1
        # ints the numbers
        counter_outer = 0
        for tests in code_lines:
            counter_inner = 0
            for words in tests:
                if words not in command_words and words != "":
                    code_lines[counter_outer][counter_inner]=int(words)
                    counter_inner+=1
                elif words in command_words:
                    counter_inner+=1
            counter_outer+=1
    # gets the command word
    do_words = []
    address = []
    values = []
    counter_out = 0
    #start_word = ""
    counter_outer = 0
    counter = 0
    for coword in code_lines:
        p = code_lines[counter_outer][0]
        do_words.append(p)
        if p == "out":
            counter_out +=1
        counter_outer+=1
        
    counter_outer = 0
    # get the adresses of where to register
    if code_lines[counter_outer][0] in more_info_command_words:
        for reg in code_lines:
            address.append(code_lines[counter_outer][1])
            counter_outer+=1
        counter_outer = 0
        for val in code_lines:
            values.append(code_lines[counter_outer][2])
            counter_outer +=1
        counter_outer+=1
    #RUNNING THE FINAL PRODUCT
    counter=0
    for command_word in do_words:
        output =check_word(command_word, address[counter],values[counter])
        counter+=1
    if __name__=="__main__":
        return output
    
has_exited = False
while not has_exited:
    ask_action = input(">>> ")
    action = ask_action.split(" ")
    #print(action)
    if action[0] == "mylangrun":
        try:
            my_lang(action[1])
        except OSError as e:
            with open("errors.txt","w")as errors_file:
                errors_file.write(str(e))
    
    elif action[0] == "exit":
        has_exited = True
