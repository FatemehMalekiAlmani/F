from os import system
system('cls')
import numpy as np

# تنظیمات اولیه
num_bandits = 3
mean_rewards = [3, 6, 10]
variance = 2
num_steps = 1000
epsilon = 0.1

# مقادیر ذخیره‌سازی نتایج
bandit_rewards = np.zeros(num_bandits)
bandit_counts = np.zeros(num_bandits)

# تابع برای انتخاب دستگاه با روش ε-greedy
def select_bandit_epsilon_greedy():
    if np.random.random() < epsilon:
        # تصادفی انتخاب می‌کنیم
        return np.random.randint(num_bandits)
    else:
        # بهترین دستگاه را انتخاب می‌کنیم
        return np.argmax(bandit_rewards / (bandit_counts + 1e-6))

# شبیه‌سازی تصمیم‌گیری
for _ in range(num_steps):
    selected_bandit = select_bandit_epsilon_greedy()
    reward = np.random.normal(mean_rewards[selected_bandit], np.sqrt(variance))
    bandit_rewards[selected_bandit] += reward
    bandit_counts[selected_bandit] += 1

# نمایش نتایج
for i in range(num_bandits):
    print(f"machine{i+1}: efforts number= {bandit_counts[i]}, reward means= {bandit_rewards[i] / (bandit_counts[i] + 1e-6)}")
