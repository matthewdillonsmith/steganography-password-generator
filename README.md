
# Steganography Password Generator

Welcome to the **Steganography Password Generator**! This Python application allows users to generate highly secure passwords by embedding them into images using steganography techniques. Users can use any image of their choice to create password/key pairs, enhancing the security and uniqueness of their passwords.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- **Generate Secure Passwords**: Creates strong, random passwords combining letters, numbers, and special characters.
- **Embed Passwords into Images**: Uses steganography to embed encrypted passwords into user-selected images.
- **Extract Passwords from Images**: Retrieves and decrypts passwords embedded within images.
- **Key Management**: Allows users to create new encryption keys and load existing ones for password encryption and decryption.
- **User-Friendly Interface**: Provides an intuitive GUI using Tkinter for easy interaction.
- **Copy to Clipboard**: Enables quick copying of generated or extracted passwords to the clipboard.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.6 or higher
- **Dependencies**:
  - [tkinter](https://docs.python.org/3/library/tkinter.html)
  - [Pillow](https://pypi.org/project/Pillow/)
  - [cryptography](https://pypi.org/project/cryptography/)
  - [pyperclip](https://pypi.org/project/pyperclip/)

## Installation

Follow these steps to get a copy of the project up and running on your local machine.

1. **Clone the Repository**
   ```bash
   git clone https://github.com/matthewdillonsmith/steganography-password-generator.git
   cd steganography-password-generator
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   **Alternatively**, you can install the dependencies individually:
   ```bash
   pip install Pillow cryptography pyperclip
   ```

4. **Run the Application**
   ```bash
   python steganography_app.py
   ```

## Usage

1. **Load/Create Encryption Key**
   - Click on **"Load Encryption Key"** to load an existing `.key` file.
   - Click on **"Save New Encryption Key"** to generate and save a new encryption key.

2. **Select Image**
   - Click on **"Select Image"** and choose a `.png` image file to embed or extract the password.

3. **Generate and Embed Password**
   - Click on **"Generate and Embed Password"** to create a new password, encrypt it, and embed it into the selected image.
   - Save the output image when prompted.

4. **Extract Password**
   - Click on **"Extract Password"** to retrieve and decrypt the password from the selected image.

5. **Copy to Clipboard**
   - After generating or extracting a password, click on **"Copy to Clipboard"** to copy the password for easy use.

## Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)

### Password Generated and Embedded
![Password Embedded](screenshots/password_embedded.png)

### Password Extracted
![Password Extracted](screenshots/password_extracted.png)

*Note: Ensure you have a `screenshots` folder in your project directory with the above images.*

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Python Software Foundation](https://www.python.org/)
- [Pillow Library](https://python-pillow.org/)
- [Cryptography Library](https://cryptography.io/)
- [Pyperclip Library](https://github.com/asweigart/pyperclip)
- [Tkinter GUI Library](https://docs.python.org/3/library/tkinter.html)

# Contact

**Matthew Dillon Smith**
- [GitHub](https://github.com/matthewdillonsmith)
- [Email](mailto:youremail@example.com)

Feel free to reach out for any questions or suggestions!

# Additional Notes

- Ensure that you handle your encryption keys securely. Do not share them publicly or commit them to version control.
- This application currently supports `.png` images for embedding and extracting passwords. Support for other image formats can be added in future updates.
- Always use high-resolution images for better steganography results.

---

Thank you for using the Steganography Password Generator! If you find this project helpful, please give it a star ⭐ on GitHub.
