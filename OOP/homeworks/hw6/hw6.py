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


with open("MOCK_DATA.txt", "r", encoding='utf-8') as file:
    content = file.read()

    full_name_list = re.findall(r"[A-Za-z'\-]+\s[A-Za-z'\-]+", content)
    print(full_name_list)

    email_list = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+", content)

    file_list = re.findall(r"[A-Z]\w+\.\w+", content)

    color_list = re.findall(r"[#]\w+", content)

fails = [Data(full_name="Nuesfs", email="beka@gmail.com", file_name="beka.py", color="#046220"),
         Data(full_name="IYAsiudy", email="tguysrc@ehow.com", file_name="UtTellus.tiff", color="#e8a767"),
         Data(full_name="HSKD", email="Josadfasd@nyu.edu", file_name="PlateaDictumst.txt", color="#ddc1be"),
         Data(full_name="ASKSD", email="rigonetqasd@mysql.com", file_name="DolorQuis.jpeg", color="aa422c"),
         Data(full_name="ASKHDSD", email="mk6@sourceforge.net", file_name="SodalesScelerisque.mov", color="#012499")]

for data in fails:
    if data.full_name in full_name_list:
        with open("FIO.txt", "w") as f:
            f.write(data.full_name)
    if data.email in email_list:
        with open("email.txt", "w") as f:
            f.write(data.email)
    if data.file_name in file_list:
        with open("filename.txt", "w") as f:
            f.write(data.file_name)
    if data.color in color_list:
        with open("color.txt", "w") as f:
            f.write(data.color)