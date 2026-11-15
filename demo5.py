# demo5.py —— 看 if 成立/不成立时，那两行到底执行了没有
# 运行：python demo5.py

km = [5.2, 3.0, 0, 8.4, 2.5, 6.0, 4.8]

最多 = km[0]
第几天 = 1

for i in range(len(km)):
    print(f"第{i + 1}圈 开始：i={i}  km[i]={km[i]}  当前 最多={最多} 第几天={第几天}")
    if km[i] > 最多:
        print(f"    条件成立 → 换擂主")
        最多 = km[i]
        第几天 = i + 1
        print(f"    执行完：第几天 = {i} + 1 = {i + 1}")
    else:
        print(f"    条件不成立 → 整段跳过，第几天 不动，还是 {第几天}")
    print()
