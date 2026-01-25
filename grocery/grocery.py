grocery_list = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        break
    
    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1

for i in sorted(grocery_list.keys()):
    print (grocery_list[i], i)
