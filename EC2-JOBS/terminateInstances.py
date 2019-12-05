import boto3
counter = 1
instanceArray = []
ec2 = boto3.resource('ec2')

print('Please select a instance to stop')

for instance in ec2.instances.all():
	if instance.state['Name'] == 'running' and instance.state['Code'] == 16  or instance.state['Name'] == 'stopped' and instance.state['Code'] == 80:
		print (counter , instance.id , instance.state)
		counter = counter + 1 
		instanceArray.append(instance.id)
item = input('')
item = int(item)

#Needed instance ids must to give in an array
ids = [instanceArray[item-1]]

counter = 1 

ec2.instances.filter(InstanceIds = ids).terminate()

for instance in ec2.instances.all():
	if instance.state['Name'] == 'running' and instance.state['Code'] == 16 or instance.state['Name'] == 'stopped' and instance.state['Code'] == 80:
		print (counter , instance.id , instance.state)
		counter = counter + 1 