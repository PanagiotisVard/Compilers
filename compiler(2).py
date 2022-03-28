# DELIOPOULOS GEORGIOS 4290
# VARDARIS PANAGIOTIS 4590

state0 = 0
state1 = 1
state2 = 2
state3 = 3
state4 = 4
state5 = 5
state6 = 6
error = -1
OK = -2
i = 0
basicWords = ['program', 'if', 'declare', 'else', 'while', 'switchcase', 'forcase', 'incase', 'case', 'default', 'not', 'and', 'or', 'function', 'procedure', 'call', 'return', 'in', 'inout', 'input', 'print']
# eof = 10
flag = False  # this var is set by default at False and will be used in order to check if . has been found when EOF.It gets True value when . is read.
# When the reading finishes,there is an if to check if it's true.


#--------------------------------- LECTURAL ----------------------------------------
def lectural():
    global flag
    totalList = []  # this list will contain every recognized word/character
    currentWord = ""  # this is a temp string that will contain a word/char and when all digits of word/char are read then the string will be appended to toalLIst and then will be cleared
    file = open('factorial.ci', 'r')
    state = state0  # starting from state 0
    while (state != OK and state != error):  # as long as you dont finish or you dont find an error
        for line in file:  # read by line
            for char in line:  # read by char
                if (state == state0):  # if you're in state0
                    if (char == ' '):  # if you find blank just continue
                        print("i found blank!")
                    elif(char == ''):
                        print("i found blank!")
                    elif (char.isalpha() == True):  # if you find letter
                        state = state1  # then go to state1
                        currentWord = currentWord + char  # and add the char to currentWord
                        print("i am in 0,i read: ", char, " and i found a letter.State now is: ", state)
                    elif (char.isdigit() == True):  # if you find number
                        state = state2  # then go to state2
                        currentWord = currentWord + char  # and add the char to currentWord
                        print("i am in 0,i read: ", char, " and i found a number.State now is: ", state)
                    elif (char == '+'):  # if you find +
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == '-'):  # if you find -
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == '*'):  # if you find *
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == '/'):  # if you find /
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == '='):  # if you find =
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == '<'):  # if you find <
                        state = state3  # then go to state 3
                        currentWord = currentWord + char  # and add < to currentWord
                        print("i am in 0, i read: ", char)
                    elif (char == '>'):  # if you find >
                        state = state4  # then go to state 4
                        currentWord = currentWord + char  # and add > to currentWord
                        print("i am in 0, i read: ", char)
                    elif (char == ':'):  # if you find :
                        state = state5  # go to state 5
                        currentWord = currentWord + char  # and add : to currentWord
                        print("i am in 0, i read: ", char)
                    elif (char == '{'):  # if you find {
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == '}'):  # if you find }
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == ','):  # if you find ,
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == ';'):  # if you find ;
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == '('):  # if you find (
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == ')'):  # if you find )
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == '+'):  # if you find +
                        totalList.append(char)  # just add it directly to totalList
                        print("i am in 0, i read: ", char)
                    elif (char == '.'):  # if you find .
                        totalList.append(char)  # add it directly to totalList
                        state = OK  # change the state to OK
                        flag = True  # and change flag's value to True
                        print("i finished!")
                    elif (char == '#'):  # if you find a comment
                        break  # just break
                    elif (char == '\n'):  # if you find newline
                        continue  # just continue
                    elif (char == '\t'):  # if you find tab
                        continue  # just continue
                    else:  # if you dont find anything from above
                        state = error  # go to state error
                        print("i am in 0,i read:", char, " and i found an error!")
                elif (state == state1):  # if you're in state 1
                    if (char.isalpha() == True or char.isdigit() == True):  # if you find letter or digit
                        currentWord = currentWord + char  # then add the char to currentWord
                        print("i am in 1,i read: ", char, " and i found a letter or number.State now is: ", state)
                    else:  # if you find anything else
                        print("i read something else: ", char, " ,the final current word is: ", currentWord)
                        state = state0  # then go to state 0
                        totalList.append(currentWord)  # add the word in totalList
                        totalList.append(char)
                        currentWord = ""  # and clear the currentWord
                        # if(char != ' ' or char != ''):
                        # totalList.append(char)
                elif (state == state2):  # if you're in state 2
                    if (char.isdigit() == True):  # if you find digit
                        currentWord = currentWord + char  # then add the digit to currentWord
                        print("i am in 2 ,i read: ", char, " and i found a number.State now is: ", state)
                    else:  # if you find anything else
                        print("i read something else: ", char, " ,the final current word is: ", currentWord)
                        state = state0  # then go to state 0
                        totalList.append(currentWord)  # add the word to totalList
                        totalList.append(char)  # and add the current char directly to totalList
                        currentWord = ""
                elif (state == state3):  # if you're in state 3
                    if (char == '='):  # if you find =
                        state = state0  # then go to state 0
                        currentWord = currentWord + char  # add the char to currentWord
                        totalList.append(currentWord)  # add the currentWord to totalList
                        currentWord = ""  # and finally clear the currentWord
                    elif (char == '>'):  # if you find >
                        state = state0  # then go to state 0
                        currentWord = currentWord + char  # add the char to currentWord
                        totalList.append(currentWord)  # add the currentWord to totalList
                        currentWord = ""  # and finally clear the currentWord
                    else:  # if you find anything else
                        state = state0  # then go to state 0
                        totalList.append(currentWord)  # and add the word to totalList
                elif (state == state4):  # if you're in state 4
                    if (char == '='):  # if you find =
                        state = state0  # go to state 0
                        currentWord = currentWord + char  # add the char to currentWord
                        totalList.append(currentWord)  # add the word to totalList
                        currentWord = ""  # and finally clear the currentWord
                    else:  # if you find anything else
                        state = state0  # go to state 0
                        totalList.append(currentWord)  # and add the word to totalList
                elif (state == state5):  # if you're in state 5
                    if (char == '='):  # if you find =
                        state = state0  # go to state 0
                        #currentWord = currentWord + char  # add the char to currentWord
                        totalList.append(currentWord)  # add the word to totalList
                        totalList.append(char)
                        currentWord = ""  # and finally clear the currentWord
                    else:  # if you find anything else
                        state = error  # just go to state error
        if (flag == False):  # if flag is False which basically means that if whole file is read and . is not read
            state = error  # go to state error

    newList = []  # create a new list in order to delete all blanks,new lines etc
    for elem in totalList:  # run totalList
        # newList.append(elem.strip())
        if (elem.isspace() == False):  # if you dont find any blank element
            newList.append(elem.strip())  # then add the element to newList
    print('my list after is %s' % (newList))
    file.close()
    return newList

