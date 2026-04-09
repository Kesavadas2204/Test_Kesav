import pyautogui
import time
import webbrowser

# Step 1: Open Gmail
webbrowser.open("https://mail.google.com")
time.sleep(10)  # wait for Gmail to load properly

# Step 2: Click "Compose"
pyautogui.click(x=106, y=279)  
time.sleep(3)

# Step 3: Enter recipient email
pyautogui.write("meenajayaraman5@gmail.com")
time.sleep(1)

# ✅ IMPORTANT FIX: Confirm recipient
pyautogui.press("enter")
time.sleep(1)

# Step 4: Move to Subject field
pyautogui.press("tab")
time.sleep(1)

# Step 5: Enter subject
pyautogui.write("Test Email from PyAutoGUI")
time.sleep(1)

# Step 6: Move to Body
pyautogui.press("tab")
time.sleep(1)

# Step 7: Enter email body
pyautogui.write("Hello, this is an automated email sent using PyAutoGUI.")
time.sleep(1)

# Step 8: Send email
pyautogui.hotkey("ctrl", "enter")
print("Email sent successfully!")
