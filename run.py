from tests.test_class_attr import ClassAttribute
from tests.test_hidden_layer import HiddenLayer
from tests.test_load_delay import LoadDelay
from tests.test_ajax_data import AJAXData
from tests.test_client_side_delay import ClientSideDelay
from tests.test_click import ClickData
from tests.test_text_input import TextInputPage
from tests.test_scrollbars import Scrollbars

import unittest
from unittest import TestSuite

def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in (
        ClassAttribute,
        HiddenLayer,
        LoadDelay,
        AJAXData,
        ClientSideDelay,
        ClickData,
        TextInputPage,
        Scrollbars
    ):
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


unittest.main(verbosity=2)