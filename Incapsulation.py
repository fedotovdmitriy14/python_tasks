class Customer:

    def __init__(self, name, age):
        self.__name = name 
        self.__age = age

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def setTraits(self, name, age):
        if Customer.__checkValue(age):
            self.__name = name 
            self.__age = age
        else: 
            print("Возраст должен быть числом!")

    def getTraits(self):
        return self.__name, self.__age

    #запускается каждый раз при обращении к атрибуту, мы его перегружаем:
    def __getattribute__(self, attr):
        if attr == "_Customer__age":
            return "Конфидециальная информация"
        else:
            return object.__getattribute__(self, attr)

    def __repr__(self):
        return self.__name


i19951 = Customer('Dmitriy', 26)
print(i19951.getTraits())

i19951.setTraits("Margosha", 5)
print(i19951.getTraits())
print(i19951._Customer__name)
#Конфидециальная информация:
print(i19951._Customer__age)