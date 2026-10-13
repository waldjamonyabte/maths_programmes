from MIDIUtil import MIDIFile

mf = MIDIFile(1)
track = 0
time = 0
mf.addTempo(track, time, 120)
mf.addNote(track, 0, 60, time, 1, 100)  # C4
with open("output.mid", "wb") as f:
    mf.writeFile(f)