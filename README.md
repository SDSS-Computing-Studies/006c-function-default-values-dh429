## SDSS Computing Studies Python Assignment
### Assignment #005d Function Default Parameters (Total Marks 10)

Objectives:
* Create default values for Function Parameters
* Send input parameters to a function in the order that is different from the input parameter definition

<Description>

### 4 Tasks

##### Task 1
Create a function called sentence() that takes 3 input paremters:
greeting: string that will contain a salutation, examples: Hello, Hiya, Ola
name: a string that will contain a person's name.  This should have a default value of "Benjamin"
question: a string that will contain a full question to ask the person.  It should have a default value of "How are you"

Have the greeting, name and question combine together into a string. Note: You are not using a print statement, so you must
use the concatenate (+) operator. Make sure your spacing is appropriate.

return value:
string. The output sentence

example assertion:
assert sentence("Hello") == "Hello Benjamin. How are you"
assert sentence("Hiya","Casey","Have you enjoyed your meal") == "Hiya Casey. Have you enjoyed your meal"

(2 points) 

##### Task 2
Create a function called multiplication that takes 2 input paremeters:
number: integer.  
end: integer. It should have a default value of 12.

The function will create a list that stores the multiplication tables for the number, and ends at end.

return value:
list.  The multiplication tables starting at a multiple of 1 and ending at whatever the default value is.

example assertion:
assert multiplication(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
assert multiplication(2,5) == [2, 4, 6, 8, 10]

(2 points)

##### Task 3
Create a function called title that creates a single line of output to display the word
"Title" with a box around it.  
The function will have 1 optional input:
symbol : string.  The symbolt to use as the border. Default symbol is "="

The return value is the output string with escaped line breaks.

example assertion:
assert title("*") == "*********\n* Title *\n*********"
assert title() == "=========\n= Title =\n========="
(2 points)
