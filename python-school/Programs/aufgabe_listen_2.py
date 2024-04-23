def min(lst):
    min_num = lst[0]
    for i in lst:
        if i < min_num:
            min_num = i
    
    return min_num



def main():
    lst = [1,3,32,2,1,5,63,2,1]
    min_num = min(lst)

    print(min_num)

if __name__ == "__main__":
    main()