import boto3
import mypy_boto3_dynamodb.service_resource as dynamodb_resources


class DynamoDefiner:
    dynamo: dynamodb_resources.DynamoDBServiceResource

    def __init__(self, endpoint_url: str = None):
        dynamo: dynamodb_resources.DynamoDBServiceResource = boto3.resource(
            "dynamodb", endpoint_url=endpoint_url
        )
        self.dynamo = dynamo

    def create_user_table(self, *, table_name):
        self.dynamo.create_table(TableName=table_name)
