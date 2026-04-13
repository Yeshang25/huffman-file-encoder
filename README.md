  #  Huffman File Encoder & Decoder

A web-based application that performs file encoding and decoding using the **Huffman Coding algorithm**, enabling efficient data compression and reconstruction.

---

##  Features

-  Upload text files for encoding and decoding  
-  Efficient compression using Huffman Coding (Greedy Algorithm)  
-  Lossless decoding (original file perfectly reconstructed)  
-  Interactive web interface using Flask  
-  Download compressed (.bin) and decompressed (.txt) files  

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS, JavaScript  
- **Core Algorithm:** Huffman Coding (Min Heap / Priority Queue)  

---

##  How It Works

1. Calculate frequency of each character  
2. Build Huffman Tree using Min Heap  
3. Generate binary codes for characters  
4. Encode text into compressed binary format  
5. Decode using stored code mapping  

---

## 📁 Project Structure
```
huffman-file-encoder/
│
├── static/
│ ├── style.css
│ └── script.js
│
├── templates/
│ └── index.html
│
├── app.py
├── huffmancode.py
├── requirements.txt
└── README.md
```


---

## ⚙️ Installation & Setup

```bash
# Clone repository
git clone https://github.com/Yeshang25/huffman-file-encoder.git

# Navigate to project
cd huffman-file-encoder

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

## 🌐 Usage

* Open browser → `http://127.0.0.1:5000`
* Upload `.txt` file to encode
* Download compressed file
* Upload compressed file to decode

---

##  Screenshots

*Add your project screenshots here (UI, encoding, decoding)*

---

## Learning Outcomes

* Implemented Huffman Coding from scratch
* Applied greedy algorithms and tree data structures
* Built full-stack web application using Flask
* Handled file processing and data transformation

---

##  Future Improvements

* Support binary file compression
* Improve compression efficiency (bit-level storage)
* Deploy on cloud (Render / AWS / Azure)
* Add drag-and-drop UI enhancements

---

##  Author

Upadhyay Yeshang
