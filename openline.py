import speech_recognition as sr
import os
import subprocess
import keyboard

# 音声認識インスタンスを作成
r = sr.Recognizer()
keyboard.wait("space")
text = ""
# スペースキーが押されるまで待機
print("スペースキーを押してください")
with sr.Microphone() as source:
    try:
        while keyboard.is_pressed("space"):  # スペースキーが押されている間
            audio = r.listen(source)  
            if audio:
                text += r.recognize_google(audio, language='ja-JP')
                

    except sr.UnknownValueError:
        print("音声が認識できませんでした")
    except sr.RequestError as e:
        print(f"エラーが発生しました: {e}")
print(f"音声認識結果: {text}")
print("音声認識を終了しました")