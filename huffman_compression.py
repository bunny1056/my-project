import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["freq", "char", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_map):
    heap = [Node(freq, char, None, None) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(node1.freq + node2.freq, None, node1, node2)
        heapq.heappush(heap, merged)

    return heap[0]

def build_code_table(node, prefix="", code_table=None):
    if code_table is None:
        code_table = {}
    if node.char is not None:
        code_table[node.char] = prefix
    else:
        build_code_table(node.left, prefix + "0", code_table)
        build_code_table(node.right, prefix + "1", code_table)
    return code_table

def huffman_encode(data, code_table):
    return ''.join(code_table[char] for char in data)

def huffman_decode(encoded_data, tree):
    decoded = ""
    node = tree
    for bit in encoded_data:
        node = node.left if bit == "0" else node.right
        if node.char:
            decoded += node.char
            node = tree
    return decoded

def main():
    print("Huffman Compression Program")
    print("="*65)
    h = int(input("Enter 1 to input text, 2 to load from file: "))

    if h == 1:
        my_string = input("Enter the string you want to compress: ")
    elif h == 2:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as f:
            my_string = f.read()
    else:
        print("Invalid input.")
        return

    if not my_string:
        print("No data to compress.")
        return

    print(f"Original string: {my_string}")
    print(f"Uncompressed size: {len(my_string) * 7} bits")

    freq_map = Counter(my_string)
    tree = build_huffman_tree(freq_map)
    code_table = build_code_table(tree)

    print("\nBinary codes:")
    for char, code in code_table.items():
        print(f"{repr(char)}: {code}")

    encoded_data = huffman_encode(my_string, code_table)
    print("\nEncoded binary data:")
    print(encoded_data)

    with open("compressed.txt", "w") as f:
        f.write(encoded_data)
    print("\nCompressed file saved as compressed.txt")

    original_bits = len(my_string) * 7
    compressed_bits = len(encoded_data)
    print(f"Compressed size: {compressed_bits} bits")
    print(f"Bits saved: {original_bits - compressed_bits}")

    decoded_data = huffman_decode(encoded_data, tree)
    print("\nDecoded string:")
    print(decoded_data)

if __name__ == "__main__":
    main()
