import boto3    

ec2client = boto3.client('ec2')
ec2 = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        #print(instance)
        instId = instance["InstanceId"]
        instType = instance["InstanceType"]
        print("EC2 Instance ID: " + instId)
        print("EC2 Instance Type: " + instType)
        az = ec2.describe_instances(InstanceIds=[instId])['Reservations'][0]['Instances'][0]['Placement']['AvailabilityZone']
        print("EC2 Availability Zone: "+ az)