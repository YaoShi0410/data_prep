'''Make hdf5 file from raw data for EQT.(miniseed or sac)
'''

from EQTransformer.utils.hdf5_maker import preprocessor

# for 202109
# for CHN_stations
params_09_CHN = {'preproc_dir': './202109/CHN_hdf5',
                 'mseed_dir': './202109/CHN',
                 'stations_json': './output/202109_CHN_station_list.json',
                 'overlap': 0.3,
                 'n_processor': 8}
preprocessor(**params_09_CHN)

