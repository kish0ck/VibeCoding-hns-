from PIL import ImageGrab
import time
time.sleep(2)
screenshot = ImageGrab.grab()
screenshot.save(r'C:\kshong\dashboard_app.png')
print("Screenshot saved to C:\\kshong\\dashboard_app.png")
