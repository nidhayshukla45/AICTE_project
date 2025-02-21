import cv2

# Load encrypted image
img = cv2.imread("encryptedImage.png")  # Use PNG for lossless data

password = input("Enter the passcode to decrypt: ")

d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

height, width, _ = img.shape
m, n, z = 0, 0, 0
decrypted_msg = ""

while True:
    char_code = int(img[n, m, z])

    if char_code == 0:  # Stop when null character is encountered
        break

    decrypted_msg += c[char_code]

    z += 1
    if z == 3:  # Move to next pixel after all 3 channels are read
        z = 0
        m += 1
        if m == width:  # Move to next row
            m = 0
            n += 1
            if n == height:
                break  # Stop if image runs out of space

print("Decrypted Message:", decrypted_msg)