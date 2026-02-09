# test_styledcomp.py
"""
Tests for StyledComp module.
"""

import unittest
from styledcomp import StyledComp

class TestStyledComp(unittest.TestCase):
    """Test cases for StyledComp class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StyledComp()
        self.assertIsInstance(instance, StyledComp)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StyledComp()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
