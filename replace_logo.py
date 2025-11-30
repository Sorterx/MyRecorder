from PIL import Image
import os

source_path = r"C:\Users\sort_\.gemini\antigravity\brain\b0184e8a-368d-47c4-a94c-f391c8aa5195\uploaded_image_1764515845608.jpg"
dest_path = r"d:\Programmieren\MyRecorder\MyRecorder\myrecorderlogo.png"

try:
    img = Image.open(source_path)
    img.save(dest_path, "PNG")
    print(f"Successfully converted and saved logo to {dest_path}")
except Exception as e:
    print(f"Error: {e}")
