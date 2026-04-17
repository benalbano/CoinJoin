# test_coinjoin.py
"""
Tests for CoinJoin module.
"""

import unittest
from coinjoin import CoinJoin

class TestCoinJoin(unittest.TestCase):
    """Test cases for CoinJoin class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinJoin()
        self.assertIsInstance(instance, CoinJoin)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinJoin()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
