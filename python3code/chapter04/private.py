# coding:utf-8

class ProtectMe: 
    def __init__(self):
        self.me = "qiwsir"
        self.__name = "kivi"

    def __python(self):
        print("I love Python.")

    def code(self):
        print("Which language do you like?")
        self.__python()

if __name__ == "__main__":
    p = ProtectMe()
    print(p.me)
    print(p.__name)
