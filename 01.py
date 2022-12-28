# 引数で指定された西暦がうるう年かどうかを判定する関数

from calendar import day_abbr


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True 
    else:
        return False
    
# 引数で指定さた年月の1日が何曜日かを返す関数
def day_of_week(year, month):
    # 1月　～　12月
    days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # うるう年の場合は、2月　29日にする
    if leap_year(year):
        days_of_month[2] = 29
        
    # 日　に　１をセット
    day = 1
    
    # 西暦 1年1月1日（月曜日）からの日数を得る
    days = 0
    
    # 年の日数を集計する
    for y in range(1, year):
        if(leap_year(y)):
            days += 366
        else:
            days += 365
            
    # 月の日数を集計する
    for m in range(1, month):
        days += days_of_month[m]
        
    # 日を集計
    days += day
    
    # 日曜日　～　土曜日を 0～6で返す
    return days % 7

if __name__ == '__main__':
    
    # 曜日
    day_of_week_name = ['日', '月', '火', '水', '木', '金', '土']
    
    # 年月をキー入力
    year = int(input('year ='))
    month = int(input('month = '))
    
    # 1日の曜日を表示
    print(day_of_week_name[day_of_week(year, month)] + '曜日')