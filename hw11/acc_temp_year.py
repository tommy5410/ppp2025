def read_file(filename, col_idx):
    weather_data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_data.append(float(tokens[col_idx]))  
    return weather_data

def get_weather_dates(filename):
    weather_dates = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])]) 
    return weather_dates

def calculate_gdd(year, tavg, dates, base_temp=5):
    total_gdd = 0
    for i in range(len(tavg)):
        t = tavg[i]
        year_in_data = dates[i][0]
        if year_in_data == year and dates[i][1] in [5, 6, 7, 8, 9]:
            if t >= base_temp:  
                total_gdd += t - base_temp 
    return total_gdd

def main():
    filename = "weather(146)_2001-2022.csv"
    dates = get_weather_dates(filename)
    tavg = read_file(filename, 4)  
    for year in range(2001, 2023):
        gdd_value = calculate_gdd(year, tavg, dates)
        print(f"{year}년=> GDD => {gdd_value:.1f}.")

if __name__ == "__main__":
    main()