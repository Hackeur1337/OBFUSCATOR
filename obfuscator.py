import sys, os, string, random, zlib, base64, codecs, marshal

def obfuscate(file_path):
    def xor_transform(data, key):
        return bytes([b ^ key for b in data])

    def reverse_transform(data):
        return data[::-1]

    def compress_transform(data):
        return zlib.compress(data)

    def b64_transform(data):
        return base64.b64encode(data)

    def rot13_transform(data):
        return codecs.encode(data, 'rot13')

    def marshal_transform(data):
        return marshal.dumps(data)

    def random_string(length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    with open(file_path, 'r') as f:
        content = f.read()
        obfuscated_content = xor_transform(content.encode('utf-8'), random.randint(0, 255))
        obfuscated_content = reverse_transform(obfuscated_content)
        obfuscated_content = compress_transform(obfuscated_content)
        obfuscated_content = b64_transform(obfuscated_content)
        obfuscated_content = rot13_transform(obfuscated_content)
        obfuscated_content = marshal_transform(obfuscated_content)

    file_name, file_extension = os.path.splitext(file_path)
    obfuscated_file_path = file_name + '_obfusq_by_zakura1337' + file_extension
    with open(obfuscated_file_path, 'wb') as f:
        f.write(random_string(128).encode('utf-8'))
        f.write(obfuscated_content)
        f.write(random_string(128).encode('utf-8'))

    os.chmod(obfuscated_file_path, 0o777)

    print('Fichier obfusqué.')

file_path = input('Entrez le chemin du fichier python à obfusquer : ')

try:
    obfuscate(file_path)
except:
    print('ERROR lors de l\'obfuscation du fichier.')
    sys.exit(1)
