Homework

#Append In [8]: a = [1, 2, 3] # enter list, then append In [10]: a.append(4) Out[11]: [1, 2, 3, 4]

In [74]: template = '{0:.2f} {1:s} are worth US${2:d}' • {0:.2f} means to format the first argument as a floating-point number with two decimal places. • {1:s} means to format the second argument as a string. • {2:d} means to format the third argument as an exact integer. In [75]: template.format(4.5560, 'Argentine Pesos', 1) Out[75]: '4.56 Argentine Pesos are worth US$1'

#Concatenate In [71]: a = 'this is the first half ' In [72]: b = 'and this is the second half' In [73]: a + b Out[73]: 'this is the first half and this is the second half'

#Control Flow if, elif, and else

if x < 0: print('It's negative') elif x == 0: print('Equal to zero') elif 0 < x < 5: print('Positive but smaller than 5') else: print('Positive and larger than or equal to 5') If any of the conditions is True, no further elif or else

#Loops You can advance a for loop to the next iteration, skipping the remainder of the block, using the continue keyword. Consider this code, which sums up integers in a list and skips None values: sequence = [1, 2, None, 4, None, 5] total = 0 for value in sequence: if value is None: continue total += value A for loop can be exited altogether with the break keyword. This code sums ele‐ ments of the list until a 5 is reached: sequence = [1, 2, 0, 4, 6, 5, 2, 1] total_until_5 = 0 for value in sequence: if value == 5: break total_until_5 += value
