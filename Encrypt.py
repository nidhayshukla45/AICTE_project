import cv2
import os

# Read image
img = cv2.imread("mypic.jpg")  # Use a lossless PNG for better results

msg = input("Enter secret message: ") + chr(0)  # Append a null terminator
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

height, width, _ = img.shape
m, n, z = 0, 0, 0

for char in msg:
    img[n, m, z] = d[char]
    
    z += 1
    if z == 3:  # Move to next pixel after modifying all 3 channels
        z = 0
        m += 1
        if m == width:  # Move to next row
            m = 0
            n += 1
            if n == height:
                break  # Stop if image runs out of space

cv2.imwrite("encryptedImage.png", img)  # Save as PNG to prevent compression
os.system("start encryptedImage.png")  # Open image (Windows only)
