Bit-to-Pixel File Encoder
This project provides a simple and efficient way to encode any binary file into a PNG image using pixel colors, and decode it back to the original file — all through a modern GUI interface built with PyQt5.

✨ Features
🔁 Encode any file (text, zip, executable, etc.) into a lossless PNG image.

🎨 Uses 24-bit RGB pixels: each pixel stores 3 bytes of data.

🧵 Fast & memory-efficient encoding (no base64 or bit strings).

🖱️ Drag-and-drop file selection.

💻 GUI built with PyQt5, styled and responsive.

🖼️ Encoded PNG can be viewed like any regular image.

🔓 Fully reversible — decode image to restore original file byte-for-byte.

🖼️ How It Works
The file is read as a sequence of bytes.

Each group of 3 bytes becomes one RGB pixel:
byte1 → R, byte2 → G, byte3 → B

If the file length isn’t divisible by 3, it’s padded with null bytes.

The pixels are arranged into a square image and saved as PNG.

The PNG is fully lossless and reversible.

🚀 Getting Started
🔧 Install dependencies
bash
Копировать
Редактировать
pip install PyQt5 pillow numpy
▶️ Run the GUI
bash
Копировать
Редактировать
python app.py
📂 File Structure
bash
Копировать
Редактировать
.
├── app.py               # PyQt5 GUI interface
├── encode_decode.py     # Core encoding/decoding logic
🛠 Example Use
Open the GUI.

Drag any file into the window.

Click "Encode to PNG" — save the image.

Later, drag the PNG back and click "Decode from PNG" to recover the original file.

⚠️ Limitations
Large files will produce large images (e.g., 1MB ≈ 600x600 px).

Padding bytes may slightly increase image size, but do not affect decoding.

📘 License
MIT License.
Feel free to use, modify, and share.
