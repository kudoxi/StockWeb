from celery import Celery
from django.conf import settings
import os
from celery.schedules import crontab
from datetime import timedelta

# 为celery设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StockProject.settings')

# 创建应用
app = Celery('testcelery')
#在settings里配置
app.config_from_object('django.conf:settings')

# redis做MQ配置
#app = Celery('website', backend='redis', broker='redis://localhost')
# rabbitmq做MQ配置
#app = Celery('website', backend='amqp', broker='amqp://admin:admin@localhost')
# 酸配置应用
app.conf.update(

    # 本地Redis服务器
    BROKER_URL='redis://176.23.1.213:6379/0',
    #定时任务
    CELERYBEAT_SCHEDULE = {
            #每20秒执行一次get_stockinfo函数，并传了两个参数5和6
            'sum-task': {
                'task': 'deploy.tasks.get_stockinfo',
                'schedule':  timedelta(seconds=20),
                #'args': (5, 6)
            },
            #每周一早上4：30执行report函数
            #'send-report': {
            #    'task': 'deploy.tasks.report',
            #    'schedule': crontab(hour=4, minute=30, day_of_week=1),
            #}
        }
)

app.autodiscover_tasks(settings.INSTALLED_APPS)

#执行celery -A SecondhandsCar worker --loglevel=DEBUG
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))