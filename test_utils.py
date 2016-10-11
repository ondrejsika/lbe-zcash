# coding: utf8
# LBE - Lite Block Explorer
# Author: Ondrej Sika <ondrej@ondrejsika.com>
# License: MIT <http://ondrejsika.com/license/mit.txt>

import unittest

from utils import var_int_deserialize


class TestCase(unittest.TestCase):

    def test__var_int_deserialize(self):
        import binascii
        from StringIO import StringIO
        self.assertEqual(var_int_deserialize(StringIO(binascii.unhexlify('fd4005'))), 1344)
