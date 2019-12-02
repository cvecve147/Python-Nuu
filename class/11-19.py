sec1 = {chr(ord('a')+i): chr(ord('a')+i-1)for i in range(26) if i % 2}
sec2 = {chr(ord('a')+i): chr(ord('a')+i+1)for i in range(26) if i % 2 == 0}
sec1.update(sec2)
print(sec1)

S = "is apples"
ss = ""
for c in S:
    if(c != " "):
        ss += sec1[c]
    else:
        ss += " "
print(ss)
bb = ""
for c in ss:
    if(c != " "):
        bb += sec1[c]
    else:
        bb += " "
print(bb)
