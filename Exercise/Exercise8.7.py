def make_album(artist, title, tracks=None):
    album = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album['tracks'] = tracks
    return album


print(make_album('sheila on 7', 'kisah klasik untuk masa depan'))
print(make_album('noah', 'seperti seharusnya'))
print(make_album('queen', 'a night at the opera', tracks=12))