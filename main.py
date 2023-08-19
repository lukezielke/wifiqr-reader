from qreader import QReader
import cv2
import argparse
from pathlib import Path


qreader = QReader()

parser = argparse.ArgumentParser()

parser.add_argument("path")

args = parser.parse_args()

qr_path = Path(args.path)

if not qr_path.exists():
    print("Invalid path.")
    raise SystemExit(1)


elif not args.path.endswith(".png") or args.path.endswith(".jpg"):
    print("Invalid file format. Only .png and .jpg work.")
    raise SystemExit(1)

else:
    image = cv2.cvtColor(cv2.imread(args.path), cv2.COLOR_BGR2RGB)
    data = qreader.decode(image)
    if data == None:
        print("No QR code could be read.")
        raise SystemExit(1)
    else:
        wifi_name = data.split("WIFI:S:",1)[1].split(";T:",1)[0]
        wifi_pass = data.split(";P:",1)[1].split(";H:",1)[0]
        encryption = data.split(";T:",1)[1].split(";P:",1)[0]
        print("----------------------")
        print(f"Wifi: {wifi_name}")
        print(f"Password: {wifi_pass}")
        print(f"Encryption Type: {encryption}")
        print("----------------------")