#--------------------------------- SYNTAX -------------------------------

def program():
    print("---i am in program---")
    global i
    if (file[i] == 'program'): #if you read program
        i += 1 #go to next word
        print("i am in program in if file[i] == 'program', new word is: ", file[i])
        id() #call id
        block() #call block
        if (file[i] == '.'): #if you read '.'
            print("Finished well!")
        else: #otherwise
            print("i am in program and '.' symbol is missing!")
    else: #if you dont read program
        print("i am in program and the keyword 'program' was expected!")

def blockstatements():
    print("---i am in blockstatements---")
    global i
    statement() #call statements
    def blockstatementsSubFunc(): #subfunction is used for (...)*
        global i
        if(file[i] == ';'): #if you find ;
            i+=1 #go to next word
            print("i am in blockstatementsSubFunc in file[i] == ';',new word is: ", file[i])
            statement() #call statement
            blockstatementsSubFunc() #call subfunction
    blockstatementsSubFunc() #call subfunction

def block():
    print("---i am in block---")
    global i
    if (file[i] == '{'): #if you read '{'
        i += 1 #go to next word
        print("i am in block == { and i found {,new word is: ", file[i])
        declarations() #call declarations
        subprograms() #call subprograms
        blockstatements() #call blockstatements
        if (file[i] == '}'): #if you read '}'
            i += 1 #go to next word
            print("i am in block and i found },new word is: ", file[i])
        else: #if you dont find '}'
            print("i am in block and you didn't close the block, '}' is missing!")
    else: #if you don't find {
        print("i am in block and '{' is missing!")

def id():
    print("---i am in id---")
    global i
    if ((file[i][0].isalpha() == True) and ((file[i][h].isalpha() == True) or (file[i][h].isdigit() == True) for h in range(1, (len(file[i])-1))) and (file[i] not in basicWords)):
        #for the above if: if first char is letter and the rest are letters or digits and if the whole word isnt a reserved word(if,for etc)
        i+=1 #go to next word
        print("i am in ID and i found that '",file[i-1],"' is OK,new word is: ", file[i])
    elif(len(file[i]) > 30): #if you find length more than 30 characters
        print("id cannot be more than 30 characters!")
    else: #otherwise id is not correct
        print("ID has a problem!")

def declarations():
    print("---i am in declarations---")
    global i
    if (file[i] == 'declare'): #if you read 'declare' word
        i += 1 #go to next word
        print("i am in declarations in file[i] == declare,new word is: ", file[i])
        varlist() #call varlist
        if (file[i] == ';'): #if you read ';'
            i += 1 #go to next word
            print("i am in declarations in file[i] == ;,new word is: ", file[i])
            declarations() #call declarations
        else: #if you dont find ;
            print("i am in declarations and ';' symbol is missing")

