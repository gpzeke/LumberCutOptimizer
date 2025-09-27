import unittest
from unittest import mock
from unittest.mock import patch
from decimal import Decimal

from data_store import *
from cli_elements import *
from user_input import *

class TestDataStoreManipulation(unittest.TestCase):
    def test_add_item_to_store(self):
        store = DataStore()
        store.add_dimension_store(Decimal('15.0'), Decimal('31.25'), 3)
        assert store.parts == [(15.0, 31.25, 3)]

    def test_add_multiple_items_to_store(self):
        store = DataStore()
        store.add_dimension_store(Decimal('15.0'), Decimal('31.25'), 3)
        store.add_dimension_store(Decimal('10.5'), Decimal('5.75'), 2)
        assert store.parts == [(15.0, 31.25, 3), (10.5, 5.75, 2)]