import os
from unittest import TestCase
from gendiscalpy.install_gendiscal import download_and_extract, select_path, install

INSTALL_PATH = os.path.join(os.path.expanduser('~'), 'bin')
INSTALL_PATH_BIN = os.path.join(INSTALL_PATH, 'GenDisCal')


class Test(TestCase):
    def tearDown(self) -> None:
        if os.path.isfile(INSTALL_PATH_BIN):
            os.remove(INSTALL_PATH_BIN)

    def test_download_and_extract(self):
        bin = download_and_extract(target_path=INSTALL_PATH)
        self.assertEqual(bin, INSTALL_PATH_BIN)
        self.assertTrue(os.path.isfile(bin))
        self.assertTrue(os.access(bin, os.X_OK))

    def test_select_path(self):
        path = select_path()
        self.assertTrue(os.path.isdir(path))

    def test_install(self):
        install()
