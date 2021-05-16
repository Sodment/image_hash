import hashlib
import os
import png

salt = os.urandom(16)

def create_hashed_image(password, image_name = 'encrypted_image.png',image_size = 64):
    password = str.encode(password)
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=image_size**2)

    with open(image_name, 'wb') as f:
        w = png.Writer(image_size, image_size, greyscale=True)
        w.write_array(f, dk)
        f.close()


def main():
    create_hashed_image('dupa', image_size=32)

if __name__ == "__main__":
    main()