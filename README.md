# Fortune Fetcher  

**Fortune Fetcher** is a Python-based application that combines stoic quotes with visually appealing images. It fetches random fortunes (quotes) from an API, overlays them onto a dynamically generated image, and displays the result in a modern, user-friendly graphical user interface (GUI) built with `tkinter`.  

## Features  

### Core Functionalities  

1. **Fetch Random Fortunes**  
   - Retrieves motivational or stoic quotes from an external API.  

2. **Dynamic Image Generation**  
   - Uses images fetched from the `https://picsum.photos` API as backgrounds.  

3. **Styled Text Overlay**  
   - Overlays the fetched quote on the image, ensuring contrast and readability with:  
     - Automatic font color adjustment based on image brightness.  
     - Text pagination for longer quotes.  

4. **Interactive GUI**  
   - A simple and intuitive interface with a single button to fetch and display fortunes.  

5. **Error Handling**  
   - Displays friendly error messages in case of network issues or API failures.  

## Installation  

### Prerequisites  

Ensure your system has the following:  

1. **Python 3.x**  
   - Verify installation with:  
     ```bash  
     python3 --version  
     ```  

2. **pip**  
   - Install if not already available:  
     ```bash  
     sudo apt install python3-pip  
     ```  

### Required Python Modules  

Install the dependencies using pip:  

```bash  
pip install requests pillow  

    Note: tkinter is bundled with Python on most systems. If not, install it via your package manager (e.g., sudo apt install python3-tk on Ubuntu).

Clone the Repository

git clone https://github.com/Leslie1302/Fortune-Fetcher.git  
cd Fortune-Fetcher  

Usage
Running the Program

Launch the program with:

python3 main.py  

How to Use

    Start the Application
        Run the program, and the GUI will open.

    Fetch a Fortune
        Click the "Fetch Fortune" button to generate a random fortune overlaid on a beautiful image.

    View the Image
        The generated image with the quote will appear in the application window.

Project Structure

    main.py: The core program script containing the GUI logic, API calls, and image processing.
    README.md: Documentation for understanding and using the project.

Technologies Used

    Python: Main programming language.
    tkinter: For creating the graphical user interface.
    requests: For making API calls to fetch fortunes and images.
    Pillow (PIL): For image manipulation, including adding text and calculating contrast.

Troubleshooting

    Error: Module Not Found
        Ensure all required modules are installed:

    pip install requests pillow  

Image Not Displaying

    Verify internet connectivity.
    Check if the https://picsum.photos API is accessible.

Font Not Found

    Ensure you have Times New Roman or Liberation Serif fonts installed on your system.
    Install fonts if necessary:

        sudo apt install ttf-mscorefonts-installer  # For Times New Roman
        sudo apt install fonts-liberation          # For Liberation Serif

Contribution

Contributions are welcome! Follow these steps:

    Fork the repository.
    Create a new branch:

git checkout -b feature-name  

Commit your changes:

git commit -m "Add feature-name"  

Push to your branch:

    git push origin feature-name  

    Open a Pull Request on GitHub.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Author
Leslie Nii Adjetey
Leslie1302
