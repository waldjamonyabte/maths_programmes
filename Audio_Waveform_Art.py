import librosa, librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load(librosa.ex('trompet'))
librosa.display.waveshow(y, sr=sr)
plt.axis("off")

#source code --> clcoding.com