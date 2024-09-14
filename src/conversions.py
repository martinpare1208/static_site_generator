from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for each_old_node in old_nodes:
        if each_old_node.text_type != text_type_text:
            nodes.append(each_old_node)
            continue
        nodes_to_add = []
        text = each_old_node.text
        list_words = text.split(delimiter)
        for i in range(len(list_words)):
            if (i == 0 or i % 2 == 0) and (len(list_words[i]) > 0):
                nodes_to_add.append(TextNode(list_words[i], text_type_text, None))
            elif (i % 2 != 0) and (len(list_words[i]) > 0):
                if (len(list_words[i][0]) == 1) and list_words[i] != ' ': 
                    nodes_to_add.append(TextNode(list_words[i], text_type, None))
        nodes.extend(nodes_to_add)
    return nodes

nodes1 = [
    TextNode('Hello i am `Superman`', text_type_code),
    TextNode('**Hello** I am superman', text_type_bold)
]

nodes = [
    TextNode("Normal text ", text_type_text),
    TextNode("with **bold** and `code`", text_type_text),
    TextNode(", and more normal text", text_type_text),
]

# Call the function with a bold delimiter
new_nodes_bold = split_nodes_delimiter(nodes, "**", text_type_bold)
print(new_nodes_bold)

# Call the function with a code delimiter on the result of the first call
final_nodes = split_nodes_delimiter(new_nodes_bold, "`", text_type_code)
print(final_nodes)