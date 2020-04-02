# Ask the user to enter the names of files to compare
fname1 = input("Enter the first filename: ")
fname2 = input("Enter the second filename: ")

# Open the file so we can start comparing them
file1 = open(fname1)
file2 = open(fname2)

# Get the first line in each file
check1 = file1.readline()
check2 = file2.readline()

# Variable to keep track of the line count
line_check = 1

while check1 != '' or check2 != '':
    
    # Strip the leading whitespaces
    check1 = check1.rstrip()
    check2 = check2.rstrip()

    # Compare the lines from both file
    if check1 != check2:
        
        # Checks if there is nothing in file2, but file1 has a value
        if check2 == '' and check1 != '':
            print("Output : ", "Line-%d" % line_check, check1)
        # Print value of file1
        elif check1 != '':
            print("Output : ", "Line-%d" % line_check, check1)
            
        # Checks if there is nothing in file1, but file1 has a value
        if check1 == '' and check2 != '':
            print("Sorted_Text : ", "Line-%d" % line_check, check2)
        # Print value of file2
        elif check2 != '':
            print("Sorted_Text : ", "Line-%d" %  line_check, check2)

        # Print a blank line
        print('\n')

    #Read the next line from the file
    check1 = file1.readline()
    check2 = file2.readline()

    #Increment line counter
    line_check += 1
    
file1.close()
file2.close()
