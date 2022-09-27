# file management using password
"""1. display contex
2. create file with password
3. read file using password
"""
import os

print("**** File Management System ****")
print("press 1 for File Access")
print("press 2 for creating File")
print("press Q for Quit")
print("*********************************")

path = "C://Users//Dell//PycharmProjects//pythonProject1//Projects//Data Science Project//Password"
file_names = os.listdir(path)


def open_file(name):  # read file function
    file = open(name, "r")
    print(file.read())


def create_file(name):  # creating a new file function
    file = open(name, "w")
    context = input("Enter what you want in your File:")
    file.write(context)  # this will add your context in your file
    file.close()


def display_files():  # to display all the file in repository
    print("**** File names ****")
    for name in file_names:
        print(name)


def code():
    while True:
        key = str(input("Enter Your choice:"))

        if key == 'q' and 'Q':
            print("end")
            break

        if key != '1' and '2':
            print('wrong choice')

        if key == '1':
            display_files()
            choice = str(input("Enter File name:"))
            if choice not in file_names:
                print("File not exist")
            else:
                print("***** File Content *****")
                open_file(choice)

        if key == '2':
            name = str(input("create file name"))
            file_names.append(name)
            create_file(name)


if __name__ == '__main__':
    code()
