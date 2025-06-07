import os.path
import requests
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def download_weather(station_id, s_year, e_year, filename):
    url = f"https://api.taegon.kr/stations/{station_id}/?sy={s_year}&ey={e_year}&format=csv"
    with open(filename, "w", encoding="UTF-8") as f:
        resp = requests.get(url)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def main():
    filename = "weather_suwon_1980_2024.csv"
    birth_month = 8
    birth_day = 8  # 내 생일

    # 집은 남양주지만 수원시 관측소 ID 사용  = 232
    if not os.path.exists(filename):
        download_weather(232, 1980, 2024, filename)

    df = pd.read_csv(filename, skipinitialspace=True)
    df = df[df["tavg"].notnull()]
    df["date"] = pd.to_datetime(df[["year", "month", "day"]])

    bday_df = df[(df["month"] == birth_month) & (df["day"] == birth_day)].copy()

    print(f"생일({birth_month}월 {birth_day}일) 데이터 개수:", len(bday_df))
    if len(bday_df) == 0:
        print("해당 날짜 데이터가 없습니다.")
        return

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(bday_df["year"].astype(str), bday_df["tavg"], color="skyblue")
    ax.set_title(f"내 생일 ({birth_month}월 {birth_day}일) 평균 기온 - 수원시")
    ax.set_xlabel("연도")
    ax.set_ylabel("기온 (℃)")
    ax.set_xticklabels(bday_df["year"].astype(str), rotation=45)
    plt.tight_layout()
    plt.savefig("birthday_bar_suwon.png")
    plt.show()

    coldest = bday_df.loc[bday_df["tavg"].idxmin()]
    hottest = bday_df.loc[bday_df["tavg"].idxmax()]
    print(f"가장 추운 생일: {int(coldest['year'])}년 ({coldest['tavg']:.1f}℃)")
    print(f"가장 더운 생일: {int(hottest['year'])}년 ({hottest['tavg']:.1f}℃)")

if __name__ == "__main__":
    main()