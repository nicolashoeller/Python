def max(lst):
    max_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i
    
    return max_num



def main():
    lst = [1,3,32,2,1,5,63,2,1]
    max_num = max(lst)

    print(max_num)

if __name__ == "__main__":
    main()