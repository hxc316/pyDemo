
#安装web.py easy_install web.py

import web
import time
import redis
r = redis.StrictRedis(host='192.168.29.197', port= 6379)
urls = ('/','visit','/online','online')

app = web.application(urls,globals())

def time_to_key(current_time):
    return 'active.user:' + time.strftime('%M',time.localtime(current_time))

def keys_in_last_10_minites():
    now = time.time()
    result = [];
    for i in range(10):
        result.append(time_to_key(now - i*60))
    return result

class visit:
    def GET(self):
        user_id = web.ctx.env['HTTP_USER_AGENT']
        current_key = time_to_key(time.time())
        pipe = r.pipeline();
        pipe.sadd(current_key,user_id);
        pipe.expire(current_key,10*60)
        pipe.execute();
        return 'user_id:\t' + user_id + '\r\nkey:\t' + current_key;

class online:
    def GET(self):
        # log = keys_in_last_10_minites();
        info = '';
        # online_user = r.sunion(keys_in_last_10_minites())
        # result = '';
        # for user in online_user:
        #     result += 'User agent: ' + user + '\r\n'
        for userId in keys_in_last_10_minites():
            info += userId + '= '
            # info += r.get(userId)
            info += '\r\n'

        return 'redis user info: \r\n' + str(info)
        #     return "hello online"

if __name__ == '__main__':
        app.run()

