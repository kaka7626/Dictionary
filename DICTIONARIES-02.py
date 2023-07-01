Long = {'Bề ngoài' : 'Bình thường', 'Học vấn' : 'Bỏ ngang đại học', 'Tài chính' : 'Éo có gì'}

print(list(Long.keys())) # method của dictionary
print(list(Long.values()))
print(list(Long.items()))
print('-----------------------------')

for a in Long.keys():
    print(a)

print('-----------------------------')

for b in Long.values():
    print(b)    

print('-----------------------------')

for c in Long.items(): # for d, e in Long.items():
    print(c)           # print(d, e)