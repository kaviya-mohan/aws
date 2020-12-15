import json
import boto3
def lambda_handler(event, context):
    client = boto3.client("ec2")
    status = client.describe_instance_status(IncludeAllInstances = True)
    for i in status["InstanceStatuses"]:
        print("AvailabilityZone :", i["AvailabilityZone"])
        print("InstanceId :", i["InstanceId"])
        print("Instance State :", i["InstanceState"])
        print("Instance Status :", i["InstanceStatus"])
        print("System Status :", i["SystemStatus"])
        print("\n")
