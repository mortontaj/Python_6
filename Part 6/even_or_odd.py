def sum_eo(n,t):

    if t == "e":
        print(sum(range(0,n,2)))
        return sum(range(0,n,2))

    elif t == "o":
        print(sum(range(1,n,2)))
        return sum(range(1,n,2))

    else:
        return -1


sum_eo(10,"e")

