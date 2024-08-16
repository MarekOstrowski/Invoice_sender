import json
def payload(order_number, pdfBase64):
    data = '''{ "params": { "documents": [
            {
                "orderSerialNumber": %(order_number)s,
                "name": "%(order_number)s.pdf",
                "pdfBase64": "%(pdfBase64)s",
                "type": "vat_invoice",
                "returnedInOrderDetails": "y",
                "additionalData": {
                    "documentId": "%(order_number)s",
                    "documentIssuedDate": "2024-08-08"
                }
            }
        ] } }''' % {"order_number": order_number, "pdfBase64": pdfBase64, "documentId": order_number}

    return json.loads(data)


