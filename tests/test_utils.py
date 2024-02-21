import unittest
from unittest.mock import patch
from pathlib import Path
import os
import sqlite3
from src.utils import get_data_dir, DB


class TestDataDirFunction(unittest.TestCase):

    def test_returns_path_object(self):
        """Test that the function returns a Path object."""
        data_dir = get_data_dir()
        self.assertIsInstance(data_dir, Path)

    def test_returns_existing_directory(self):
        """Test that the function returns an existing directory."""
        data_dir = get_data_dir()
        self.assertTrue(data_dir.exists())
        self.assertTrue(data_dir.is_dir())

    def test_returns_correct_data_directory(self):
        """Test that the returned path ends with 'data' directory."""
        data_dir = get_data_dir()
        self.assertTrue(str(data_dir).endswith('data'))

    @patch.dict(os.environ, {'MY_PROJECT_DATA_DIR': '/tmp/test_data_dir'})
    def test_uses_environment_variable_if_set(self):
        """Test that the function uses the path from an environment variable when set."""
        expected_path = Path('/tmp/test_data_dir')
        data_dir = get_data_dir()
        self.assertEqual(data_dir, expected_path)

    # Additional tests for environment variable scenarios can be added here

class TestDBClass(unittest.TestCase):
    
    def setUp(self):
        self.DB = DB()
        
    def test_connection_exists(self):
        self.assertIsInstance(self.DB.con, sqlite3.Connection)
    
if __name__ == '__main__':
    unittest.main()
