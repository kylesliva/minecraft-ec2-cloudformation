# Minecraft todo

## CFTs 

1. VPC
2. Static Infrastructure
    * EBS
    * DNS stuff
    * ENIs?
    * KMS key 
3. EC2
    * should be stateless

## Todo

# general
0. IAM roles are critical
1. add in dynamic billing tags via params
   1. done


# core
1. snapshots?
2. create KMS key in template

# ec2
1. mappings for SSH keys
   1. done
2. set up cfn-init
   1. done
3. set up instance profile stuff
4. harden cfn-init
5. add in admin user that isn't ec2-user


# post
1. logging
2. spigot
3. monitoring
4. replace default VPC
   1. create static ENI to give us a static IP
5. start/stop lambda
   1. run appstart cmd on instance startup
   2. https://stackoverflow.com/questions/49594391/aws-ec2-run-script-program-at-startup
   3. or... subprocess