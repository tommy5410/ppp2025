import os
import requests

# 평균 
def average(nums):
    return sum(nums) / len(nums)

# 5mm 이상 강우일수
def count_rain_days(rainfalls):
    count = 0
    for rain in rainfalls:
        if rain >= 5:
            count += 1
    return count

def get_weather_data(filename, col_idx):
    weather_data = []
    with open(filename) as f:
        lines = f.readlines()[1:] 
        for line in lines:
            tokens = line.strip().split(",")
            weather_data.append(float(tokens[col_idx]))  
    return weather_data


def download_weather_data(station_id, year, filename):
    url = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    response = requests.get(url)
    with open(filename, "w", encoding="UTF-8-sig") as f:
        f.write(response.text)

def main():
    filename = "weather(146)_2020-2020.csv"
    if not os.path.exists(filename):
        download_weather_data(146, 2020, filename)


    # 기온 데이터 (일평균 기온)
    tavgs = get_weather_data(filename, 4) 
    avg_temp = average(tavgs) 
    # 강수량 데이터 (5mm 이상)
    rains = get_weather_data(filename, 9)  
    rain_days_5mm = count_rain_days(rains)  

    # 총 강우량 
    total_rain = sum(rains)

   
    print(f"2020년 연평균 기온: {avg_temp:.2f}°C")
    print(f"2020년 5mm 이상 강우일수: {rain_days_5mm}일")
    print(f"2020년 총 강우량: {total_rain:.2f}mm")


if __name__ == "__main__":
    main()