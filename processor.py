"""
Accesses Spotify Web API through GET requests and restructures the resulting dictionary of data into
a DataFrame object with indices and columns for writing into a csv file.
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Global declaration of secrets and credentials for generating access token
id = 'my_client_id'
secret = 'my_client_secret'
client_credentials_manager = SpotifyClientCredentials(client_id=id, client_secret=secret)
token = client_credentials_manager.get_access_token()
sp = spotipy.Spotify(auth=token)

def searchTracks(keyword):
    """
    Searches 50 tracks and get the resulting data. Indexed by track name with track artist and popularity
    the track as columns. Ordered by the descending order of popularity.
    :param: The keyword used for searching
    :return: DataFrame object for csv file output.
    """

    results = sp.search(q=keyword, limit=50)
    results = results['tracks']['items']

    trackList = []
    artistList = []
    popularityList = []
    for i in range(len(results)):
        tempList = results[i]['artists']
        artistName = ''
        for j in range(len(tempList)):
            artistName += tempList[j]['name']
            # Separate items by comma for when there are more than one artist
            if j+1 in range(len(tempList)):
                artistName += ', '
        artistList.append(artistName)
        trackList.append(results[i]['name'])
        popularityList.append(results[i]['popularity'])

    dataDict = {
        'Artist(s)': artistList,
        'Popularity': popularityList
    }
    return pd.DataFrame(dataDict, trackList).sort_values(by=['Popularity'], ascending=False)

def getPlaylist(playlist_id):
    """
    Gets the data for all tracks contained in a playlist and calculates the number of tracks and
    their total runtime in the playlist for each artist. Indexed by the artist name(s) with their
    number of tracks and their total runtime in the playlist.
    :param: Spotify ID for the playlist
    :return: DataFrame object for csv file output.
    """

    results = sp.user_playlist(user='redmusiccompany',
                               playlist_id = playlist_id,
                               fields='tracks.items(track(id))')
    results = results['tracks']['items']

    artistList = []
    runtimeList = []
    trackCountList = []
    # Get artist names and track duration from each track in playlist, and counts number of tracks per artist
    for i in range(len(results)):
        tempDict = sp.track(results[i]['track']['id'])
        tempList = tempDict['artists']
        artistName = ''
        for j in range(len(tempList)):
            artistName += tempList[j]['name']
            if j+1 in range(len(tempList)):
                artistName += ', '
        # If artist name already exists, add up the track runtime and increment number of tracks of artist
        if artistName in artistList:
            runtimeIndex = artistList.index(artistName)
            runtimeList[runtimeIndex] += tempDict['duration_ms']
            trackCountList[runtimeIndex] += 1
        else:
            artistList.append(artistName)
            runtimeList.append(tempDict['duration_ms'])
            trackCountList.append(1)

    dataDict = {
        '# of Tracks': trackCountList,
        'Total Runtime (ms)': runtimeList
    }
    return pd.DataFrame(dataDict, index=artistList)

def getNewrelease():
    """
    Gets data for 50 albums tagged as New Releases. Indexed by the album name with artist name(s) and
    number of tracks as columns. If there is only one track in album, number of tracks is denoted as "snigle".
    :return: DataFrame object for csv file output.
    """
    results = sp.new_releases(limit = 50)
    results = results['albums']['items']

    artistList = []
    albumList = []
    total_trackList = []
    for i in range(len(results)):
        tempList = results[i]['artists']
        albumList.append(results[i]['name'])
        if results[i]['total_tracks'] == 1:
            total_trackList.append('single')
        else:
            total_trackList.append(results[i]['total_tracks'])
        artistName = ''
        for j in range(len(tempList)):
            artistName += tempList[j]['name']
            # Separate items by comma for when there are more than one artist
            if j + 1 in range(len(tempList)):
                artistName += ', '
        artistList.append(artistName)

    dataDict = {
        'Artist(s)': artistList,
        'Total Tracks': total_trackList
    }
    return pd.DataFrame(dataDict, index=albumList)