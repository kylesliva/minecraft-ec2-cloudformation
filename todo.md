## TODO

1. test start/stop Lambda
```
{
  "ec2-id": "i-0014e5fa657f8d541",
  "action": "start"
}
```
   * can't seem to do it with lambda, investigate more 
   * needs to be checked with AWS
     * https://aws.amazon.com/premiumsupport/knowledge-center/ec2-launch-issue/
1. Add in conditionals for Spot if a persistent instance is desired
2. Set up logging/monitoring (may require mods)
3. Harden IAM roles
4. Add instance profile to CFN
5. Create app run user
6. for 2.0, test ability to make multiple servers
7. 1. create KMS key in core template


Done:
2. set up snapshots
   1. done, test
   2. add to core CFT
      1. is the default role ARN okay?
      2. done
3. cfn-init tuning
   1. rc.conf
      1. done
      2. 
4. replace default VPC 
   3. diagram out network design
      1. in progress
   4. VPC created
5. set up SSM
    1.  add IAM role and it works, no more SSH SG
    2.  add to CFN
6.  Create custom route table with:
   1. local route to VPC
   2. route to IGW
      1. 0/0 to igw-id
   3. done
7. Use S3 on core creation to push desired files to EBS (perhaps from snapshot)