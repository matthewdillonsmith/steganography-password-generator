import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import random
import string

class StenoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stenography Password Generator")
        
        # Set the desired window size (e.g., 800x600)
        window_width = 800
        window_height = 600

        # Get the screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position to center the window
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # Set the geometry of the window (width x height + x_position + y_position)
        self.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        
        # Layout frames
        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Select Image Button
        self.select_image_button = tk.Button(self.left_frame, text="Select Image", command=self.select_image)
        self.select_image_button.pack(pady=10)

        # Generate Password/Key/Embedded Image Button
        self.generate_button = tk.Button(self.left_frame, text="Generate Password/Key/Embedded Image", command=self.generate_password_key_embed)
        self.generate_button.pack(pady=10)

        # Placeholder for generated password display
        self.password_label = tk.Label(self.left_frame, text="")
        self.password_label.pack(pady=10)
        self.copy_password_button = None

        # Extract Password Button
        self.extract_button = tk.Button(self.left_frame, text="Extract Password", command=self.extract_password)
        self.extract_button.pack(pady=10)

        # Placeholder for extracted password display
        self.decrypted_password_label = tk.Label(self.left_frame, text="")
        self.decrypted_password_label.pack(pady=10)
        self.copy_decrypted_password_button = None

        # Status Label
        self.status_label = tk.Label(self.left_frame, text="")
        self.status_label.pack(pady=10)

        # Image display area
        self.image_label = tk.Label(self.right_frame)
        self.image_label.pack()

        # Variables to store generated data
        self.image_path = None
        self.password = None
        self.key = None
        self.iv = None
        self.tag = None
        self.ciphertext = None
        self.encrypted_data = None
        self.output_image_path = None
        self.key_file_path = None

    def select_image(self):
        self.image_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if self.image_path:
            self.status_label.config(text=f"Selected Image: {os.path.basename(self.image_path)}")
            self.display_image(self.image_path)
        else:
            self.status_label.config(text="No image selected.")

    def display_image(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((300, 300))  # Resize the image to fit the display area
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk  # Keep a reference to avoid garbage collection

    def generate_password_key_embed(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first.")
            return

        # Generate Password
        self.password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(16))

        # Generate Key
        self.key = os.urandom(32)

        # Encrypt Password
        backend = default_backend()
        self.iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(self.iv), backend=backend)
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(self.password.encode()) + padder.finalize()

        self.ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        self.encrypted_data = self.iv + encryptor.tag + self.ciphertext

        # Embed Encrypted Data into Image
        try:
            self.output_image_path = self.embed_password_in_image(self.image_path, self.encrypted_data)
            self.save_key_file(self.output_image_path, self.key)
            self.status_label.config(text=f"Data embedded in: {os.path.basename(self.output_image_path)}")
            self.display_generated_password()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def embed_password_in_image(self, image_path, encrypted_password):
        image = Image.open(image_path)
        image = image.convert("RGB")

        length_prefix = len(encrypted_password).to_bytes(2, byteorder='big')
        data_to_embed = length_prefix + encrypted_password

        binary_password = ''.join(format(byte, '08b') for byte in data_to_embed)

        data_index = 0
        binary_password_len = len(binary_password)

        pixels = list(image.getdata())
        new_pixels = []

        for pixel in pixels:
            r, g, b = pixel[:3]

            if data_index < binary_password_len:
                r = (r & 0xFE) | int(binary_password[data_index])
                data_index += 1

            if data_index < binary_password_len:
                g = (g & 0xFE) | int(binary_password[data_index])
                data_index += 1

            if data_index < binary_password_len:
                b = (b & 0xFE) | int(binary_password[data_index])
                data_index += 1

            new_pixels.append((r, g, b))

        if data_index < binary_password_len:
            raise ValueError("The image is too small to embed the entire encrypted password.")

        image.putdata(new_pixels)

        output_image_path = filedialog.asksaveasfilename(
            title="Save Output Image",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if output_image_path:
            image.save(output_image_path)
            return output_image_path
        else:
            raise ValueError("No output file path provided.")

    def save_key_file(self, output_image_path, key):
        key_file_path = os.path.splitext(output_image_path)[0] + ".key"
        with open(key_file_path, 'wb') as key_file:
            key_file.write(key)
        self.key_file_path = key_file_path

    def display_generated_password(self):
        self.password_label.config(text=f"Generated Password: {self.password}")
        if not self.copy_password_button:
            self.copy_password_button = tk.Button(self.left_frame, text="Copy to Clipboard", command=self.copy_password_to_clipboard)
            self.copy_password_button.pack(pady=5)

    def copy_password_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")

    def extract_password(self):
        # Select the image with embedded data
        embedded_image_path = filedialog.askopenfilename(
            title="Select Image with Embedded Data",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )

        # Select the corresponding key file
        key_file_path = filedialog.askopenfilename(
            title="Select Key File",
            filetypes=[("Key files", "*.key"), ("All files", "*.*")]
        )

        if not embedded_image_path or not key_file_path:
            messagebox.showerror("Error", "Please select both the embedded image and the key file.")
            return

        # Load the key
        with open(key_file_path, 'rb') as key_file:
            key = key_file.read()

        try:
            # Extract encrypted data from the image
            extracted_encrypted_data = self.extract_encrypted_data(embedded_image_path)

            # Decrypt the password
            decrypted_password, iv, tag, ciphertext = self.decrypt_password(extracted_encrypted_data, key)

            self.display_decrypted_password(decrypted_password)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def extract_encrypted_data(self, image_path):
        image = Image.open(image_path)
        binary_password = ""

        pixels = list(image.getdata())

        for pixel in pixels:
            r, g, b = pixel[:3]
            binary_password += str(r & 1)
            binary_password += str(g & 1)
            binary_password += str(b & 1)

        length_prefix = int(binary_password[:16], 2)
        encrypted_password_bits = binary_password[16:16 + length_prefix * 8]

        byte_password = [encrypted_password_bits[i:i+8] for i in range(0, len(encrypted_password_bits), 8)]
        encrypted_password = bytes([int(b, 2) for b in byte_password if len(b) == 8])

        return encrypted_password

    def decrypt_password(self, encrypted_password, key):
        backend = default_backend()

        iv = encrypted_password[:16]
        tag = encrypted_password[16:32]
        ciphertext = encrypted_password[32:]

        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=backend)
        decryptor = cipher.decryptor()

        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        decrypted_password = unpadder.update(padded_data) + unpadder.finalize()

        return decrypted_password.decode('utf-8'), iv, tag, ciphertext

    def display_decrypted_password(self, decrypted_password):
        self.decrypted_password_label.config(text=f"Decrypted Password:\n{decrypted_password}")
        if not self.copy_decrypted_password_button:
            self.copy_decrypted_password_button = tk.Button(self.left_frame, text="Copy to Clipboard", command=lambda: self.copy_decrypted_password_to_clipboard(decrypted_password))
            self.copy_decrypted_password_button.pack(pady=5)

    def copy_decrypted_password_to_clipboard(self, decrypted_password):
        self.clipboard_clear()
        self.clipboard_append(decrypted_password)
        messagebox.showinfo("Copied", "Decrypted password copied to clipboard.")

if __name__ == "__main__":
    app = StenoApp()
    app.mainloop()
