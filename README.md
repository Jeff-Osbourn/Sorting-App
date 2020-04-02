# Sorting-App
Sorts elements in a text files into a list organized in ascending order by length of the name, then alphabetically. 

Need python to run the Sorting App. You can use any linux distribution you like but I used the windows subsystem for linux.

Once you load the files into the linux distro you should be able to find the files then run the command 
"python3 SortFunction.py" and it should work. You might have to install python for it so run by running the command "sudo apt install python3 python3-pi" if you do not already have it.

Once you run SortFunction.py you will be asked which file you would like to sort. Type in the name of the file and the output can be seen in the output.txt file.

Do perform a test, we can use the Sorted_Text.txt file to help us as it has the proper output that are SortFunction should get. We can run the SortTest.py and it will ask us which two files we would like to compare. We want the output.txt file and the Sorted_Text.txt file to see if our current output matches the correct output. This will print out and compare all the lines in each text file that are different. If nothing is printed then that means no differences were found, which is what we want because then the test was passed :). 
