import os
import markups as nav
from aiogram.utils import executor
from aiogram import types, Dispatcher, Bot
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from googleapiclient.http import MediaIoBaseUpload

bot_token = '5426309139:AAH5w4zsJFQumFrxeNSJWpXB26k_vmALA4k'

SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'for-me-379114-e0d0af25d67e.json')
scope = ['https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/spreadsheets.readonly',
         'https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
client = gspread.authorize(creds)
drive_service = build('drive', 'v3', credentials=creds)
bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
sheet_id = '1pPXWHasK9MGNTtTZ3NQz8mZTtBmJFdANNHW_XMLsBmU'
sheet_range = 'Topshiriqlar'
sheet_service = build('sheets', 'v4', credentials=creds)
sheet = sheet_service.spreadsheets()
sheet2 = gc.open_by_key('1pPXWHasK9MGNTtTZ3NQz8mZTtBmJFdANNHW_XMLsBmU').sheet1
folder_id = '1RgaMjUK7bKtLbzRbtkXRIO_gLFT3Y9bj'
result = sheet.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
values = result.get('values', [])

@dp.callback_query_handler(text="Ortga qaytish")
async def cancel(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Fakultetingizni tanlang!", reply_markup=nav.mainMenu)

async def yuklash(message: types.Message):
    file_id = message.document.file_id
    file_info = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    task_name = message.document.file_name
    file_metadata = {'name': f'{task_name}', 'parents': [folder_id]}
    media = await bot.send_message(message.chat.id, "Fayl yuklanmoqda...")
    try:
        file = drive_service.files().create(body=file_metadata, media_body=MediaIoBaseUpload(downloaded_file, mimetype=message.document.mime_type), fields='id').execute()
        await bot.edit_message_text("Fayl muvaffaqiyatli yuklandi!", chat_id=media.chat.id,  message_id=media.message_id)
    except HttpError as error:
        await bot.edit_message_text("Yuklashda moamu yuz berdi qayta urunib ko'ring!" % error, chat_id=media.chat.id,  message_id=media.message_id)

row_number = 2
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu Alaykum FDU Botiga hush kelibsiz! \nFakultetingizni tanlang!", reply_markup=nav.mainMenu)

@dp.callback_query_handler(text=('Fizika kafedrasi','Texnologik ta’lim kafedrasi','Matematika kafedrasi',
                                 'Matematik analiz va differensial tenglamalar kafedrasi',
                                 'Amaliy matematika va informatika kafedrasi','Axborot texnologiyalari kafedrasi',
                                 'Kimyo kafedrasi','Geografiya kafedrasi','Ekologiya kafedrasi',
                                 'Zoologiya va umumiy biologiya kafedrasi','Botanika va biotexnologiya kafedrasi',
                                 'Tuproq-shunoslik kafedrasi','Zoinjeneriya va doirivor o‘simliklar kafedasi','Mevachilik va sabzavotchilik kafedrasi',
                                 'Aholi tomorqalaridan samarali foydalanish kafedrasi',
                                 'Ingliz tili kafedrasi','Nemis va fransuz tillari kafedrasi',
                                 'Gumanitar yo‘nalishlar bo‘yicha chet tillari kafedrasi','Tabiiy yo‘nalishlar bo‘yicha chet tillari kafedrasi',
                                 'Amaliy ingliz tili kafedrasi','Ingliz tili o‘qitish metodikasi kafedrasi',
                                 'Tilshunoslik kafedrasi','Adabiyotshunoslik kafedrasi','O‘zbek tili va adabiyoti kafedrasi',
                                 'Rus filologiyasi kafedrasi','Rus tili metodikasi kafedrasi','Jahon tarixi kafedrasi',
                                 'O‘zbekiston tarixi kafedrasi','Falsafa kafedrasi','Pedagogika kafedrasi',
                                 'Psixologiya  kafedrasi','Tasviriy san’at  kafedrasi','Musiqiy ta’lim va madaniyat',
                                 'Vokal va cholg‘u ijrochiligi','Boshlang‘ich ta’lim uslubiyoti kafedrasi',
                                 'Maktabgacha ta’lim kafedrasi','Jismoniy madaniyat kafedrasi','Jismoniy madaniyat nazariyasi va uslubiyoti kafedrasi',
                                 'Sport o‘yinlari kafedrasi','Jahon va mintaqa iqtisodiyoti kafedrasi','Iqtisodiyot va servis kafedrasi',
                                 'Moliya kafedrasi','Buxgalteriya hisobi va iqtisodiy tahlil kafedrasi',
                                 'Harbiy ta’lim kafedrasi','Aniq va tabiiy fanlar kafedrasi','Ijtimoy gumanitar fanlar kafedrasi'))
async def main(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    result = sheet.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
    values = result.get('values', [])
    if not values:
        await bot.send_message(chat_id=message.from_user.id, text='Topshiriq turi topilmadi!')
    else:
        markup = InlineKeyboardMarkup(row_width=1)
        for row in values:
            item = InlineKeyboardButton(text=row[0], callback_data=f"{row[0]}")
            markup.add(item)
        await bot.send_message(message.from_user.id, text='Topshiriq turini tanlang!', reply_markup=markup)
    message_text = message.data
    user_name = message.from_user.username
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!C{row}"
        range_name2 = f"Natijalar!G{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            body2 = {"values": [[user_name]]}
            try:
                asd = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name2,
                    valueInputOption="RAW",
                    body=body2
                ).execute()
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Fizika-texnika fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra1)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break

@dp.callback_query_handler(text='Matematika informatika fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra2)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break

@dp.callback_query_handler(text='Tabiiy fanlar fakuleti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra3)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break

@dp.callback_query_handler(text='Agrar qoʻshma fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra4)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Chet tillari fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra5)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Ingliz tili va adabiyoti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra6)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Filologiya fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra7)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Tarix fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra8)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Pedagogika psixologiya fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra9)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='San’atshunoslik fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra10)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Maktabgacha va boshlang‘ich ta’lim fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra11)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Jismoniy madaniyat fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra12)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Iqtisodiyot fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra13)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Harbiy ta’lim fakulteti')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra14)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break
@dp.callback_query_handler(text='Sirtqi bo‘limi')
async def handle_diplom_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Kaferangizni tanlang!", reply_markup=nav.Kafedra15)
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!B{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break

@dp.callback_query_handler()
async def handle_send_message(message: types.Message):
    global row_number
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Fayilni yuklang!")
    dp.register_message_handler(yuklash, content_types=['document'])
    message_text = message.data
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scope)
    service = build('sheets', 'v4', credentials=creds)
    for row in range(row_number, 1000000):
        range_name = f"Natijalar!D{row}"
        try:
            existing_value = service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=range_name
            ).execute().get("values", [])
        except HttpError as error:
            continue

        if not existing_value:
            body = {"values": [[message_text]]}
            try:
                result = service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                ).execute()
                row_number = row
                break
            except HttpError as error:
                break

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
