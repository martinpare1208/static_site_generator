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
    for k, v in self._props.items():
      string_to_add = ' ' + k + '=' + '"' + v + '"'
      print(string_to_add)
      string_repr += string_to_add
    print(string_repr)
    return string_repr
  
  def get_tag(self):
    return self._tag
      
