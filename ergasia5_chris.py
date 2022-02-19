f = open('tale.txt')
inp = str(f.read())
inp=inp.lower()
inp=inp.split()
newlist=list(set(inp))
fr=[]
for i in range(len(newlist)):
    fr.append(0)
for i in range(1,len(inp)):
    for q in range(len(newlist)):
        if newlist[q]==inp[i]:
            fr[q]+=1
for i in range(len(newlist)):
    for q in range(i+1,len(newlist)):
        if fr[i]<fr[q]:
            fr[q],fr[i]=fr[i],fr[q]
            newlist[q],newlist[i]=newlist[i],newlist[q]
duo=[]
tria=[]
d=-1
t=-1
print("highest frequency words")
for i in range(10):
    print(newlist[i])
for i in range(len(newlist)):
    if len(newlist[i])>=2:
        d+=1
        duo.append(newlist[i][0:2])
    if len(newlist[i])>=3:
        t+=1
        tria.append(newlist[i][0:3])
duon=list(set(duo))
trian=list(set(tria))
frd=[]
frt=[]
for i in range(len(duon)):
    frd.append(0)
for i in range(len(trian)):
    frt.append(0)

for i in range(len(duo)):
    for j in range(len(duon)):
        if duon[j]==duo[i]:
            frd[j]+=1

for i in range(len(tria)):
    for j in range(len(trian)):
        if trian[j]==tria[i]:
            frt[j]+=1
for i in range(len(duon)):
    for j in range(i+1,len(duon)):
        if duon[i]<duon[j]:
            duon[i],duon[j]=duon[j],duon[i]
            frd[j],frd[i]=frd[i],frd[j]
        

for i in range(len(trian)):
    for j in range(i+1,len(trian)):
        if tria[i]<trian[j]:
            trian[i],trian[j]=trian[j],trian[i]
            frt[j],frt[i]=frt[i],frt[j]
print("------------------------------")
for i in range(3):
    print(duon[i])
print("------------------------------")
for i in range(3):
    print(trian[i])
print("------------------------------")    