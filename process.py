# this line opens the file and assigns the open file to a variable
log_file = open("um-server-01.txt")

# the beginning of a function declaration with one parameter
def sales_reports(log_file):
    # a for statement that reads through each line within the file that we opened
    for line in log_file:
        # strip the whitespace
        line = line.rstrip()
        # day is now equal to the first three characters of the line
        day = line[0:3]
        # if the string just taken from the line is equal to "Mon"
        if day == "Mon":
            # print the whole line to the console
            print(line)

# close the file that we opened
sales_reports(log_file)
