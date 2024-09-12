from textnode import *
from htmlnode import *


print('hello world')
a_text_node = TextNode('Hello', text_type_bold, 'www.google.com')
print(a_text_node)
print(TextNode.__eq__(a_text_node, a_text_node))
a_html_node = HTMLNode(props={
  "href": 'youtube.com',
  "src": "images/hello.png"
})
