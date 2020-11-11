# # with open("E:\pythonEx\python_crash_course\Part I Basics\ch10\pi_digits.txt") as file_object:
# #  contents=file_object.read()
# # print(contents)

# filename = 'E:\pythonEx\python_crash_course\Part I Basics\ch10\pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line)
filename = 'E:\pythonEx\python_crash_course\Part I Basics\ch10\pi_digits.txt'

filename="E:\4_5771416386228193177.pdf"
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))