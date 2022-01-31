# upper
# a = str(input(""))
# natija = ''
# for i in a:
#     if ord(i) >= 97 and ord(i) <= 122:
#         b = ord(i) - 32
#         natija += chr(b)
# print(natija)

a = int(input("newta honali son "))
n = ''
b = 0
d = []
c = 0
st = ''
s = ''
h = []
for i in range(a):
    b = input('{} - sonni kiriting '.format(i+1))
    d.append(b)
d.sort()

for k in d:
    if k == '0':
        s += k
        continue
    h.append(k)
h.insert(1, s)
for e in h:
    n += e
print(h)



