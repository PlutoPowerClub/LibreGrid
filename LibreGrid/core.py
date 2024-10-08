# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['get_solar_building_insights', 'return_energy_solar_api', 'fetch_meter_usage', 'fetch_latest_meter_data',
           'round_now_to_last_half_hour', 'dummy_meter', 'insert_meter_data', 'get_meter_data']

# %% ../nbs/00_core.ipynb 2
import httpx
import asyncio
import os
import requests
import random
import sqlite3
import aiosqlite
import json
from dotenv import load_dotenv
from datetime import datetime, timedelta

# %% ../nbs/00_core.ipynb 8
def get_solar_building_insights(solar_key, latitude, longitude):
    """
    Call Google Solar building insights API
    """
    url = 'https://solar.googleapis.com/v1/buildingInsights:findClosest'
    params = {
    'location.latitude': latitude,
    'location.longitude': longitude,
    'requiredQuality': 'LOW',
    'key':solar_key
    }
    response = requests.get(url, params=params)
    return response.json()

# %% ../nbs/00_core.ipynb 9
def return_energy_solar_api(building_insights):
    """
    Get the solar potential for a building.
    The solar api gives the potential for many different array setups, so we take one somewhere around the third of number of panels.
    """
    third = round(building_insights['solarPotential']['maxArrayPanelsCount']/3)
    
    energy_dc = (item for item in building_insights['solarPotential']['solarPanelConfigs'] if (item["panelsCount"] == third or item["panelsCount"] == third+1 or item["panelsCount"] == third-1))
    
    return list(energy_dc)[0]['yearlyEnergyDcKwh']

# %% ../nbs/00_core.ipynb 11
def fetch_meter_usage(MPAN_import,serial_number, period_from, period_to):
    # period_from, period_to format: "YYYY-MM-dd hh:mm:ss"
    api_key = os.environ['phil_key']
    url = f"https://api.octopus.energy/v1/electricity-meter-points/{MPAN_import}/meters/{serial_number}/consumption/"
    params = {
        "period_from":f'{period_from}',
        "period_to":f'{period_to}',
        "page_size":"20"
    }
    response = requests.get(url,auth=(api_key,''), params = params)
    return response.json()
    

# %% ../nbs/00_core.ipynb 12
def fetch_latest_meter_data(api_key, mpan, serial_num):
    """
    Function to get last hour of meter consumption data
    """ 
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=10)
    url = f"https://api.octopus.energy/v1/electricity-meter-points/{mpan}/meters/{serial_num}/consumption/"
    params = {
        #"period_from":start_time.isoformat(),
        #"period_to":end_time.isoformat(),
        #'group_by':'hour',
        "page_size":"2"
    }
    
    response = requests.get(url, auth=(api_key, ''), params=params)
    if response.status_code == 200:
        data = response.json()
        results = data['results'] if data['results'] else None
        if results:
            for result in results:
                result['mpan_import'] = mpan
                result['serial_number'] = serial_num
        return results
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None
    

# %% ../nbs/00_core.ipynb 13
def round_now_to_last_half_hour():
    """
    Helper function to round current time to last half hour
    """
    dt = datetime.now()
    rounded = dt.replace(second=0, microsecond=0)
    if rounded.minute >= 30:
        rounded = rounded.replace(minute=30)
    else:
        rounded = rounded.replace(minute=0)
    return rounded

# %% ../nbs/00_core.ipynb 14
def dummy_meter(page_size=2):
    """
    Meter data simulator that just generates random consumption values at every full half hour, at a given interval
    """
    responses = []
    for item in range(0,page_size): 
        start_time = round_now_to_last_half_hour() - timedelta(minutes=30*(item+1))
        end_time = round_now_to_last_half_hour() - timedelta(minutes=30*(item))
        entry = {
            'mpan_import': 'dummy',
            'serial_number': f'dummy:{int(random.uniform(1,100))}',
            'consumption': round(random.uniform(0, 0.3), 3),
            'interval_start': start_time.isoformat(),
            'interval_end': end_time.isoformat()
        }
        responses.append(entry)
    return responses
        
    

# %% ../nbs/00_core.ipynb 16
async def insert_meter_data(consumption_list):
    """
    Function to insert data into the libergrid database
    Doing async in case there is a lot of data
    """
    async with aiosqlite.connect('libregrid.db') as db:
        await db.executemany('''
        INSERT OR REPLACE INTO meter_data (mpan_import, serial_number, interval_start, interval_end, consumption)
        VALUES (:mpan_import, :serial_number, :interval_start, :interval_end, :consumption)
        ''', consumption_list)
        await db.commit()

# %% ../nbs/00_core.ipynb 17
async def get_meter_data():
    """
    Get data from database. Again async to be able to do other stuff while it's reading.
    """
    async with aiosqlite.connect('libregrid.db') as db:
        async with db.execute('SELECT * FROM meter_data') as cursor:
            rows = await cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
