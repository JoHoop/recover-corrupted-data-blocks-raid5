lines = []

# open the file and read lines into a list
# closes file automatically
with open('data.txt') as f:
    lines = f.readlines()

# split each line into list where each block is a list item containing a list of characters
for l in range(len(lines)):
    lines[l] = lines[l].split()
    for b in range(len(lines[l])):
        lines[l][b] = list(lines[l][b])

# if the line contains x blocks, remove them, otherwise skip that line
for l in range(len(lines)):
    try:
        lines[l].remove(['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
    except ValueError as e:
        continue

    # transpose the list so that corresponding characters of each block in a line are in the same list
    x_block = list(map(list, zip(*lines[l])))

    # create an integer object (from base 16) of each character and perform the bitwise XOR
    for b in range(len(x_block)):
        value = int(x_block[b][0], 16) ^ int(x_block[b][1], 16) ^ int(x_block[b][2], 16) ^ int(x_block[b][3], 16)

        # convert each integer to letters and strings
        if value >= 10:
            x_block[b] = format(value, 'x')
        else:
            x_block[b] = str(value)

    # concatenate the block and print the result
    print("\nx_block of line",l+1,"=","".join(x_block))
