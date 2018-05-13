# menu: A:1, B:2, C:5, D:7
# total$ 15 = 15 * A = 1 * A + 7 * B = 3 * C
def say_hello():
    print 'Hello, World'

def menu_combination(price,total):
    # price a list
    # total integer
    # return list of list
    number = 0
    result_combination = []


    while price[0]*number <= total:
        if len(price)>1:
            rest_combination = menu_combination(price[1:],total-price[0]*number)
            for ele in rest_combination:
                result_combination.append([number] + ele)
                # print ele
        elif price[0]*number == total:
            result_combination.append([number])
        number += 1
    return result_combination

def print_menu(combination,name):
    # new_combine = []
    for item in combination:
        print (zip(name,item))

print_menu(menu_combination([3,2,15,25],15),["A","B","C","D"])