# Image Stenography wihout key

# No encryption is used in this example

# The synthax is as shown below
from stegano import lsb
secret = lsb.hide(path_to_img, secret_msg)
secret.save(ecrypted_img_name)

# The following code is used for decryption
from stegano import lsb
lsb.reveal(path_to_an_image)
