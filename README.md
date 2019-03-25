# SpotifyWriter
## Overview
This is a program written in Python to perform API call to Spotify Web API to read in data and process it for outputting the result into three exported spreadsheets.

Spotify Web API is accessed through a basic client-server interaction through authentication process using client credentials from Spotify for Developers and authorization process via the access token. Using the token, a group of 50 to 100 data from the Web API in JSON format is accessed through the Spotipy library's functions and returned as a nested dictionary. Data from the result are then extracted through written functions, manipulated and cleaned so that data are formatted and truncated into a necessary portion, and then restrutured into objects suitable for exporting into csv files with designated indices and two columns each.

## Files
### *processor.py*
Creates global access token with secrets to send GET requests to the Spotify web API to get a nested dictionary resutling data, and extracts its data into a DataFrame object containing collection of lists and dictionaries for writing to csv files. This script has a method each specifically for generating the DataFrame object to be written on each one of the three csv files. 

### *csvwriter.py*
The main script of the program. Calls methods in processor.py to get the three formatted DataFrame objects and outputs each one's data onto a spreadsheet. The arguments passed in to get the DataFrame objects such as search keyword and playlist ID can be changed within code.

### *tracksearch.csv*
Generated from searching data for 50 tracks using a search keyword. The resulting data are in descending order of the track's popularity.
- Index: Track name
- Column 1: Artist name(s)
- Column 2: Track's popularity

### *playlistartists.csv*
Generated from data for all tracks in a given playlist. Data about the same artists but different tracks are merged to denote the artist's total number of tracks and runtime in the playlist.
- Index: Artist name(s)
- Column 1: Number of artist's tracks in the playlist
- Column 2: Total runtime of artist's tracks in the playlist (ms)

### *newreleases.csv*
Generated from data for 50 albums under "New Releases". If the album has only one track, it will be denoted as "single".
- Index: Album name
- Column 1: Artist name(s)
- Column 2: Number of tracks

## Libraries used
### *Spotipy*
Used to access the Spotify Web API from the Python scripts. Generates the access token from the predeclared client ID and client secret values which is used for performing different types of GET queries with necessary keyword arguments to filter the resulting JSON data returned as a dictionary.

### *pandas*
Used to create the instances of the DataFrame object from the lists and dictionaries of processed data. The resulted collection of data are then output onto the spreadsheets in .cvs format. 
