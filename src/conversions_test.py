import unittest
from conversions import *


class TestBlockMarkDown(unittest.TestCase):
    def test_markdown_to_block(self):
        test_string = """
        # I am a markdown
        
        # Hello
        
        * I am List Item\n* I am List Item
        """

        new_test_string = markdown_to_blocks(test_string)
        self.assertEqual(new_test_string, ['# I am a markdown', '# Hello', '* I am List Item', '* I am List Item'])

if __name__ == "__main__":
    unittest.main()
