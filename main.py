class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"{self.name} อายุ {self.age} ขวบ")

    def __str__(self): 
        return f"{self.name} อายุ {self.age} ขวบ"
def main():
    my_dog = Dog("guts",5)
    my_dog.info()
    your_dog = Dog("cis",10)
    your_dog.info()
    print(my_dog) #ดีกว่าเรียกใช้ .info แต่ตอง return wdawdwadwaddwadw
    print(your_dog)



if __name__ == "__main__":
    main()
