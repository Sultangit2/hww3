class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        ad = input(f'Введите сумму которую добавите к нынешним {self._balance} : ')
        print(self._balance + int(ad))

    def _kill(self):
        if self._balance > 0:
            print(' вас на счяту не осталось денег')
            return self._balance - self._balance


    def __jackpot(self):
        self._balance *= 10

    def get_jeckp(self):
        print(self.__jackpot())


    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, a):
        self.__name = a


    @property
    def balance(self):
        return f'{self._balance}'

    @balance.setter
    def balance(self,b):
        self.balance = b
    def _copyy(self, other):
        print(f'ваш сложенный баланс {self._balance + other._balance}\n'
              f'было{self._balance}')




bank = Bank('optima', 400)
load = Bank('kicb', 500)
bank.moneyX()
print(bank._kill())
bank._copyy(load)
print(Bank.get_jeckp(load))
bank.get_jeckp()