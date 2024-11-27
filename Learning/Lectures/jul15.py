class Player:
    def __init__(self, score):
        self.score = score

    @staticmethod
    def add_bonus(player, bonus):
        player.score += 10
        bonus = 5


p1 = Player(20)
bonus = 3

Player.add_bonus(p1, bonus)


class Gradebook:
    def __init__(self, grades=[]):
        self.grades = grades

    @staticmethod
    def averages(self):
        l_len = len(self.grades)
        middle = l_len // 2

        avg = sum(self.grades) / l_len

        if l_len % 2 ==  0:
            med = (self.grades[middle] + self.grades[middle - 1]) / 2
        else:
            med = self.grades[middle]

        return [avg, med]


# list_of_grades = [80, 90, 94]
# # list_of_grades = [1,2,3,4]
# gradebook = Gradebook(list_of_grades)
# print(Gradebook.averages(gradebook))



class BankAccount:
    def __init__(self, acc_num, aac_holder, balance):
        self.acc_num = acc_num
        self.acc_holder = aac_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount

    @property
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account number {self.acc_num} " +\
            f"under {self.acc_holder} holds a total balance of " + \
            f"{self.balance}"


b = BankAccount(1234,'bri harris', 100)
print(b.get_balance)







