import tkinter as tk
from tkinter import messagebox, simpledialog
import base64
def encrypt():
    message = text_area.get("1.0", "end-1c")
    key = simpledialog.askstring("Encryption Key", "Enter the encryption key:")
    if key is None:
        return
    encrypted_message = base64.b64encode(message.encode() + key.encode())
    text_area.delete("1.0", "end")
    text_area.insert("1.0", encrypted_message.decode())
def decrypt():
    encrypted_message = text_area.get("1.0", "end-1c")
    key = simpledialog.askstring("Decryption Key", "Enter the decryption key:")
    if key is None:
        return
    try:
        decrypted_message = base64.b64decode(encrypted_message).decode()
        if decrypted_message.endswith(key):
            decrypted_message = decrypted_message[:-len(key)]
        text_area.delete("1.0", "end")
        text_area.insert("1.0", decrypted_message)
    except (UnicodeDecodeError, base64.binascii.Error):
        messagebox.showerror("Error", "Invalid encrypted message or decryption key.")
root = tk.Tk()
root.title("Encryption/Decryption Tool")
text_area = tk.Text(root, height=10, width=50)
text_area.pack(pady=10)
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack(pady=5)
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=5)
root.mainloop()