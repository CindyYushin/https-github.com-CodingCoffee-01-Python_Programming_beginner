import calendar

if __name__ == "__main__":
  try:
    year = int(input("請輸入年份："))
    month = int(input("請輸入月份 (1-12)："))

    if 1 <= month <= 12:
      days = calendar.monthrange(year, month)[1]
      print(f"{year} 年 {month} 月有 {days} 天。")
    else:
      print("輸入的月份無效。")

  except ValueError:
    print("輸入的年份和月份必須是整數。")
