import json
import boto3
import logging
import os
import pprint as p

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def input_validation(event):
    if not event.get('ec2-id'):
        logger.info("no ec2 instance ID detected")
        return False
    if not event.get('action'):
        logger.info("no action supplied")
        return False

    if event['action'] not in ("start", "stop", "restart"):
        logger.info("invalid action")
        return False

    if not event['ec2-id'].startswith("i-"):
        logger.info("instance ID malformed")
        return False


    return True


def start_instance(id, awssvc):
    action = None
    try:
        action = awssvc['ec2'].start_instances(
            InstanceIds=[
                id
            ],
            DryRun = False
        )
    except ClientError as e:
        logger.info(f"Error starting instance {id}: {e}")
    
    return action


def stop_instance(id, awssvc):
    action = None
    try:
        action = awssvc['ec2'].stop_instances(
            InstanceIds=[
                id
            ],
            DryRun = False
        )
    except ClientError as e:
        logger.info(f"Error stopping instance {id}: {e}")
    
    return action

def restart_instance(id, awssvc):
    action = None
    try:
        action = awssvc['ec2'].reboot_instances(
            InstanceIds=[
                id
            ],
            DryRun = False
        )
    except ClientError as e:
        logger.info(f"Error restarting instance {id}: {e}")
    
    return action

def lambda_handler(event, context):
    
    awssvc = {}
    awssvc['ec2'] = boto3.client('ec2')
    
    validated = False
    if input_validation(event):
        validated = True

    if validated:
        if event['action'] == "start":
            start_instance(event['ec2-id'], awssvc)
        if event['action'] == "stop":
            stop_instance(event['ec2-id'], awssvc)
        if event['action'] == "restart":
            restart_instance(event['ec2-id'], awssvc)
    
    return {
        'statusCode': 200,
        'validated': validated,
        'body': {
            'ec2-id': event.get('ec2-id'),
            'action': event.get('action')
        }
    }