def varlist():
    print("---i am in varlist---")
    global i
    if ((file[i][0].isalpha() == True) and ((file[i][h].isalpha() == True) or (file[i][h].isdigit() == True) for h in range(1, (len(file[i]) - 1))) and (file[i] not in basicWords)):
        #for the above if: similar with 218 line,if you find ID
        id()    #call id
        def varlistSubFunc(): #subfunction for ( , ID)*
            global i
            if (file[i] == ','): #if you find ','
                i += 1 #go to next word
                print("i am in varlistSubFunc in file[i] == , ,new word is: ", file[i])
                id() #call id
                varlistSubFunc() #call call subfunction

        varlistSubFunc() #call subfunction

def subprograms():
    print("----i am in subprograms---")
    global i
    def subprogramsSubFunc(): #subfunction for (subprogram)*
        global i
        if((file[i] == 'function') or (file[i] == 'procedure')): #if you find function or procedure call subprogram but DONT do i+=1 because...
            #...we want to go on subprogram with the same word(function or procedure) and do the job there
            subprogram() #call subprogram
            subprogramsSubFunc() #call subfunction
    subprogramsSubFunc() #call subfunction

def subprogram():
    print("---i am in subprogram---")
    global i
    if (file[i] == 'function'): #if you read 'function'
        i += 1 #go to next word
        print("(function)i am in subprogram in file[i] == 'function',new word is: ", file[i])
        id() #call id
        if (file[i] == '('): #if you read '('
            i += 1 #go to next word
            print("(function)i am in subprogram in file[i] == '(',new word is: ", file[i])
            formalparlist() #call formalparlist
            if (file[i] == ')'): #if you read ')'
                i += 1 #go to next word
                print("(function)i am in subprogram in file[i] == ')',new word is: ", file[i])
                block() #call block
            else: #if you dont read ')'
                print("i am in subprogram in function and ')' is missing!")
        else:
            print("i am in subprogram in function and '(' is missing!")
    elif (file[i] == 'procedure'): #else if you read 'procedure'
        i += 1 #go to next word
        print("(procedure)i am in subprogram in file[i] == 'procedure',new word is: ", file[i])
        id() #call id
        if (file[i] == '('): #if you read '('
            i += 1 #go to next word
            print("(procedure)i am in subprogram in file[i] == '(' ,new word is: ", file[i])
            formalparlist() #call formalparlist
            if (file[i] == ')'): #if you find ')'
                i += 1 #go to next word
                print("(procedure)i am in subprogram in file[i] == ')' ,new word is: ", file[i])
                block() #call block
            else:
                print("i am in subprogram in procedure and ')' is missing!")
        else:
            print("i am in subprogram in procedure'(' is missing!")
    else:
        print("i am in subprogram and i was expecting function or procedure!")

def formalparlist():
    print("---i am in formalparlist---")
    global i
    if (file[i] == 'in') or (file[i] == 'inout'): #if you read 'in' or 'inout'
        formalparitem() #call formalparitem
        def formalparlistSubFunc(): #subfunction for ( , formalparitem)*
            global i
            if (file[i] == ','): #if you read ','
                i += 1 #go to next word
                print("i am in formalparlistSubFunc in file[i] == ',' ,new word is: ", file[i])
                formalparitem() #call formalparitem
                formalparlistSubFunc() #call subfunction
        formalparlistSubFunc() #call subfunction

def formalparitem():
    print("---i am in formalparitem---")
    global i
    if(file[i] == 'in'): #if you read 'in'
        i+=1 #go to next word
        print("(in) i am in formalparitem in file[i] == 'in',new word is: ", file[i])
        id() #call id
    elif(file[i] == 'inout'): #else if you read inout
        i += 1 #go to next word
        print("(inout) i am in formalparitem in file[i] == 'in',new word is: ", file[i])
        id() #call id
    else: #if you dont read 'in' or 'inout'
        print("i am in formalparitem,expected in or inout!")

