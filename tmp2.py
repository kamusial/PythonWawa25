import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

# 1. Tworzenie wektoryzowanego środowiska (1 instancja dla maksymalnej szybkości)
env = make_vec_env('CartPole-v1', n_envs=1)

# 2. Inicjalizacja modelu DQN z optymalnymi parametrami
model = DQN(
    "MlpPolicy",
    env,
    learning_rate=1e-3,
    buffer_size=10000,
    learning_starts=500,  # Mniej kroków przed rozpoczęciem uczenia
    batch_size=64,  # Optymalny rozmiar batcha
    gamma=0.98,  # Nieco niższe dyskontowanie dla szybszej zbieżności
    target_update_interval=250,
    verbose=0  # Wyciszenie logów
)

# 3. Skrócony trening (2500 kroków)
model.learn(total_timesteps=2500)

# 4. Szybka ewaluacja (5 epizodów)
mean_reward, std_reward = evaluate_policy(
    model,
    env,
    n_eval_episodes=5,
    deterministic=True  # Wybór zawsze najlepszej akcji
)

print(f"Średnia nagroda: {mean_reward:.2f} ± {std_reward:.2f}")

# 5. Test w trybie headless (bez renderowania)
test_env = gym.make('CartPole-v1')
obs, _ = test_env.reset()
episode_reward = 0

for _ in range(500):  # Maksymalnie 500 kroków testowych
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, _, _ = test_env.step(action)
    episode_reward += reward

    if done:
        print(f"Epizod zakończony z nagrodą: {episode_reward}")
        break

test_env.close()