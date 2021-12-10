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

# extra credit function
def big_melon_order(log_file):
    # second verse same as the first!
    for line in log_file:
        line = line.rstrip()
        # make a new variable and split it up along any whitespace
        line_list = line.split()
        # if the number of melons we find is greater than 10
        if (int(line_list[2]) > 10):
            # print the line we are reading
            print(line)

# call the function with the file we opened at the start
sales_reports(log_file)

# go back to the beginning of the document
log_file.seek(0, 0)

# call the big melon order function
big_melon_order(log_file)

# close the file that we opened (I added this)
log_file.close()