def statements():
    print("---i am in statements---")
    global i
    if ((file[i][0].isalpha() == True) and ((file[i][h].isalpha() == True) or (file[i][h].isdigit() == True) for h in range(1, (len(file[i])-1))) and (file[i] not in basicWords)):
        print("i am in statements in file[i] == ID")
        id()
        if(file[i] == ';'): #if you find ';'
            i+=1 #go to next word
            print("i am in statements in file[i] == ID in file[i] == ';',new word is: ",file[i])
    elif(file[i] == 'if'):
        print("i am in statements in file[i] == ifStat")
        ifStat()
        if (file[i] == ';'): #if you find ';'
            i += 1 #go to next word
            print("i am in statements in file[i] == if in file[i] == ';',new word is: ", file[i])
    elif (file[i] == 'while'):
        print("i am in statements in file[i] == whileStat")
        whileStat()
        if (file[i] == ';'):  # if you find ';'
            i += 1  # go to next word
            print("i am in statements in file[i] == while in file[i] == ';',new word is: ", file[i])
    elif (file[i] == 'switchcase'):
        print("i am in statements in file[i] == switchcaseStat")
        switchcaseStat()
        if (file[i] == ';'):  # if you find ';'
            i += 1  # go to next word
            print("i am in statements in file[i] == switchcase in file[i] == ';',new word is: ", file[i])
    elif (file[i] == 'forcase'):
        print("i am in statements in file[i] == forcaseStat")
        forcaseStat()
        if (file[i] == ';'):  # if you find ';'
            i += 1  # go to next word
            print("i am in statements in file[i] == forcase in file[i] == ';',new word is: ", file[i])
    elif (file[i] == 'incase'):
        print("i am in statements in file[i] == incaseStat")
        incaseStat()
        if (file[i] == ';'):  # if you find ';'
            i += 1  # go to next word
            print("i am in statements in file[i] == incase in file[i] == ';',new word is: ", file[i])
    elif (file[i] == 'call'):
        print("i am in statements in file[i] == callStat")
        callStat()
        if (file[i] == ';'):  # if you find ';'
            i += 1  # go to next word
            print("i am in statements in file[i] == call in file[i] == ';',new word is: ", file[i])
    elif (file[i] == 'return'):
        print("i am in statements in file[i] == returnStat")
        returnStat()
        if (file[i] == ';'):  # if you find ';'
            i += 1  # go to next word
            print("i am in statements in file[i] == return in file[i] == ';',new word is: ", file[i])
    elif (file[i] == 'input'):
        print("i am in statements in file[i] == input")
        inputStat()
        if (file[i] == ';'):  # if you find ';'
            i += 1  # go to next word
            print("i am in statements in file[i] == input in file[i] == ';',new word is: ", file[i])
    elif (file[i] == 'print'):
        print("i am in statements in file[i] == print")
        printStat()
        if (file[i] == ';'):  # if you find ';'
            i += 1  # go to next word
            print("i am in statements in file[i] == print in file[i] == ';',new word is: ", file[i])
    elif(file[i] == '{'): #if you read '{'
        i+=1 #go to next word
        print("i am in statements in file[i] == '{',new word is: ", file[i])
        statement() #call statement
        def statementsSubFunc(): #subfunction for ( ; statement )*
            global i
            if(file[i] == ';'): #if you read ';'
                i+=1 #go to next word
                print("i am in statementsSubFunc in file[i] == ';',new word is: ", file[i])
                statement() #call statement
                statementsSubFunc() #call subfunction
        statementsSubFunc() #call subfunction
        if(file[i] == '}'): #if you read '}'
            i+=1 #go to next word
            print("i am in statements in file[i] == '}',new word is: ", file[i])
        else: #if you dont read '}'
            print("i am in statements and } is missing!")

def statement():
    print("---i am in statement---")
    global i
    if ((file[i][0].isalpha() == True) and ((file[i][h].isalpha() == True) or (file[i][h].isdigit() == True) for h in range(1, (len(file[i])-1))) and (file[i] not in basicWords)):
        #for the above if: if it's ID then call assignStat
        print("i am in statement in assignStat if")
        assignStat() #call assignStat
    elif file[i] == 'if': #if you read 'if'
        print("i am in statement in ifStat if")
        ifStat() #call ifStat
    elif (file[i] == 'while'): #else if you read 'while'
        print("i am in statement in whileStat if")
        whileStat() #call whileStat
    elif (file[i] == 'switchcase'): #else if you read 'switchcase'
        print("i am in statement in switchcaseStat if")
        switchcaseStat() #call 'switchcaseStat'
    elif (file[i] == 'forcase'): #else if you read 'forcase'
        print("i am in statement in forStat if")
        forcaseStat() #call forcaseStat
    elif (file[i] == 'incase'): #else if you read 'incase'
        print("i am in statement in incaseStat if")
        incaseStat() #call incaseStat
    elif (file[i] == 'call'): #else if you read 'call'
        print("i am in statement in callStat if")
        callStat() #call callStat
    elif (file[i] == 'return'): #else if you read 'return'
        print("i am in statement in returnStat if")
        returnStat() #call returnStat
    elif (file[i] == 'input'): #else if you read 'input'
        print("i am in statement in inputStat if")
        inputStat() #call inputStat
    elif (file[i] == 'print'): #else if you read 'print'
        print("i am in statement in printStat if")
        printStat() #call printStat


def assignStat():
    print("---i am in assignStat---")
    global i
    id() #call id
    if(file[i] == ':'): #if you read ':'
        i+=1 #go to next word
        print("i am in assignStat in file[i] == ':',new word is: ", file[i])
        if(file[i] == '='): #if you read '='
            i+=1 #go to next word
            print("i am in assignStat in file[i] == '=',new word is: ", file[i])
            expression() #call expression
        else: #if you dont find '='
            print("i am in assignStat and = is missing!")
    else: #if you dont inf ':"
        print("i am in assignStat and : is missing!")

