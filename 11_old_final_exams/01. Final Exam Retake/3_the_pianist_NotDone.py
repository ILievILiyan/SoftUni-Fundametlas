def add_songs(songs, piece, composer, key):
    piece_already_not_in = True

    if piece not in songs.keys():
        songs[piece] = []
    if composer not in songs[key]:
        songs[key][composer] = []
    for compositors_pieces in songs.values():
        for pieces in compositors_pieces.values():
            if piece in pieces:
                piece_already_not_in = False
    if piece_already_not_in:
        songs[key][composer].append(piece)
    return songs


def remove_piece(songs, piece):
    piece_deleted = False
    for compositors_pieces in songs.values():
        for pieces in compositors_pieces.values():
            if piece in pieces:
                pieces.remove(piece)
                piece_deleted = True
    if piece_deleted:
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return songs


def change_key(songs, piece, new_key):
    piece_deleted = False
    name_compositor = ""
    old_key = ""
    for key, compositors_pieces in songs.items():
        for compositor, pieces in compositors_pieces.items():
            if piece in pieces:
                piece_deleted = True
                old_key = key
                break

    if piece_deleted:
        songs[new_key] = songs.pop(old_key)
        add_songs(songs, piece, name_compositor, new_key)
        print(f'Changed the key of {piece} to {new_key}!')
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
        break
    command = cmd.split("|")

    if command[0] == "Add":
        current_piece, current_composer, current_key = command[1], command[2], command[3]

        old_length = sum([len(v.values()) for v in all_songs.values()])
        add_songs(all_songs, current_piece, current_composer, current_key)
        new_length = sum([len(v.values()) for v in all_songs.values()])
        if new_length > old_length:
            print(f"{current_piece} by {current_composer} in {current_key} added to the collection")
        else:
            print(f"{current_piece} is already in the collection!")

    elif command[0] == "Remove":
        current_piece = command[1]
        remove_piece(all_songs, current_piece)

    elif command[0] == "ChangeKey":
        current_piece, current_new_key = command[1], command[2]
        change_key(all_songs,current_piece, current_new_key)

print(all_songs)

for key, composer_piece in all_songs.items():
    for composer, piece in composer_piece.items():
        if len(piece) > 0:
            print(f'{"".join(piece)} -> Composer: {composer}, Key: {key}')