import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

v_0 = 10
e_values = [0.2, 0.4,0.6, 0.8]
n_values = np.arange(1, 21, 1)

plt.figure(figsize=(10, 6))
for e in e_values:
    v_n_values = [(1 - (-e)**n) / 2 * v_0 for n in n_values]
    plt.plot(n_values, v_n_values, marker='o', label=f'$e = {e}$')

plt.xlabel('衝突回数''$n$''(回)')
plt.ylabel('小球Bの速さ''$V_n$''(m/s)')
plt.title('小球Bの速さと衝突回数の関係')
plt.legend()
plt.grid()
plt.xticks(n_values)

# グラフを画像ファイルとして保存
plt.savefig("C:\\Users\\s26n2\\OneDrive - 東京理科大学\\レポート\\3.law of conservation of momentum\\images\\com_simulate_B.png")

plt.show()
