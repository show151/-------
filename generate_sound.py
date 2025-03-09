import numpy as np
import soundfile as sf

# 各音の周波数(Hz)
frequencies = {
    'doredo': [261.63, 293.66, 261.63],  # ドレド
    'remire': [293.66, 329.63, 293.66],  # レミレ
    'mifami': [329.63, 349.23, 329.63],  # ミファミ
    'fasofa': [349.23, 392.00, 349.23],  # ファソファ
    'solaso': [392.00, 440.00, 392.00],  # ソラソ
    'rashira': [440.00, 493.88, 440.00],  # ラシラ
    'shidoshi': [493.88, 523.25, 493.88],  # シドシ
}

# 音生成のパラメータ
samplerate = 44100 # サンプリングレート
duration = 0.5 # 各音の継続時間(s)

def generate_tone(frequency, duration, samplerate):
  t = np.linspace(0, duration, int(samplerate * duration), False)
  tone = 0.5 * np.sin(2 * np.pi * frequency * t)
  return tone

def generate_sound_file(name, frequencies, duration, samplerate):
  sound = np.concatenate([generate_tone(freq, duration, samplerate) for freq in frequencies])
  sf.write(f'audio/{name}.wav', sound, samplerate)

if __name__ == "__main__":
  for name, freqs in frequencies.items():
    generate_sound_file(name, freqs, duration, samplerate)