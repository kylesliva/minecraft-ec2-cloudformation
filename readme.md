# Minecraft Server on AWS

## Introduction
This project creates a stateless Minecraft EC2 server in AWS. Game state and configuration is stored on an EBS to facilitate easier maintenance of the server. 

## CFTs 
1. VPC (to be added later)
   1. CIDR used: 10.0.1.0/24 (10.0.1.0/25, 10.0.1.128/25)
      1. Small, but I don't run a lot of stuff and I tend towards IP conservation
2. Core Infrastructure (core.json)
   1. must be named "minecraft-core" or imports in the next CFT will fail
3. EC2 (ec2.json)
   1. Server infrastructure. 
   2. Minecraft JAR file is saved to /usr/local/games so it persists as long as the instance is online.


## Deployment
   0. (This guide assumes you have a VPC set up. You can use any VPC for this, not just the one I have a CFT for.)
   1. Deploy core.json. Supply desired subnet and VPC for resources to be deployed. They must match the subnets for the EC2 instance.
   2. Deploy ec2.json in the same subnet+VPC as core.json. I prefer to name it minecraft-ec2. 
      1. AMI should be Amazon Linux 2.
      2. c5a.large is a good instance type for my purposes.
      3. Max Spot price is set to the on-demand price for c5a.large. Customize to fit your needs.
      4. Supply link to the JAR you'd like to use.

At this point, a server should come up. You will then need to customize Minecraft according to [these instructions](https://help.minecraft.net/hc/en-us/articles/360058525452-How-to-Setup-a-Minecraft-Java-Edition-Server). My preferred configuration is in the mc_cfg directory outside of the UUID allow list.


## Updating server
The upside of this design is that updating to a new Minecraft version / snapshot is very simple. Just delete the ec2.json stack and re-create the stack with the link to the new JAR specified. All game state will be saved in core.json's EBS, so it will come back up very quickly. 