def ifStat():
    print("---i am in ifStat---")
    global i
    if(file[i] == 'if'): #if you read 'if'
        i+=1 #go to next word
        print("i am in ifStat in file[i] == 'if',new word is: ", file[i])
        if(file[i] == '('): #if you read '('
            i+=1 #go to next word
            print("i am in ifStat in file[i] == '(',new word is: ", file[i])
            condition() #call condition
            if(file[i] == ')'): #if you read ')'
                i+=1 #go to next word
                statements() #call statements
                elsepart() #call elsepart
            else: #if you dont read ')'
                print("i am in ifStat and ')' is missing!")
        else: #if you dont read '('
            print("i am in ifStat and '(' is missing!")
    else: #if you dont read 'if'
        print("i am in ifStat and 'if' is missing!")

def elsepart():
    print("---i am in elsepart---")
    global i
    if(file[i] == 'else'): #if you read 'else'
        i+=1 #go to next word
        print("i am in elsepart in file[i] == 'else',new word is: ", file[i])
        statements() #call statements

def whileStat():
    print("---i am in whileStat---")
    global i
    if(file[i] == 'while'): #if you read 'while'
        i+=1 #go to next word
        print("i am in whileStat in file[i] == 'while',new word is: ", file[i])
        if(file[i] == '('): #if you read '('
            i+=1 #go to next word
            print("i am in whileStat in file[i] == '(',new word is: ", file[i])
            condition() #call condition
            if(file[i] == ')'): #if you read ')'
                i+=1 #go to next word
                print("i am in whileStat in file[i] == ')',new word is: ", file[i])
                statements() #call statements
            else: #if you don't read ')'
                print("i am in whileStat and ')' is missing!")
        else: #if you don't read '('
            print("i am in whileStat and '(' is misssing!")
    else: #if you don't read 'while'
        print("i am in whileStat and 'while' is missing!")

def switchcaseStat():
    print("---i am in switchcaseStat---")
    global i
    if(file[i] == 'switchcase'): #if you read 'switchcase'
        i+=1 #go to next word
        print("i am in switchcaseStat in file[i] == 'switchcase',new word is: ", file[i])
        def switchcaseStatSubFunc(): #subfunction for ( case ( condition ) statements )*
            global i
            if(file[i] == 'case'): #if you read 'case'
                i+=1 #go to next word
                print("i am in switchcaseStatSubFunc in file[i] == 'case',new word is: ", file[i])
                if(file[i] == '('): #if you read '('
                    i+=1 #go to next word
                    print("i am in switchcaseStatSubFunc in file[i] == '(',new word is: ", file[i])
                    condition() #call condition
                    if(file[i] == ')'): #if you read ')'
                        i+=1 #go to next word
                        print("i am in switchcaseStatSubFunc in file[i] == ')',new word is: ", file[i])
                        statements() #call statements
                        switchcaseStatSubFunc() #call subfunction
                    else: #if you don't read ')'
                        print("i am in switchcaseStatSubFunc and ')' is missing!")
                else: #if you dont read '('
                    print("i am in switchcaseStatSubFunc and '(' is missing!")
        switchcaseStatSubFunc() #call subfunction
        if(file[i] == 'default'): #if you read 'default'
            i+=1 #go to next word
            print("i am in switchcaseStat in file[i] == 'default',new word is: ", file[i])
            statements() #call statements
        else: #if you don't read 'default'
            print("i am in switchcaseStat and default is missing!")
    else: #if you don't read 'switchcase'
        print("i am in switchcaseStat and 'switchcase' is missing!")

def forcaseStat():
    print("---i am in forcaseStat---")
    global i
    if(file[i] == 'forcase'): #if you read 'forcase'
        i+=1 #go to next word
        print("i am in forcaseStat in file[i] == 'forcase',new word is: ", file[i])
        def forcaseStatSubFunc(): #subfunction for ( case ( condition ) statements )*
            global i
            if(file[i] == 'case'): #if you read 'case'
                i+=1 #go to next word
                print("i am in forcaseStatSubFunc in file[i] == 'case',new word is: ", file[i])
                if(file[i] == '('): #if you read '('
                    i+=1 #go to next word
                    print("i am in forcaseStatSubFunc in file[i] == '(',new word is: ", file[i])
                    condition() #call condition
                    if(file[i] == ')'): #if you read ')'
                        i+=1 #go to next word
                        print("i am in forcaseStatSubFunc in file[i] == ')',new word is: ", file[i])
                        statements() #call statements
                        forcaseStatSubFunc() #call subfunction
                    else: #if you don't read ')'
                        print("i am in forcaseStatSubFunc and ')' is missing!")
                else: #if you don't read '('
                    print("i am in forcaseStatSubFunc and '(' is missing!")
        forcaseStatSubFunc() #call subfunction
        if (file[i] == 'default'): #if you read 'default'
            i += 1 #go to next word
            print("i am in forcaseStat in file[i] == 'default',new word is: ", file[i])
            statements() #call statements
        else: #if you dont read 'default'
            print("i am in forcaseStat and default is missing!")
    else: #if you don't read 'forcase'
        print("i am in forcaseStat and 'switchcase' is missing!")

