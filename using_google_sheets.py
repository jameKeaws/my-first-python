import gspread
import json

from google.oauth2 import service_account

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

service_account_info = json.load(open('client_secret.json'))

credentials = service_account.Credentials.from_service_account_file(
    'client_secret.json',
    scopes=scope,
    subject='python-service-account@learning-python-scripting.iam.gserviceaccount.com')

client = gspread.authorize(credentials)

sheet = client.open('ServiceAccountTest').sheet1

# sheet.update_cell(1,1,"test")
# sheet.update_cell(2,1,"herewego")

print(sheet.row_values(1))