from PIL import Image
import os

def remove_background(input_path, output_path, tolerance=30):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        datas = img.getdata()

        new_data = []
        # Get the background color from the top-left pixel
        bg_color = datas[0]
        
        for item in datas:
            # Check if the pixel is close to the background color
            if all(abs(item[i] - bg_color[i]) < tolerance for i in range(3)):
                new_data.append((255, 255, 255, 0)) # Transparent
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(output_path, "PNG")
        print(f"Successfully saved transparent logo to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Source path from previous step
source_path = r"C:\Users\sort_\.gemini\antigravity\brain\b0184e8a-368d-47c4-a94c-f391c8aa5195\uploaded_image_1_1764513924938.png"
dest_path = r"d:\Programmieren\MyRecorder\MyRecorder\myrecorderlogo.png"

remove_background(source_path, dest_path)