def incaseStat():
    global i
    print("---i am in incaseStat---")
    if (file[i] == 'incase'): #if you read 'incase'
        i += 1 #go to next word
        print("i am in incaseStat in file[i] == 'incase',new word is: ", file[i])
        def incaseStatSubFunc(): #subfunction for  ( case ( condition ) statements )*
            global i
            if (file[i] == 'case'): #if you read 'case'
                i += 1 #go to next word
                print("i am in incaseStatSubFunc in file[i] == 'case',new word is: ", file[i])
                if (file[i] == '('): #if you read '('
                    i += 1 #go to next word
                    print("i am in incaseStatSubFunc in file[i] == '(',new word is: ", file[i])
                    condition() #call condition
                    if (file[i] == ')'): #if you read ')'
                        i += 1 #go to next word
                        print("i am in incaseStatSubFunc in file[i] == ')',new word is: ", file[i])
                        statements() #call statements
                        incaseStatSubFunc() #call subfunction
                    else: #if you don't read ')'
                        print("i am in incaseStatSubFunc and ')' is missing!")
                else: #if you dont read '('
                    print("i am in incaseStatSubFunc and '(' is missing!")
        incaseStatSubFunc() #call subfunction
    else:
        print("i am in incaseStat and 'switchcase' is missing!")

def returnStat():
    print("---i am in returnStat---")
    global i
    if(file[i] == 'return'): #if you read 'return'
        i+=1 #go to next word
        print("i am in returnStat in file[i] == 'return',new word is: ", file[i])
        if(file[i] == '('): #if you read '('
            i+=1 #go to next word
            print("i am in returnStat in file[i] == '(',new word is: ", file[i])
            expression() #call expression
            if(file[i] == ')'): #if you read ')'
                i+=1 #go to next word
                print("i am in returnStat in file[i] == ')',new word is: ", file[i])
            else: #if you dont read ')'
                print("i am in returnStat and ')' is missing! ")
        else: #if you dont read '('
            print("i am in returnStat and '(' is missing! ")
    else: #if you dont read 'return'
        print("i am in returnStat and 'return' is missing! ")

def callStat():
    print("---i am in callStat---")
    global i
    if (file[i] == 'call'): #if you read 'call'
        i += 1 #go to next word
        print("i am in callStat in file[i] == 'return',new word is: ", file[i])
        id() #call id
        if (file[i] == '('): #if you read '('
            i += 1 #go to next word
            print("i am in returnStat in file[i] == '(',new word is: ", file[i])
            actualparlist() #call actualparlist
            if (file[i] == ')'): #if you read ')'
                i += 1 #go to next word
                print("i am in returnStat in file[i] == '(',new word is: ", file[i])
            else: #if you dont read ')'
                print("i am in returnStat and ')' is missing! ")
        else: #if you dont read '('
            print("i am in returnStat and '(' is missing! ")
    else: #if you dont read 'call'
        print("i am in returnStat and 'return' is missing! ")

def printStat():
    print("---i am in printStat---")
    global i
    if (file[i] == 'print'): #if you read 'print'
        i += 1 #go to next word
        print("i am in printStat in file[i] == 'file',new word is: ", file[i])
        if (file[i] == '('): #if you read '('
            i += 1 #go to next word
            print("i am in printStat in file[i] == '(',new word is: ", file[i])
            expression() #call expression
            if (file[i] == ')'): #if you read ')'
                i += 1 #go to next word
                print("i am in printStat in file[i] == '(',new word is: ", file[i])
            else: #if you dont read ')'
                print("i am in printStat and ')' is missing! ")
        else: #if you dont read '('
            print("i am in printStat and '(' is missing! ")
    else: #if you dont read 'print'
        print("i am in printStat and 'print' is missing! ")

def inputStat():
    print("---i am in inputStat---")
    global i
    if (file[i] == 'input'): #if you read 'input'
        i += 1 #go to next word
        print("i am in inputStat in file[i] == 'input',new word is: ", file[i])
        if (file[i] == '('): #if you read '('
            i += 1 #go to next word
            print("i am in inputStat in file[i] == '(',new word is: ", file[i])
            id() #call id
            if (file[i] == ')'): #if you read ')'
                i += 1 #go to next word
                print("i am in inputStat in file[i] == ')',new word is: ", file[i])
            else: #if you dont read ')'
                print("i am in inputStat and ')' is missing! ")
        else: #if you dont read '('
            print("i am in inputStat and '(' is missing! ")
    else: #if you dont read 'input'
        print("i am in inputStat and 'input' is missing! ")

