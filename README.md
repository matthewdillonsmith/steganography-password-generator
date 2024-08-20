
# Stenography Password Generator

## Overview
Welcome to the Steganography Password Generator! This Python application allows users to generate highly secure passwords by embedding them into images using steganography techniques. Users can use any image of their choice to create embedded image/key pairs, enhancing the security and uniqueness of their passwords. The application uses AES-256 encryption to ensure the highest level of security for the embedded passwords.

## How the App Works
1. **Select Image**: Users start by selecting an image (only tested with PNG format at this time...) where the password will be embedded.
2. **Generate Password/Key/Embedded Image**: The app generates a random password, encrypts it using AES encryption, and embeds the encrypted data into the selected image. The user is prompted to save the output image and the corresponding key file.
3. **Extract Password**: Users can select an image with embedded data and the corresponding key file to extract and decrypt the embedded password.

## Features
- **Password Generation**: Generates a 16-character password consisting of letters, digits, and punctuation.
- **AES Encryption**: The password is encrypted using AES-256 encryption with GCM mode for security.
- **Data Embedding**: The encrypted password is embedded into the image using the least significant bit (LSB) technique.
- **Password Extraction**: Allows users to extract and decrypt the password from an image using the corresponding key file.

## Constraints & Limitations
1. **Image Size**: Ensure that the image selected for embedding the password is large enough to store the encrypted data. If the image is too small, the process will fail.
2. **File Format**: Only PNG images are supported for embedding and extracting the password.
3. **Key File**: The key file generated during the embedding process is essential for password extraction. Losing this file will make it impossible to decrypt the password.
4. **Data Integrity**: Any modification to the image with embedded data or the key file after the embedding process may result in unsuccessful password extraction or decryption.
5. **Security**: While AES encryption is strong, users should still manage their key files securely to prevent unauthorized access.

## Requirements
- Python 3.x
- Tkinter (included with standard Python installations)
- PIL (Pillow) library
- cryptography library

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/matthewdillonsmith/steganography-password-generator.git
   cd steganography-password-generator
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python steno-password.py
   ```

## Usage
1. Open the application.
2. Select an image using the **Select Image** button. <b>NOTE:</b> <i>At this time, this app has only been tested with `.png` images.</i></b>
3. Click **Generate Password/Key/Embedded Image** to generate and embed a password.
4. Save the output image and the key file with the filename of your choosing. <b>NOTE:</b> <i>This will dump the matching `.key` and embedded `.png` files into your current directory.</i>
5. To extract the password, click **Extract Password**, and provide the matching embedded image and key files. <i>This will work even if you close out of the app and want to do this at a later time.</i>

## License
Not sure how the licensing stuff works yet, but I will add this later.

## Contributing
Please feel free to tear this apart; any critisim is welcome! Follow these steps to contribute:

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/<some-new-feature>
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add <some-new-feature>'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/<some-new-feature>
   ```
5. **Open a Pull Request**

## Contact
For any inquiries or issues, please reach out via [GitHub Issues](https://github.com/matthewdillonsmith/stenography-password-generator/issues).

