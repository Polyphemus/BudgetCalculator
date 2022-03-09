import math

class Category:
    def __init__(self, catName):
        self.catName = catName
        self.ledger = []
        self.balance = 0
        self.spent = 0

    def __str__(self):
        CatStrLst = ['*'*((30-len(self.catName))//2) + self.catName + '*'*((30-len(self.catName))//2) + '\n']
        for entry in self.ledger:
            amntTwoDec = "{:.2f}".format(entry['amount'])[:7]
            CatStrLst.append(entry['description'][:23] + ' '*(30-len(entry['description'][:23])-len(amntTwoDec)) + amntTwoDec + '\n')
        CatStrLst.append(f'Total: {self.balance:.2f}')
        return ''.join(CatStrLst)

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        return True

    def get_balance(self):
        return self.balance

    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": 0 - amount, "description": description})
            self.balance -= amount
            self.spent += amount
            return True
        return False

    def transfer(self, amount, destCat):
        if self.check_funds(amount):
            self.ledger.append({"amount": 0 - amount, "description": 'Transfer to ' + destCat.catName})
            self.balance -= amount
            destCat.deposit(amount,'Transfer from ' + self.catName)
            return True
        return False

def create_spend_chart(categories):
    budgetTotal = 0
    catsPercents = {}
    longestNameLen = 0
    answer = ['Percentage spent by category\n']

    for category in categories:
        budgetTotal += category.spent
        if len(category.catName) > longestNameLen:
            longestNameLen = len(category.catName)

    for category in categories:
        catsPercents.update({category.catName: 10*math.floor(category.spent/budgetTotal*10)})

    for i in range(100, -10, -10):
        answer.append(' '*(3-len(str(i))) + str(i) + '| ')
        for v in catsPercents.values():
            if v >= i:
                answer.append('o  ')
            else:
                answer.append('   ')
        answer.append('\n')
    answer.append('    ' + '-'*(len(catsPercents) * 3 + 1) + '\n')
    for i in range(longestNameLen):
        answer.append('     ')
        for category in categories:
            try:
                answer.append(category.catName[i] + '  ')
            except:
                answer.append('   ')
        answer.append('\n')
    answer.pop()
    return ''.join(answer)