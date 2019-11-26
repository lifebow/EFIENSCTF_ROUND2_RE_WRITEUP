value=[196,2880,6892,5853,93,1986,7891,9872,235,687,3477,4911,5762,5766,9512,9457,9913,299,1656,1929,430,5390,4272,7516,3276]

base=[10,16,8,13,12,16,2,10,17,3,21,23,19,18,14,26,4,2,9,15,7,24,6,22,20]
table="0123456789abcdefghijklmnopq"
def convert(val,bas):
    a=[]
    while (val >= bas):
        a.append(table[(val%bas)])
        val=int(val/bas)
    a.append(table[val])
    return a[::-1]
print("1")
for i in range(len(value)):
    print("".join(convert(value[i],base[i])))