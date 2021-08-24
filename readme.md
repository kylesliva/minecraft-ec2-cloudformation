# Minecraft todo

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

## TODO

1. Static Infrastructure
    * EBS
    * DNS stuff
    * ENIs?
    * KMS key 
2. EC2
    * should be stateless

## Todo
1. Create custom route table with:
   1. local route to VPC
   2. route to IGW
      1. 0/0 to igw-id
   3. done
2. Use S3 on core creation to push desired files to EBS (perhaps from snapshot)

### core
1. snapshots?
2. create KMS key in template

### ec2
1. set up instance profile stuff
2. harden cfn-init
3. add outputs
4. figure out multiple ENI model


### post
1. logging
2. harden IAM roles
   1. add on what we need
3. spigot
4. monitoring
5. create app run user for mc
   1. https://stackoverflow.com/questions/16733633/how-to-run-script-on-aws-cloud-formation-startup-as-a-different-user
   2. sudo -u minecraft ... ?
6. replace default VPC 
   1. diagram out network design
      1. in progress
   2. VPC created
7. figure out how to turn subnet-id into VPC-ID, tamping down on stuff needed for core cft
8. start/stop lambda
   1. run appstart cmd on instance startup
   2. https://stackoverflow.com/questions/49594391/aws-ec2-run-script-program-at-startup
   3. or... stick scipt in startup dir
   4. create role
   5. add SGs
   6. add dryrun
   7. weirdness with VPC / timeouts 
      1. turn VPC off and it works
9.  make core CFT able to make multiple servers
10. set up SSM
    1.  add IAM role and it works, no more SSH SG
11. EBS snapshots
12. start/stop script


Next steps:
1. test start/stop
```
{
  "ec2-id": "i-0014e5fa657f8d541",
  "action": "start"
}
```
   * can't seem to do it with lambda, investigate more 
   * needs to be checked with AWS

2. set up snapshots
   1. done, test
   2. add to core CFT
3. cfn-init tuning
   1. rc.conf
      1. done