def join_array_remove_duplicate(arrayA, arrayB):
    for x in arrayA:
        for y in arrayB:
            if x in arrayB:
                arrayB.remove(x)
            if arrayA.count(x) > 1:
                arrayA.remove(x)
            if arrayB.count(y) > 1:
                arrayB.remove(y)
    return arrayA + arrayB

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
