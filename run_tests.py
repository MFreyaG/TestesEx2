from core.test_loader import TestLoader
from core.test_runner import TestRunner
from core.test_suite import TestSuite
from framework_tests.test_loader_test import TestLoaderTest
from framework_tests.test_case_test import TestCaseTest
from framework_tests.test_suite_test import TestSuiteTest

loader = TestLoader()
test_case_suite = loader.make_suite(TestCaseTest)
test_suite_suite = loader.make_suite(TestSuiteTest)
test_load_suite = loader.make_suite(TestLoaderTest)

suite = TestSuite()
suite.add_test(test_case_suite)
suite.add_test(test_suite_suite)
suite.add_test(test_load_suite)

runner = TestRunner()
runner.run(suite)