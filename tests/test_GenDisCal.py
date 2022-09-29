import os
import shutil
import logging
from unittest import TestCase
from gendiscalpy.GenDisCal import GenDisCal
import numpy as np

logging.basicConfig(level=logging.INFO)

os.chdir('..')


class TestGenDisCal(TestCase):
    def test_version(self):
        version = GenDisCal().version
        print(version)
        self.assertEqual(version, 'GenDisCal v1.3.1')

    def test_run_files(self):
        res = GenDisCal().run('test-data/*.fna')
        print(res)

    def test_run_fifo(self):
        res = GenDisCal().run('test-data/fifo.txt', file_list=True)
        print(res)

    def test_run_hist(self):
        res = GenDisCal().run('test-data/*.fna', histogram=True)
        print(res)

    def test_run_dist(self):
        res = GenDisCal().run('test-data/*.fna', distance_matrix=True)
        print(res)

    def test_preset(self):
        m1 = GenDisCal().run('test-data/*.fna', distance_matrix=True, preset='PaSiT4')
        m2 = GenDisCal().run('test-data/*.fna', distance_matrix=True, preset='PaSiT6')
        self.assertEqual(first=list(m1.columns), second=list(m2.columns))
        self.assertFalse(np.allclose(m1.values, m2.values))

    def test_method(self):
        m1 = GenDisCal().run('test-data/*.fna', distance_matrix=True, method='manhattan')
        m2 = GenDisCal().run('test-data/*.fna', distance_matrix=True, method='euclid')
        self.assertEqual(first=list(m1.columns), second=list(m2.columns))
        self.assertFalse(np.allclose(m1.values, m2.values))

    def test_two(self):
        val = GenDisCal().compare_two(assembly_1='test-data/FAM3257-i1-1.fna', assembly_2='test-data/FAM13496-i1-1.fna')
        self.assertGreater(val, 0)

    def test_no_permissions(self):
        no_permissions_file = 'test-data/FAM3257-i1-1.fna.no_permissions'
        if not os.path.isfile(no_permissions_file):
            shutil.copy('test-data/FAM3257-i1-1.fna', no_permissions_file)
        os.chmod(no_permissions_file, mode=0)  # make unreadable
        with self.assertRaises(Exception):
            val = GenDisCal().compare_two(assembly_1=no_permissions_file, assembly_2='test-data/FAM13496-i1-1.fna')
