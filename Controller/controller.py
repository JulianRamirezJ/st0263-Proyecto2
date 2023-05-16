import multiprocessing as mp
import boto3
from Controller.instance import instance

def start_process(instance_state, event):
    client = boto3.client('ec2')
    resource = boto3.resource('ec2')
    inst = instance(client=client, resource=resource, instance_state=instance_state, event=event)
    inst.run()
    


    
    
