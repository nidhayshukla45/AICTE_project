SECURE DATA HIDING IN IMAGES USING STGANOGRAPHY :-

This project demonstrates how to hide and extract secret messages in images using Python and OpenCV. The message is embedded into the pixel values of an image in a way that is invisible to the human eye.

Features :

✅ Hide secret text inside an image without noticeable changes.
✅ Extract the hidden message using a decryption script.
✅ Uses PNG format for lossless storage.
✅ Simple and efficient pixel-based encoding.

Technologies Used :

* Python

* OpenCV (for image processing)

How It Works :

Encryption (Hiding the Message):-

1. Load an image (mypic.jpg).


2. Convert the message into ASCII values and embed them into the RGB pixel values.


3. Save the modified image as encryptedImage.png.



Decryption (Extracting the Message):-

1. Load encryptedImage.png.


2. Extract pixel values and convert them back to text.


3. Display the hidden message.



Installation :


1. Install dependencies:

pip install opencv-python 


2. Run the encryption script:

python encrypt.py


3. Run the decryption script:

python decrypt.py



Usage :

Encryption Script (encrypt.py)

Run the script and enter the secret message.

The modified image (encryptedImage.png) will be created.


Decryption Script (decrypt.py)

Run the script and enter the passcode.

The hidden message will be revealed.


Demo :
![image alt](https://github.com/nidhayshukla45/AICTE_project/blob/0703e7c9cf72a4ba8a1295ee039047e73b55b5a5/Screenshot%20of%20Encrypt%20Code%20with%20Output.png)

![image alt](https://github.com/nidhayshukla45/AICTE_project/blob/57cd89174711bdeba11f9e43d0b880d3f818efe3/Screenshot%20of%20encryptedImage%20created.png)

![image alt](https://github.com/nidhayshukla45/AICTE_project/blob/ff7517ce5eabc46e0d591cf30a0423ffd635bc1d/Screenshot%20of%20Decrypt%20Code%20with%20Output.png)

Future Scope :

🔹 Support for multiple image formats (JPG, BMP, etc.).
🔹 Encrypt the message before embedding it for added security.
🔹 Use AI techniques to resist steganalysis detection.

Contributing :

Pull requests are welcome! Feel free to improve the algorithm or suggest new features.

License :

This project is licensed under the MIT License.

GitHub Repository :

🔗 GitHub Link

https://github.com/nidhayshukla45/AICTE_project.git
---

Let me know if you want any modifications!
