import redis

r=redis.Redis(host="127.0.0.1",port=6379,db=1)
j=0
for i in r.lrange("celery",0,-1):
    j+=1
    print(i)
print(j)