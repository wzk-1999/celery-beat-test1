### Start the producer:
#### celery beat
`celery -A celery_tasks beat`

it will generate the tasks to queue based on the configurations in `beat_schedule`

### Start the consumer:
`celery -A celery_tasks worker -l info -P eventlet --pool=threads -c 3`

if in linux, use the default spawn worker pool, -c to specify the concurrency