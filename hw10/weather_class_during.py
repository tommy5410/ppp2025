def average(nums):
    return sum(nums) / len(nums)

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            #print(tokens[col_idx], typ(tokens[col_idx]))
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas


def get_weather_data_int(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            # print(tokens[col_idx], typ(tokens[col_idx]))
            weather_datas.append(int(tokens[col_idx]))

    return weather_datas

def count_bigger_days(nums, criteria):
    count = 0
    for num in nums:
        if num >= criteria:
            count += 1
    return count

def get_rain_events(rainfalls):
    events = []
    continued_raindays = 0
    for rain in rainfalls:
        if rain > 0:
            continued_raindays += 1
        else:
            if continued_raindays > 0:
                events.append(continued_raindays)
            continued_raindays = 0
    if continued_raindays > 0:
        events.append(continued_raindays)
    return events

def events_rainfall(rainfalls):
    events = []
    continued_rainfalls = 0
    for rain in rainfalls:
        if rain > 0:
            continued_rainfalls += rain
        else:
            if continued_rainfalls > 0:
                events.append(continued_rainfalls)
            continued_rainfalls = 0
    if continued_rainfalls > 0:
        events.append(continued_rainfalls)
    return events

def sumifs(rainfalls, months, selected = [6, 7, 8]):
    total = 0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        month = months[i]
        if month in selected:
            total += rain
    return total

def main():
    filename = "./weather(146)_2022-2022 (4).csv"

    # 1. 일평균 기온의 연평균
    tavgs = get_weather_data(filename, 4)
    print(f"연평균 기온 (avg. of 일평균) = {average(tavgs):.2f}℃")

    # 2. 5mm이상 강우일수
    rainfalls = get_weather_data(filename, 9)
    count_over5_rain = count_bigger_days(rainfalls, 5)
    print(f"5mm이상 강우일수 = {count_over5_rain}일")

    # 3. 총 강우량
    print(f"총 강우량 = {sum(rainfalls):,.1f}mm")

    # 4. 최장연속 강우일수
    print(f"최장 연속 강우일수 = {max(get_rain_events(rainfalls))}일")

    # 5. 강우인벤트 중 최대 강수량은?
    print(f"강우 이벤트 중에서 최대 강수량은 {max(events_rainfall(rainfalls)):.1f}입니다.")

    # 6. top3 of tmax
    top3_tmax = sorted(get_weather_data(filename, 3))[-3:][::-1]
    print(f"가장 높았던 최고기온 3개는 {top3_tmax}입니다.")

    # 1) 여룸철(6월-8월) 총 강수량은?
    months = get_weather_data(filename, 1)
    print(f"여름철 강수량은 {sumifs(rainfalls, months, selected = [6, 7, 8]):.1f}mm 입니다.")
if __name__=="__main__":
    main()