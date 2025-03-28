from google_drive_ocr import GoogleOCRApplication

app = GoogleOCRApplication('client_secret.json')

app.perform_ocr('Screenshot_2.png')