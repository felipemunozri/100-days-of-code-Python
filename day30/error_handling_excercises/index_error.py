fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:  # if index is out of range simply print 'Fruit pie'
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
