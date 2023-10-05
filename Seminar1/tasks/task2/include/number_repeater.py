def number_repeater(number, n):
    if isinstance(number, int):
        if isinstance(n, int):
            return int(str(number)*n)
        else:
            print('error: invalid n type')
            return -1;
    else:
        if isinstance(n, int):
            print('error: invalid n type')
            return -1;

        print('error: invalid number type')
        return -1;    
