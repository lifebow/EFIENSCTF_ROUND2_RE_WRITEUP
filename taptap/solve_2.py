flag="Q806R554767513UR32QS4Q4120T00V91"
tap=1628775989156
sum1=tap*(tap+1)//2
def take_table(param):
    if param.isdigit():
        return ("0123456789",(ord(param)-ord('0')))
    else:
        
        return ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",(ord(param)-ord('A')))
def decode(param):
    table,index=take_table(param)
    print(sum1,table,i,table[(int)(sum1+index)%len(table)])
    return table[(int)(sum1+index)%len(table)]
a=[]
for i in flag:
    a.append(decode(i))
print("EFIENSCTF{"+"".join(a)+"}")

