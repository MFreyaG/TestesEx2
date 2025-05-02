from test_case import TestCase
from test_result import TestResult

class MyTest(TestCase):
    def set_up(self):
        pass
    
    def tear_down(self):
        pass
        
    def test_a(self):
        pass

    def test_b(self):
        pass

    def test_c(self):
        pass

result = TestResult()

test = MyTest('test_a')
test.run(result)

test = MyTest('test_b')
test.run(result)

test = MyTest('test_c')
test.run(result)

print(result.summary())