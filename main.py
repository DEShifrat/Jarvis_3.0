
# coding=<Non-UTF-8>

import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2t4ru import num2text
import webbrowser
from playsound import playsound
import random


print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")


def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "и открывать браузер"
        tts.va_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Сейч+ас " + num2text(now.hour) + " " + num2text(now.minute)
        tts.va_speak(text)

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                 'Программист это машина для преобразования кофе в код']

        tts.va_speak(random.choice(jokes))

    elif cmd == 'open_browser':
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
        #webbrowser.get(chrome_path).open("http://python.org")
        webbrowser.open_new("http://python.org")

    elif cmd =='im_home':
        meet = ['Добрый день,сэр!',
                'Я рад вас видеть!',
                'Пришло время поработать,я к вашим услугам',
                'Проверяю все системы. Сээр,всё готово',
                'Ожидаю ваши команды']
        tts.va_speak(random.choice(meet))
        path = r"C:\Users\ilyua\Documents\Python_projects\Jarvis_3.0\music\acdc.mp3"
        playsound(path)

    elif cmd == 'sueta':
        dialog = ['Сэр,вы уверены в этом?','Как скажете','Видимо у вас хорошее настроение','Включаю']
        new_dialog = random.choice(dialog)
        if new_dialog == 'Сэр,вы уверены в этом?':
            dialog = 'Сэр,вы уверены в этом?'
            tts.va_speak(dialog)
            dialog2 = 'Хотя смысл мне спрашивать'
            tts.va_speak(dialog2)
            path1 = [r"C:\Users\ilyua\Documents\Python_projects\Jarvis_3.0\music\acdc.mp3",
                     r"C:\Users\ilyua\Documents\Python_projects\Jarvis_3.0\music\1.mp3",
                     r"C:\Users\ilyua\Documents\Python_projects\Jarvis_3.0\music\2.mp3"]

            playsound(random.choice(path1))

        else:
            tts.va_speak(new_dialog)
        path = [r"C:\Users\ilyua\Documents\Python_projects\Jarvis_3.0\music\acdc.mp3", r"C:\Users\ilyua\Documents\Python_projects\Jarvis_3.0\music\1.mp3", r"C:\Users\ilyua\Documents\Python_projects\Jarvis_3.0\music\2.mp3"]
        playsound(random.choice(path))

    elif cmd == 'working':
        work = ['Полностью поддерживаю вас в начинаниях',
                'Успехов в программировании',
                'Советую не отвлекаться','Я готов вам помочь','Активирую режим сканирования базы данных']
        tts.va_speak(random.choice(work))

    elif cmd == 'open_video':
        webbrowser.open_new("https://coub.com")

    elif cmd =='programming':
        meet = ['У меня только одна реакция на это',
                'Включу вам в помощь',
                'Возможно это вам поможет',
                'Люди называют это реакцией,на ваш запрос моя реакция будет такой',
                'Думаю так вам будет понятно']
        tts.va_speak(random.choice(meet))
        path = r"C:\Users\ilyua\Documents\Python_projects\Jarvis_3.0\music\ebany.mp3"
        playsound(path)

    #elif cmd == 'dialog_human':

    #playsound(random.choice())


    #elif cmd == 'weather':



# начать прослушивание команд
stt.va_listen(va_respond)