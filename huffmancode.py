class HuffmanNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}

    def make_frequency_dict(self, text):
        """Create frequency dictionary for each character"""
        frequency_dict = {}
        for char in text:
            if char not in frequency_dict:
                frequency_dict[char] = 0
            frequency_dict[char] += 1
        return frequency_dict

    def make_heap(self, frequency_dict):
        """Create a priority queue (min-heap) from frequency dictionary"""
        from heapq import heappush
        self.heap = []

        for char in frequency_dict:
            node = HuffmanNode(char, frequency_dict[char])
            heappush(self.heap, (node.frequency, id(node), node))

    def merge_nodes(self):
        """Merge nodes to build Huffman Tree"""
        from heapq import heappush, heappop

        while len(self.heap) > 1:
            freq1, _, node1 = heappop(self.heap)
            freq2, _, node2 = heappop(self.heap)

            merged_node = HuffmanNode(None, freq1 + freq2)
            merged_node.left = node1
            merged_node.right = node2

            heappush(self.heap, (merged_node.frequency, id(merged_node), merged_node))

    def make_codes_helper(self, node, current_code):
        """Recursive helper to generate Huffman codes"""
        if node is None:
            return

        if node.character is not None:
            self.codes[node.character] = current_code
            self.reverse_codes[current_code] = node.character
            return

        self.make_codes_helper(node.left, current_code + "0")
        self.make_codes_helper(node.right, current_code + "1")

    def make_codes(self):
        """Generate Huffman codes from tree"""
        if not self.heap:
            return

        _, _, root = self.heap[0]

        self.codes = {}
        self.reverse_codes = {}

        self.make_codes_helper(root, "")

    def get_encoded_data(self, text):
        """Encode text using Huffman codes"""
        encoded_data = ""
        for char in text:
            encoded_data += self.codes[char]
        return encoded_data

    def compress(self, text):
        """Encode input text using Huffman coding"""
        frequency_dict = self.make_frequency_dict(text)
        self.make_heap(frequency_dict)
        self.merge_nodes()
        self.make_codes()

        encoded_data = self.get_encoded_data(text)
        return encoded_data, self.codes

    def decompress(self, encoded_data):
        """Decode encoded binary string back to original text"""
        current_code = ""
        decoded_text = ""

        for bit in encoded_data:
            current_code += bit
            if current_code in self.reverse_codes:
                character = self.reverse_codes[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text