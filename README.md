# PotatoScript
PotatoScript is a stack-based programming laungage utelising **RPN** (Reverse Polish Notation), this creats a intresting dynamic where the interpeter does not see any difference between a whitespace, newline or tab, this makes it so that you can format the code however you want.

PotatoScript uses .ptsc files

## Syntax
### Mathimatical operators
<P>+ - Addition</P>
<P>- - Subtraction</P>
<P>/ - Division</P>
<P>* - Multiplication</P>
<P>^ - To the power off</P>
<P>! - Factorial</P>

### Constants
PotatoScript has some built in constants that can be used, **Note** that they can be used alongside variables. These are:

g - 9.82

e - 2.71828

pi - 3.141592

### Variables
Variables is declared whit **'** before the variable name.

    'x 2 store --> Stores 2 in the varibale x

### Strings
Strings are detected by starting and ending them whit **|**, but do to the design of PotatoScript makes it so that a string is ended when you have a whitespace

    |HelloWorld| --> This is a valid string

### Operators
print - Prints the top value on the stack

    2 print -->This would print 2

print[n] - Prints the **n** value on the stack

    2 print[n] --> This would print the second value on the stack

clear - Clears the stack of all data

store - Store is used to store data in varibales

load - Loads the value of a varibale, this is needed to use it in a program

    'x load --> Loads the value of the varibale x into the stack

round - Rounds nubers to integers, as by default numbers are appended as floats

input - Accept nummeric or boolean inputs

dump - Prints out evrything in the stack, varibale array and token list
<br>**Note**: This made to be used as a debugging feature

stack-dump - Prints out only the stack
<br>**Note**: This made to be used as a debugging feature

var-dump - Prints out all variables
<br>**Note**: This made to be used as a debugging feature

dup - Dupplicates the top value of the stack

swap - Swaps the two topvalues of the stack

drop - Drops the top value of the stack

= - Returns a true or false deppening on if the two evaluated values are equal or not

    2 2 = --> Return True
    1 2 = --> Returns False

< - Returns true or false depednig if the first value is smaller or bigger then the second

    2 1 < --> Returns False
    1 2 < --> Returns True

<p>> - Returns true or false depednig if the first value is smaller or bigger then the second</p> 

    2 1 > --> Returns True
    1 2 > --> Returns False

if - Is executed if the top value in the stack is True

    2 2 = if
        2 2 + print
    end

end - Marks the end of a if statment

rand - Takes two arguments and generate a random number between them

    1 5 rand

randint - Takes two arguments and generates an integer between them

    1 5 randint

