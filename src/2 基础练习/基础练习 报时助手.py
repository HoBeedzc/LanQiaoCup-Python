time = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',
        6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
        11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
        16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',
        30:'thirty',40:'forty',50:'fifty'}

h,m = map(int,input().split())
ho,mo = '',''
ho = time.get(h,'twenty')
if h > 20:
    ho += " "+time.get(h-20,'')
if m <= 20:
    mo = time.get(m,'')
else:
    m_2 = m%10
    m_1 = m-m_2
    mo = time.get(m_1)
    if m_2:
        mo += " "+time.get(m_2)
if m == 0:
    mo = "o'clock"
print("{} {}".format(ho,mo))