score = [ ]
s = 0
cnt = 0
for i in range(5):
    x = int(input( "수 입력:"))
    score.append(x) 

for i in score:
    if i >= 50:
        s = s + i
        cnt = cnt +1

print(s, cnt)
