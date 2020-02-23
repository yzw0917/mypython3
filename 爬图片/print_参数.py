
th={}
for i in range (1,10):
    key="alex"+str(i)
    value=i+30
    th[key]=str(value)   #th[key]本身就是value

for k in th.keys():     #想要调出字典key本身，需要用k去赋值   th[k]就是value
    print('%s，今年的年龄是：%s'%(k,th[k]))