def actualparlist():
    print("---i am in actualparlist---")
    global i
    if((file[i] == 'in') or (file[i] == 'inout')): #if you read 'in' or 'inout'
        actualparitem() #call actualparitem
        def actualparlistSubFunc(): #subfunction for ( , actualparitem )*
            global i
            if(file[i] == ','): #if you read ','
                i+=1 #go to next word
                print("i am in actualparlistSubFunc in file[i] == ',',new word is: ", file[i])
                actualparitem() #call actualparitem
                actualparlistSubFunc() #call subfunction
        actualparlistSubFunc() #call subfunction

def actualparitem():
    print("---i am in actualparitem---")
    global i
    if(file[i] == 'in'): #if you read 'in'
        i+=1 #go to next word
        print("i am in actualparitem in file[i] == 'in',new word is: ", file[i])
        expression() #call expression
    elif(file[i] == 'inout'): #else if you read 'inout'
        i += 1 #go to next word
        print("i am in actualparitem in file[i] == 'in',new word is: ", file[i])
        id() #call id

def condition():
    print("---i am in condition---")
    global i
    boolterm() #call boolterm
    def conditionSubFunc(): #subfunction for ( or boolterm )*
        global i
        if(file[i] == 'or'): #if you read 'or'
            i+=1 #go to next word
            print("i am in conditionSubFunc in file[i] == 'or',new word is: ", file[i])
            boolterm() #call boolterm
            conditionSubFunc() #call subfunction
    conditionSubFunc() #call subfunction

def boolterm():
    print("---i am in boolterm---")
    global i
    boolfactor() #call boolfactor
    def booltermSubFunc(): #subfunction for ( and boolfactor )*
        global i
        if(file[i] == 'and'): #if you read 'and'
            i+=1 #go to next word
            print("i am in booltermSubFunc in file[i] == 'and',new word is: ", file[i])
            boolfactor() #call boolfactor
            booltermSubFunc() #call subfunction
    booltermSubFunc() #call subfunction

def boolfactor():
    print("---i am in boolfactor---")
    global i
    if(file[i] == 'not'): #if you read 'not'
        i+=1 #go to next word
        print("i am in boolfactor in file[i] == 'not',new word is: ", file[i])
        if(file[i] == '['): #if you read '['
            i+=1 #go to next word
            print("i am in boolfactor in file[i] =='[',new word is: ", file[i])
            condition() #call condition
            if(file[i] == ']'): #if you read ']'
                i+=1 #go to next word
                print("i am in boolfactor in file[i] ==']',new word is: ", file[i])
            else: #if you dont read ']'
                print("i am in boolfactor and i was expecting a ']'!")
        else: #if you dont read '['
            print("i am in boolfactor and i i was expecting a '['!")
    elif (file[i] == '['): #else if you read '['
        i += 1 #go to next word
        print("i am in boolfactor in file[i] =='[',new word is: ", file[i])
        condition() #call condition
        if (file[i] == ']'):#if you read ']'
            i += 1 #go to next word
            print("i am in boolfactor in file[i] ==']',new word is: ", file[i])
        else: #if you dont read ']'
            print("i am in boolfactor and i was expecting a ']'!")
    elif((file[i] == '+') or (file[i] == '-') or (file[i].isdigit() == True) or (file[i] == '(') or (file[i].isalpha() == True)):
        #the above if is expression which could be optionalSign or term.OptionalSign could be either + or - and term could start...
        #...with either integer or ( or letter.If you find any of these,dont do i+=1 but just call expression
        print("i am in third if in boolfactor with file[i]: ", file[i])
        expression() #call expression
        REL_OP() #call REL_OP
        expression() #call expression

def expression():
    global i
    print("---i am in expression--- with file[i]: ", file[i])
    optionalSign() #call optionalSign
    term() #call term
    def expressionSubFunc(): #subfunction for ( ADD_OP term )*
        global i
        print("BABUSKAAA: ", file[i])
        if(file[i] == '-'):
            i+=1 #go to next word
            print("i am in expressionSubFunc in file[i] == '-',new word is: ", file[i])
            term() #call term
            expressionSubFunc() #call subfunction
        elif(file[i] == '+'):
            i+=1  # go to next word
            print("i am in expressionSubFunc in file[i] == '+',new word is: ", file[i])
            term()  # call term
            expressionSubFunc()  # call subfunction
        print("BABUSKAAA2: ", file[i])
    expressionSubFunc() #call subfunction

