"""import numpy as np
from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Apply a basic mathematical operation (XOR) to each pixel with the key
    encrypted_array = img_array ^ key
    
    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))

    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")


def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert the encrypted image to a NumPy array
    encrypted_array = np.array(encrypted_img)

    # Apply the inverse operation (XOR) to each pixel with the key
    decrypted_array = encrypted_array ^ key
    
    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))

    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")


def main():
    print("Image Encryption and Decryption using Pixel Manipulation")

    # Enter the path to the image file
    image_path = r"C:\Users\Admin\Desktop\Python\Internship\1bf2430c28b31d6a82821619d8e49187.jpg"

    # Generate a random key (you can use any integer as the key)
    key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)

    # Encrypt the image
    encrypt_image(image_path, key)

    # Decrypt the image
    decrypt_image("encrypted_image.png", key)


if __name__ == "__main__":
    main()"""


from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    img_array = np.array(img)
    encrypted_array = np.bitwise_xor(img_array, key)
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_image_path)
    print("Image encrypted successfully.")
    return encrypted_array  

def decrypt_image(encrypted_array, output_image_path, key):
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_image_path)
    print("Image decrypted successfully.")

if __name__ == "__main__":
    input_image_path = r"C:\Users\Admin\Desktop\Python\Internship\1bf2430c28b31d6a82821619d8e49187.jpg"
    img = Image.open(input_image_path)
    width, height = img.size
    key = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)  # 3 for RGB channels
    encrypted_image_path = 'encrypted_image.jpg'    
    encrypted_array = encrypt_image(input_image_path, encrypted_image_path, key)
    decrypted_image_path = 'decrypted_image.jpg'
    decrypt_image(encrypted_array, decrypted_image_path, key)
