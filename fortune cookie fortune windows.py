import os
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
from io import BytesIO

# Function to get a fortune from the API
def get_fortune():
    url = "https://stoic-quotes.com/api/quote"  # API endpoint for stoic quotes
    try:
        response = requests.get(url)
        if response.status_code == 200:
            fortune_data = response.json()
            return fortune_data['text']
        else:
            return "Sorry, I couldn't get a fortune at the moment."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Function to split text into paginated chunks
def paginate_text(text, max_length=100):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= max_length:
            line += (word + " ")
        else:
            lines.append(line.strip())
            line = word + " "
    if line:
        lines.append(line.strip())
    return lines

# Function to calculate contrasting font color
def get_contrasting_color(rgb):
    r, g, b = rgb
    brightness = (r * 299 + g * 587 + b * 114) / 1000  # Luminosity formula
    return "white" if brightness < 128 else "black"

# Function to add paginated, styled text to the image
def add_text_to_image(img, text):
    draw = ImageDraw.Draw(img)

    # Attempt to load Times New Roman or fallback to Liberation Serif
    font_path = r"C:\Windows\Fonts\arial.ttf"  # Default Arial path
    if not os.path.exists(font_path):
        font_path = r"C:\Windows\Fonts\times.ttf"  # Fallback to Times New Roman
    font = ImageFont.truetype(font_path, size=24)  # Adjust font size

    # Split text into paginated chunks
    lines = paginate_text(text, max_length=40)

    # Get background color from the center of the image
    img_width, img_height = img.size
    center_pixel = img.getpixel((img_width // 2, img_height // 2))  # Sample center pixel
    font_color = get_contrasting_color(center_pixel)

    # Calculate vertical alignment
    line_height = 30  # Approximate height of each text line
    y_start = (img_height - (len(lines) * line_height)) // 2

    for i, line in enumerate(lines):
        text_width = draw.textlength(line, font=font)
        x = (img_width - text_width) // 2
        y = y_start + i * line_height
        draw.text((x, y), line, font=font, fill=font_color)

    return img

# Function to fetch an image and overlay text
def fetch_image_with_text():
    # Use the provided working image URL
    image_url = "https://picsum.photos/2000/2000"
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))

            # Get a fortune and add text to the image
            fortune = get_fortune()
            img = add_text_to_image(img, fortune)

            return img
        else:
            messagebox.showerror("Error", "Failed to fetch image.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to display the image with text overlay
def display_image():
    img = fetch_image_with_text()
    if img:
        tk_img = ImageTk.PhotoImage(img)
        image_label.config(image=tk_img)
        image_label.image = tk_img

# Create the main application window
app = tk.Tk()
app.title("Fortune Fetcher")
app.geometry("600x500")
app.configure(bg="#2e2e2e")  # Dark background for a modern look

# Create a label for instructions
instruction_label = tk.Label(
    app, text="Click the button to fetch a fortune:", font=("Arial", 14), bg="#2e2e2e", fg="white"
)
instruction_label.pack(pady=20)

# Create a button to fetch the image with the fortune
fetch_button = tk.Button(
    app,
    text="Fetch Fortune",
    command=display_image,
    font=("Arial", 12),
    bg="#4caf50",
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
)
fetch_button.pack(pady=10)

# Create a label to display the image
image_label = tk.Label(app, bg="#2e2e2e")
image_label.pack(pady=20)

# Start the GUI event loop
app.mainloop()
