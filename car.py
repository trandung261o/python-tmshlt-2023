class Car:
    def __init__(self, parameterName, parameterBrand, parameterColor):
        self.name = parameterName
        self.brand = parameterBrand
        self.color = parameterColor

    def drive(self):
        print(f"Ban dang lai chiec xe {self.name} mau {self.color} cua hang xe {self.brand}")

kiaMorning = Car("KIA Morning", "KIA", "xanh duong")
kiaMorning.drive()

ferrariTributo = Car("Ferrari F8 Tributo", "Ferrari", "do")
ferrariTributo.drive()