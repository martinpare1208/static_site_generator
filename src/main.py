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


leaf_node = a_text_node.text_node_to_html_node()
leaf_node.to_html()

words = f"This is text with a ` code block ` word"
wordy = f'Super  i am `super` `not`'
print(wordy.split('`'))