
import redis

r = redis.StrictRedis(host='192.168.29.197', port= 6379); #db= 0


r.zadd('shuxue',15,'jack')
r.zadd('shuxue',98,'luck')
r.zadd('shuxue',60,'mark')

print(r.zrange('shuxue',0,3))
print(r.zrangebyscore('shuxue',60,100)) # 60分 到 100分
