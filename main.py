"""class file"""

def summ(a_num, b_num):
    """summ function"""

    return a_num + b_num


class Human():
    """Human class"""

    def __init__(self, name, height, weight):
        """__init__ function"""

        self.name = name
        self.height = height
        self.weight = weight

    def is_weight_normal(self, height, weight):
        """is_weight_normal function"""

        if height - 100 >= weight:
            return self.name + ", Your weight is normal."

        return self.name + ", Your weight isn't normal!"

    def letters_count(self):
        """letters_count function"""

        name_list = []
        for letter in self.name:
            name_list.append(letter)

        return len(name_list)

print("Enter your name, height and weight: ")
NEW_HUMAN = Human(input().capitalize(), int(input()), int(input()))
print("Hello, " + NEW_HUMAN.name + ". ")
print(NEW_HUMAN.is_weight_normal(NEW_HUMAN.height, NEW_HUMAN.weight))
print(NEW_HUMAN.letters_count())
