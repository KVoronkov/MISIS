violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
n = int(input('Сколько песен выбрать?: '))
song_names = [input(f'Название {i}-й песни: ')
              for i in range(1, n+1)]


total_playtime = 0
for i in range(len(violator_songs)):
    for name in song_names:
        if name == violator_songs[i][0]:
            total_playtime += violator_songs[i][1]

print(f'Общее время звучания песен: {round(total_playtime, 2)} минуты')
