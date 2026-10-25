# test_defivortex.py
"""
Tests for DefiVortex module.
"""

import unittest
from defivortex import DefiVortex

class TestDefiVortex(unittest.TestCase):
    """Test cases for DefiVortex class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = DefiVortex()
        self.assertIsInstance(instance, DefiVortex)

    def test_run_method(self):
        """Test the run method."""
        instance = DefiVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
