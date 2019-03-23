import celery, os

from celery.utils.log import get_task_logger
from boto.ec2 import cloudwatch
from boto.utils import get_instance_metadata

logger = get_task_logger(__name__)

@celery.task()
def upload_stat_tracker_metrics(time):
    metadata = get_instance_metadata(timeout=1, num_retries=1)
    instance_id = metadata.get('instance-id')

    if instance_id is None:
        logger.warn('This is not an EC2 Instance, not uploading stats')
        return
    
    region = metadata.get('placement').get('availability-zone')[0:-1]

    app_name = os.environ.get('APP_NAME')
    metric_name = 'stat_tracker_time_{}'.format(app_name)
    metrics = {metric_name: time}

    cw = cloudwatch.connect_to_region(region)
    cw.put_metric_data('FN Dash Metrics', metrics.keys(), metrics.values(),
                       unit='Second',
                       dimensions={'InstanceId': instance_id})