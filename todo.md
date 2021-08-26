# TODO

## Things that need to get done
1. test start/stop Lambda
   * can't seem to do it with lambda, investigate more 
   * needs to be checked with AWS
     * https://aws.amazon.com/premiumsupport/knowledge-center/ec2-launch-issue/
2. Add in conditionals for Spot price
   1. see here https://github.com/vatertime/minecraft-spot-pricing/blob/master/cf.yml
3. Set up logging/monitoring (may require mods)
4. Harden IAM roles
5. Add instance profile to CFN
6. Create app run user
7. create EC2 keypair in core.json
8. document blkid trickery greatly simplifying EBS business :D 
   1. https://serverfault.com/questions/975196/using-blkid-to-check-if-an-attached-ebs-volume-is-formatted
   
## Things that got done
1. set up snapshots
   1. done, test
   2. add to core CFT
      1. is the default role ARN okay?
      2. done
2. cfn-init tuning
   1. rc.conf
      1. done
      2. 
3. replace default VPC 
   1. diagram out network design
      1. in progress
   2. VPC created
4. set up SSM
    1.  add IAM role and it works, no more SSH SG
    2.  add to CFN
5.  Create custom route table with:
   1. local route to VPC
   2. route to IGW
      1. 0/0 to igw-id
   3. done
6. Use S3 on core creation to push desired files to EBS (perhaps from snapshot)
7. for 2.0, test ability to make multiple servers
   1. create KMS key in core template
      1. done
   2. done
8. do server.properties changes in cfn-init
   1. done


## Start/stop Lambda dummy request 
```
{
  "ec2-id": "i-0014e5fa657f8d541",
  "action": "start"
}
```