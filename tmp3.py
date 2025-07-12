import gymnasium as gym
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import EvalCallback
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn

# 1. Tworzenie środowiska Acrobot
env = make_vec_env("Acrobot-v1", n_envs=4)  # 4 równoległe środowiska

# 2. Konfiguracja modelu A2C
model = A2C(
    policy="MlpPolicy",
    env=env,
    learning_rate=7e-4,  # Szybkość uczenia (dostosowana do RMSprop)
    n_steps=8,  # Kroki na aktualizację
    gamma=0.99,  # Dyskontowanie
    gae_lambda=1.0,  # Parametr GAE
    ent_coef=0.01,  # Współczynnik entropii
    vf_coef=0.25,  # Waga funkcji wartości
    max_grad_norm=0.5,  # Przycinanie gradientu
    use_rms_prop=True,  # Użyj RMSprop zamiast Adam
    normalize_advantage=True,  # Normalizuj przewagę
    policy_kwargs={
        "net_arch": [dict(pi=[64, 64], vf=[64, 64])],  # Mniejsza sieć
        "activation_fn": nn.ReLU,
        "ortho_init": True
    },
    verbose=1,
    tensorboard_log="./a2c_acrobot_tensorboard/"
)

# 3. Callback do ewaluacji
eval_callback = EvalCallback(
    env,
    best_model_save_path="./best_model_a2c/",
    eval_freq=5000,  # Ewaluacja co 5000 kroków
    deterministic=True
)

# 4. Trening (krótszy ze względu na prostotę środowiska)
model.learn(total_timesteps=100000, callback=eval_callback)

# 5. Ewaluacja
mean_reward, std_reward = evaluate_policy(
    model,
    env,
    n_eval_episodes=15,
    deterministic=True
)
print(f"Średnia nagroda: {mean_reward:.2f} ± {std_reward:.2f}")


# 6. Wizualizacja wyników
def plot_training_results(log_dir):
    from stable_baselines3.common.results_plotter import load_results, ts2xy
    results = load_results(log_dir)
    x, y = ts2xy(results, "timesteps")
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.xlabel("Liczba kroków")
    plt.ylabel("Średnia nagroda")
    plt.title("Postęp treningu A2C w Acrobot-v1")
    plt.grid(True)
    plt.savefig("acrobot_training.png")
    plt.show()


# 7. Animacja działania
def animate_episode(model):
    env = gym.make("Acrobot-v1", render_mode="rgb_array")
    obs, _ = env.reset()
    frames = []
    total_reward = 0

    for _ in range(500):  # Maks 500 kroków
        frames.append(env.render())
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, _, _ = env.step(action)
        total_reward += reward

        if done:
            print(f"Epizod zakończony! Nagroda: {total_reward}")
            break

    env.close()

    # Tworzenie animacji
    plt.figure(figsize=(8, 6))
    for i, frame in enumerate(frames[::3]):  # Wyświetl co 3 klatkę
        plt.imshow(frame)
        plt.axis('off')
        plt.title(f"Krok: {i * 3} | Nagroda: {total_reward}")
        plt.pause(0.05)
        plt.clf()


# Wywołanie funkcji
plot_training_results("./a2c_acrobot_tensorboard/A2C_1")
animate_episode(model)