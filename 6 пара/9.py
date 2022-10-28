class bank:
    def __init__(self):
        self.acc = dict()
        self.conform = {"deposit": 2, "withdraw": 2, "transfer": 3, "balance": 1, "income": 1}
    def deposit(self, name, sum):
        sum = int(sum)
        if not name in self.acc:
            self.acc[name] = 0
        self.acc[name] += sum

    def withdraw(self, name, sum):
        sum = int(sum)
        if not name in self.acc:
            self.acc[name] = 0
        self.acc[name] -= sum

    def transfer(self, n1, n2, sum):
        sum = int(sum)
        if not n1 in self.acc:
            self.acc[n1] = 0
        if not n2 in self.acc:
            self.acc[n2] = 0
        self.acc[n1] -= sum
        self.acc[n2] += sum

    def balance(self, name):
        if not name in self.acc:
            print("ERROR")
        else:
            print(int(self.acc[name]))

    def income(self, p):
        p = int(p)
        for i,j in self.acc.items():
            if j > 0:
                self.acc[i] += int(j * p / 100)

    def parse_command(self, cmd):
        arg = list(map(str.lower, cmd.split()))
        
        if len(arg) < 1:
            print("Ошибка, введите команду")
            return

        cmd = arg[0]

        if(not cmd in self.conform or self.conform[cmd] != len(arg) - 1):
            print("Ошибка, команда введена неверно")
            return

        match cmd:
            case "deposit":
                self.deposit(arg[1], arg[2])
            case "withdraw":
                self.withdraw(arg[1], arg[2])
            case "transfer":
                self.transfer(arg[1], arg[2], arg[3])
            case "balance":
                self.balance(arg[1])
            case "income":
                self.income(arg[1])

if __name__ == "__main__":
    d = bank()

    while(True):
        s = input()
        d.parse_command(s)