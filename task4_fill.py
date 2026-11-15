# task4_fill.py —— 气温题：架子搭好，你只填 3 个空
# 变量名已改成英文；三个空用 BLANK1/2/3 占位，填掉就不会报错
# 运行：python task4_fill.py

temps = [21, 24, 19, 26, 30, 27, 22]

total = sum(temps)
avg = total / len(temps)

# ↓ 循环开始前，先把"记忆用的变量"立好。这四行是这次练习的重点，别改它们
hottest = temps[0]      # 擂主：先站第 1 天
hottest_day = 1         # 擂主是第几天
above_days = 0          # 高于平均的天数
below_days = 0          # 低于平均的天数

for i in range(len(temps)):
    if temps[i] > hottest:            # ① 跟擂台上的哪个变量比？
        hottest = temps[i]
        hottest_day = i+1        # ② 换擂主了，日子怎么写？（用到 i）
    if temps[i] > avg:
        above_days += 1                       # ③ 让 above_days 加 1（就一行）
    if temps[i] < avg:
        below_days += 1

print(f"平均气温：{avg:.1f}")
print(f"最高气温：{hottest}，出现在第 {hottest_day} 天")
print(f"高于平均气温的日子：{above_days} 天")
print(f"低于平均气温的日子：{below_days} 天")
