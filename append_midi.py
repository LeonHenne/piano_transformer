from email import message
from mido import MidiFile
from mido import merge_tracks
from mido import format_as_string

# loading start and end midi files
start = MidiFile("results/midi/midi_var16_pretrained_model.mid")
end = MidiFile("/Users/leonhenne/Desktop/midi_var_16_end.midi")

# takes a look at the different tracks
print("start tracks: " + str(start.tracks))
print("end tracks: " + str(end.tracks))

# adding up distances between notes
end_of_first_sequence = 0
for msg in start.tracks[1]:
    if not msg.is_meta:
        end_of_first_sequence += msg.time
        msg = format_as_string(msg)
print("end_of_first_sequence " + str(end_of_first_sequence))

# adding the sum of distances to the first note of the appending midi
print(end.tracks[0][1])
end.tracks[0][1].time = end.tracks[0][1].time + end_of_first_sequence

# combining both midi files
combined_midi = MidiFile()
combined_midi.ticks_per_beat = start.ticks_per_beat
combined_midi.tracks = start.tracks + end.tracks

print(combined_midi.tracks[2][1])
print(combined_midi.tracks)

# saving the new midi file
combined_midi.save("mashup2.mid")
print("Finished!!")