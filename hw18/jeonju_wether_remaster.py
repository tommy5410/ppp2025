import requests
import pandas as pd
import os
from sfarm_hw import submit_to_api

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    resp = requests.get(URL)
    resp.encoding = 'utf-8'
    with open(filename, 'w', encoding='UTF-8-sig') as f:
        f.write(resp.text)

def main():
    name = "이원재"
    affiliation = "스마트팜학과"
    student_id = "202110672"

    files = {
        'weather_146_2012.csv': (146, 2012),
        'weather_146_2020.csv': (146, 2020),
        'weather_146_2024.csv': (146, 2024),
        'weather_119_2019.csv': (119, 2019),
        'weather_146_2019.csv': (146, 2019),
    }
    
    for filename, (station, year) in files.items():
        if not os.path.exists(filename):
            download_weather(station, year, filename)

    df_2012 = pd.read_csv('weather_146_2012.csv', skipinitialspace=True)
    answer1 = round(df_2012['rainfall'].sum(), 1)

    df_2024 = pd.read_csv('weather_146_2024.csv', skipinitialspace=True)
    answer2 = round(df_2024['tmax'].max(), 1)

    df_2020 = pd.read_csv('weather_146_2020.csv', skipinitialspace=True)
    df_2020['tdiff'] = df_2020['tmax'] - df_2020['tmin']
    answer3 = round(df_2020['tdiff'].max(), 1)

    df_suwon = pd.read_csv('weather_119_2019.csv', skipinitialspace=True)
    df_jeonju = pd.read_csv('weather_146_2019.csv', skipinitialspace=True)
    answer4 = round(abs(df_suwon['rainfall'].sum() - df_jeonju['rainfall'].sum()), 1)

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__ == "__main__":
    main()