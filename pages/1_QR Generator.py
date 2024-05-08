import qrcode
import qrcode.constants
import streamlit as st

filename = "qr_code/qr_code.png"

def generateQR(url, filename):
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

st.set_page_config(page_title="QR Generator", page_icon="", layout="centered")
st.title("QR Generator")
url = st.text_input("Enter text or URL")

if st.button("Generate QR"):
    generateQR(url, filename)
    st.image(filename, use_column_width=True)
    with open(filename, "rb") as f:
        image_data = f.read()
    download = st.download_button(label="Download QR", data=image_data,file_name="QR_Generated.png" )