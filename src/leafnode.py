from htmlnode import *


class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, props)
    self._value = value
    self._tag = tag
    self._props = props
    
  def __eq__(self, other):
    if (self._value == other._value) and (self._tag == other._tag) and (self._props == other._props):
      return True
    return False
    
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
      
      


