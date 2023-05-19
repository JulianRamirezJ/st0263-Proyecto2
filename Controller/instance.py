from botocore.exceptions import ClientError
import time as t


class instance:
    def __init__(self, client, resource, instance_state, event):
        self.client = client
        self.resource = resource
        self.instance_state = instance_state
        self.event = event

    def run(self):
        current_instance_ids = self.get_current_instance_ids()
        self.terminate_instances(current_instance_ids)
        instances = self.create_instances(min=2, max=2)
        self.add_instances(instances=instances)
        print('Cree las instancias por primera vez')
        self.event.set()

        instance_creating_ids = []
        for instance in instances:
            instance_creating_ids.append(instance.id)

        while True:
            for instance_id in instance_creating_ids:
                if self.instance_state[instance_id][0]:
                    instance_creating_ids.remove(instance_id)

            active_instances_ids = self.get_active_instance_ids()
            active_instances_quantity = len(active_instances_ids)
            instances_creating_quantity = len(instance_creating_ids)

            prom = self.calculate_prom()
            if active_instances_quantity < 2:
                if (active_instances_quantity + instances_creating_quantity) < 2: 
                    n = 2 - (active_instances_quantity + instances_creating_quantity)
                    new_instances = self.create_instances(
                    min=n, max=n)
                    self.add_instances(instances=new_instances)
                    for instance in new_instances:
                        instance_creating_ids.append(instance.id)
            elif not prom == 0 and prom < 40 and active_instances_quantity > 2:
                instance_id = ''
                for key in self.instance_state.keys():
                    current_instance = self.instance_state[key]
                    if current_instance[0]:
                        instance_id = key
                        break
                self.terminate_instances(instance_ids=[instance_id])
                self.remove_instances([instance_id])
            elif not prom == 0 and prom > 70 and active_instances_quantity < 5 and instances_creating_quantity == 0:
                    instance_created = self.create_instances(min=1, max=1)
                    self.add_instances(instances=instance_created)
                    for instance in instance_created:
                        instance_creating_ids.append(instance.id)
            t.sleep(10)

    def calculate_prom(self):
            sum = 0
            n = 0
            for key in self.instance_state.keys():
                current_instance = self.instance_state[key]
                if current_instance[0]:
                    sum += current_instance[2]
                    n += 1
            if n == 0:
                return 0
            else: 
                return sum/n
    

    def get_active_instance_ids(self):
        instances = []
        for key in self.instance_state.keys():
            current_instance = self.instance_state[key]
            if current_instance[0]:
                instances.append(key)
        return instances

    def add_instances(self, instances):
        for instance in instances:
            self.instance_state[instance.id] = [
                False, instance.private_ip_address, 0]

    def create_instances(self, min, max):
        return self.resource.create_instances(
            ImageId='ami-0440e490864032c0e',
            MinCount=min, MaxCount=max,
            KeyName='vockey',
            InstanceType='t2.micro',
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': 'eafit-instance'
                        }
                    ]
                }
            ],
            SecurityGroups=[
                'eafit-security-group',
            ],
            UserData='''#!/bin/bash
            sudo apt update
            git clone https://github.com/JulianRamirezJ/st0263-Proyecto2.git
            cd st0263-Proyecto2/Monitor_C
            sudo apt install python3-pip -y
            sudo python3 -m pip install --upgrade pip
            sudo python3 -m pip install grpcio
            sudo python3 -m pip install grpcio-tools
            sudo pip install protobuf==3.20.*
            python3 monitor_c.py'''
        )

    def remove_instances(self, instance_ids):
        for instance_id in instance_ids:
            del self.instance_state[str(instance_id)]


    def terminate_instances(self, instance_ids):
        if len(instance_ids) > 0:
            self.client.terminate_instances(InstanceIds = instance_ids)

    def get_current_instance_ids(self):
        instances=self.client.describe_instances(Filters = [
            {
                'Name': 'tag:Name',
                'Values': [
                    'eafit-instance',
                ]
            },
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running'
                ]
            }
        ],)
        ids=[]
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id=instance['InstanceId']
                ids.append(instance_id)

        return ids
