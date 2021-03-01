import win32clipboard as wc
import win32con
import time
import os
import pyttsx3


def get_text():
    """读取剪贴板"""
    wc.OpenClipboard()
    text = wc.GetClipboardData(win32con.CF_TEXT)
    wc.CloseClipboard()
    return str(text.decode('gbk'))


def main():
    pre_t = ''

    with open('麻解选择题.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    while 1:
        t = get_text()
        if pre_t != t:
            pre_t = t
            for line in lines:
                if t in line:
                    # tts
                    engine = pyttsx3.init()
                    engine.say(line.replace('@', '：'))
                    engine.runAndWait()
                    break
            else:
                engine = pyttsx3.init()
                engine.say('未查询到结果')
                engine.runAndWait()
            
        time.sleep(0.2)


if __name__ == "__main__":
    main()
