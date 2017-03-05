""" A module that providing a set of decorators """

from datetime import datetime
import time
import os


class DecoratorsBase:
    """Base Decorator class"""

    @staticmethod
    def args_vs_types(types, *args):
        """args_vs_types

        :param types
        :param *args
        :param **kwargs
        """

        for (_arg, _type) in zip(args, types):
            if not isinstance(_arg, _type):
                raise TypeError('arg {} does not match {}'.format(_arg, _type))

    @staticmethod
    def accepts(*types):
        """decorator method that check and test arguments vs types"""

        def check_accepts(function):
            """Inner decorator function"""

            assert len(types) == function.__code__.co_argcount

            def new_f(*args, **kwargs):
                """Actual test args vs types"""
                DecoratorsBase.args_vs_types(types, *args)
                return function(*args, **kwargs)

            new_f.__name__ = function.__name__
            return new_f

        return check_accepts


class DecoratorsEncrypt:

    """ A class that provides Ceaser Cipher encryption"""

    key = None

    @staticmethod
    def encrypt_processor(function):
        """encrypt_processor

            :param function - decorated function
        """

        data = function()
        encrypt = [map(lambda n: n + DecoratorsEncrypt.key, map(ord, list(d))) for d in data if d]

        temp = list()

        _ = [temp.extend(d) for d in encrypt]

        return lambda: ''. join(map(chr, temp)).replace('"', ' ')

    @staticmethod
    @DecoratorsBase.accepts(int)
    def encrypt(key):
        """encrypt

        :param key int
        """

        DecoratorsEncrypt.key = key

        return DecoratorsEncrypt.encrypt_processor


class DecoratorLogger:

    """DecoratorLogger - providing logging functionality"""

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOGS_DIR = '{}/../logs/'.format(BASE_DIR)

    @staticmethod
    def log(log_file, **kwargs):

        """log

        :param log_file - filename
        :param **kwargs - dict that can contains 'msg' and 'name' keys
        """

        def logger(function):

            """logger

            :param function
            """

            function_name = kwargs.get('name') or function.__name__

            with open(DecoratorLogger.LOGS_DIR + log_file, 'a') as _file:

                if kwargs.get('msg') is None:

                    _file.write(
                        'Function {} was called at: {}\n'.format(
                            function_name, datetime.now()
                        )
                    )

                else:

                    _file.write(
                        'Function {} was called at: {} and took {} seconds\n'.format(
                            function_name, datetime.now(), kwargs.get('msg')
                        )
                    )

            _file.close()

            return function

        return logger


class DecoratorPerformance:

    """DecoratorPerformance"""

    @staticmethod
    def timeit(log_file):
        """timeit

        :param log_file
        """

        def logger(function):
            """logger

            :param f
            """

            start = time.time()
            result = function()
            end = time.time()
            total_time = end - start

            @DecoratorLogger.log(log_file, msg=total_time, name=function.__name__)
            def _log():
                """_log"""
                return result

            return _log

        return logger


class Decorators:
    """Decorators"""

    encrypt = DecoratorsEncrypt()
    logger = DecoratorLogger()
    performance = DecoratorPerformance()

