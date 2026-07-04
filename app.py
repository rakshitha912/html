#text is witeen in  " " or ' '
print("hio"); 
print("hii");
print("Hello World!");
print("Hello World!");
print("Hello World!");
print("Hello World!");
print("This will work!");
# for new next line to appear in same line use end="" so that it prints in same line
print("This will work!", end=" ");
print("This will work!");
print("This will work!");
# numbers r written withpuit quotes
print(3);
print(358);
# for adding   of number normal addition is used
print(3+4);
print(3+3+7);
# BY ASSIGNING A VARIABLE 
#(variable r containers for storinfg data values)
X=5;
Y=10;
print(X+Y);

#This is a single line comment
#FOR ADDING TEXT AND NUYMBERS TOGETHER, it can be done by serrprating with comma
print("I am ", 23,"years old.");
# Write a single-line comment

# Comment out this line so it does not run:


# This is a multiline comment
"""This is a multiline comment"""
#casting  is a proces  of specifying the data type of the variable 
x=str(3);
y=int(3);
z=float(3);
#to print
print(X);
print(Y);
print(z);
# strings can be declare din a single or double quotes
x="hi";
y='hi';
print(x+y)   # both r same 


a=3
A=5
#a will not overwrite A because python is case sensitive

# variabe must start with only letters, or underscore there cnnot be space or special character between them.
# IT CAN CONTAIN alphabets, numbers, underscores int it
# in it we can asign multiple vales to multiple vvariables or asign same vale to multiple variable 

# example:assign multiple values to multiple variables
x,y,z="orange","banana","cherry"
#printof multiple vsroable can be done using comma in between them.

print(x,y,z)
# assign same value to ,ultiple variables
x=y=z="orange"
print(x,y,z)
#print the variable are usually dont by putting inside print 
x="hi"
print(x)
# can add multiple variable by assigning the = operator to them
x="hi"
y="hello"
z="world"
print(x+y+z)
print(x,y,z)  # this will print in same line with space between them

# global variable can be used inside a function by using the global keyword
x="hlo"
def myfun():
  
    print("hi"+x)
    myfun()
x="hi"
def myfun1():
    x="hi"
    print("hi" +x)
    myfun1()
    print("hi"+ x)