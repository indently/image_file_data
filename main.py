import shutil


def create_file(original, output, message: str):
    shutil.copyfile(original, output)

    # Append bytes
    with open(output, 'ab') as jpg:
        byte_message = message.encode()
        jpg.write(byte_message)


def read_file(file):
    # Open file and append bytes (without overwriting)
    with open(file, 'rb') as jpg:
        content = jpg.read()
        offset = content.index(b'\xff\xd9')  # Bytes: print(bytes.frcartomhex('FFD9'))
        message = content[offset + 2:].decode()
        print(message)


def read_file_bytes(file):
    with open(file, "rb") as image:
        f = image.read()
        print(f)


if __name__ == '__main__':
    # read_file_bytes('cat.jpg')
    create_file(original='cat.jpg', output='output.jpg', message='This is a secret message!')
    read_file('output.jpg')
