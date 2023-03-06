from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Menyu = InlineKeyboardButton(text="Ortga qaytish", callback_data="Ortga qaytish")
#Fakultet
item1 = InlineKeyboardButton(text='Fizika-texnika fakulteti', callback_data="Fizika-texnika fakulteti")
item2 = InlineKeyboardButton(text='Matematika informatika fakulteti', callback_data="Matematika informatika fakulteti")
item3 = InlineKeyboardButton(text='Tabiiy fanlar fakuleti', callback_data="Tabiiy fanlar fakuleti")
item4 = InlineKeyboardButton(text='Agrar qoʻshma fakulteti', callback_data="Agrar qoʻshma fakulteti")
item5 = InlineKeyboardButton(text='Chet tillari fakulteti', callback_data="Chet tillari fakulteti")
item6 = InlineKeyboardButton(text='Ingliz tili va adabiyoti',callback_data="Ingliz tili va adabiyoti")
item7 = InlineKeyboardButton(text='Filologiya fakulteti',callback_data="Filologiya fakulteti")
item8 = InlineKeyboardButton(text='Tarix fakulteti',callback_data="Tarix fakulteti")
item9 = InlineKeyboardButton(text='Pedagogika psixologiya fakulteti',callback_data="Pedagogika psixologiya fakulteti")
item10 = InlineKeyboardButton(text='San’atshunoslik fakulteti',callback_data="San’atshunoslik fakulteti")
item11 = InlineKeyboardButton(text='Maktabgacha va boshlang‘ich ta’lim fakulteti',callback_data="Maktabgacha va boshlang‘ich ta’lim fakulteti")
item12 = InlineKeyboardButton(text='Jismoniy madaniyat fakulteti',callback_data="Jismoniy madaniyat fakulteti")
item13 = InlineKeyboardButton(text='Iqtisodiyot fakulteti',callback_data="Iqtisodiyot fakulteti")
item14 = InlineKeyboardButton(text='Harbiy ta’lim fakulteti',callback_data="Harbiy ta’lim fakulteti")
item15 = InlineKeyboardButton(text='Sirtqi bo‘limi',callback_data="Sirtqi bo‘limi")
mainMenu = InlineKeyboardMarkup(row_width=1).add(item1, item2, item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15)


#Kafedra Fizika-texnika fakulteti
item16 = InlineKeyboardButton(text='Fizika kafedrasi', callback_data='Fizika kafedrasi')
item17 = InlineKeyboardButton(text='Texnologik ta’lim kafedrasi', callback_data='Texnologik ta’lim kafedrasi')
Kafedra1 = InlineKeyboardMarkup(row_width=1).add(item16, item17,Menyu)

#Kafedra Matematika informatika fakulteti
item18 = InlineKeyboardButton(text='Matematika kafedrasi', callback_data='Matematika kafedrasi')
item19 = InlineKeyboardButton(text='Matematik analiz va differensial tenglamalar kafedrasi', callback_data='Matematik analiz va differensial tenglamalar kafedrasi')
item20 = InlineKeyboardButton(text='Amaliy matematika va informatika kafedrasi', callback_data='Amaliy matematika va informatika kafedrasi')
item21 = InlineKeyboardButton(text='Axborot texnologiyalari kafedrasi', callback_data='Axborot texnologiya- lari kafedrasi')
Kafedra2 = InlineKeyboardMarkup(row_width=1).add(item18, item19,item20,item21,Menyu)

#Kafedra Tabiiy fanlar fakuleti
item22 = InlineKeyboardButton(text='Kimyo kafedrasi', callback_data='Kimyo kafedrasi')
item23 = InlineKeyboardButton(text='Geografiya kafedrasi', callback_data='Geografiya kafedrasi')
item24 = InlineKeyboardButton(text='Ekologiya kafedrasi', callback_data='Ekologiya kafedrasi')
item25 = InlineKeyboardButton(text='Zoologiya va umumiy biologiya kafedrasi', callback_data='Zoologiya va umumiy biologiya kafedrasi')
item26 = InlineKeyboardButton(text='Botanika va biotexnologiya kafedrasi', callback_data='Botanika va biotexnologiya kafedrasi')
item27 = InlineKeyboardButton(text='Tuproq-shunoslik kafedrasi', callback_data='Tuproq-shunoslik kafedrasi')
Kafedra3 = InlineKeyboardMarkup(row_width=1).add(item22,item23,item24,item25,item26,item27,Menyu)

