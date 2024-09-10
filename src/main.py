from textnode import *
print('hello world')
a_text_node = TextNode('Hello', 'bold', 'www.google.com')
print(a_text_node)
print(TextNode.__eq__(a_text_node, a_text_node))
