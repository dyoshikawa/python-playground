from unittest import main, TestCase
from unittest.mock import MagicMock, patch
from sample_use_case import SampleUseCase


class TestSampleUseCase(TestCase):
    @patch.multiple(SampleUseCase, __abstractmethods__=set())
    def test_sample(self):
        use_case = SampleUseCase()
        use_case.execute = MagicMock(return_value="hello")
        self.assertEqual(use_case.execute(), "hello")


if __name__ == "__main__":
    main()