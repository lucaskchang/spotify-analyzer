import json
import math

with open('liked.json') as f:
    songs = json.load(f)

total_songs = len(songs)
popularity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
danceability = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
energy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
loudness = [0, 0, 0, 0, 0, 0]
speechiness = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
acousticness = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
instrumentalness = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
liveness = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
valence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
genre_frequency = {}
added_month_frequency = {}
explicit_songs = 0
durations =  []
tempos = []
time_signatures = [0, 0, 0, 0, 0]

for song in songs:
    genres = song['Artist Genres'].split(',')
    for genre in genres:
        if genre in genre_frequency:
            genre_frequency[genre] += 1
        else:
            genre_frequency[genre] = 1
    
    if song['Explicit']:
        explicit_songs += 1

    added_month = song['Added At'][:7]
    if added_month in added_month_frequency:
        added_month_frequency[added_month] += 1
    else:
        added_month_frequency[added_month] = 1

    popularity[song['Popularity'] // 10] += 1
    danceability[math.floor(song['Danceability'] * 10)] += 1
    energy[math.floor(song['Energy'] * 10)] += 1
    if song['Key'] != -1:
        Key[song['Key']] += 1
    loudness[abs(math.floor(song['Loudness'] / 10))] += 1
    speechiness[math.floor(song['Speechiness'] * 10)] += 1
    acousticness[math.floor(song['Acousticness'] * 10)] += 1
    instrumentalness[math.floor(song['Instrumentalness'] * 10)] += 1
    liveness[math.floor(song['Liveness'] * 10)] += 1
    valence[math.floor(song['Valence'] * 10)] += 1
    time_signatures[song['Time Signature'] - 3] += 1

    durations.append(song['Track Duration (ms)'] / 1000)
    tempos.append(song['Tempo'])

# genre frequency
genre_frequency = sorted(genre_frequency.items(), key=lambda x: x[1], reverse=True)
for genre in genre_frequency[:10]:
    print(f'{genre[0]}: {genre[1]}')

# explicit song percentage
print(f'{explicit_songs / total_songs * 100:.2f}% of songs are explicit')

# popularity score distribution
for i, popularity_score in enumerate(popularity):   
    print(f'{i * 10}-{i * 10 + 9}: {popularity_score / total_songs * 100:.2f}%')

# danceability score distribution
for i, danceability_score in enumerate(danceability):   
    print(f'{i / 10:.1f}-{(i + 1) / 10:.1f}: {danceability_score / total_songs * 100:.2f}%')

# energy score distribution
for i, energy_score in enumerate(energy):   
    print(f'{i / 10:.1f}-{(i + 1) / 10:.1f}: {energy_score / total_songs * 100:.2f}%')

# key distribution
for i, key in enumerate(Key):   
    print(f'{i}: {key / total_songs * 100:.2f}%')

# loudness distribution
for i, loudness_score in enumerate(loudness):   
    print(f'{i * 10}-{i * 10 + 9}: {loudness_score / total_songs * 100}%')

# speechiness distribution
for i, speechiness_score in enumerate(speechiness):   
    print(f'{i / 10:.1f}-{(i + 1) / 10:.1f}: {speechiness_score / total_songs * 100:.2f}%')

# acousticness distribution
for i, acousticness_score in enumerate(acousticness):   
    print(f'{i / 10:.1f}-{(i + 1) / 10:.1f}: {acousticness_score / total_songs * 100:.2f}%')

# instrumentalness distribution
for i, instrumentalness_score in enumerate(instrumentalness):   
    print(f'{i / 10:.1f}-{(i + 1) / 10:.1f}: {instrumentalness_score / total_songs * 100:.2f}%')

# liveness distribution
for i, liveness_score in enumerate(liveness):   
    print(f'{i / 10:.1f}-{(i + 1) / 10:.1f}: {liveness_score / total_songs * 100:.2f}%')

# valence distribution
for i, valence_score in enumerate(valence):   
    print(f'{i / 10:.1f}-{(i + 1) / 10:.1f}: {valence_score / total_songs * 100:.2f}%')

# time signature distribution
for i, time_signature in enumerate(time_signatures):   
    print(f'{i + 3}: {time_signature / total_songs * 100:.2f}%')

# duration distribution
durations = sorted(durations)
longest_duration = durations[-1]
shortest_duration = durations[0]
range_duration = longest_duration - shortest_duration
tenth_length = range_duration / 10
duration_distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for duration in durations:
    if math.floor((duration - shortest_duration) / tenth_length) == 10:
        duration_distribution[9] += 1
    else:
        duration_distribution[math.floor((duration - shortest_duration) / tenth_length)] += 1

for i, duration_score in enumerate(duration_distribution):
    print(f'{shortest_duration + i * tenth_length:.2f}-{shortest_duration + (i + 1) * tenth_length:.2f}: {duration_score / total_songs * 100:.2f}%')

# tempo distribution
tempos = sorted(tempos)
slowest_tempo = tempos[0]
fastest_tempo = tempos[-1]
range_tempo = fastest_tempo - slowest_tempo
tenth_length = range_tempo / 10
tempo_distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for tempo in tempos:
    if math.floor((tempo - slowest_tempo) / tenth_length) == 10:
        tempo_distribution[9] += 1
    else:
        tempo_distribution[math.floor((tempo - slowest_tempo) / tenth_length)] += 1

for i, tempo_score in enumerate(tempo_distribution):
    print(f'{slowest_tempo + i * tenth_length:.2f}-{slowest_tempo + (i + 1) * tenth_length:.2f}: {tempo_score / total_songs * 100:.2f}%')


output = {'total_songs': total_songs, 'genre_frequency': genre_frequency, 'added_month_frequency': added_month_frequency, 'explicit_songs': explicit_songs, 'popularity': popularity, 'danceability': danceability, 'energy': energy, 'key': Key, 'loudness': loudness, 'speechiness': speechiness, 'acousticness': acousticness, 'instrumentalness': instrumentalness, 'liveness': liveness, 'valence': valence, 'time_signatures': time_signatures, 'duration_distribution': duration_distribution, 'tempo_distribution': tempo_distribution}
with open('output.json', 'w') as f:
    json.dump(output, f, indent=4)