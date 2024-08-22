class House:
    def __init__(self, name, number_of_floors):
        self.new_floor = None
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(self.new_floor):
                print(i + 1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
