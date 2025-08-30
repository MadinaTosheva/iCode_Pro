# Создайте класс User, с атрибутами name, email, my_wish и методом introduce(), который печатает:
#
# "Привет, я Адам, моя почта adam@gmail.com и у меня есть мечта "


class User:
    def __init__(self, name, email, my_wish):
        self.name = name
        self.email = email
        self.my_wish = my_wish


    def introduce(self):
        print(f'Привет, я {self.name}, моя почта {self.email} и у меня есть мечта: {self.my_wish}')


name = input("Имя: ")
email = input("Почта: ")
my_wish = input("Желания: ")


a = User (name, email, my_wish)
a.introduce()
