import image_hash as ih

def main():
    ih.create_hashed_image('dupa', image_size= 32, hashing_algorithm='sha256')

if __name__ == '__main__':
    main()