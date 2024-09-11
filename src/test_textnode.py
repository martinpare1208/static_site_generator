import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2, "Both are equal.")
    
    def test_noteq(self):
      node = TextNode("This is a text node", "bold")
      node2 = TextNode("This is a text", 'bold')
      self.assertNotEqual(node, node2, msg="Both are not equal.")
      
    def test_url_is_none(self):
      node = TextNode("This is a text node", "bold")
      self.assertIsNone(node.get_url())


if __name__ == "__main__":
    unittest.main()
