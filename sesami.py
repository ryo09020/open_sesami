import pyaudio
import deepspeech
import numpy as np

# ホットワード検出
hotword_samples = load_hotword_samples()
is_hotword_detected = False

while True:
    audio_stream = ... # PyAudioでマイク入力ストリームを取得

    # ホットワード検出
    if detect_hotword(audio_stream, hotword_samples):
        is_hotword_detected = True
        break

if is_hotword_detected:
    # 音声認識と声紋照合
    speech_recognizer = deepspeech.Model(...)
    transcript = speech_recognizer.recognize(audio_stream)
    speaker_vector = extract_speaker_vector(transcript)

    if match_voiceprint(speaker_vector, allowed_speaker_vectors):
        unlock_door()
    else:
        print("認証失敗")