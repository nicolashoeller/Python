def sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1] :
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst


def main():
    lst = [4, 1, 12, 34, 312, 563, 3, 54]
    lst = sort(lst)
    print(lst)

if __name__ == "__main__":
    main()