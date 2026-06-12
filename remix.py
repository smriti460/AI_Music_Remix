from pydub import AudioSegment

def remix_song(song_file, mood):

    song = AudioSegment.from_file(song_file)

    if "Happy" in mood:
        song = song.speedup(playback_speed=1.2)
        song = song + 5

    elif "Sad" in mood:
        song = song - 10

    elif "Energetic" in mood:
        song = song.speedup(playback_speed=1.4)
        song = song + 10

    elif "Relaxing" in mood:
        song = song - 15

    output_file = "remixed/remix.wav"

    song.export(output_file, format="wav")

    return output_file