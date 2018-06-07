playlist = {
  'title': 'patagonia bus',
  'author': 'joe shmoe',
  'songs': [
    {"title": "song1", "artist": ["bol"], "duration": 2.35},
    {"title": "song2", "artist": ["bol", "simba"], "duration": 5.35},
    {"title": "Purrr", "artist": ["google"], "duration": 3.0}
  ]
}

total_length = 0

for song in playlist['songs']:
  total_length += song['duration']
print(total_length)