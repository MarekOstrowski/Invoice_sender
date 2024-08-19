import base64
import requests
from config import API_KEY
from request_body import payload
import fitz
import os


url = "https://butomaniak.pl/api/admin/v3/orders/documents"
headers = {"accept": "application/json",
           "content-type": "application/json",
           "X-API-KEY": API_KEY}


orders_list = list(map(lambda x: x.replace(".pdf", ""), os.listdir("./Invoices")))

for order_number in orders_list:

    with open(f"invoices/{order_number}.pdf", "rb") as pdf_file:
        pdf = fitz.open(pdf_file)
        if len(pdf) > 1:
            pdf.delete_page(1)
            pdf.save("output.pdf")
            output_pdf = open("output.pdf", "rb")
            encoded_string = base64.b64encode(output_pdf.read())
            encoded_string = encoded_string.decode("ascii")
            output_pdf.close()
        else:
            print(f"{order_number} is not valid {len(pdf)} page detected")
            continue

    request_data = payload(order_number=order_number, pdfBase64=encoded_string)
    response = requests.post(url, json=request_data, headers=headers)

    print(f'URL: {response.request.url}')
    # print(f'BODY: {response.request.body}')
    print(f'HEADERS: {response.request.headers}')
    print(f'RESPONSE: {response.text}')
    print(f'STATUS CODE: {response.status_code}')
