import math
from threading import Thread

def main():
    # usr manual

    print("average calculator tool v1.2.3")
    print("once you have typed the maximum amount of numbers you want to average...")

    while True:
        
        print('\n')

        num2 = float(input("How many number(s) are you avereging? 2-10\n" + '>>> '))
    
        print("You may continue with entering data")

        # averaging

        if num2 ==float('2'):
            stock1 = float(input('>>> '))
            stock2 = float(input('>>> '))
            num1 = stock1 + stock2
            sum = num1 / num2
            print(">>> " + str(sum))

        if num2 ==float('3'):
            stock1 = float(input('>>> '))
            stock2 = float(input('>>> '))
            stock3 = float(input('>>> '))
            num1 = stock1 + stock2 + stock3
            sum = num1 / num2
            print(">>> " + str(sum))

        if num2 ==float('4'):
            stock1 = float(input('>>> '))
            stock2 = float(input('>>> '))
            stock3 = float(input('>>> '))
            stock4 = float(input('>>> '))
            num1 = stock1 + stock2 + stock3 + stock4
            sum = num1 / num2
            print(">>> " + str(sum))

        if num2 ==float('5'):
            stock1 = float(input('>>> '))
            stock2 = float(input('>>> '))
            stock3 = float(input('>>> '))
            stock4 = float(input('>>> '))
            stock5 = float(input('>>> '))
            num1 = stock1 + stock2 + stock3 + stock4 + stock5
            sum = num1 / num2
            print(">>> " + str(sum))

        if num2 ==float('6'):
            stock1 = float(input('>>> '))
            stock2 = float(input('>>> '))
            stock3 = float(input('>>> '))
            stock4 = float(input('>>> '))
            stock5 = float(input('>>> '))
            stock6 = float(input('>>> '))
            num1 = stock1 + stock2 + stock3 + stock4 + stock5 + stock6
            sum = num1 / num2
            print(">>> " + str(sum))

        if num2 ==float('7'):
            stock1 = float(input('>>> '))
            stock2 = float(input('>>> '))
            stock3 = float(input('>>> '))
            stock4 = float(input('>>> '))
            stock5 = float(input('>>> '))
            stock6 = float(input('>>> '))
            stock7 = float(input('>>> '))
            num1 = stock1 + stock2 + stock3 + stock4 + stock5 + stock6 + stock7
            sum = num1 / num2
            print(">>> " + str(sum))

        if num2 ==float('8'):
            stock1 = float(input('>>> '))
            stock2 = float(input('>>> '))
            stock3 = float(input('>>> '))
            stock4 = float(input('>>> '))
            stock5 = float(input('>>> '))
            stock6 = float(input('>>> '))
            stock7 = float(input('>>> '))
            stock8 = float(input('>>> '))
            num1 = stock1 + stock2 + stock3 + stock4 + stock5 + stock6 + stock7 + stock8
            sum = num1 / num2
            print(">>> " + str(sum))

        if num2 ==float('9'):
            stock1 = float(input('>>> '))
            stock2 = float(input('>>> '))
            stock3 = float(input('>>> '))
            stock4 = float(input('>>> '))
            stock5 = float(input('>>> '))
            stock6 = float(input('>>> '))
            stock7 = float(input('>>> '))
            stock8 = float(input('>>> '))
            stock9 = float(input('>>> '))
            num1 = stock1 + stock2 + stock3 + stock4 + stock5 + stock6 + stock7 + stock8 + stock9
            sum = num1 / num2
            print(">>> " + str(sum))

        if num2 ==float('10'):
            stock1 = float(input('>>> '))
            stock2 = float(input('>>> '))
            stock3 = float(input('>>> '))
            stock4 = float(input('>>> '))
            stock5 = float(input('>>> '))
            stock6 = float(input('>>> '))
            stock7 = float(input('>>> '))
            stock8 = float(input('>>> '))
            stock9 = float(input('>>> '))
            stock10 = float(input('>>> '))
            num1 = stock1 + stock2 + stock3 + stock4 + stock5 + stock6 + stock7 + stock8 + stock9 + stock10
            sum = num1 / num2
            print(">>> " + str(sum))

        print("would you like to round you answer?  y/n")
        rond = input('>>> ').lower()

        if rond =='y':
            print(round(sum))
        
        rept = input("do you want to run again? y/n | >>> ").lower
        
        if rept == 'n':
            continue
        else:
            break

# start/end Threads

t1 = Thread(target=main)
t1.start()
t1.join()
