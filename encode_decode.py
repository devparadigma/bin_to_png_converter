
from PIL import Image
import numpy as np
import math

def file_to_image(input_file, output_image="output.png"):
    with open(input_file, "rb") as f:
        byte_data = f.read()

    # Группируем по 3 байта (R, G, B)
    pixels = []
    for i in range(0, len(byte_data), 3):
        chunk = byte_data[i:i+3]
        if len(chunk) < 3:
            chunk += b'\x00' * (3 - len(chunk))
        pixels.append(tuple(chunk))

    side = math.ceil(math.sqrt(len(pixels)))
    total_pixels = side * side
    pixels += [(0, 0, 0)] * (total_pixels - len(pixels))

    img_array = np.array(pixels, dtype=np.uint8).reshape((side, side, 3))
    img = Image.fromarray(img_array, mode='RGB')
    img.save(output_image)
    print(f"Файл закодирован в PNG: {output_image} ({side}x{side})")

def image_to_file(input_image="output.png", output_file="restored.bin"):
    img = Image.open(input_image).convert('RGB')
    data = np.array(img).reshape(-1, 3)

    byte_array = bytearray()
    for r, g, b in data:
        byte_array += bytes([r, g, b])

    byte_array = byte_array.rstrip(b'\x00')

    with open(output_file, "wb") as f:
        f.write(byte_array)

    print(f"Файл восстановлен из PNG: {output_file}")

file_to_square_image = file_to_image
square_image_to_file = image_to_file
