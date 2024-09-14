from textnode import *


class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    #html tag name like <a>
    self._tag = tag
    #string value of html tag
    self._value = value
    #HTMLNode objects
    self._children = children
    #dictionary of html attributes
    self._props = props
    
  def __eq__(self, other):
    if (self._tag == other._tag) and (self._value == other._value) and (self._children == other._children) and (self._props == other._props):
      return True
    return False
    
  def to_html(self):
    raise NotImplementedError('Not yet implemented')
  
  def props_to_html(self):
    string_repr = f''
    if self._props is None:
      return ''
    for k, v in self._props.items():
      string_to_add = ' ' + k + '=' + '"' + v + '"'
      print(string_to_add)
      string_repr += string_to_add
    print(string_repr)
    return string_repr
  
  def get_tag(self):
    return self._tag
  

      

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    
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
        formatted_props = self.props_to_html()
        print(formatted_props)
        html_string = f'<{self._tag}{formatted_props}>{self._value}</{self._tag}>'
        print(html_string)
        return html_string
      
      

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

  def to_html(self):
      if self._children is None or len(self._children) == 0:
        raise ValueError('Parent Node must have children')
      elif self._tag is None:
        raise ValueError('Parent Node must have a tag')
      else:
        html_string = f''
        for each_children in self._children:
          html_string += each_children.to_html()
      return f"<{self._tag}{self.props_to_html()}>{html_string}</{self._tag}>"
      

node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
)
      
print(node.to_html())
