def 計算矩形面積(高度, 寬度):
  """計算矩形的面積。"""
  return 高度 * 寬度

try:
  高度 = float(input("請輸入矩形的高度："))
  寬度 = float(input("請輸入矩形的寬度："))

  面積 = 計算矩形面積(高度, 寬度)
  print(f"矩形的面積是：{面積}")

except ValueError:
  print("輸入的必須是數值。")
