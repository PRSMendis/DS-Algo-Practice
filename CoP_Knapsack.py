import time
import csv
MAX_CALORIES = 2000


class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value)\
            + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                         calories[i]))
    return menu


def testMaxVal(foods, maxUnits, printItems=True):
    print('Allocate', maxUnits, 'calories')
    tic = time.time()
    val, taken = maxVal(foods, maxUnits)
    toc = time.time() - tic
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)
    print("time: %.5fs" % (toc))


def buildMenuFromCSV():
    menu = []
    with open('menu.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            try:
                menu.append(Food(row[0], int(row[1]),
                                 int(row[2])))
            except:
                continue
        return menu


def run():
    # example
    names = ['wine', 'beer', 'pizza', 'burger', 'fries',
             'cola', 'apple', 'donut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]
    foods = buildMenu(names, values, calories)
    testMaxVal(foods, 750)

    # challenge
    menu = buildMenuFromCSV()
    testMaxVal(menu, MAX_CALORIES)


def maxVal(toConsider, avail):
    """Assumes toConsider is a list of Food, avail a weight (number of calories)
       Returns a tuple of the total value of a solution to the problem
       and a list of Food that comprise the solution"""

    ##################
    # YOUR CODE HERE #
    ##################
    # newlist = sorted(toConsider, key=lambda x: x.density(), reverse=True)
    # used = 0
    # value = 0
    # foodlist = []
    # for food in newlist:
    #     print(food, "density:", food.density())
    #     if food.calories + used <= avail:
    #         value = value + food.getValue()
    #         used = used + food.calories
    #         foodlist.append(food)
    #     print(f"used ={used}")
    # return (value, foodlist)

    jay = 'suck'
    for letter in jay:
        print(letter)


if __name__ == '__main__':
    run()
