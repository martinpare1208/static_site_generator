class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    #html tag name like <a>
    self.__tag = tag
    #string value of html tag
    self.__value = value
    #HTMLNode objects
    self.__children = children
    #dictionary of html attributes
    self.__props = props
    
  def __eq__(self, other):
    if (self.__tag == other.__tag) and (self.__value == other.__value) and (self.__children == other.__children) and (self.__props == other.__props):
      return True
    return False
    
  def to_html(self):
    raise NotImplementedError('Not yet implemented')
  
  def props_to_html(self):
    string_repr = f''
    for k, v in self.__props.items():
      string_to_add = f''
      string_to_add = string_to_add + k + '=' + '"' + v + '" '
      print(string_to_add)
      string_repr += string_to_add
    print(string_repr)
    return string_repr
  
  def get_tag(self):
    return self.__tag
      
