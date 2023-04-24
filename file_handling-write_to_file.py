# File handling - Writing multiple line of text contents into a text file
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# open mylife.txt file
with open("mylife.txt", "w") as text_file:
    # input line of text
    while True:
        input_line = input("\033[0;30;45m Enter a line you want to write: ")
        # write line of text to mylife.txt
        text_file.write(input_line + "\n")
        # ask user if there are more lines
        ask_for_line = input("\033[0;36m Do you want to add a line? (Yes/No): ")
        # if yes, loop
        if ask_for_line != "Yes":
            # break loop
            break
# print "all files have been written"
print("\033[0;35m All lines have been written. Thank you!")
