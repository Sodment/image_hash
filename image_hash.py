from array import array
import hashlib
from typing import final
import png



def main():
    dk = hashlib.pbkdf2_hmac('sha256', b'dupa', b'salt', 100000, dklen=64**2)

    with open('encrypted_image.png', 'wb') as f:
        w = png.Writer(64, 64, greyscale=True)
        w.write_array(f, dk)

if __name__ == "__main__":
    main()