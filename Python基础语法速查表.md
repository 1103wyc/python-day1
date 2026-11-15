# Python 基础语法中文速查表

> 适用：Python 3.10+。配合 `python-day1/` 里的练习使用。
> 用法：写代码时先扫一眼「要做什么 → 用哪条」，别背。

---

## 0. 怎么跑起来

| 目的 | 做法 |
|---|---|
| 运行一个文件 | 终端里 `python 文件名.py`（先 `cd` 到文件所在文件夹） |
| 进交互模式试一行 | 终端输入 `python`，出现 `>>>` 后直接敲代码，`exit()` 退出 |
| 看 Python 版本 | `python --version` |
| 注释 | `# 单行注释`；`"""多行"""` 也可当说明用 |
| 文件名 | 用英文、数字、下划线，别用中文和空格 |

---

## 1. 变量与类型

```python
age = 18            # int 整数
price = 9.9         # float 小数
name = "小明"       # str 字符串
ok = True           # bool：只有 True / False（大写开头）
nothing = None      # None：空值，表示"没有"
```

| 操作 | 写法 | 结果 |
|---|---|---|
| 看类型 | `type(age)` | `<class 'int'>` |
| 转整数 | `int("12")` → 12；`int(9.9)` → 9（直接截断） | |
| 转小数 | `float("3.5")` → 3.5 | |
| 转字符串 | `str(18)` → "18" | |
| 转布尔 | `bool(0)`→False，`bool("")`→False，`bool("0")`→True | |

变量名：小写字母 + 下划线，如 `total_steps`。`=` 是赋值，`==` 才是比较。

---

## 2. 数字运算

| 运算 | 符号 | 例子 |
|---|---|---|
| 加 减 乘 | `+ - *` | `2 + 3` → 5 |
| 除（结果一定是小数） | `/` | `7 / 2` → 3.5 |
| 整除（砍掉小数） | `//` | `7 // 2` → 3 |
| 取余（除完剩多少） | `%` | `7 % 2` → 1，`n % 2 == 0` 判偶数 |
| 乘方 | `**` | `2 ** 10` → 1024 |
| 复合赋值 | `+= -= *=` | `n += 1` 等于 `n = n + 1` |

---

## 3. 字符串 str

```python
s = "Hello, 世界"
len(s)              # 长度
s[0]                # 'H'（下标从 0 开始）
s[-1]               # '界'（-1 是最后一个）
s[0:5]              # 'Hello'（切片，含头不含尾）
s.upper() / s.lower()
s.strip()           # 去掉首尾空格
s.replace("Hello", "Hi")
s.split(",")        # 按逗号切成列表
"-".join(["a", "b"])  # 'a-b'
"界" in s           # True，判断包不包含
```

f 字符串（最常用，别用 `+` 拼）：

```python
name, score = "小明", 92.5
print(f"{name} 考了 {score} 分")     # 小明 考了 92.5 分
print(f"{score:.1f}")                # 92.5  保留 1 位小数
print(f"{score:.0f}")                # 92    保留整数（四舍五入）
print(f"{1234567:,}")                # 1,234,567  千分位
```

---

## 4. 列表 list（一串有序的数据）

```python
steps = [6200, 7800, 5100]
```

| 操作 | 写法 | 说明 |
|---|---|---|
| 取一个 | `steps[0]` / `steps[-1]` | 下标或倒数 |
| 取一段 | `steps[0:2]` | `[6200, 7800]` |
| 改一个 | `steps[0] = 7000` | 列表可修改 |
| 加一个 | `steps.append(9000)` | 加到末尾 |
| 插入 | `steps.insert(1, 6500)` | 插到 1 号位 |
| 删除 | `steps.remove(7800)` / `steps.pop()` | 按值删 / 删末尾 |
| 排序 | `steps.sort()` / `sorted(steps)` | 就地改 / 返回新列表 |
| 反转 | `steps.reverse()` | |
| 长度 | `len(steps)` | |
| 求和 最大 最小 | `sum(steps)` `max(steps)` `min(steps)` | |
| 是否包含 | `7800 in steps` | True |

⚠️ `steps.sort()` 改自己、返回 None；`sorted(steps)` 返回新列表，原列表不动。

---

## 5. 判断 if

```python
if 分数 >= 90:
    等级 = "A"
elif 分数 >= 60:
    等级 = "B"
else:
    等级 = "C"
```

