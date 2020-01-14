# TESTS MUST BE RUN FROM PROJECT ROOT (i.e. `[...]/root/tests/..`)
# absolute import
import unittest

from dlk_cloud.foo import Foo
from dlk_cloud.bar_abs import Bar as BarAbs
from dlk_cloud.bar_rel import Bar as BarRel

class TestAbsImport(unittest.TestCase):
    def test_foo(self):  
        self.assertEqual('bar', Foo().bar())
    
