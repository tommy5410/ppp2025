import requests
import os

def average(nums):
    return sum(nums) / len(nums)


def get_rain_data(filename, col_idx):
    weather_data = []
    with open(filename) as f:
        lines = f.readlines()[1:]  
        for line in lines:
            tokens = line.strip().split(",")
            weather_data.append(float(tokens[col_idx]))
    return weather_data

def get_daily_temperature_range(filename, tmax_idx, tmin_idx):
    temperature_ranges = []
    with open(filename) as f:
        lines = f.readlines()[1:]
        for line in lines:
            tokens = line.strip().split(",")
            tmax = float(tokens[tmax_idx])
            tmin = float(tokens[tmin_idx])
            temperature_ranges.append(tmax - tmin)
    return temperature_ranges

def download_weather_data(station_id, year, filename):
    url = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    response = requests.get(url)
    with open(filename, "w") as f:
        f.write(response.text)

def main():
    file_2015 = "weather_146_2015.csv"
    file_2022 = "weather_146_2022.csv"
    file_2024 = "weather_146_2024.csv"
    file_2024_suwon = "weather_119_2024.csv"

    if not os.path.exists(file_2015):
        download_weather_data(146, 2015, file_2015)
    if not os.path.exists(file_2022):
        download_weather_data(146, 2022, file_2022)
    if not os.path.exists(file_2024):
        download_weather_data(146, 2024, file_2024)
    if not os.path.exists(file_2024_suwon):
        download_weather_data(119, 2024, file_2024_suwon)
   
      # 1) 전주시 2015년 연 강수량
    total_rain_2015 = round(sum(get_rain_data(file_2015, 9)), 1)

    # 2) 전주시 2022년 최대 평균기온(tavg)
    tavg_2022_list = get_rain_data(file_2022, 4)
    max_avg_temp_2022 = round(max(tavg_2022_list), 1)

    # 3) 전주시 2024년 최대 일교차 (tmax-tmin)
    temp_range_2024 = get_daily_temperature_range(file_2024, 3, 5)
    max_temp_range_2024 = round(max(temp_range_2024), 1)

    # 4) 수원시와 전주시 2024년 총강수량 차이(절대값)
    total_rain_2024_jeonju = sum(get_rain_data(file_2024, 9))
    total_rain_2024_suwon = sum(get_rain_data(file_2024_suwon, 9))
    rain_diff_2024 = round(abs(total_rain_2024_jeonju - total_rain_2024_suwon), 1)


from sfarm_hw import submit_to_api

def main():
    name = "이원재"
    affiliation = "스마트팜학과"
    student_id = "202110672"
    file_2015 = "weather_146_2015.csv"
    file_2022 = "weather_146_2022.csv"
    file_2024 = "weather_146_2024.csv"
    file_2024_suwon = "weather_119_2024.csv"

    if not os.path.exists(file_2015):
        download_weather_data(146, 2015, file_2015)
    if not os.path.exists(file_2022):
        download_weather_data(146, 2022, file_2022)
    if not os.path.exists(file_2024):
        download_weather_data(146, 2024, file_2024)
    if not os.path.exists(file_2024_suwon):
        download_weather_data(119, 2024, file_2024_suwon)
   
      # 1) 전주시 2015년 연 강수량
    total_rain_2015 = round(sum(get_rain_data(file_2015, 9)), 1)

    # 2) 전주시 2022년 최대 평균기온(tavg)
    tavg_2022_list = get_rain_data(file_2022, 4)
    max_avg_temp_2022 = round(max(tavg_2022_list), 1)

    # 3) 전주시 2024년 최대 일교차 (tmax-tmin)
    temp_range_2024 = get_daily_temperature_range(file_2024, 3, 5)
    max_temp_range_2024 = round(max(temp_range_2024), 1)

    # 4) 수원시와 전주시 2024년 총강수량 차이
    total_rain_2024_jeonju = sum(get_rain_data(file_2024, 9))
    total_rain_2024_suwon = sum(get_rain_data(file_2024_suwon, 9))
    rain_diff_2024 = round(abs(total_rain_2024_jeonju - total_rain_2024_suwon), 1)
    answer1 = total_rain_2015
    answer2 = max_avg_temp_2022
    answer3 = max_temp_range_2024
    answer4 = rain_diff_2024

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__ == "__main__":
    main()




