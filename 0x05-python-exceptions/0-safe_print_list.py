def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end=" ")
            count += 1
        except IndexError:
            break
    print()
    return count

elements_printed = safe_print_list(["Hello", 42, "World", True], 5)
print("Number of elements printed:", elements_printed)
