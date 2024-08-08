import json
import math

with open('liked.json') as f:
    songs = json.load(f)

total_songs = len(songs)
explicit_songs = 0
popularity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
danceability = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
energy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
keys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
keys_key= ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
speechiness = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
acousticness = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
instrumentalness = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
liveness = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
valence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
loudness = [0, 0, 0, 0, 0, 0]
genre_frequency = {}
genre_frequency_output = {}
added_month_frequency = {}
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
        keys[song['Key']] += 1
    loudness[abs(math.floor(song['Loudness'] / 10))] += 1
    speechiness[math.floor(song['Speechiness'] * 10)] += 1
    acousticness[math.floor(song['Acousticness'] * 10)] += 1
    instrumentalness[math.floor(song['Instrumentalness'] * 10)] += 1
    liveness[math.floor(song['Liveness'] * 10)] += 1
    valence[math.floor(song['Valence'] * 10)] += 1
    time_signatures[song['Time Signature'] - 3] += 1

    durations.append(song['Track Duration (ms)'] / 1000)
    tempos.append(song['Tempo'])

output = {
    'total_songs': total_songs,
    'explicit_songs': explicit_songs,
    'popularity': {},
    'danceability': {},
    'energy': {},
    'speechiness': {},
    'acousticness': {},
    'instrumentalness': {},
    'liveness': {},
    'valence': {},
    'loudness': {},
    'key': {},
    'genre_frequency': genre_frequency_output,
    'added_month_frequency': {},
    'time_signatures': time_signatures,
    'duration_distribution': {},
    'tempo_distribution': {}
}

# genre frequency
genre_frequency = sorted(genre_frequency.items(), key=lambda x: x[1], reverse=True)
print('Top 10 Genres')
for genre in genre_frequency[:10]:
    print(f'{genre[0]}: {genre[1]}')
for genre in genre_frequency:
    genre_frequency_output[genre[0]] = genre[1]

# explicit song percentage
print(f'\nPercentage of explicit songs: {explicit_songs / total_songs * 100:.2f}%')

# popularity score distribution
print('\nPopularity Score Distribution')
for i, popularity_score in enumerate(popularity):  
    popularity_range = f'{i * 10}-{i * 10 + 9}'
    range_percentage = popularity_score / total_songs * 100 
    output['popularity'][popularity_range] = range_percentage
    print(f'{popularity_range}: {range_percentage:.2f}%')

# danceability score distribution
print('\nDanceability Score Distribution')
for i, danceability_score in enumerate(danceability):   
    danceability_range = f'{i / 10:.1f}-{(i + 1) / 10:.1f}'
    range_percentage = danceability_score / total_songs * 100
    output['danceability'][danceability_range] = range_percentage
    print(f'{danceability_range}: {range_percentage:.2f}%')

# energy score distribution
print('\nEnergy Score Distribution')
for i, energy_score in enumerate(energy):
    energy_range = f'{i / 10:.1f}-{(i + 1) / 10:.1f}'
    range_percentage = energy_score / total_songs * 100
    output['energy'][energy_range] = range_percentage
    print(f'{energy_range}: {range_percentage:.2f}%')

# speechiness distribution
print('\nSpeechiness Distribution')
for i, speechiness_score in enumerate(speechiness):
    speechiness_range = f'{i / 10:.1f}-{(i + 1) / 10:.1f}'
    range_percentage = speechiness_score / total_songs * 100
    output['speechiness'][speechiness_range] = range_percentage
    print(f'{speechiness_range}: {range_percentage:.2f}%')

# acousticness distribution
print('\nAcousticness Distribution')
for i, acousticness_score in enumerate(acousticness):
    acousticness_range = f'{i / 10:.1f}-{(i + 1) / 10:.1f}'
    range_percentage = acousticness_score / total_songs * 100
    output['acousticness'][acousticness_range] = range_percentage
    print(f'{acousticness_range}: {range_percentage:.2f}%')

# instrumentalness distribution
print('\nInstrumentalness Distribution')
for i, instrumentalness_score in enumerate(instrumentalness):
    instrumentalness_range = f'{i / 10:.1f}-{(i + 1) / 10:.1f}'
    range_percentage = instrumentalness_score / total_songs * 100
    output['instrumentalness'][instrumentalness_range] = range_percentage
    print(f'{instrumentalness_range}: {range_percentage:.2f}%')

# liveness distribution
print('\nLiveness Distribution')
for i, liveness_score in enumerate(liveness):
    liveness_range = f'{i / 10:.1f}-{(i + 1) / 10:.1f}'
    range_percentage = liveness_score / total_songs * 100
    output['liveness'][liveness_range] = range_percentage
    print(f'{liveness_range}: {range_percentage:.2f}%')

# valence distribution
print('\nValence Distribution')
for i, valence_score in enumerate(valence):
    valence_range = f'{i / 10:.1f}-{(i + 1) / 10:.1f}'
    range_percentage = valence_score / total_songs * 100
    output['valence'][valence_range] = range_percentage
    print(f'{valence_range}: {range_percentage:.2f}%')

# loudness distribution
print('\nLoudness Distribution')
for i, loudness_score in enumerate(loudness):
    loudness_range = f'-{i * 10} to -{i * 10 + 9}'
    range_percentage = loudness_score / total_songs * 100
    output['loudness'][loudness_range] = range_percentage
    print(f'{loudness_range}: {range_percentage:.2f}%')

# key distribution
print('\nKey Distribution')
for i, key_score in enumerate(keys):
    key = keys_key[i]
    range_percentage = key_score / total_songs * 100
    output['key'][key] = range_percentage
    print(f'{key}: {range_percentage:.2f}%')

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

print('\nDuration Distribution')
for i, duration_score in enumerate(duration_distribution):
    duration_range = f'{shortest_duration + i * tenth_length:.2f}-{shortest_duration + (i + 1) * tenth_length:.2f}'
    range_percentage = duration_score / total_songs * 100
    output['duration_distribution'][duration_range] = range_percentage
    print(f'{duration_range}: {range_percentage:.2f}%')

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

print('\nTempo Distribution')
for i, tempo_score in enumerate(tempo_distribution):
    tempo_range = f'{slowest_tempo + i * tenth_length:.2f}-{slowest_tempo + (i + 1) * tenth_length:.2f}'
    range_percentage = tempo_score / total_songs * 100
    output['tempo_distribution'][tempo_range] = range_percentage
    print(f'{tempo_range}: {range_percentage:.2f}%')

new_added_month_frequency = {}
for year in range(2018, 2025):
    for month in range(1, 13):
        month_str = f"{year:04d}-{month:02d}"
        new_added_month_frequency[month_str] = added_month_frequency.get(month_str, 0)

output['added_month_frequency'] = new_added_month_frequency
print('\nAdded Month Frequency')
for month, frequency in new_added_month_frequency.items():
    print(f'{month}: {frequency}')

with open('output.json', 'w') as f:
    json.dump(output, f, indent=4)