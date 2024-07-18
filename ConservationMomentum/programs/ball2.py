import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# 定数の設定
M = 48.0  # Mを48.0とします
m = 14.0  # mを14.0とします
e = 0.87  # eを0.87とします
g = 9.81  # 重力加速度

# 与えられた点
points = [(30, 80), (40, 105), (50, 130)]

# 傾きの計算
slope = (M * e**2 + 2 * M * e - m) / (M + m)

# hを計算する関数
def calculate_h(h0):
    return slope * h0

# 与えられた点のデータの準備
h0_values = np.array([point[0] for point in points])
h_values = np.array([point[1] for point in points])

# 理論値の計算
theory_h_values = calculate_h(h0_values)

# 最小二乗法で近似直線の傾きを計算
fit_slope, _ = np.polyfit(h0_values, h_values, 1)

# 近似直線の式（原点を通るように調整）
fit_line = fit_slope * np.array([0, max(h0_values)])

# 理論値の直線（原点を通るように調整）
theory_line = slope * np.array([0, max(h0_values)])

# グラフの準備
plt.figure(figsize=(10, 8))

# 与えられた点のプロット
plt.scatter(h0_values, h_values, color='blue', label='測定値')

# 理論値の点のプロット
plt.scatter(h0_values, theory_h_values, color='green', label='理論値')

# 近似直線のプロット（原点を通るように調整）
plt.plot([0, max(h0_values)], fit_line, color='blue', linestyle='-', label=f'近似直線: y = {fit_slope:.2f}x')

# 理論値の直線（原点を通るように調整）
plt.plot([0, max(h0_values)], theory_line, color='green', linestyle='-', label=f'理論値: y = {slope:.2f}x')

# 原点を設定
plt.xlim(left=0)
plt.ylim(bottom=0)

# グラフの装飾
plt.title('測定値と理論値の比較')
plt.xlabel(r'$h_0$''(cm)')
plt.ylabel(r'$h$''(cm)')
plt.grid(True)
plt.legend()

plt.savefig("3.law of conservation of momentum\\images\\ball.png")

# グラフの表示
plt.show()
