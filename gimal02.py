import pandas as pd
from IPython.display import display

# 첫 번째 데이터프레임
districts1 = ['합계', '종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
total_waste1 = [10852.9, 229.8, 298.2, 293.6, 271.9, 250.5, 320.2, 288.3, 372.6, 258.6, 251.9, 372.4, 378.9, 265.2, 545.2, 353.1, 2060.7, 373.2, 270.2, 441.7, 297.5, 400.4, 485.3, 679.5, 693.7, 416.1]
recycling_amount1 = [6084.5, 124.4, 137.3, 187.2, 186.9, 171.8, 206.9, 175.9, 275.6, 174.8, 146.5, 261.9, 150.9, 97.4, 140.4, 148.8, 453.2, 128.8, 115.0, 175.6, 116.6, 149.0, 150.8, 210.6, 275.0, 151.5]

# 두 번째 데이터프레임
total_waste2 = [8396.1, 160.6, 219.7, 231.5, 195.2, 167.8, 227.0, 204.2, 285.9, 194.4, 179.8, 256.7, 301.0, 204.2, 467.2, 264.7, 1929.7, 291.4, 214.7, 310.2, 217.0, 308.7, 337.9, 447.3, 494.1, 285.3]
recycling_amount2 = [3627.7, 55.2, 58.8, 125.1, 110.2, 89.1, 113.7, 91.8, 188.9, 110.6, 74.4, 146.2, 150.9, 97.4, 140.4, 148.8, 453.2, 128.8, 115.0, 175.6, 116.6, 149.0, 150.8, 210.6, 275.0, 151.5]

# 세 번째 데이터프레임
food_waste = {'음식물폐기물 발생량': [2456.8, 69.2, 78.5, 62.1, 76.7, 82.7, 93.2, 84.1, 86.7, 64.2, 72.1, 115.7, 77.9, 61.0, 78.0, 88.4, 130.0, 81.8, 55.5, 131.5, 80.5, 91.7, 147.4, 232.2, 199.6, 116.4],
'음식물폐기물 재활용량': [2456.8, 69.2, 78.5, 62.1, 76.7, 82.7, 93.2, 84.1, 86.7, 64.2, 72.1, 115.7, 77.9, 61.0, 78.0, 88.4, 130.0, 81.8, 55.5, 131.5, 80.5, 91.7, 147.4, 232.2, 199.6, 116.4]
}

# 첫 번째 데이터프레임 생성
df1 = pd.DataFrame({'지역': districts1, '발생량': total_waste1, '재활용량': recycling_amount1})

# 두 번째 데이터프레임 생성
df2 = pd.DataFrame({'생활폐기물 발생량': total_waste2, '생활폐기물 재활용량': recycling_amount2})

# 세 번째 데이터프레임 생성
df3 = pd.DataFrame(food_waste)

# 데이터프레임 합치기
df = pd.concat([df1, df2, df3], axis=1)

# 출력 포맷 조정
pd.set_option('display.unicode.east_asian_width', True)

# 데이터프레임 출력
#display(df)

# '합계' 자치구 제외
df_without_total = df[df['지역'] != '합계']

# 생활 폐기물 발생량 가장 많은 자치구를 선택
most_waste_district = df_without_total.sort_values(by='생활폐기물 발생량', ascending=False).iloc[0]

# 결과 출력
print("생활 폐기물이 가장 많은 자치구:", most_waste_district['지역'])

# 음식물폐기물 발생량 가장 적은 자치구를 선택
least_waste_district = df_without_total.sort_values(by='음식물폐기물 발생량').iloc[0]

# 결과 출력
print("음식물폐기물이 가장 적은 자치구:", least_waste_district['지역'])

# 생활폐기물 재활용량이 가장 적은 자치구를 선택
least_recycling_district = df_without_total.sort_values(by='생활폐기물 재활용량').iloc[0]

# 결과 출력
print("생활폐기물 재활용이 가장 적은 자치구:", least_recycling_district['지역'])