import boto3
import mypy_boto3_dynamodb.service_resource as dynamodb_resources
from abc import ABCMeta, abstractmethod
from user_repository import UserRepository, SavingParams
from typing import Optional


class UserDynamoRepository(UserRepository):
    dynamoTable: dynamodb_resources.Table

    def __init__(self, *, user_table_name: str, endpoint_url: Optional[str] = None):
        dynamodb: dynamodb_resources.DynamoDBServiceResource = boto3.resource(
            "dynamodb", endpoint_url=endpoint_url
        )
        self.dynamoTable = dynamodb.Table(user_table_name)

    def save(self, params: SavingParams):
        self.dynamoTable.put_item(Item={"id": params.id, "name": params.name})