#Kafedra Agrar qoʻshma fakulteti
item28 = InlineKeyboardButton(text='Zoinjeneriya va doirivor o‘simliklar kafedasi', callback_data='Zoinjeneriya va doirivor o‘simliklar kafedasi')
item29 = InlineKeyboardButton(text='Mevachilik va sabzavotchilik kafedrasi', callback_data='Mevachilik va sabzavotchilik kafedrasi')
item30 = InlineKeyboardButton(text='Aholi tomorqalaridan samarali foydalanish kafedrasi', callback_data='Aholi tomorqalaridan samarali foydalanish kafedrasi')
Kafedra4 = InlineKeyboardMarkup(row_width=1).add(item28, item29, item30,Menyu)

#Kafedra Chet tillari fakulteti
item31 = InlineKeyboardButton(text='Ingliz tili kafedrasi', callback_data='Ingliz tili kafedrasi')
item32 = InlineKeyboardButton(text='Nemis va fransuz tillari kafedrasi', callback_data='Nemis va fransuz tillari kafedrasi')
item33 = InlineKeyboardButton(text='Gumanitar yo‘nalishlar bo‘yicha chet tillari kafedrasi', callback_data='Gumanitar yo‘nalishlar bo‘yicha chet tillari kafedrasi')
item34 = InlineKeyboardButton(text='Tabiiy yo‘nalishlar bo‘yicha chet tillari kafedrasi', callback_data='Tabiiy yo‘nalishlar bo‘yicha chet tillari kafedrasi')
Kafedra5 = InlineKeyboardMarkup(row_width=1).add(item31,item32,item33,item34,Menyu)

#Kafedra Ingliz tili va adabiyoti
item35 = InlineKeyboardButton(text='Amaliy ingliz tili kafedrasi', callback_data='Amaliy ingliz tili kafedrasi')
item36= InlineKeyboardButton(text='Ingliz tili o‘qitish metodikasi kafedrasi', callback_data='Ingliz tili o‘qitish metodikasi kafedrasi')
Kafedra6 = InlineKeyboardMarkup(row_width=1).add(item35, item36,Menyu)

#Kafedra Filologiya fakulteti
item37 = InlineKeyboardButton(text='Tilshunoslik kafedrasi', callback_data='Tilshunoslik kafedrasi')
item38 = InlineKeyboardButton(text='Adabiyotshunoslik kafedrasi', callback_data='Adabiyotshunoslik kafedrasi')
item39 = InlineKeyboardButton(text='O‘zbek tili va adabiyoti kafedrasi', callback_data='O‘zbek tili va adabiyoti kafedrasi')
item40 = InlineKeyboardButton(text='Rus filologiyasi kafedrasi', callback_data='Rus filologiyasi kafedrasi')
item41 = InlineKeyboardButton(text='Rus tili metodikasi kafedrasi', callback_data='Rus tili metodikasi kafedrasi')
Kafedra7 = InlineKeyboardMarkup(row_width=1).add(item37,item38,item39,item40,item41,Menyu)

#Kafedra Tarix fakulteti
item42 = InlineKeyboardButton(text='Jahon tarixi kafedrasi', callback_data='Jahon tarixi kafedrasi')
item43 = InlineKeyboardButton(text='O‘zbekiston tarixi kafedrasi', callback_data='O‘zbekiston tarixi kafedrasi')
item44 = InlineKeyboardButton(text='Falsafa kafedrasi', callback_data='Falsafa kafedrasi')
Kafedra8 = InlineKeyboardMarkup(row_width=1).add(item42,item43,item44,Menyu)

