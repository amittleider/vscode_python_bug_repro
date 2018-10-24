from unittest import TestCase

from vscode_python_bug_repro_lib.my_class import MyClass

class TestMyClass(TestCase):
    def test_my_class(self):
        self.assertEqual(MyClass().my_integer, 1)