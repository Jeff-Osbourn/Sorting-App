
with open("Sort_Me.txt", "r") as file1:
    with open("output.txt", "r") as file2:
        checkIntersection = set(file1).intersection(file2)

checkIntersection.discard('\n')

with open('some_output_file.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)