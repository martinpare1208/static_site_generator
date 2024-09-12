from htmlnode import *
import unittest


class TestHTMLNode(unittest.TestCase):
  def test_eq(self):
      
    test_node = node = HTMLNode(tag='<a>', value='hello', children=None, props={'href': 'www.youtube.com'})
    node = HTMLNode('<a>', 'hello', children=test_node, props={
      'href': 'www.youtube.com'
    })
    node2 = HTMLNode('<a>', 'hello', children=test_node, props={
      'href': 'www.youtube.com'
    })
    self.assertEqual(node, node2)
    
if __name__ == "__main__":
    unittest.main()
