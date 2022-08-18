"""
Utilities for reading CINRAD files and transfering to Py-art class Radar
"""
import numpy as np
from pyart.core.radar import Radar
import re
import json

with open('station.json', 'r') as f:
    station_info = json.load(f)


def _unzip(filename):
    # if file end with .bz2, unzip
    #
    pass


def _get_station_info(filename: str):
    # Z_RADR_I_Z9250_20160701001000_O_DOR_SA_CAP.bin.bz2
    # find and return station name, data type, scan time
    re_station_id = r'_Z\d{4}_'
    re_scan_time = r'_\d+_'
    re_radar_band = r'_SA_|_SB_|_SC_|_CA_|_CB_|_CC_|_CD_'
    try:
        station_id = re.findall(re_station_id, filename)[0][1:-1]
        scan_time = re.findall(re_scan_time, filename)[0][1:-1]
        radar_band = re.findall(re_radar_band, filename)[0][1:-1]
    except:
        print('Failed parsing station info, check your file name.\n')
    return station_id, scan_time, radar_band


def _SA_SB_decoder():
    header = [('reserved1', '14B'), ('radar', 'i2'), ('reserved2', '12B')]

    description = [('time', 'u4'), ('date', 'u2'), ('unambiguous_range', 'u2'), ('azimuth', 'u2'), ('radial_index', 'u2'),
                   ('radial_status', 'u2'),
                   ('elevation', 'u2'), ('num_elevation', 'u2'), ('start_refractivity_range_bin', 'u2'),
                   ('start_doppler_range_bin', 'u2'), ('step_refractivity_range_bin', 'u2'), ('step_doppler_range_bin', 'u2'),
                   ('num_refractivity_range_bin', 'u2'), ('num_doppler_range_bin', 'u2'), ('sector', 'u2'),
                   ('adjustment', 'u4'), ('refractivity_pointer', 'u2'), ('doppler_pointer', 'u2'),
                   ('spectrum_width_pointer', 'u2'), ('resolution_doppler', 'u2'), ('volume_cover_pattern', 'u2'),
                   ('reserved3', '4B'), ('bk_refractivity_pointer', 'u2'), ('bk_doppler_pointer', 'u2'),
                   ('bk_spectrum_width_pointer', 'u2'), ('nyquist_velocity', 'u2')]

    base_data = [('reserved1', '19B'), ('refractivity', '460u1'), ('doppler_velocity', '920u1'), ('spectrum_width', '920u1'),
                 ('reserved2', '14B')]

    pass


def cinrad2pyart(filename: str):

    _get_station_info()
    _SA_SB_decoder()
    return Radar()