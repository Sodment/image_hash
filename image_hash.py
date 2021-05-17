import hashlib
import png
from os import urandom


def create_hashed_image(password, image_name = 'encrypted_image.png',image_size = 64, salt_size=16,hashing_algorithm = 'shaa256'):

    password = str.encode(password)
    salt = urandom(16)
    dk = hashlib.pbkdf2_hmac(hashing_algorithm, password, salt, 100000, dklen=image_size**2)

    with open(image_name, 'wb') as f:
        w = png.Writer(image_size, image_size, greyscale=True)
        w.write_array(f, dk)
    