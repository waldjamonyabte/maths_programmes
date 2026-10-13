from music21 import stream, note, tempo

s = stream.Stream()
s.append(tempo.MetronomeMark(number=60))
s.append(note.Note("C4", quarterLength=1))
s.append(note.Note("D4", quarterLength=1))
s.append(note.Rest(quarterLength=0.5))
s.append(note.Note("A4", quarterLength=1.5))
s.show('midi')  # ou 'musicxml' si tu préfères une partition