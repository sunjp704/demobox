"""
Utilities for reading CINRAD files and transfering to Py-art class Radar
"""
from curses import meta
import numpy as np
import pyart
import re
import json
import bz2

# get file raw data
def _get_raw(filename):
    with open(filename,'rb') as f:
        raw=f.read()
        if raw.startswith(b'BZh'):
            raw = bz2.decompress(raw)
    return raw


# parse file name
def _get_file_info(filename: str,user_defined_file_info:bool=False,station_id=None,scan_time=None,radar_band=None):
    if user_defined_file_info:
        try:
            if station_id is None or scan_time is None or radar_band is None:
                raise ValueError('file info is None.')
        except ValueError as e:
            print(e)
        return station_id, scan_time, radar_band
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
        print('Failed parsing file info, check your file name.\n')
    return station_id, scan_time, radar_band


def _SA_SB_decoder(byte_data:bytes):

    header = [('reserved1', '14B'), ('radar', 'u2'), ('reserved2', '12B')]
    description = [('time', 'u4'), ('date', 'u2'), ('unambiguous_range', 'u2'), ('azimuth', 'u2'), ('radial_index', 'u2'),
                   ('radial_status', 'u2'),
                   ('elevation', 'u2'), ('num_elevation', 'u2'), ('start_refractivity_range_bin', 'u2'),
                   ('start_doppler_range_bin', 'u2'), ('step_refractivity_range_bin', 'u2'), ('step_doppler_range_bin', 'u2'),
                   ('num_refractivity_range_bin', 'u2'), ('num_doppler_range_bin', 'u2'), ('sector', 'u2'),
                   ('adjustment', 'u4'), ('refractivity_pointer', 'u2'), ('doppler_pointer', 'u2'),
                   ('spectrum_width_pointer', 'u2'), ('resolution_doppler', 'u2'), ('volume_cover_pattern', 'u2'),
                   ('reserved3', '8B'), ('bk_refractivity_pointer', 'u2'), ('bk_doppler_pointer', 'u2'),
                   ('bk_spectrum_width_pointer', 'u2'), ('nyquist_velocity', 'u2')]
    base = [('reserved4', '38B'), ('refractivity', '460u1'), ('doppler_velocity', '920u1'), ('spectrum_width', '920u1'),
                 ('reserved5', '4B')]
    data_type= np.dtype(header+description+base)

    try:
        if len(byte_data)%data_type.itemsize == 0:
            data=np.frombuffer(byte_data,dtype=data_type)
        else:
            raise Exception('byte_data size must be a multiple of data_type size')
    except Exception as e:
        print('Failed decoding: ', e)
    except:
        print('Failed decoding: check your format.')
    return data

# create pyart Radar object
def cinrad2pyart(filename: str):
    station_id, scan_time, radar_band=_get_file_info()
    with open('station.json', 'r') as f:
        station_info = json.load(f)

    station_name=station_info[station_id][0]
    station_longitude=station_info[station_id][1]
    station_latitude=station_info[station_id][2]
    station_altitude=station_info[station_id][4]
    try:
        if radar_band is not station_info[station_id][3]:
            raise Exception('radar_band in filename is different from staion.json.')
    except Exception as e:
        print(e)

    filemetadata=pyart.config.FileMetadata('cinrad_SA_SB')
    
    time=filemetadata('time')
    time['units'] = 'seconds_since_197001010000'
    time['calendar'] = 'standard'
    time['comment'] = 'UTC'
    time['data'] = scan_time

    _range=filemetadata('range')
    # _range['data] = todo

    metadata=filemetadata('metadata')
    metadata['instrument_name']='CINRAD'

    scan_type='ppi'

    longitude=filemetadata('longitude')
    longitude['data']=station_longitude
    latitude = filemetadata('latitude')
    latitude['data']=station_latitude
    altitude=filemetadata('altitude')
    altitude['data']=station_altitude
    sweep_number=filemetadata('sweep_number')
    sweep_mode = filemetadata('sweep_mode')
    fixed_angle = filemetadata('fixed_angle')
    sweep_start_ray_index = filemetadata('sweep_start_ray_index')
    sweep_end_ray_index = filemetadata('sweep_end_ray_index')
    azimuth = filemetadata('azimuth')
    elevation = filemetadata('elevation')
    # instrument_parameters=instrument_parameters










    raw_data = _get_raw(filename)
    data=_SA_SB_decoder(raw_data)

    # using pyart default configuration
    filemetadata=pyart.config.FileMetadata('cinrad_SA_SB')
    time=filemetadata('time')
    time['units'] = 'seconds_since_197001010000'
    time['calendar'] = 'stadard'
    





    return Radar()
