"""U-Pass Auto Completer Initializer (init.py)

This script is complementary to the main script (upass.py). It initiates a text file that upass.py reads.

This tool requires no additional scripts or libraries.

This script requires that users input their data manually.

"""

import os

exists = os.path.exists('info.txt')
if exists:
    print("exists")
    os.remove("info.txt")

#User input
while True:
    school = input("What school do you go to?\nEnter a number:\n1 - Simon Fraser University\n2 - University of British Columbia\n3 - Douglas College\n4 - Kwantlen Polytechnic University\n5 - British Columbia Institute of Technology\n6 - Capilano University\n7 - Emily Carr University of Art and Design\n8 - Langara College\n9 - Vancouver Community College\n10 - Nicola Valley Institute of Technology\n")
    school = int(school)
    if school<1 and school>10:
        print("Please enter a valid school.")
        continue
    else:
        break

school_dict = {
    1 : "9",
    2 : "4",
    3 : "1",
    4 : "2",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "10",
    10 : "3"
}

email = input("Enter your email: ")
pw = input("Enter your password: ")
info = [school_dict[school], email, pw]

f = open("info.txt", "w")

for line in info:
    f.write(line)
    f.write("\n")
f.close() 
