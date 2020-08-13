
def binary_search(list, item):
    found = False
    first = 0
    last = len(list)

    while first <= last and not found:
        mid = (first + last) // 2
        if list[mid] == item:
            found = True
        elif list[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return found

list = [1,2,3,4,14,18,19,24,31,40]

try:
    item = int(input("What number do you want to check if is in the list?: "))
    if binary_search(list, item):
        print("The item is in the list.")
    else:
        print("The item is not in the list.")
except:
    print("Your input must be a integer number.")