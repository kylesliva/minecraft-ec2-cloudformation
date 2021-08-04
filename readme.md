# Minecraft todo

## Introduction
This project creates a stateless Minecraft EC2 server in AWS. Game state is stored on an EBS to facilitate easier maintenance of the server. 

## CFTs 
1. VPC (to be added later)
   1. CIDR used: 10.0.144.0/24 (10.0.144.0/25, 10.0.144.128/25)
      1. Small, but I don't run a lot of stuff and I tend towards IP conservation
2. Core Infrastructure (core.json)
   1. must be named "minecraft-core" or imports in the next CFT will fail
3. EC2 (ec2.json)

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


### post
1. logging
2. harden IAM roles
3. spigot
4. monitoring
5. create app run user for mc
   1. https://stackoverflow.com/questions/16733633/how-to-run-script-on-aws-cloud-formation-startup-as-a-different-user
   2. sudo -u minecraft ... ?
6. replace default VPC 
   1. create static ENI to give us a static IP
      1. done, but still in default VPC
   2. diagram out network design
      1. in progress
   3. VPC created
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
9. make core CFT able to make multiple servers
10. Figure out single-AZ restriction AZ
    1.  can't use fn::getatt on supplied subnet, which is tough