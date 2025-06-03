This project implements a **Huffman Coding-based compression and decompression utility** using Python. It demonstrates an efficient approach to lossless data compression by applying a classic greedy algorithm and optimized data structures like priority queues.

Features

- Compresses text using Huffman Coding
- Supports input via command-line or text file
- Displays character frequency, binary codes, and compression stats
- Writes compressed binary to a file (`compressed.txt`)
- Decodes the binary back to the original string

Concepts Used

- Greedy Algorithms
- Min-Heap (Priority Queue) for optimal tree construction
- Binary Tree Traversal
- Recursion
- File I/O in Python

Technologies

- Python 3.x
- `heapq` for min-heap
- `collections.Counter` for frequency counting
- `namedtuple` for tree node representation

How It Works

1. Input: Accepts string from user or file.
2. Frequency Map: Uses `Counter` to calculate frequencies of characters.
3. Huffman Tree: Built using a min-heap for efficient node merging.
4. Code Table: Recursively traverses the tree to assign binary codes.
5. Encoding: Replaces each character with its binary code.
6. Compression Stats: Compares compressed and uncompressed bit sizes.
7. Decoding: Traverses the tree based on binary code to recover the original string.

File Structure

- `huffman_compression.py`: Main Python script
- `compressed.txt`: Output file containing the binary-encoded message



