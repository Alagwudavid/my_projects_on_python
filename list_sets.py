#import random
#import math

def fibonacci_seq(fn):
    if fn == 0:
        return 0
    elif fn == 1:
        return 1
    else:
        fn_seq = (fn - 1) + (fn - 2)
        return fn_seq

print(fibonacci_seq(13))

#randList = []
#for i in range(5):
#    randList.append(random.randrange(1, 10, 2))

#print(randList)

##########################
#randList = []
#for i in range(6):
#    randList.append(random.randrange(1, 9))
#
#print(randList)

##############
#oneTo10 = list(range(10))

#randList = randList + oneTo10

#print(randList[0])
#print("length:", len(randList))

#############################

#inputs = input("Enter Numbers: ")
#lists_sets = inputs.split("")

#print(f'inputs: {lists_sets}')