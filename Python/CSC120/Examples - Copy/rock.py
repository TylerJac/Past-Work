import csv
from collections import defaultdict
from collections import Counter
import re

def read_csv(filename):
    """
    Reads a CSV file containing ranked songs and artists, 
    returns a dictionary of the top 1000 rock and roll songs.
    """
    top_songs = defaultdict(list)
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            artist = row['Artist']
            song = row['Song']
            top_songs[artist].append(song)
    return top_songs

def get_top_artists(songs_dict):
    """
    Processes the dictionary and returns a list of tuples (song count, artist).
    """
    artists_songs_count = [(len(songs), artist) for artist, songs in songs_dict.items()]
    artists_songs_count.sort(reverse=True)
    return artists_songs_count

def most_common_word(songs_dict):
    """
    Processes the dictionary to return a tuple of the most common word found in the song titles
    with more than 3 letters. This should NOT count duplicate words in the same title.
    """
    word_counter = Counter()
    for songs in songs_dict.values():
        for song in songs:
            words = re.findall(r'\b\w{4,}\b', song) # extracting words with more than 3 letters
            word_counter.update(set(words))  # Counting only unique words per song
    return word_counter.most_common(1)[0]

def main():
    filename = 'top1000.csv'  # Adjust filename as needed
    top_songs_dict = read_csv(filename)
    
    # Problem 1: Who is the top artist?
    top_artist = max(top_songs_dict, key=lambda x: len(top_songs_dict[x]))
    print("1. The top artist is:", top_artist)
    
    # Problem 2: Who are the top five artists?
    top_artists = get_top_artists(top_songs_dict)[:5]
    print("2. The top five artists are:")
    for count, artist in top_artists:
        print(f"- {artist}: {count} songs")
    
    # Problem 3: What is the most common word that appears in all the titles, including its count?
    common_word, word_count = most_common_word(top_songs_dict)
    print(f"3. The most common word is '{common_word}' with a count of {word_count}.")
    
    # Problem 4:
    # a. Duplicate words handling: I handled it by using set() to count only unique words per song.
    # b. For problem 3, the algorithm iterates over all song titles, extracts words with more than 3 letters,
    #    counts only unique words per song, and returns the most common one.
    
if __name__ == "__main__":
    main()
