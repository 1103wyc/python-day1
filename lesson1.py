# lesson1.py —— 第 1 课：一周步数小统计
# 运行：在本文件夹打开终端，输入  python lesson1.py

steps=[6200,7800,5100,9300,10400,4300,8800]  #列表:一周7天的步数

total=sum(steps) #总步数
days=len(steps) #一共有几个数
avg =total/days #平均数

print(f'总步数:{total}步')
print(f'平均每天:{round(avg)}步')
print(f"最多:{max(steps)}步 最少:{min(steps)}步")
print(f"最多；{max(steps)}步 最少：{min(steps)}步")


for i in range(days):
    if steps[i] >=8000:
        print(f"第{i+1}天 {steps[i]}步,达标")
