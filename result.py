print("=====" * 16)
# details area

name = input("Enter Your Name: ")
mother_name = input('Enter your Mother Name: ')
father_name = input("Enter Your Father's Name: ")
course_name = input("Enter your Course Name: ")
course_year = int(input('Enter your Course Year: '))
roll_number = int(input("Enter Your Roll Number: "))
uni_name = input('Enter Your University Name : ')
collage_name = input("Enter Your collage Name : ")
dob = input("Enter your date of birth : ")

# if course year

if course_year == 1:
    course_year = str(course_year) + "st year"

elif course_year == 2:
    course_year = str(course_year) + "nd year"

elif course_year == 3:
    course_year = str(course_year) + "rd year"

elif course_year == 4:
    course_year = str(course_year) + "th year"

else:
    print("invalided course year")

print('\x1B[1m' + '========ENTER YOUR SUBJECTS========' + '\x1B[1m')

# subjects area

sub1 = input("Enter subject 1: ")
sub2 = input("Enter subject 2: ")
sub3 = input("Enter subject 3: ")
sub4 = input("Enter subject 4: ")
sub5 = input("Enter subject 5: ")
sub6 = input("Enter subject 6: ")

# #marks area
print("=====" * 16)

marks1 = int(input("Enter " + sub1 + "'s marks : "))
marks2 = int(input("Enter " + sub2 + "'s marks : "))
marks3 = int(input("Enter " + sub3 + "'s marks : "))
marks4 = int(input("Enter " + sub4 + "'s marks : "))
marks5 = int(input("Enter " + sub5 + "'s marks : "))
marks6 = int(input("Enter " + sub6 + "'s marks : "))

print("=====" * 16)
max_marks = int(input('Enter Maximum Marks for Each subjects :'))

# grade code area
#subject 1 grade

if marks1 > 80:
    grade1 = "A"
elif marks1 > 70:
    grade1 = "B"
elif marks1 > 60:
    grade1 = "C"
elif marks1 > 50:
    grade1 = "D"
else:
    grade1 = "F"

#subject 2

if marks2 > 80:
    grade2 = "A"
elif marks2 > 70:
    grade2 = "B"
elif marks2 > 60:
    grade2 = "C"
elif marks2 > 50:
    grade2 = "D"
else:
    grade2 = "F"

#subject 3

if marks3 > 80:
    grade3 = "A"
elif marks3 > 70:
    grade3 = "B"
elif marks3 > 60:
    grade3 = "C"
elif marks3 > 50:
    grade3 = "D"
else:
    grade3 = "F"

#subject 4

if marks4 > 80:
    grade4 = "A"
elif marks4 > 70:
    grade4 = "B"
elif marks4 > 60:
    grade4 = "C"
elif marks4 > 50:
    grade4 = "D"
else:
    grade4 = "F"

#subject 5

if marks5 > 80:
    grade5 = "A"
elif marks5 > 70:
    grade5 = "B"
elif marks5 > 60:
    grade5 = "C"
elif marks5 > 50:
    grade5 = "D"
else:
    grade5 = "F"

#subject 6

if marks6 > 80:
    grade6 = "A"
elif marks6 > 70:
    grade6 = "B"
elif marks6 > 60:
    grade6 = "C"
elif marks6 > 50:
    grade6 = "D"
else:
    grade6 = "F"


# main output code starts here ;)

print("_____" * 11)
print('\x1B[1m \n \t \t \t \t ', uni_name.upper(), '\x1B[1m \n')
print("_____" * 11)
print('\t \t \t \t PERSONAL DETAILS ')
print("_____" * 11)

# personal details

print("Roll Number = ", roll_number)
print("Student Name = ", name)
print("Father's Name = ", father_name)
print("Mother's Name = ", mother_name)
print("Course Name = " + course_name + " " + course_year)
print("Collage Name = ", collage_name)

# marks details here

print("_____" * 11)
print(' \t \t \t \t MARKS DETAILS ')
print("_____" * 11)

gap = "      "

heading = f"{'Subject':10s}{gap}{'Max Marks':7s}{gap}{'Obt. Marks':7s}{gap}{'Grade':6s}"
print(heading)
print("_____" * 11)

line1 = f"{sub1.upper():10s}{gap}{max_marks:7d}{gap}{marks1:7d}{gap}{gap}{grade1}"
line2 = f"{sub2.upper():10s}{gap}{max_marks:7d}{gap}{marks2:7d}{gap}{gap}{grade2}"
line3 = f"{sub3.upper():10s}{gap}{max_marks:7d}{gap}{marks3:7d}{gap}{gap}{grade3}"
line4 = f"{sub4.upper():10s}{gap}{max_marks:7d}{gap}{marks4:7d}{gap}{gap}{grade4}"
line5 = f"{sub5.upper():10s}{gap}{max_marks:7d}{gap}{marks5:7d}{gap}{gap}{grade5}"
line6 = f"{sub6.upper():10s}{gap}{max_marks:7d}{gap}{marks6:7d}{gap}{gap}{grade6}"

# result output mark-sheet

print(line1)
print(line2)
print(line3)
print(line4)
print(line4)
print(line6)

print("_____" * 11)

total = marks1 + marks2 + marks3 + marks4 + marks5 + marks6
print(f"{'                                  PERCENTAGE = '}{total / (max_marks * 6):>5.1%}")
print(f"{'TOTAL = '}{total:<3d}{'/'}{max_marks * 6:3d}{gap}")
print("_____" * 11)

# greeting in end

if total <= (total/(max_marks*6))*100:
    print("         You're failed bro, kuch padh liya karo bee!")
else:
    print("         Hurrah! You are passed. Party kab dera fir?")
print("_____" * 11)