def term():
    print("---i am in term---")
    global i
    factor() #call factor
    def termSubFunc(): #subfunction for ( MUL_OP factor )*
        global i
        if (file[i] == '*') or (file[i] == '/'): #if you read '*' or '/'
            i+=1 #go to next word
            print("i am in term in file[i] == '*' or file[i] == '/'),new word is: ", file[i])
            factor() #call factor
            termSubFunc() #call subfunction
    termSubFunc() #call subfunction

def factor():
    print("---i am in factor---")
    global i
    if(file[i].isdigit() == True): #if you read number
        i+=1 #go to next word
        print("i am in factor in file[i].isdigit() == True,new word is: ",file[i])
    elif(file[i] == '('): #if you read '('
        i+=1 #go to next word
        print("i am in factor in file[i] == '(',new word is: ", file[i])
        expression()
        if(file[i] == ')'):
            i+=1
            print("i am in factor in file[i] == '(',new word is: ", file[i])
    elif((file[i][0].isalpha() == True) and ((file[i][h].isalpha() == True) or (file[i][h].isdigit() == True) for h in range(1, (len(file[i]) - 1))) and (file[i] not in basicWords)):
        # for the above if: if first char is letter and the rest are letters or digits and if the whole word isnt a reserved word(if,for etc)
        print("i am in factor in file[i] == ID")
        id()
        idtail() #call idtail
    else: #if you dont find anything from above
        print("i am in factor and i was expecting integer or (expression) or ID idtail!")

def idtail():
    print("---i am in idtail---")
    global i
    if(file[i] == '('): #if you read '('
        i+=1 #go to next word
        print("i am in idtail in file[i] == '(',new word is: ",file[i])
        actualparlist() #call actualparlist
        if(file[i] == ')'): #if you read ')'
            i += 1 #go to next word
            print("i am in idtail in file[i] == ')',new word is: ", file[i])
        else: #if you dont find ')'
            print("i am in idtail and i was expecting )!")

def optionalSign():
    print("---i am in optionalSign---")
    global i
    if ((file[i] == '+') or (file[i] == '-')): #if you read '+' or '-'
        i += 1 #go to next word
        print("i am in optionalSign in if,new word is: ", file[i])


def REL_OP():
    print("---i am in REL_OP---")
    global i
    if((file[i] == '=')):
        #for the above if: if you read '=' or '<=' or '>=' or '>' or '<' or '<>'
        i+=1 #go to next word
        print("i am in REL_OP in big if,new word is: ", file[i])
    elif(file[i] == '<'):
        i+=1
        print("i am in REL_OP in if file[i] == '<',new word is: ",file[i])
        if(file[i] == '='):
            i+=1
            print("i am in REL_OP in file[i] == '<=',new word is: ",file[i])
        elif(file[i] == '>'):
            i+=1
            print("i am in REL_OP in file[i] == '<>',new word is: ",file[i])
    elif(file[i] == '>'):
        i+=1
        print("i am in REL_OP in if file[i] == '>',new word is: ", file[i])
        if (file[i] == '='):
            i += 1
            print("i am in REL_OP in file[i] == '>=',new word is: ", file[i])
    else: #if you dont find anything from above
        print("i am in REL_OP and i found a symbol different than the above!")

def ADD_OP():
    print("---i am in ADD_OP---")
    global i
    if((file[i] == '+') or (file[i] == '-')): #if you read '+' or '-'
        i+=1 #go to next word
        print("i am in ADD_OP in file[i] == '+' or file[i] == '-',new word is: ", file[i])
    else: #if you dont read '+' or '-'
        print("i am in ADD_OP and found string different than '+' or '-'!")

def MUL_OP():
    print("---i am in MUL_OP---")
    global i
    if((file[i] == '*') or (file[i] == '/')): #if you read '*' or '/'
        i+=1 #go to next word
        print("i am in MUL_OP in file[i] == '*' or file[i] == '/',new word is: ", file[i])
    else: #if you dont read '*' or '/'
        print("i am in MUL_OP and found string different than '*' or '/'!")

def INTEGER():
    print("---i am in INTEGER---")
    global i
    if(file[i].isdigit() == True): #if you read number
        i+=1 #go to next word
        print("i am in INTEGER in file[i].isdigit() == True,new word is: ", file[i])
    else: #if you dont read number
        print("i am in INTEGER and string cannot be different than digit!")



def syntax(file): #
    program() #program is called

######--------INTERMEDIATE CODE-------##########
#list = []

#def nextquad(list):
 #   return (len(list))

#def genquad(op,x,y,z):
 #   array = [op,x,y,z]
  #  list.append(array)

#def newtemp():
 #   global

#T_1 = newtemp()
#######------ MAIN ------########
file = lectural() #here lectural runs
print("-----------------------------------------------------------------------")
syntax(file) #here syntactical runs
#genquad()