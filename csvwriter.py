"""
Creates CSV files where the data manipulations and cleaning are performed
"""

import csv
import processor

def writecsv(filename, keyword=None):
    """
    Function for writing data into csv files
    :param filename: Name of the file to be generated
    """

    if filename == 'tracksearch':
        print('Generating  ' + filename + '.csv...')
        data = processor.searchTracks(keyword)
        data.to_csv(filename + '.csv')
        print(filename + ' has been created successfully.')
    #
    elif filename == 'playlistartists':
        print('Generating  ' + filename + '.csv...')
        data = processor.getPlaylist(keyword)
        data.to_csv(filename + '.csv')
        print(filename + ' has been created successfully.')

    #
    elif filename == 'newreleases':
        print('Generating  ' + filename + '.csv...')
        data = processor.getNewrelease()
        data.to_csv(filename + '.csv')
        print(filename + ' has been created successfully.')

writecsv('tracksearch', keyword='ambient')
writecsv('playlistartists', keyword='spotify:user:redmusiccompany:playlist:6TMuXkxElkRUIEFmxyrCcq')
writecsv('newreleases')
