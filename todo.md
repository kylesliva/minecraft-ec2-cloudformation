# TODO

## TODO TODO
* [switch to this](https://github.com/todomd/todo.md)
  
## Things that need to get done
1. Set up logging/monitoring (may require mods)
   1. Set up polling for https://github.com/sladkoff/minecraft-prometheus-exporter
      1. avoiding due to security issues
   2. looking at CloudWatch
2. Harden IAM roles
   2. figure out what I need to create roles in CFN
   3. Create admin role
      1. everything needed to manage the CFN setup
   4. Create op role
      1. start/stop, SSM perhaps
3. Create app run user
   1. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-init.html
4. document blkid trickery greatly simplifying EBS business :D 
   1. https://serverfault.com/questions/975196/using-blkid-to-check-if-an-attached-ebs-volume-is-formatted
5. Put in warning about releasing Elastic IPs upon deletion of core.json
6. Clean up docs and add in references to best practices
7. change modes on non-executables
8. https://github.com/YouHaveTrouble/minecraft-optimization
   
## Things that got done

1. set up snapshots
   1. done, test
   2. add to core CFT
      1. is the default role ARN okay?
      2. done
2. Add instance profile to CFN
      1. done
3. cfn-init tuning
   1. rc.conf
      1. done
4. replace default VPC 
   1. diagram out network design
      1. in progress
   2. VPC created
5. set up SSM
    1.  add IAM role and it works, no more SSH SG
    2.  add to CFN
6.  Create custom route table with:
   1. local route to VPC
   2. route to IGW
      1. 0/0 to igw-id
   3. done
7. Use S3 on core creation to push desired files to EBS (perhaps from snapshot)
8. for 2.0, test ability to make multiple servers
   1. create KMS key in core template
      1. done
   2. done
9. do server.properties changes in cfn-init
   1. done
10. Set up AZ selection in core.json
   2. done
11. set up auto-spot pricing conditional
   3. https://github.com/vatertime/minecraft-spot-pricing/blob/master/cf.yml
12. Swing SGs out to VPC CFT and rename so that multiple core+ec2 stacks can be deployed in one VPC


## Start/stop Lambda dummy request 
```
{
  "ec2-id": "i-0014e5fa657f8d541",
  "action": "start"
}
```

## Compiling Prometheus plugin
```
# clone this https://github.com/sladkoff/minecraft-prometheus-exporter
# http://rdwl.xyz/blog/how-to-compile-spigot-plugins/
sudo apt install default-jre default-jdk maven                         
mvn clean package 
```