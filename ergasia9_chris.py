f = open('txt.txt')
text = str(f.read())
text =''.join('{0:07b}'.format(ord(c), 'b') for c in text)
max0,max1,temp0,temp1=-1,-1,0,0
for i in range(len(text)):
    if text[i]=="0":
        temp0+=1
    else:
        if temp0>max0:
            max0=temp0
        temp0=0
for i in range(len(text)):
    if text[i]=="1":
        temp1+=1
    else:
        if temp1>max1:
            max1=temp1
        temp1=0
print(max0,max1)
