# demo3.py —— 看懂 range(len(km)) 到底给了什么
# 运行：python demo3.py

km = [5.2, 3.0, 0, 8.4, 2.5]

print("len(km)  =", len(km))                        # 5：一共 5 个柜子
print("编号清单 =", list(range(len(km))))            # [0, 1, 2, 3, 4]

for i in range(len(km)):
    print(f"第 {i + 1} 天：编号 {i} → 柜子里的数是 {km[i]}")

print("---- 对比：for x in km 拿到的是数，不是编号 ----")

for x in km:
    print(x)
