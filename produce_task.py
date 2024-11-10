import pytz

from celery_tasks.task01 import send_email
from datetime import datetime


# 方式一
local_tz = pytz.timezone('Asia/Shanghai')
v1 = local_tz.localize(datetime(2024, 11, 9, 20, 20, 00))
print(v1)
v2 = datetime.fromtimestamp(v1.timestamp(),local_tz)
print(v2)
result = send_email.apply_async(args=["egon",], eta=v2)
print(result.id)

# # 方式二
# ctime = datetime.now()
# # 默认用utc时间
# utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
# from datetime import timedelta
# time_delay = timedelta(seconds=10)
# task_time = utc_ctime + time_delay

# # 使用apply_async并设定时间
# result = send_email.apply_async(args=["egon"], eta=task_time)
# print(result.id)