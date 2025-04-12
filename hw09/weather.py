# 기상자료를 받아서 연 평균 기온(일평균 기온의 연평균), 5mm이상 강우일수, 총 강우량을 구하시오.
def get_avg_temp(data_rows, temp_index):
    total_temp = 0
    total_days = 0
    
    for row in data_rows:
        total_temp += float(row[temp_index])
        total_days += 1
    
    return total_temp / total_days

def get_rain_info(data_rows, rain_index):
    rainy_days = 0
    total_rain = 0
    
    for row in data_rows:
        rain = float(row[rain_index])
        total_rain += rain
        
        if rain >= 5:
            rainy_days += 1
    
    return rainy_days, total_rain

def main():
    filename = 'weather(146)_2022-2022 (4).csv'
    
    with open(filename, 'r', encoding='utf-8-sig') as file:
        all_data = [line.strip().split(', ') for line in file]
        title = ['date', 'location', 'tavg', 'tmin', 'tmax', 'rainfall']  
        data_rows = all_data[1:]  
        temp_index = title.index('tavg')  
        rain_index = title.index('rainfall')  
    
    avg_temp = get_avg_temp(data_rows, temp_index)
    rainy_days, total_rain = get_rain_info(data_rows, rain_index)
    
    print(f"연평균 기온: {avg_temp:.2f}℃")
    print(f"5mm 이상 강우일수: {rainy_days}일")
    print(f"총 강우량: {total_rain}mm")

if __name__ == "__main__":
    main()