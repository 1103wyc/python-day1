# task4.py —— 一周气温（批改后的可运行版本）
# 和你那版比，只有三处根本不同：
#   ① 三件事分成三个平行的 if，谁也不套谁
#   ② 每个 if 只改自己那几个变量（找最高不动计数器，计数器不记日子）
#   ③ 循环里没有 print，四行结论都在循环外
# 运行：python task4.py

temps = [21, 24, 19, 26, 30, 27, 22]

total = sum(temps)
avg = total / len(temps)

# 循环开始前，先把四个"抽屉"立好——这一步你原来跳过了，所以只能去改 max()
hottest = temps[0]      # 擂主
hottest_day = 1         # 擂主是第几天
above_days = 0          # 高于平均的天数
below_days = 0          # 低于平均的天数

for i in range(len(temps)):
    # 第一件事：找最高——跟擂主比
    if temps[i] > hottest:
        hottest = temps[i]
        hottest_day = i + 1
    # 第二件事：数高于平均——跟平均值比
    if temps[i] > avg:
        above_days += 1
    # 第三件事：数低于平均
    if temps[i] < avg:
        below_days += 1

print(f"平均气温：{avg:.1f}")
print(f"最高气温：{hottest}，出现在第 {hottest_day} 天")
print(f"高于平均气温的日子：{above_days} 天")
print(f"低于平均气温的日子：{below_days} 天")
