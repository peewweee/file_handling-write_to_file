# File handling - Writing multiple line of text contents into a text file
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# open mylife.txt file
with open("mylife.txt", "w") as text_file:
    # input line of text
    input_line = input("Enter a line you want to write: ")
    # write line of text to mylife.txt
    text_file.write(input_line + "\n")
    # ask user if there are more lines
    # if yes, loop
         # break loop
# print "all files have been written"
