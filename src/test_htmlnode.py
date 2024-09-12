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
    
  def test_not_eq(self):
    node = HTMLNode('<a>', 'hello', children=None, props={
      'href': 'www.youtube.com'
    })
    node2 = HTMLNode('<a>', 'hello', children=None, props={
      'href': 'youtube.com'
    })
    self.assertNotEqual(node, node2)
    
  def test_tag_eq(self):
    node = HTMLNode('<a>', 'hello', children=None, props={
    'href': 'www.youtube.com'
  })
    node2 = HTMLNode('<a>', 'hello', children=None, props={
    'href': 'youtube.com'
  })
    self.assertEqual(node.get_tag(), node2.get_tag())
    



if __name__ == "__main__":
    unittest.main()
