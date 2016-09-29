# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import call

from .context import p4gen

class CompilationTests(unittest.TestCase):
    """Parser test cases."""

    def setUp(self):
        self.assertIsNotNone(os.environ.get('P4BENCHMARK_ROOT'))
        self.assertIsNotNone(os.environ.get('PYTHONPATH'))
        pypath = os.environ.get('PYTHONPATH')
        p4bench = os.environ.get('P4BENCHMARK_ROOT')
        self.assertIn(p4bench, p4bench.split(os.pathsep))
        bmv2 = os.path.join(p4bench, 'behavioral-model')
        self.p4c = os.path.join(p4bench, 'p4c-bm/p4c_bm/__main__.py')
        switch_path = os.path.join(bmv2, 'targets/simple_switch/simple_switch')
        cli_path = os.path.join(bmv2, 'tools/runtime_CLI.py')


    def tearDown(self):
        pass

    def test_benchmark_parser_generator(self):
        ret = p4gen.bm_parser.benchmark_parser(10, 4)
        self.assertTrue(ret)
        prog = 'main'
        ret = call([self.p4c, 'output/%s.p4' % prog , '--json', 'output/%s.json' % prog])
        self.assertEqual(ret, 0)

    def test_benchmark_pipeline_generator(self):
        ret = p4gen.bm_pipeline.benchmark_pipeline(10, 128)
        self.assertTrue(ret)
        prog = 'main'
        ret = call([self.p4c, 'output/%s.p4' % prog , '--json', 'output/%s.json' % prog])
        self.assertEqual(ret, 0)

    def test_benchmark_memory_consumption_generator(self):
        ret = p4gen.bm_memory.benchmark_memory(10, 32, 1024)
        self.assertTrue(ret)
        prog = 'main'
        ret = call([self.p4c, 'output/%s.p4' % prog , '--json', 'output/%s.json' % prog])
        self.assertEqual(ret, 0)

    def test_benchmark_add_header_generator(self):
        ret = p4gen.bm_modification.benchmark_modification(10, 4, 'add')
        self.assertTrue(ret)
        prog = 'main'
        ret = call([self.p4c, 'output/%s.p4' % prog , '--json', 'output/%s.json' % prog])
        self.assertEqual(ret, 0)

    def test_benchmark_remove_header_generator(self):
        ret = p4gen.bm_modification.benchmark_modification(10, 4, 'rm')
        self.assertTrue(ret)
        prog = 'main'
        ret = call([self.p4c, 'output/%s.p4' % prog , '--json', 'output/%s.json' % prog])
        self.assertEqual(ret, 0)

    def test_benchmark_modify_header_generator(self):
        ret = p4gen.bm_modification.benchmark_modification(10, 4, 'mod')
        self.assertTrue(ret)
        prog = 'main'
        ret = call([self.p4c, 'output/%s.p4' % prog , '--json', 'output/%s.json' % prog])
        self.assertEqual(ret, 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CompilationTests)
    unittest.TextTestRunner(verbosity=2).run(suite)