- 条件后面必须有冒号 `:`，下一行**缩进 4 个空格**。
- 比较：`==` `!=` `>` `<` `>=` `<=`
- 组合：`and`（并且）、`or`（或者）、`not`（不是）
- `0 < 分数 <= 100` 这种连写 Python 支持。

---

## 6. 循环 for / while

```python
for x in [1, 2, 3]:        # 逐个取出
    print(x)

for i in range(5):         # 0 1 2 3 4
    print(i)

for i in range(1, 6):      # 1 2 3 4 5
for i in range(0, 10, 2):  # 0 2 4 6 8
for i, v in enumerate(steps, start=1):   # 同时要下标和值
    print(i, v)
```

```python
n = 0
while n < 3:               # 条件为真就一直转
    n += 1
```

| 关键字 | 作用 |
|---|---|
| `break` | 立刻跳出整个循环 |
| `continue` | 跳过本次，进下一次 |
| `range(n)` | 造出 0 到 n-1 的整数序列（注意不含 n） |

`for i in range(len(lst))` 适合"我要下标"；`for x in lst` 适合"我只要值"。

---

## 7. 函数 def

```python
def 平均分(scores):
    """求平均分（文档字符串，可省）"""
    return sum(scores) / len(scores)

print(平均分([90, 80, 70]))   # 80.0
```

- 定义用 `def`，调用是 `平均分(...)`。
- `return` 交回结果；没有 return 的函数返回 `None`。
- 默认参数：`def f(x, times=2): ...`

---

## 8. 字典 dict（键值对）

```python
d = {"语文": 90, "数学": 85}
d["语文"]              # 90，键不存在会报错
d.get("英语", 0)       # 0，键不存在给默认值（不报错）
d["英语"] = 88         # 新增/修改
"语文" in d            # True
for k, v in d.items(): # 同时拿键和值
    print(k, v)
```

---

## 9. 输入输出

```python
name = input("你叫什么？")          # 注意：拿到的永远是字符串
age = int(input("几岁？"))          # 要算数就先转 int
print("a", "b")                     # a b（默认空格分隔）
print("a", end="")                  # 不换行
print(f"{name} 今年 {age} 岁")
```

---

## 10. 一行搞定（列表推导式，看懂即可）

```python
nums = [1, 2, 3, 4]
[n * 2 for n in nums]              # [2, 4, 6, 8]
[n for n in nums if n % 2 == 0]    # [2, 4]
```

---

## 11. 报错了先看最后一行

| 报错 | 人话 | 常见原因 |
|---|---|---|
| `SyntaxError` | 语法写错 | 冒号漏了、括号没闭、中文标点（`，` `：` `（）`） |
| `IndentationError` | 缩进不对 | 少了 4 个空格，或空格和 Tab 混用 |
| `NameError` | 名字没定义 | 变量名拼错、变量还没赋值就用 |
| `TypeError` | 类型不对 | `"3" + 3`，字符串没转成 int |
| `IndexError` | 下标越界 | 列表只有 3 个，却取 `lst[3]` |
| `KeyError` | 键不存在 | 字典取值用 `[]` 前先确认键 |
| `ValueError` | 值不对 | `int("abc")` |
| `ZeroDivisionError` | 除以 0 | 分母算出来是 0 |

排错三步：① 读最后一行是什么错 ② 看它指的行号 ③ 在那行前后 `print()` 出变量的值。

---

## 12. 常用内置函数速记

| 函数 | 作用 |
|---|---|
| `len(x)` | 长度（几个） |
| `sum(lst)` `max(lst)` `min(lst)` | 求和 / 最大 / 最小 |
| `round(x, 2)` | 四舍五入，可指定位数 |
| `abs(x)` | 绝对值 |
| `sorted(lst)` | 排序后返回新列表 |
| `range(a, b, c)` | 整数序列 |
| `enumerate(lst)` | 带下标遍历 |
| `zip(a, b)` | 两个列表配对遍历 |
| `int() float() str() bool()` | 类型转换 |
| `type(x)` | 查类型 |
| `input()` `print()` | 输入 / 输出 |

---

## 13. 新手五条纪律

1. **冒号配缩进**：`if`/`for`/`def` 行尾冒号，下一行缩进 4 个空格。
2. **标点用英文**：`:` `,` `"` `(` 全是半角，中文标点必报 SyntaxError。
3. **变量名有意义**：`total_steps` 好过 `a`、`x1`。
4. **一次只改一处**：改完立刻跑一遍，报错才知道是哪一步坏的。
5. **算数前先统一类型**：`input()` 拿到的是字符串，别忘了 `int()`。
