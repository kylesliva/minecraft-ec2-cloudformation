# Minecraft todo

## Introduction
This project creates a stateless Minecraft EC2 server in AWS. Game state is stored on an EBS to facilitate easier maintenance of the server. 

## CFTs 
1. VPC (to be added later)
2. Core Infrastructure (core.json)
   1. must be named "minecraft-core" or imports in the next CFT will fail
3. EC2 (ec2.json)

## TODO

1. VPC
   1. CIDR used: 10.0.144.0/24 (10.0.144.0/25, 10.0.144.128/25)
      1. Small, but I don't run a lot of stuff and I tend towards IP conservation
2. Static Infrastructure
    * EBS
    * DNS stuff
    * ENIs?
    * KMS key 
3. EC2
    * should be stateless

## Todo

### core
1. snapshots?
2. create KMS key in template

### ec2
1. set up cfn-init
   1. done
2. set up instance profile stuff
3. harden cfn-init
4. add outputs


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
7. start/stop lambda
   1. run appstart cmd on instance startup
   2. https://stackoverflow.com/questions/49594391/aws-ec2-run-script-program-at-startup
   3. or... subprocess
8. Can probably turn SBT in core.json into VPC
9. make core CFT able to make multiple servers