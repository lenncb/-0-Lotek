from random import randint

your_numbers = set()
draw = set()
counter = 0


def pass_numbers(your_numbers):
    while len(your_numbers) < 6:
        number = int(input(f'Wprowadź liczbę numer {(len(your_numbers)+1)} w zakresie od 1 do 49:'))
        your_numbers.add(number)
    return your_numbers

def draw_numbers(draw):
    draw.clear()
    while len(draw) < 6:
        draw.add(randint(1,50))
    return draw

def check(counter):
    while draw.issuperset(your_numbers) is False:
        draw_numbers(draw)
        counter += 1
    return counter

def message():
    print(f'Wygrałeś za {counter} razem.')
    print(f'Jeśli puszczałbyś 7 kuponów tygodniowo, wygrałbyś za {int(counter/365)} lat. ')
    print(f'Koszt Twojej inwestycji wyniesie: {counter*3:,} PLN')

pass_numbers(your_numbers)
draw_numbers(draw)
check(counter)
message()
