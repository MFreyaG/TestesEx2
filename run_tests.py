from core.test_loader import TestLoader
from core.test_runner import TestRunner
from framework_tests.test_loader_test import TestLoaderTest

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)