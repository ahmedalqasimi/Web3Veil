# test_web3veil.py
"""
Tests for Web3Veil module.
"""

import unittest
from web3veil import Web3Veil

class TestWeb3Veil(unittest.TestCase):
    """Test cases for Web3Veil class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Veil()
        self.assertIsInstance(instance, Web3Veil)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Web3Veil()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
