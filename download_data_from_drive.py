import gdown
import os
import zipfile

# Create local data/ folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Your ZIP file's Google Drive ID
file_id = "1XYxfgKdmDp-l9TDobaaeMP0D4oWPdtVa"
url = f"https://drive.google.com/uc?id={file_id}"
output_path = "data/wildfire_dataset.zip"

# Download the ZIP file with a progress bar
print("Downloading ZIP from Google Drive...")
gdown.download(url, output_path, quiet=False)

# Unzip contents into data/
print("Extracting ZIP contents...")
with zipfile.ZipFile(output_path, 'r') as zip_ref:
    zip_ref.extractall("data/")

print("Done! Files are available in /data")
