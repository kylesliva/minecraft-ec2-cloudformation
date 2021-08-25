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
1. create KMS key in template

### ec2
1. set up instance profile stuff
   1. done


### post
1. logging
2. harden IAM roles
   1. add on what we need
3. spigot
4. monitoring
5. create app run user for mc
   1. https://stackoverflow.com/questions/16733633/how-to-run-script-on-aws-cloud-formation-startup-as-a-different-user
   2. sudo -u minecraft ... ?
   3. perhaps just use rc.local for appstart, and do a reboot to start app
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
     * https://aws.amazon.com/premiumsupport/knowledge-center/ec2-launch-issue/

2. set up snapshots
   1. done, test
   2. add to core CFT
      1. is the default role ARN okay?
      2. done
3. cfn-init tuning
   1. rc.conf
      1. done
4. add craftbukkit for mod capabilities
