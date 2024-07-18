import openpyxl
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

# data_only=True を使用して数式の評価結果を取得する
wb = openpyxl.load_workbook("3.law of conservation of momentum/data/com.xlsx", data_only=True)
ws1 = wb["Sheet3"]

# データの集合nとhnを設定
n = []
hn = []

# データを取得する
for row in ws1['H4:H9']:
    for cell in row:
        n.append(cell.value)

for row in ws1['I4:I9']:
    for cell in row:
        hn.append(cell.value)

h_0 = 100  # 初期値 h_0

# Noneを除いたフィルタリングされたデータを作成
filtered_n = []
filtered_hn = []

for i in range(len(hn)):
    if hn[i] is not None:
        filtered_n.append(n[i])
        filtered_hn.append(hn[i])

# データを数値型に変換
filtered_n = np.array(filtered_n, dtype=float)
filtered_hn = np.array(filtered_hn, dtype=float)

# 対数変換
log_h_ratio = np.log(filtered_hn / h_0)

# 原点を通る直線のパラメータを計算
b = np.sum(filtered_n * log_h_ratio) / np.sum(filtered_n * filtered_n)

# プロット
plt.plot(filtered_n, log_h_ratio, marker='o', linestyle='', color='blue')
plt.plot(filtered_n, b * filtered_n, color='red', linestyle='-', label=f'近似直線: $y = {b:.2f}x$')

# グラフの装飾
plt.title('スーパーボールの衝突回数と振れ角の対数関係')
plt.xlabel('スーパーボールの衝突回数 $n$ (回)')
plt.ylabel(r'$\log \left(\frac{h_n}{h_0}\right)$')
plt.grid()
plt.legend()

# グラフを画像ファイルとして保存
plt.savefig("3.law of conservation of momentum/images/balljump1.png")

# グラフを表示
plt.show()

print(f"Slope b: {b}")
