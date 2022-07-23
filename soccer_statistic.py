import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import Counter

PATH_DRIVER = "F:/chromedriver/chromedriver.exe"
URL = "https://24score.pro/football/argentina/primera_division/2022/regular_season/result_matrix/"
NUM = "1"

driver = webdriver.Chrome(PATH_DRIVER)
driver.get(URL)
draw = driver.find_elements(By.CLASS_NAME, 'bglly')
name_league = driver.find_element(By.TAG_NAME, 'h1').text
name_league_2 = name_league.replace("Шахматка чемпионата", "Чемпионат").upper()

draw_list = []
for item in draw:
    draw_list.append(item.text)
sum_draw = Counter(draw_list)
number_draws = len(draw_list)
print(f"------------{name_league_2}------------")
print("-" * 100)
print("Самые популярные ничьи:")
print(sum_draw)
print(f"Общее количество ничьих: {number_draws}")
print("-" * 100)
win = driver.find_elements(By.CLASS_NAME, 'bglgreen')
loose = driver.find_elements(By.CLASS_NAME, 'bglred')

win_list = []
for item in loose:
    win_list.append(item.text[::-1])

for item in win:
    win_list.append(item.text)
sum_win = Counter(win_list)
number_wins = len(win_list)
print("Самые популярные победы или поражения:")
print(sum_win)
print(f"Общее количество побед или поражений: {number_wins}")
sum_number_in_score = len([item for item in win_list if item.find(NUM) != -1])
sum_scores_all = number_wins + number_draws
percent_score = round(100 / (sum_scores_all / sum_number_in_score), 2)
print("-" * 100)
print(f"Цифра: {NUM} присутствует в: {sum_number_in_score} матчах")
print(f"Общее число матчей: {sum_scores_all}")
print(f"Вероятность в матче цифры ({NUM}): {percent_score}%")

time.sleep(5)

driver.close()
