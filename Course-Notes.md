
**Chapter 2**

#Introspection
Using a question mark (?) before or after a variable will display some general infor‐
mation about the object:
In [8]: b = [1, 2, 3]
In [9]: b?


##Terminal Keyboard Shortcuts

Ctrl-P or up-arrow Search backward in command history for commands starting with currently entered text
Ctrl-N or down-arrow Search forward in command history for commands starting with currently entered text
Ctrl-R Readline-style reverse history search (partial matching)
Ctrl-Shift-V Paste text from clipboard
Ctrl-C Interrupt currently executing code
Ctrl-A Move cursor to beginning of line
Ctrl-E Move cursor to end of line
Ctrl-K Delete text from cursor until end of line
Ctrl-U Discard all text on current line
Ctrl-F Move cursor forward one character
Ctrl-B Move cursor back one character

#Operations

a + b Add a and b
a - b Subtract b from a
a * b Multiply a by b
a / b Divide a by b
a // b Floor-divide a by b, dropping any fractional remainder
a ** b Raise a to the b power
a & b True if both a and b are True; for integers, take the bitwise AND
a | b True if either a or b is True; for integers, take the bitwise OR
a ^ b For booleans, True if a or b is True, but not both; for integers, take the bitwise EXCLUSIVE-OR

#Lists
In [64]: s = 'python'
In [65]: list(s)
Out[65]: ['p', 'y', 't', 'h', 'o', 'n']


##Control Flow

if, elif, and else
The if statement is one of the most well-known control flow statement types. It
checks a condition that, if True, evaluates the code in the block that follows:
if x < 0:
 print('It's negative')
An if statement can be optionally followed by one or more elif blocks and a catchall else block if all of the conditions are False:
if x < 0:
 print('It's negative')
elif x == 0:
 print('Equal to zero')
elif 0 < x < 5:
 print('Positive but smaller than 5')
else:
 print('Positive and larger than or equal to 5')
 
 ##For loops
 
 sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
 if value == 5:
 break
 total_until_5 += value
 
 #While Loops
 
 while loops
A while loop specifies a condition and a block of code that is to be executed until the
condition evaluates to False or the loop is explicitly ended with break:
x = 256
total = 0
while x > 0:
 if total > 500:
 break
 total += x
 x = x // 2
 
 #Pass
 pass is the “no-op” statement in Python. It can be used in blocks where no action is to
be taken (or as a placeholder for code not yet implemented); it is only required
because Python uses whitespace to delimit blocks:
if x < 0:
 print('negative!')
elif x == 0:
 # TODO: put something smart here
 pass
else:
 print('positive!')

**Chapter 3**
 
 A tuple is a fixed-length, immutable sequence of Python objects. The easiest way to
create one is with a comma-separated sequence of values:
In [1]: tup = 4, 5, 6
In [2]: tup
Out[2]: (4, 5, 6)

#Unpacking tuples
If you try to assign to a tuple-like expression of variables, Python will attempt to
unpack the value on the righthand side of the equals sign:
In [15]: tup = (4, 5, 6)
In [16]: a, b, c = tup
In [17]: b
Out[17]: 5

#Sorting
You can sort a list in-place (without creating a new object) by calling its sort
function:
In [61]: a = [7, 2, 5, 1, 3]
In [62]: a.sort()
In [63]: a
Out[63]: [1, 2, 3, 5, 7]

 
