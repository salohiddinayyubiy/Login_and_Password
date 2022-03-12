# import os
import sys


class User:
    def __init__(self, user_info_file="user.txt"):
        self.name = None
        self.login = None
        self.kasbi = None
        self.password = None
        self.password1 = None
        self.age = None
        self.user_info_file = user_info_file
        self.all_users = []
        self.welcome()


    def welcome(self):
        log = input("""
        Iltimos bittasini tanlang:
        [1] Ro'yxatdan o'tish
        [2] Tizimga kirish
        [3] Tizimdan chiqish
        """)

        while log.strip() not in ["1", "2", "3"]:
            # os.system("clear")
            print("Noto'g'ri kirish")
            log = input("""
                Iltimos tanlang:
                [1] Ro'yxatdan o'tish
                [2] Tizimga kirish
                [3] Tizimdan chiqish
                """)
        if log == "1":
            self.register()
        elif log == "2":
            self.log_in()
        else:
            sys.exit()

    def register(self):
        if self.name is not None and self.age is not None and self.kasbi is not None and \
                self.login is not None and self.password is not None and self.password1 is not None:
            print("siz allaqachon Tizimda borsiz ")

        #    name
        self.name = input("Ismingizni kiriting: ").strip().capitalize()
        while not self.name.isalpha():
            print("Ismingizni to'g'ri yozing")
            self.name = input("Ismingizni kiriting: ").strip().capitalize()

        self.age = input("Yoshingizni kiriting: ").strip()
        while not self.age.isdigit():
            print("Yoshingizni to'g'ri kiriting")
            self.age = input("Yoshingizni kiriting: ").strip()

        self.kasbi = input("Kasbingizni  kiriting: ").strip().capitalize()
        while not self.kasbi.isalpha():
            print("Kasbingizni to'g'ri yozing")
            self.kasbi = input("Kasbingizni kiriting: ").strip().capitalize()

        self.login = input("Loginni kiriting: ").strip().capitalize()
        while not self.login.isalnum():
            print("Loginni to'gri kiriting")
            self.login = input("Loginni kiriting: ").strip().capitalize()

        self.password = input("passwordni kiriting: ").strip()
        while not self.password or len(self.password) < 6:
            print("Password 6 ta belgi bo'lishi kerak")
            self.password = input("passwordni kiriting: ").strip()

        self.password1 = input("Passwordni qayta kiriting: ").strip()
        while self.password1 != self.password:
            print("Qaytadan kiriting: ")
            self.password1 = input("Passwordni qayta kiriting: ").strip()

        with open(self.user_info_file, "a") as file:
            file.write(f"login={self.login}|password={self.password}|name={self.name}|age={self.age}|kasbi={self.kasbi}|password1={self.password1}\n")
            print("Siz ro'yhattan o'ttingiz")
            self.wel_in()
        self.name = None
        self.login = None
        self.kasbi = None
        self.password = None
        self.password1 = None
        self.age = None
        self.welcome()

    def log_in(self):
        if self.login is not None and self.password is not None:
            print(f"Siz  allaqachon Tizimda borsiz ")
        else:
            if self.file_empty():
                print("Siz ro'yhattan o'tmagansiz!")
            else:
                # Get User login
                # os.system("clear")
                self.login = input("Login:").strip().capitalize()
                while not self.login.isalnum():
                    # os.system("cls")
                    print("iltimos loginni alfanumerik tarzda kiriting: ")
                    self.login = input("Login: ").strip()

                # Get User password
                self.password = input("Parol: ")
                while not self.password or len(self.password) < 6:
                    # os.system("clear")
                    print("Parol 6 ta belgi bo'lishi kerak!Qaytatdan parol kiriting: ")
                    self.password = input("Parol: ")

                self.get_all_user_in_db()

                if self.user_exists():
                    print(f"Siz tizimga muofiqiyatli kirdingiz! :)")
                    self.wel_in()
                else:
                    print("Tizimga kiraolmaysiz")

    def wel_in(self):
        regis = input("""
                [1] change pasword
                [2] log out
                [3] exit system
            """)
        while regis.strip() not in ["1", "2", "3"]:
            print("Noto'g'ri kirittingiz")
            regis = input("""
                            [1] change pasword
                            [2] log out
                            [3] exit system
                        """)
        if regis == "1":
            print("ERROR")
        elif regis == "2":
            self.log_out()
        else:
            print("Tizimdan chiqdingiz")
            sys.exit()

    def log_out(self):
        self.welcome()
        pass

    def change_login(self):
        pass

    def change_password(self):
        pass

    def file_empty(self):
        with open(self.user_info_file) as file:
            text = file.read()
        return text == ""

    def get_all_user_in_db(self):
        with open(self.user_info_file) as file:
            for user_row in file.read().split():
                user_dic = {
                 user_row.split("|")[0].split("=")[0]: user_row.split("|")[0].split("=")[1],
                 user_row.split("|")[1].split("=")[0]: user_row.split("|")[1].split("=")[1],
                }
                self.all_users.append(user_dic)

    def user_exists(self):
        for row in self.all_users:
            if self.login == row["login"] and self.password == row["password"]:
                return True
        return False


person = User()


