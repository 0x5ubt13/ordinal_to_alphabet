'''
Created by 0x5ubt13
Refined by Dacker
'''

# Declaring needed variables
code = []
numbers = []
output = []
final_output = []

# Greeting message
print('Welcome to the upgraded version of "5ubt13\'s number-to-alphabet-letter converter"!')
print('Please input your code to decode. Example: "19 21 2 20 12 5 _ 3 20 6 { 8 1 8 1 _ 19 15 _ 25 15 21 _ 4 5 3 15 4 5 4 _ 20 8 9 19 _ 5 8 , _ 23 5 12 12 _ 4 15 14 5 !}"')

# Main input
code = list(input('Enter or paste the code here: ').strip().split())

# Magic begins

running = True
while running:
    x = 0
    for i in code:
        if code[x].isnumeric() == True:
            numbers.append(int(code[x]))
        else:
            pass
        x += 1

    for i in numbers:
        i += 96
        i = chr(i)
        output.append(i)

    x = 0
    y = 0
    if len(output) == len(code):
        final_output = output
    else:
        for i in code:
            if code[x].isnumeric() == True:
                final_output.append(output[y])
                y += 1
            else:
                final_output.append(code[x])
            x += 1

    decode = ''.join(final_output)
    print("Here's the result: " + decode)
