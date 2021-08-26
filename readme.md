# Minecraft Server on AWS

## Introduction
This project creates a reusable, performant Minecraft EC2 server in AWS. Game state and configuration is stored on an EBS to facilitate easier maintenance of the server.

### Important notes
1. Familiarize yourself with AWS pricing to prevent any unwanted surprises. [calculator.aws](https://calculator.aws) is a great resource in that regard.

## CloudFormation templates
1. VPC (vpc.json)
   1. CIDR used: 10.0.1.0/24 (10.0.1.0/25, 10.0.1.128/25)
2. Core Infrastructure (core.json)
   1. Must be named "minecraft-core" or imports in the EC2 CFT will fail.
   2. Static Elastic IP is created so you can set up DNS with it. This will incur extra costs, depending on the domain.
3. EC2 (ec2.json)
   1. Server infrastructure. 
   2. Minecraft JAR file is saved to /usr/local/games so it persists as long as the instance is online.
4. Start/Stop Lambda
   1. Used to auto start/stop instance.
   2. Working with AWS on why it won't start a spot instance from a stopped state. 


## Deployment
   0. (This guide assumes you have a VPC set up. You can use any VPC for this, not just the one included.)
   1. Deploy core.json. Supply desired subnet and VPC for resources to be deployed. They must match the subnets for the EC2 instance. "minecraft-core" is a good default if you are only deploying one server.
      1. Note the stack name you enter, it will be important in Step 2.
      2. Note the public Elastic IP that is created. You can find it in the Outputs section after creation.
   2. Create an EC2 key pair and note its name. 
      1. [Info on this process here.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair)
   3. Deploy ec2.json in the same subnet+VPC as core.json. I prefer to name it minecraft-ec2. 
      1. AMI should be Amazon Linux 2.
      2. c5a.large is a good instance type for my purposes. With the amount of time I play MC with my family+friends, it costs me around $9 a month.
      3. Max Spot price is set to the on-demand price for c5a.large. Customize to fit your needs.
      4. Supply link to the JAR you'd like to use. Works with Spigot, CraftBukkit, and vanilla.
      5. CoreStackName should be the stack name you used in the previous step, while deploying core.json. 
   4. Verify that the server comes up. 

At this point, a server will come up at the Elastic IP created in core.json. You will then need to customize Minecraft according to [these instructions](https://help.minecraft.net/hc/en-us/articles/360058525452-How-to-Setup-a-Minecraft-Java-Edition-Server). My preferred configuration is in the cfg directory outside of the UUID allow list. Copy those to your /mnt/minecraft directory to customize your installation. 

## Updating server
The upside of this design is that updating to a new Minecraft version / snapshot is very simple. Just delete the ec2.json stack and re-create the stack with the link to the new JAR specified. All game state will be saved in core.json's EBS, so it will come back up very quickly. 
