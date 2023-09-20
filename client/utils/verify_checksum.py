import hashlib
from utils.constants import FILE_NAME



def verify_checksum(server_checksum):
    md5_hash = hashlib.md5()
    with open(f"{FILE_NAME}", "rb") as file:
        # Read the file in chunks to handle large files
        while chunk := file.read(8192):
            md5_hash.update(chunk)
        print(f"server checksum: {server_checksum}")
        print(f"client checksum: {md5_hash.hexdigest()}")
    return server_checksum == md5_hash.hexdigest()

