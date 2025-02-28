import numpy as np
from pydub import AudioSegment
import simpleaudio as sa

frequencies = {
  'ド': 261.63,
  'レ': 293.66,
  'ミ': 329.63,
}

def generate_sine_wave(frequency, duration=0.5, sample_rate=44100):
  t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
  wave = np.sin(2 * np.pi * frequency * t)
  return wave

def pley_wave(wave, sample_rate=44100):
  wave_int16 = np.int16(wave * 32767)
  audio_segment = AudioSegment(
    wave_int16.tobytes(),
    frame_rate=sample_rate,
    sample_width=2,
    channels=1
  )

  play_obj = sa.play_buffer(audio_segment.raw_data, 1, 2, sample_rate)
  play_obj.wait_done()

def play_sequence(notes, sample_rate=44100):
  for note in notes:
    wave = generate_sine_wave(frequencies[note])
    pley_wave(wave, sample_rate)

def play_sequence_smooth(notes, sample_rate=44100):
  for i, note in enumerate(notes):
    wave = generate_sine_wave(frequencies[note])
    
    if i != 0:
      fade_duration = 0.001
      wave[:int(sample_rate * fade_duration)] *= np.linspace(0, 1, int(sample_rate * fade_duration))
    if i != len(notes) - 1:
      fade_duration = 0.001
      wave[-int(sample_rate * fade_duration):] *= np.linspace(1, 0, int(sample_rate * fade_duration))

    pley_wave(wave, sample_rate)

play_sequence_smooth(['ド', 'レ', 'ミ', 'レ', 'ド'])