import re

class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name
    
    @full_name.setter
    def full_name(self, new_full_name):
        self.__full_name = new_full_name


    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, new_email):
        self.__cpu = new_email


    @property
    def file_name(self):
        return self.__file_name
    
    @file_name.setter
    def file_name(self, new_file_name):
        self.__file_name = new_file_name

    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, new_color):
        self.__color = new_color


with open('MOCK_DATA.txt', 'r', encoding="utf-8") as file_with_names:
    file = file_with_names.readlines()
    contents = []
    for line in file:
        full_name = re.findall(r"^[A-Za-z'\-]+\s[A-Za-z'\-]+", line)
        emails = re.findall(r"	[a-zA-Z0-9]+@[-a-zA-Z0-9]+\.[a-zA-Z0-9]+", line)
        files = re.findall(r"	\w+\.\w+", line)
        colors = re.findall(r"[#]\w+", line)
        contents.append(
            Data(full_name, emails, files, colors)
        )

    with open('full_name', 'w', encoding="utf-8") as file1:
        for i in contents:
            file1.writelines(i.full_name)

    with open('email', 'w', encoding="utf-8") as file2:
        for i in contents:
            file2.writelines(i.email)

    with open('file_name', 'w', encoding="utf-8") as file3:
        for i in contents:
            file3.writelines(i.file_name)

    with open('color', 'w', encoding="utf-8") as file4:
        for i in contents:
            file4.writelines(i.color)
