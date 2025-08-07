import os
import sys
import re
import pyperclip
from PIL import Image, ImageGrab
from pix2tex.cli import LatexOCR

def format_equation(latex):
    """Makes the LaTeX output compatible with Markdown standards, the .strip() command removes unnecessary whitespace"""
    return f"$$ {latex.strip()} $$"

def main():
    try:
        # Takes the image from the clipboard
        image = ImageGrab.grabclipboard()
        if not image:
            print("ERROR: No image found in clipboard!")
            input("Press Enter to exit...")
            return
            
        # Converts the image to RGB format to ensure the AI model works
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Initializes and uses the model
        model = LatexOCR()
        raw_latex = model(image)
        
        # Formats the output using the function on top
        stripped_latex = format_equation(raw_latex)
        
        # Outputs the result
        print("\n" + "="*50)
        print("OUTPUT:")
        print(stripped_latex)
        print("="*50 + "\n")
        
        # Copies to clipboard
        pyperclip.copy(stripped_latex)
        print("LaTeX copied to clipboard")
        
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERROR: {str(e)}")
        print("!"*50 + "\n")
        import traceback
        traceback.print_exc()
        
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()