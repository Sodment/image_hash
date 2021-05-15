import hashlib 

def main():
    m = hashlib.sha256()
    m.update(b"kurwa")
    m.digest()
    print(m.digest())



if __name__ == "__main__":
    main()