class Casi():
    def __init__(self, name, year, hometown):
        self.name = name
        self.year = year
        self.hometown = hometown

class casiManager():
    def __init__(self):
        self.List_singer = []

    def input(self):
        name = input("Nhap Ten:")
        year = int(input("Nhap Nam Sinh:"))
        hometown = input("Nhap Que Quan:")
        casi = Casi(name, year, hometown)
        self.List_singer.append(casi)
        print("THem casi thanh cong:")

    def Ninput(self):
        n = int(input("Nhap SO casi can nhap:"))
        for _ in range(n):
            self.input()

    def pritn(self):
        if not self.List_singer:
            print("Danh sach trong!!!")
        else:
            print('DAnh sach casi:')
            for casi in self.List_singer:
                print(f"Ten casi: {casi.name} Nam sinh: {casi.year} Que quan: {casi.hometown}")

    # def abc(self):
    #     self.List_singer.sort(key= lambda casi: casi.name)
    #     for casi in self.List_singer:
    #         print(f"Ten casi: {casi.name} Nam sinh: {casi.year} Que quan: {casi.hometown}")

    # def cba(self):
    #     self.List_singer.sort(key=lambda casi: casi.name, reverse=True) 
    #     for casi in self.List_singer:
    #         print(f"Ten casi: {casi.name} Nam sinh: {casi.year} Que quan: {casi.hometown}")

    def yearss(self):
        self.List_singer.sort(key=lambda casi: casi.year)
        for casi in self.List_singer:
                print(f"Ten casi: {casi.name} Nam sinh: {casi.year} Que quan: {casi.hometown}")


cs = casiManager()
cs.Ninput()
# print("DANH sach ca si sau khi sap xep la")
# cs.abc()
print("Danh sach sap xep giam dan")
# cs.cba()
cs.yearss()

