import webbrowser, sys
import pyperclip

# webbrowser.open("https://google.com")

# Check if cmd argument were passed
if len(sys.argv) > 1:
    address = "".join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
webbrowser.open(f"https://google.com/maps/place/{address}")