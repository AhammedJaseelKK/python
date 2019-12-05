import boto3
ec2 = boto3.resource('ec2')
keypair = input('Type keypair name:(Pls add .pem in name): ')
# create a file to store the key locally
outfile = open(keypair,'w')
if keypair.endswith('.pem'):
    keypair = keypair[:-4]
# call the boto ec2 function to create a key pair
key_pair = ec2.create_key_pair(KeyName=keypair)

# capture the key and store it in a file
KeyPairOut = str(key_pair.key_material)
print(KeyPairOut)
outfile.write(KeyPairOut)
