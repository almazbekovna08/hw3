from aiogram import Bot, Dispatcher, types, F

from aiogram.filters import CommandStart, Command

from aiogram import Router

from app.keyboards import *

router=Router()



@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Здравствуйте! \nВас приветствует online-магазин "noglass_osh" ❤️. \nМожете рассмотреть наш ассортимент ✨', reply_markup=keyboard)

@router.message(F.text=='Серьги')
async def cmd_ear(message: types.Message):
    await message.answer('Мы имеем в наличии несколько видов сережек 💕:', reply_markup=ear_keyboard)

@router.message(F.text=='Косметика')
async def cmd_cosm(message: types.Message):
    await message.answer('Мы имеем в наличии 🙌:', reply_markup=cosm_keyboard)  

@router.message(F.text=='Подарки')
async def cmd_gift(message: types.Message):
    await message.answer('Мы имеем в наличии 🙌:', reply_markup=gift_keyboard)

@router.message(F.text=='Сердечки')
async def cmd_heart(message: types.Message):
    await message.answer_photo(photo='https://ae01.alicdn.com/kf/S427aebdc8e494a8f84c70187633805bdN.png')
    await message.answer("Серьги в форме сердца ❤️✨. \nСтоимость: 330 сом")   

@router.message(F.text=='Звездочки')
async def cmd_star(message: types.Message):
    await message.answer_photo(photo='https://ae04.alicdn.com/kf/S770457dba3c44926b72c670a24e3c375U.jpg_480x480.jpg')
    await message.answer("Серьги в форме звезды 💫. \nСтоимость: 330 сом")   

@router.message(F.text=='Облачко')
async def cmd_cloud(message: types.Message):
    await message.answer_photo(photo='https://ir.ozone.ru/s3/multimedia-7/c400/6377157139.jpg')
    await message.answer("Серьги в форме облачка 💨. \nСтоимость: 330 сом")

@router.message(F.text=='Каффы')
async def cmd_caf(message: types.Message):
    await message.answer_photo(photo='https://ir-3.ozone.ru/s3/multimedia-8/c1000/6682407956.jpg')
    await message.answer("Серьги на всю длинну 😍. \nСтоимость: 360 сом")   

@router.message(F.text=='Ягодки')
async def cmd_berries(message: types.Message):
    await message.answer_photo(photo='https://ae04.alicdn.com/kf/S4130c21cdae747e3a9bfcdf9e23a82962.jpg_480x480.jpg')
    await message.answer("Серьги в форме ягод 🫐. \nСтоимость: 350 сом")   

@router.message(F.text=='Тающие блески')
async def cmd_lips(message: types.Message):
    await message.answer_photo(photo='https://cosmetos.shop/upload/iblock/4e5/tj9gfncgwd8rtuw9nynuqwxr3r3k1ovl.gif')
    await message.answer("Нежный блеск ✨. \nСтоимость: 420 сом")
    
@router.message(F.text=='Тени')
async def cmd_eye(message: types.Message):
    await message.answer_photo(photo='https://ae04.alicdn.com/kf/S029bd1a77a864862b6a426f857fbdb50B.jpg')   
    await message.answer("Тени - корейские 💕. \nСтоимость: 440  сом") 

@router.message(F.text=='Подводки')
async def cmd_eye1(message: types.Message):
    await message.answer_photo(photo='https://koreamania.kg/media/products/1257/LM5DIPGM2S1IZH1.JPEG')
    await message.answer("Подводки - коричневые, черные 🖤. \nСтоимость: 270  сом") 

@router.message(F.text=='Румяна')
async def cmd_face(message: types.Message):
    await message.answer_photo(photo='https://images.prom.ua/5376444620_zhidkie-matovye-rumyana.jpg')
    await message.answer("Румяна - жидкие, сухие 💞. \nСтоимость: 350 сом") 

@router.message(F.text=='Мягкие игрушки')
async def cmd_g1(message: types.Message):
    await message.answer_photo(photo='https://images.satu.kz/181686615_w600_h600_181686615.jpg')
    await message.answer("Все виды. \nСтоимость: \nБольшие: 720 сом \nСредние: 500 сом \nМаленькие: 300 сом") 

@router.message(F.text=='Кружки с милым принтом')
async def cmd_g2(message: types.Message):
    await message.answer_photo(photo='https://ae04.alicdn.com/kf/Sa9ec2493ed7a4fa1914045b05316f809N.jpg_480x480.jpg')
    await message.answer("Все виды ✨✨. \nСтоимость: 520 сом") 

@router.message(F.text=='Картины по номерам')
async def cmd_g3(message: types.Message):
    await message.answer_photo(photo='https://images.prom.ua/4534024609_w640_h640_kartina-po-nomeram.jpg')
    await message.answer("Холсты с красками, всех размеров и видов 🥰. \nСтоимость: \nБольшие: 720 сом \nСредние: 470 сом \nМаленькие: 280 сом") 

@router.message(F.text=='Лего наборы')
async def cmd_g4(message: types.Message):
    await message.answer_photo(photo='https://legmir.ru/uploads/goods/kollekcionnye-nabory/40648/600/webp/2292972890.webp')
    await message.answer("Все виды ✨✨. \nСтоимость: 440 сом")

@router.message()
async def echo(message: types.Message):
    await message.answer('Я вас не понял')