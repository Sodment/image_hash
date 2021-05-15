from array import array
import hashlib 
import png



def main():
    dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000, dklen=256)
    #print(type(dk))
    dk = bytearray(dk)
    # dk = int.from_bytes(dk, byteorder='big', signed=True)
    with open('encrypted_image.png', 'wb') as f:
        w = png.Writer(1, 1, greyscale=False)
        w.write_packed(f, dk)
    print("Done")


if __name__ == "__main__":
    main()