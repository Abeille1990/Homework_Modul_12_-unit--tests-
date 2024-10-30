from functools import wraps
import unittest

def skip_if_frozen(test_func):
    @wraps(test_func)
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            # print("Тесты в этом кейсе заморожены")
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return test_func(self, *args, **kwargs)
    return wrapper