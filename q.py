a = [ ]
while True:
    k = input( )
    if k =='q':
        break
    else:
        a.append(int(k))
cnt = 0
for i in a:
    if i % 2 == 0:
        print(i)
        cnt = cnt +1

print(cnt + 1)
