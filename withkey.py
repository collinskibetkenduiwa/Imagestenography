# An encryption key is used in this example
# Encryption is done using the code below

from steganocryptopy.steganography import Steganography
Steganography.generate_key(path_to_key)
encrypted = Steganography.encrypt(path_to_key, path_to_img, path_to_secretfile)
encrypted.save(encrypted_imgname)


# Decryption is don using the code below
from steganocryptopy.steganography import Steganography
Steganography.decrypt(path_to_key, path_to_image)
