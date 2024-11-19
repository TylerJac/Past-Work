# Imported library
import csv

def read_csv(filename):
    """
    Reads a CSV file containing song data and returns a dictionary where keys are artists 
    and values are lists of songs associated with each artist.
    
    Params: filename (str): The path to the CSV file to be read.
        
    Returns: A dictionary where keys are artist names and values are lists of songs by each artist.
    """
    # Initialize an empty dictionary to store songs
    songs_dict = {}
    
    # Open the CSV file
    with open(filename, 'r') as file:
        # Create a CSV reader object
        reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Extract the artist and song information from the row
            artist = row['Artist']
            song = row['Song']
            
            # Check if the artist is already in the dictionary
            if artist not in songs_dict:
                # If the artist is not in the dictionary, add a new key-value pair
                songs_dict[artist] = [song]
            else:
                # If the artist is already in the dictionary, append the song to the list of songs
                songs_dict[artist].append(song)
    
    # Return the dictionary of songs
    return songs_dict

def process_data(songs_dict):
    """
    Process data from a dictionary of songs to determine the count of songs by each artist.
    
    Params: songs_dict (dict): A dictionary where keys are artist names and values are lists of songs.
        
    Returns: A list of tuples containing the count of songs, the corresponding artist name, and the number of songs by that artist, sorted in descending order of song count.
    """
    # Initialize an empty list to store tuples of song count, artist name, and number of songs
    song_count_by_artist = [(len(songs), artist, len(songs)) for artist, songs in songs_dict.items()]
    # Sort the list in descending order based on song count
    song_count_by_artist.sort(reverse=True)
    return song_count_by_artist

def find_most_common_word(songs_dict):
    """
    Find the most common word among all songs in a dictionary of songs along with its frequency.
    
    Params: songs_dict (dict): A dictionary where keys are artist names and values are lists of songs.
        
    Returns: A tuple containing the most common word and its frequency among all songs.
    """
    # Initialize an empty dictionary to store word frequencies
    word_count = {}
    # Iterate through each list of songs for each artist
    for songs in songs_dict.values():
        # Iterate through each song
        for song in songs:
            # Split the song into words
            words = song.split()
            # Iterate through each word
            for word in words:
                # Strip punctuation marks and convert to lowercase
                word = word.strip(',.').lower()
                # Check if the word is longer than 3 characters
                if len(word) > 3:
                    # Update word frequency count
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    # Find the word with the highest frequency
    most_common_word = max(word_count, key=word_count.get)
    return (most_common_word, word_count[most_common_word])

def main(filename):
    """
    Main function to process song data and print results.
    
    Params: filename (str): The path to the CSV file containing song data.
    """
    # Read song data from the CSV file
    songs_dict = read_csv(filename)
    
    # Process data to determine top artist, top five artists, and most common word
    top_artist = process_data(songs_dict)[0][1]
    top_artists = process_data(songs_dict)[:5]
    top_five_artists = [f"{artist}: {count} songs" for _, artist, count in top_artists]
    common_word, common_word_count = find_most_common_word(songs_dict)
    
    # Print results
    print(f"1. Top artist: {top_artist}")
    print(f"2. Top artists and number of songs:")
    for i, (song_count, artist, _) in enumerate(top_artists, start=1):
        print(f"   {i}. {artist}: {song_count} songs")
    print(f"3. Most common word and its count: {common_word} - {common_word_count}")
    print("4. Two-part problem: ")
    print("   a. For songs with duplicate words, I used a dictionary to count the occurrences of words in the song titles.")
    print("   b. For problem 3, I iterated through all song titles, counted the occurrences of words with more than 3 letters, and found the most common word.")
    

# Call the main function with the filename
if __name__ == "__main__":
    main("Data/top1000.csv")