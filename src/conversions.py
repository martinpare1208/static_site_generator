block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

from textnode import *
import re

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



def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
    
text = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text,)]
print(split_nodes_image(text))


"""
        Function:
        raw string into a list of textnodes.
"""

def text_to_textnodes(text):
    delimiters = [['**',text_type_bold], ['*', text_type_italic], ['`',text_type_code]]
    text = [TextNode(text, text_type_text, None)]
    nodes = split_nodes_image(text)
    nodes = split_nodes_link(nodes)
    for each_delimiter in delimiters:
        nodes = split_nodes_delimiter(nodes, each_delimiter[0], each_delimiter[1])
    return nodes


string_test = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
print(text_to_textnodes(string_test))


"""
Function: Take raw markdown blocks into a list of strings
"""

def markdown_to_blocks(markdown):
    markdown = markdown.split('\n')
    new_markdown = []
    for each_markdown in markdown:
        each_markdown = each_markdown.strip()
        if each_markdown != '':
            new_markdown.append(each_markdown)
    return new_markdown


md = '''
# Markdown
> Markdown
> Markdown
'''
print(markdown_to_blocks(md))


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
a_block = '1. Hello\n2. Hello'
print(block_to_block_type(a_block))



