from pystray import MenuItem as item
from PIL import Image, ImageTk
import pystray
import time


title="Tray title"
image=Image.open('OUTGOING.ICO')
icon = pystray.Icon("name", image, title, menu = None)
# if __name__ == '__main__':
icon.run()
icon.notify('dd',"My test notification sub title")

