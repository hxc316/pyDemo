

import redis

r = redis.StrictRedis(host='192.168.29.197', port= 6379); #db= 0
# r.set("name","hxc316");
# print(r.get("name"))
# print(r.keys('*'))

# for i in range(500):
#     a = r.sadd('city',i)
#     print("r.sadd: ",i ,'result:',a)
#
# print('citys ',r.smembers('city'))


pro = range(2)
name = ['a','b']    #两个省份
for i in pro:
    r.set('pro'+str(i),name[i])

for m in pro:
    print(r.get('pro'+str(m)))
    for c in range(10):
        r.sadd("citys"+str(m),i*10+c)

print("citys = ",r.smembers('citys0'))
print("citys0里面有15这个城市么? " , r.sismember('citys0',9))
