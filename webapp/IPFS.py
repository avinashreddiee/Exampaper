import ipfshttpclient
import os
from io import BytesIO

# Connect to IPFS node
client = ipfshttpclient.connect()

def store(pdf_path):
    """Uploads a PDF file to IPFS and returns the CID."""
    try:
        result = client.add(pdf_path)  # Upload PDF file
        pdf_cid = result['Hash']
        print(f"PDF CID: {pdf_cid}")
        return pdf_cid
    except Exception as e:
        print(f"Error uploading PDF: {e}")
        return None

def ipfsget(pdf_cid, save_directory="D://Django//ExamPaper//downloads"):
    """Downloads a PDF file from IPFS and saves it locally."""
    try:
        # Fetch raw PDF data from IPFS
        pdf_data = client.cat(pdf_cid)

        # Ensure the directory exists
        os.makedirs(save_directory, exist_ok=True)

        # Define the file path
        file_path = os.path.join(save_directory, f"{pdf_cid}.pdf")

        # Save the PDF file
        with open(file_path, "wb") as pdf_file:
            pdf_file.write(pdf_data)

        print(f"PDF saved at: {file_path}")
    except Exception as e:
        print(f"Error downloading PDF: {e}")

if __name__ == '__main__':
    # Example: Store a PDF
    pdf_cid = store("sample.pdf")  # Change "sample.pdf" to your file path

    # Example: Retrieve the PDF using its CID
    if pdf_cid:
        get(pdf_cid)
