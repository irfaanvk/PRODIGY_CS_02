from PIL import Image


# Function to encrypt the image
def encrypt_image(image_path, key):
    # Open image
    img = Image.open(image_path)
    # Convert image to RGB mode (to handle color images)
    img = img.convert("RGB")
    # Get image data as a list of tuples (R, G, B)
    pixels = list(img.getdata())

    encrypted_pixels = []

    # Apply encryption by modifying pixel values
    for pixel in pixels:
        r, g, b = pixel
        # Simple encryption: XOR each color channel with a key
        encrypted_pixels.append((r ^ key, g ^ key, b ^ key))

    # Create new encrypted image
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)

    # Save encrypted image
    encrypted_img.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'.")


# Function to decrypt the image
def decrypt_image(encrypted_image_path, key):
    # Open encrypted image
    img = Image.open(encrypted_image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    decrypted_pixels = []

    # Reverse the encryption by applying the same XOR operation
    for pixel in pixels:
        r, g, b = pixel
        decrypted_pixels.append((r ^ key, g ^ key, b ^ key))

    # Create new decrypted image
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)

    # Save decrypted image
    decrypted_img.save('decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'.")


# Main program
if __name__ == "__main__":
    choice = input("Enter 'encrypt' to encrypt an image or 'decrypt' to decrypt an image: ").lower()

    if choice == 'encrypt':
        image_path = input("Enter the path to the image: ")
        key = int(input("Enter the encryption key (a number): "))
        encrypt_image(image_path, key)

    elif choice == 'decrypt':
        encrypted_image_path = input("Enter the path to the encrypted image: ")
        key = int(input("Enter the decryption key (same as encryption key): "))
        decrypt_image(encrypted_image_path, key)

    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
