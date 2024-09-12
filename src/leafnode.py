from htmlnode import *


class LeafNode(HTMLNode):
  def __init__(self, tag, value, props):
    super().__init__(tag, props)
    self._value = value
    self._tag = tag
    self._props = props
    
  def to_html(self):
      if self._value is None:
        raise ValueError('Leaf Node must have a value')
      elif self._tag is None:
        return self._value
      else:
        formatted_props = HTMLNode.props_to_html(self)
        print(formatted_props)
        html_string = f'<{self._tag}{formatted_props}>{self._value}</{self._tag}>'
        print(html_string)
        return html_string
      
      
a_leaf_node = LeafNode('a', 'Hello', {
  'href': 'www.youtube.com',
  'src': 'hello.img'
})

a_leaf_node.to_html()


