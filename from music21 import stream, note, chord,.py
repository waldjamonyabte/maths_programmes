from music21 import stream, note, chord, tempo, key, meter, choir

# Paramètres de la pièce
title = "And the Glory Day"
tonality = "C"  # tonalité: C majeur
time_signature = "4/4"
tempo_bpm = 100
measures = 8
voices = 1  # une voix melodyline

# Création de la partition (score)
score = stream.Score()
score.insert(0, tempo.MetronomeMark(number=tempo_bpm))
score.insert(0, key.Key(tonality))
score.insert(0, meter.TimeSignature(time_signature))

# Partie mélodique (melody)
melody_part = stream.Part()
melody_part.partName = "Melody"

# Exemple de phrase mélodique simple en C majeur
melody_notes = [
    ("C4", 1.0), ("E4", 1.0), ("G4", 2.0),  # mesure 1
    ("D4", 1.0), ("E4", 1.0), ("F4", 1.0), ("G4", 1.0),  # mesure 2
    ("E4", 1.0), ("G4", 1.0), ("A4", 2.0),  # mesure 3
    ("C5", 1.0), ("B4", 1.0), ("C5", 2.0),  # mesure 4
    ("G4", 1.0), ("E4", 1.0), ("C4", 2.0),  # mesure 5
    ("A4", 1.0), ("B4", 1.0), ("C5", 2.0),  # mesure 6
    ("D5", 1.0), ("C5", 1.0), ("B4", 2.0),  # mesure 7
    ("C5", 1.0), ("D5", 1.0), ("E5", 2.0),  # mesure 8
]

# Construction des notes
for pitch, dur in melody_notes:
    melody_part.append(note.Note(pitch, quarterLength=dur))

# Ajouter la partie au score
score.insert(0, melody_part)

# Option: ajouter une basse simple (root suivi d'octaves)
bass_part = stream.Part()
bass_part.partName = "Bass"
bass_notes = [
    ("C3", 2.0), ("G3", 2.0),  # mesures 1-2
    ("F3", 2.0), ("G3", 2.0),  # 3-4
    ("C3", 2.0), ("G3", 2.0),  # 5-6
    ("C3", 2.0), ("G3", 2.0),  # 7-8
]
for pitch, dur in bass_notes:
    bass_part.append(note.Note(pitch, quarterLength=dur))

score.insert(0, bass_part)

# Export MIDI et MusicXML
midi_fp = score.write('midi', fp='and_the_glory_day.mid')
xml_fp = score.write('musicxml', fp='and_the_glory_day.xml')

print(f"MIDI enregistré: {midi_fp}")
print(f"MusicXML enregistré: {xml_fp}")