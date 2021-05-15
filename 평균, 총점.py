score = [ ]
s = 0
for i in range(5):
    k = int(input("점수입력:"))
    score.append(k)

s = 0
for i in score:
    s = s + i

print("총점:", s)
print("평균:", s/5)
