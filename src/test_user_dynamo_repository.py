from os import environ
from dotenv import load_dotenv
from unittest import main, TestCase
from unittest.mock import MagicMock, patch
from sample_use_case import SampleUseCase
from user_dynamo_repository import UserDynamoRepository
from user_repository import SavingParams


class TestUserDynamoRepository(TestCase):
    userDynamoRepository: UserDynamoRepository

    def setUp(self):
        load_dotenv()
        self.userDynamoRepository = UserDynamoRepository(
            user_table_name=environ["USER_TABLE_NAME"],
            endpoint_url=environ["AWS_ENDPOINT_URL"],
        )

    def test_case(self):
        self.userDynamoRepository.save(SavingParams(id="1", name="John Doe"))


if __name__ == "__main__":
    main()