#Kafedra Pedagogika psixologiya fakulteti
item45 = InlineKeyboardButton(text='Pedagogika kafedrasi', callback_data='Pedagogika kafedrasi')
item46 = InlineKeyboardButton(text='Psixologiya  kafedrasi', callback_data='Psixologiya  kafedrasi')
Kafedra9 = InlineKeyboardMarkup(row_width=1).add(item45,item46,Menyu)

#Kafedra San’atshunoslik fakulteti
item47 = InlineKeyboardButton(text='Tasviriy san’at  kafedrasi', callback_data='Tasviriy san’at  kafedrasi')
item48 = InlineKeyboardButton(text='Musiqiy ta’lim va madaniyat', callback_data='Musiqiy ta’lim va madaniyat')
item49 = InlineKeyboardButton(text='Vokal va cholg‘u ijrochiligi', callback_data='Vokal va cholg‘u ijrochiligi')
Kafedra10 = InlineKeyboardMarkup(row_width=1).add(item47,item48,item49,Menyu)

#Kafedra Maktabgacha va boshlang‘ich ta’lim fakulteti
item50 = InlineKeyboardButton(text='Boshlang‘ich ta’lim uslubiyoti kafedrasi', callback_data='Boshlang‘ich ta’lim uslubiyoti kafedrasi')
item51 = InlineKeyboardButton(text='Maktabgacha ta’lim kafedrasi', callback_data='Maktabgacha ta’lim kafedrasi')
Kafedra11 = InlineKeyboardMarkup(row_width=1).add(item50,item51,Menyu)

#Kafedra Jismoniy madaniyat fakulteti
item52 = InlineKeyboardButton(text='Jismoniy madaniyat kafedrasi', callback_data='Jismoniy madaniyat kafedrasi')
item53 = InlineKeyboardButton(text='Jismoniy madaniyat nazariyasi va uslubiyoti kafedrasi', callback_data='Jismoniy madaniyat nazariyasi va uslubiyoti kafedrasi')
item54 = InlineKeyboardButton(text='Sport o‘yinlari kafedrasi', callback_data='Sport o‘yinlari kafedrasi')
Kafedra12 = InlineKeyboardMarkup(row_width=1).add(item52,item53,item54,Menyu)

#Kafedra Iqtisodiyot fakulteti
item55 = InlineKeyboardButton(text='Jahon va mintaqa iqtisodiyoti kafedrasi', callback_data='Jahon va mintaqa iqtisodiyoti kafedrasi')
item56 = InlineKeyboardButton(text='Iqtisodiyot va servis kafedrasi', callback_data='Iqtisodiyot va servis kafedrasi')
item57 = InlineKeyboardButton(text='Moliya kafedrasi', callback_data='Moliya kafedrasi')
item58 = InlineKeyboardButton(text='Buxgalteriya hisobi va iqtisodiy tahlil kafedrasi', callback_data='Buxgalteriya hisobi va iqtisodiy tahlil kafedrasi')
Kafedra13 = InlineKeyboardMarkup(row_width=1).add(item55,item56,item57,item58,Menyu)

#Kafedra Harbiy ta’lim fakulteti
item59 = InlineKeyboardButton(text='Harbiy ta’lim kafedrasi', callback_data="Harbiy ta’lim kafedrasi")
Kafedra14 = InlineKeyboardMarkup(row_width=1).add(item59,Menyu)


#Kafedra Sirtqi bo‘limi
item59 = InlineKeyboardButton(text='Aniq va tabiiy fanlar kafedrasi', callback_data="Aniq va tabiiy fanlar kafedrasi")
item60 = InlineKeyboardButton(text="Ijtimoy gumanitar fanlar kafedrasi", callback_data="Ijtimoy gumanitar fanlar kafedrasi")
Kafedra15 = InlineKeyboardMarkup(row_width=1).add(item59,item60,Menyu)






