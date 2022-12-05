def add_songs(songs, piece, composer, key):
    if piece not in songs.keys():
        songs[piece] = []
        songs[piece].append(composer)
        songs[piece].append(key)
    return songs


def remove_piece(songs, piece):
    if piece in songs.keys():
        print(f'Successfully removed {piece}!')
        del songs[piece]
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return songs


def change_key(songs, piece, new_key):
    if piece in songs.keys():
        songs[piece][1] = new_key
        print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return songs


num_of_pieces = int(input())
all_songs = {}

for i in range(num_of_pieces):
    text = input()
    current_piece, current_composer, current_key = text.split("|")
    add_songs(all_songs, current_piece, current_composer, current_key)


while True:
    cmd = input()
    if cmd == "Stop":
        for pieces, composer_key in all_songs.items():
            print(f'{pieces} -> Composer: {composer_key[0]}, Key: {composer_key[1]}')
        break
    command = cmd.split("|")

    if command[0] == "Add":
        current_piece, current_composer, current_key = command[1], command[2], command[3]

        if current_piece in all_songs.keys():
            print(f'{current_piece} is already in the collection!')
        else:
            add_songs(all_songs, current_piece, current_composer, current_key)
            print(f'{current_piece} by {current_composer} in {current_key} added to the collection!')

    elif command[0] == "Remove":
        current_piece = command[1]
        remove_piece(all_songs, current_piece)

    elif command[0] == "ChangeKey":
        current_piece, current_new_key = command[1], command[2]
        change_key(all_songs,current_piece, current_new_key)

