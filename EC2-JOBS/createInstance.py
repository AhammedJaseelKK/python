import boto3
import os
ec2 = boto3.resource('ec2')

#read AMI Id
amiId = input('Please enter AMI Id: ')

#read min count
minimum = input('Please enter min number of instances:')
minimum = int (minimum)
#read max count
maximum = input('Please enter max number of instances: ')
maximum = int (maximum)
#read insatnce type 
instanceType = input('Please enter instance type: ')

keyName = input('Please type keyname: ')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId=amiId,
     MinCount=minimum,
     MaxCount=maximum,
     InstanceType=instanceType,
     KeyName=keyName
 )

#amiId = ami-00c03f7f7f2ec15c3
#minimum = 1 
#maximum = 1
#instanceType = t2.micro
#keyName = ec2-keypair