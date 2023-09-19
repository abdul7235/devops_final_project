import requests
import os
from utils.verify_checksum import verify_checksum
from dotenv import load_dotenv
from utils.constants import FILE_NAME

load_dotenv()
URL = os.getenv('URL')

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    file_content = data.get("file")
    # Save the file
    with open(FILE_NAME, "w") as file:
        file.write(file_content)

    print(f"File '{FILE_NAME}' received successfully.")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")

if verify_checksum(data.get("checksum")):
    print("Checksum Matched")
else:
    print("Checksum not Matched")