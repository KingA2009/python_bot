import asyncio
from mailbox import Message

from aiogram import F, types
from aiogram.types import CallbackQuery
from aiogram.filters import CommandStart, Command
from loader import dp, bot
from aiogram import types
from keyboards.inlines.buttons import btn, btn2, btn3, btn4
from api import weather, chatgpt


@dp.message(CommandStart())
async def start_bot(message: types.Message):
    await message.answer(
        f"Assalomu alalykum @{message.from_user.username}, @KingA_09 ning botiga xush kelibsiz!\nQuyidagilardan birini tanlang:",
        reply_markup=btn)


@dp.callback_query(F.data)
async def inline_button(call: CallbackQuery):
    if call.data == "ob-havo":
        await obHavo(call.message)
    if call.data == "dasturlash":
        await dasturlash(call.message)
    if call.data == "chatgpt":
        await chatgpt_answer(call.message)
    if call.data == "back":
        await reply_bot(call.message)
    if call.data == "tokyo":
        await call.message.answer(weather("tokyo"), reply_markup=btn2)
    if call.data == "london":
        await call.message.answer(weather("london"), reply_markup=btn2)
    if call.data == "new-york":
        await call.message.answer(weather("new-york"), reply_markup=btn2)
    if call.data == "paris":
        await call.message.answer(weather("paris"), reply_markup=btn2)
    if call.data == "madrid":
        await call.message.answer(weather("madrid"), reply_markup=btn2)
    if call.data == "dubai":
        await call.message.answer(weather("dubai"), reply_markup=btn2)
    if call.data == "python":
        await call.message.answer(
            "Python — bu keng qo'llaniladigan va yuqori darajadagi dasturlash tili bo'lib, u o'zining soddaligi va o'qilishi osonligi bilan mashhur. Python dasturlash tili haqida batafsilroq ma'lumot olish uchun Python rasmiy saytini python.org sahifasida ko'rishingiz mumkin ",
            reply_markup=btn3)
    if call.data == "java":
        await call.message.answer(
            "Java - bu yuqori darajadagi dasturlash tili bo'lib, dastlab Sun Microsystems tomonidan ishlab chiqilgan va 1995-yilda chiqarilgan. Java tilining asosiy maqsadi mustaqil platforma bo'lishdir, ya'ni bir marta yozilgan dastur har qanday muhitda ishlay olishi kerak. Java'Write Once, Run Anywhere' (WORA) prinsipiga amal qiladi, bu esa dasturchilarga bir marta yozilgan kodni turli platformalarda qayta yozmasdan ishlatish imkonini beradi. ",
            reply_markup=btn3)
    if call.data == "ruby":
        await call.message.answer(
            "Ruby – bu yuqori darajadagi, interpretatsion dasturlash tili bo‘lib, 1995-yilda Yaponiyalik Yukihiro 'Matz' Matsumoto tomonidan ishlab chiqilgan. Uning asosiy maqsadi sodda, samarali va insonga qulay kod yozishni ta'minlashdir.",
            reply_markup=btn3)
    if call.data == "cpp":
        await call.message.answer(
            "C++ - bu umumiy maqsadli dasturlash tili bo'lib, 1979-yilda Bjarne Stroustrup tomonidan ishlab chiqilgan. C++ dasturlash tili yuqori samaradorlik, tezlik va muvozanatli dastur yaratish imkoniyatlari bilan mashhurdir. ",
            reply_markup=btn3)
    if call.data == "javascript":
        await call.message.answer(
            "JavaScript (JS) bu yuqori darajadagi, ko‘p maqsadli dasturlash tili bo‘lib, asosan veb-sahifalarni dinamik va interaktiv qilish uchun ishlatiladi. 1995-yilda Brendan Eich tomonidan Netscape Communications Corporation kompaniyasida yaratilgan. ",
            reply_markup=btn3)
    if call.data == "rust":
        await call.message.answer(
            "Rust - bu zamonaviy tizim dasturlash tili bo'lib, xavfsizlik, samaradorlik va bir vaqtning o'zida bajariladigan vazifalarni (konkurrensiya) qo'llab-quvvatlashga katta e'tibor qaratadi. Mozilla tomonidan ishlab chiqilgan va 2015 yilda birinchi barqaror versiyasi chiqarilgan. ",
            reply_markup=btn3)


@dp.message(F.text)
async def massage_text(message: Message):
   await message.answer(chatgpt(message.text))


async def obHavo(message: types.Message):
    await message.answer("Ob havo haqida malumot bilmoqchi bo`lsangiz quyidagi viloyatlardan birini tanlang.",
                         reply_markup=btn2)


async def dasturlash(message: types.Message):
    await message.answer(
        "Dasturlash tillari haqida malumot bilmoqchi bo`lsangiz quyidagi dasturlash tillaridan birini tanlang.",
        reply_markup=btn3)


async def reply_bot(message: types.Message):
    await message.answer("Quyidagilardan birini tanlang:", reply_markup=btn)


async def chatgpt_answer(message: types.Message):
    await message.answer("Chatgpt botga xush kelibsiz! Qanday savolingiz bor", reply_markup=btn4)
