# file management using password
import os   

print("**** File Management System ****")
print("press 1 for File Access")
print("press 2 for creating File")
print("press Q for Quit")
print("*********************************")

path = " ... "    # past the path of your folder where you want your file going to be open or create
file_names = os.listdir(path)


def open_file(name):  # read file function
    file = open(name, "r")   # r is for only reading the file
    print(file.read())


def create_file(name):  # creating a new file function
    file = open(name, "w")    # w is to write in your file
    context = input("Enter what you want in your File:")
    file.write(context)  # this will add your context in your file
    file.close()


def display_files():  # to display all the file in repository
    print("**** File names ****")
    for name in file_names:
        print(name)


def code():
    while True:
        print("*********************************")
        key = str(input("Enter Your choice:"))

        if key == 'q' and 'Q':
            print("*** Thank You ***")
            break

        if key != '1' and '2':
            print('** Wrong Choice **')

        if key == '1':
            display_files()
            choice = str(input("Enter File name:"))
            if choice not in file_names:
                print("** File not exist ***")
            else:
                print("***** File Content *****")
                open_file(choice)

        if key == '2':
            name = str(input("create file name"))
            file_names.append(name)
            create_file(name)


if __name__ == '__main__':
    code()
