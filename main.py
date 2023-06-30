from tree_sitter import Language, Parser

PY_LANGUAGE = Language('build/sage.so', 'python')

SAMPLE_CODE = bytes("""
x = 2^4

# y = 4.sqrt()
""", "utf8")

def ast_tree(code=SAMPLE_CODE):
    parser = Parser()
    parser.set_language(PY_LANGUAGE)
    tree = parser.parse(code)
    return tree

def capture_ints(tree=ast_tree()):
    PY_LANGUAGE.query("(integer) @").captures(tree.root_node)

def output(start_byte, end_byte, code=SAMPLE_CODE, start_include=True, end_include=True):
    if not start_include:
        start_byte += 1
    if not end_include:
        end_byte -= 1
    print(code[start_byte:end_byte].decode("utf-8"), end="")

def process(node=ast_tree().root_node, code=SAMPLE_CODE):
    start = node.start_byte
    end = node.end_byte
    cursor = start
    if node.type == "integer":
        print("Integer(", end="")
        #output(start, end)
        print(code[start: end].decode("utf-8"), end="")
        print(")", end="")
        return
    if node.type == "module":
        print("from sage.all_cmdline import *")
    for child_node in node.children:
        child_start = child_node.start_byte
        child_end = child_node.end_byte
        #output(cursor, child_start)
        print(code[cursor: child_start].decode("utf-8"), end="")
        process(child_node, code)
        cursor = child_end
    #output(cursor, end)
    print(code[cursor: end].decode("utf-8"), end="")

process()

