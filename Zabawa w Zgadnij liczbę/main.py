import random
import time

#==========A==============

def searh(number):
    step = 1
    random_number = random.randint(0, 1000)
    while number != random_number:
        random_number = random.randint(0, 1000)
        #print(" moze to ", random_number)
        if random_number == number:
            print("Udało się za ", step, "podejsciem ","liczba to ", random_number)
        step += 1




#==========B==============


def advanced_searh(number):
    step = 1
    ran_max = 1000
    ran_min = 0
    random_number = random.randint(ran_min, ran_max)
    while number != random_number:
        random_number = random.randint(ran_min, ran_max)
        #print(" moze to ", random_number)
        if random_number == number:
            print("Udało się za ", step, "podejsciem ","liczba to ", random_number)
        step += 1
        if random_number > number:
            ran_max = random_number-1
        elif random_number < number:
            ran_min = random_number+1



#==========C==============
def search_binary(number):
    LB = number
    UB = 1001
    step = 1
    while LB < UB:
        tmp = LB + (UB-LB+1)//2
        step += 1
        if tmp > LB:
            UB = tmp - 1
        elif tmp < LB:
            LB = tmp + 1
        else:
            print(tmp)
            return tmp
    print("Udało się za ", step, "podejsciem ","liczba to ", tmp-1)
    return -1


number = int(input("Podaj liczbe do zgadnięcia "))
start = time.time()
searh(number)
stop = time.time()
print("czas szukania ",stop - start , "\n")

start = time.time()
advanced_searh(number)
stop = time.time()
print("czas zaawansowanego szukania  ",stop - start , "\n")

start = time.time()
search_binary(number)
stop = time.time()
print("czas  szukania binarngego   ",stop - start, "\n")
