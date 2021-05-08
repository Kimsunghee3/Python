import faker
f = faker.Faker("ko-KR")
t = [ ] 
for i in range(1,101):
    p = [ f.name(), f.address(), f.ssn(), f.email()]
    t.append(p)
for i in t:
    n= int(i[2] [0:2])
    if (n >= 80):
        print(i)
