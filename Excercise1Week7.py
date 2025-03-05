while True:
    h=input('Please enter file name:')
    try:
        i=open(h)
        for line in i:
            line=line.upper()
            print(line)
    except:
        print('That is not a valid answer')