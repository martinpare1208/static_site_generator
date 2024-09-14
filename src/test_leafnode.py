from leafnode import *
import unittest

class LeafNodeTest(unittest.TestCase):
  def test_eq(self):
    node = LeafNode('a', 'Hello', {
  'href': 'www.youtube.com',
  'src': 'hello.img'
})
    node2 = LeafNode('a', 'Hello', {
  'href': 'www.youtube.com',
  'src': 'hello.img'
})
    
    self.assertEqual(node, node2)
    
  def test_not_eq(self):
    node = LeafNode('a', 'Hello', {
  'href': 'www.youtube.com',
  'src': 'hello.img'
})
    node2 = LeafNode('a', 'Hello', {
  'href': 'www.youtube.com',
  'src': 'hello.im'
})

    self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
