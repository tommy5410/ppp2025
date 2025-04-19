def get_weather_data_int(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            # print(tokens[col_idx], typ(tokens[col_idx]))
            weather_datas.append(int(tokens[col_idx]))

    return weather_datas

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            #print(tokens[col_idx], typ(tokens[col_idx]))
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas


def sumifs(rainfalls, years, selected = [2000]):
    total = 0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        year = years[i]
        if year in selected:
            total += rain
    return total



def main():
    filename = "weather(146)_2001-2022.csv"
    years = get_weather_data_int(filename, 0)
    rainfalls = get_weather_data(filename, 9)
    print(f"2021년의 총 강수량은 {sumifs(rainfalls, years, selected=[2021]):.1f}")
    print(f"2022년의 총 강수량은 {sumifs(rainfalls, years, selected=[2022]):.1f}")

if __name__=="__main__":
    main()