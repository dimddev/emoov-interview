import time
import unittest
from src.decorators import DecoratorsBase, DecoratorsEncrypt, DecoratorLogger, DecoratorPerformance


class TestDecoratorBase(unittest.TestCase):

    def setUp(self):
        self.dec = DecoratorsBase

    @staticmethod
    @DecoratorsBase.accepts(str)
    def method_to_be_tested_str(name):
        return True

    @staticmethod
    @DecoratorsBase.accepts(int)
    def method_to_be_tested_int(num):
        return True


    @staticmethod
    @DecoratorsBase.accepts(str, int)
    def method_to_be_tested_str_and_int(name, num):
        return True

    @staticmethod
    @DecoratorsBase.accepts(int, str)
    def method_to_be_tested_int_and_str(num, name):
        return True

    @staticmethod
    @DecoratorsBase.accepts(int, int)
    def method_to_be_tested_int_and_int(num, num1):
        return True

    def test_accept_str(self):
        self.assertTrue(self.method_to_be_tested_str("emoov"))

    def test_accept_int(self):
        self.assertTrue(self.method_to_be_tested_int(42))

    def test_accept_str_and_int(self):
        self.assertTrue(self.method_to_be_tested_str_and_int("emoov", 42))

    def test_accept_int_and_str(self):
        self.assertTrue(self.method_to_be_tested_int_and_str(42, 'emoov'))

    def test_accept_int_and_int(self):
        self.assertTrue(self.method_to_be_tested_int_and_int(42, 420))

    def test_accpet_type_error(self):
        with self.assertRaises(TypeError):
            self.method_to_be_tested_int_and_int('42', 42)

    @staticmethod
    @DecoratorsEncrypt.encrypt(2)
    @DecoratorLogger.log('log.txt')
    def ceaser_cipher():
        return "Get get get low"

    def test_encrypt(self):
        self.assertEqual(self.ceaser_cipher(), "Igv igv igv nqy")

    @DecoratorLogger.log('log.txt', msg="test data", name="test_log_decorator")
    def log_decorator(self):
        return True

    def test_log_decorator(self):
        self.assertTrue(self.log_decorator())

    @staticmethod
    @DecoratorPerformance.timeit('timeit.log')
    def decorator_performance():
        time.sleep(1)
        return True

    def test_decorator_performance(self):
        self.assertTrue(self.decorator_performance())

if __name__ == '__main__':
    unittest.main()
