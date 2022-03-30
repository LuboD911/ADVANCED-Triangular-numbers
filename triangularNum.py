from math import sqrt
# input --> biggest number in the triangular form
# output --> number of the sequence (triangular num) and the triangle(from number)

'''
2 ----->  ***
          ***
n.(n+1)  ------> 2*(2+1)
                4 + 2 = 6
                
2 -------> *
           **
n*(n+1)/2  ------> 2*(2+1) / 2 = 3

x^2 + x - 6 = 0

D=k^2 - (a*c)
x1,2 = -0.5 +- sqrt(x+0.25)

'''
def main(num):
    # search for the closest triangle nums
    smaller = num
    bigger = num

    x = sequenceNumber(num)

    if isIntiger(x):
        x = int(x)
        print("Triangle num:", x)
        draw(num, x)
    else:

        while True:
            x = sequenceNumber(smaller)
            if isIntiger(x):
                x = int(x)
                print("Smaller triangle seq num: ", smaller)
                print()
                draw(smaller, x)
                print()
                print()
                break
            smaller -= 1

        while True:
            x = sequenceNumber(bigger)
            if isIntiger(x):
                x = int(x)
                print("Bigger triangle seq num: ", bigger)
                print()
                draw(bigger, x)
                break
            bigger += 1


def sequenceNumber(triangle_num):
    seq_num = -0.5 + sqrt(triangle_num*2+0.25)
    return seq_num


def isIntiger(num):
    if type(num) is int:
        return True

    f,s = str(num).split('.')
    if s != '0':
        return False
    return True

def draw(triangl_num, seq_num):

    if triangl_num < 1:
        return
    start = triangl_num - seq_num + 1
    end = triangl_num + 1

    res = []
    for i in range(start, end):
        i = str(i)
        res.append(i)

    res = ' '.join(res)
    print(res)

    draw(triangl_num - seq_num, seq_num - 1)

main(11)