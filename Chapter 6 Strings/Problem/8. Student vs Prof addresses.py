# A program prints out a message indicating either all addresses
# are student or professor addresses entered
# @.student.college.edu and @prof.college.edu

n = eval(input('How many email addresses you will be entering?'))

for s in range(n):
    s = input('Enter those addresses:')
    
    if s[-20] in '@student.college.edu' :
        print('Student address')
    elif s[-20] in '@prof.college.edu':
        print('Professor address')
    
