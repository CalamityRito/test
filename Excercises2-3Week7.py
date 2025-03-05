while True:
    h=input('Please enter file name:')
    if h=='na na boo boo':
        print('Ha ha you fool! By uttering those words, you have fulfilled the prophecy and set me free!!')
        quit()
    try:
        i=open(h)
        count=0
        sum=0
        for line in i:
            if line.startswith('X-DSPAM-Confidence:'):
                count+=1
                t=line.split(' ')
                integer=t[1]
                integer=float(integer)
                sum=sum+integer
        sum=sum/count
        print('The average value following "X-DSPAM-Confidence" is:',sum)
    except:
        print('That is not a valid answer')