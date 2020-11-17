num=int(input())
out={}
test={}
for i in range(1,num+1):
    test={i:i*i}
    out.update(test)
print(out)
    
