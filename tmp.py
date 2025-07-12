import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

# Tworzenie środowiska CartPole
# Środowisko symuluje wózek z zamocowanym odwrotnym wahadłem
env = make_vec_env('CartPole-v1', n_envs=1)

# Inicjalizacja modelu DQN (Deep Q-Network)
# DQN to algorytm RL łączący uczenie Q-learning z sieciami neuronowymi
model = DQN(
    "MlpPolicy",  # Używana polityka (wielowarstwowy perceptron)
    env,  # Środowisko
    learning_rate=1e-3,  # Szybkość uczenia
    buffer_size=10000,  # Rozmiar pamięci doświadczeń
    learning_starts=1000,  # Kroki przed rozpoczęciem uczenia
    verbose=0  # Wyciszenie logów
)

# Trening agenta przez 5000 kroków
model.learn(total_timesteps=5000)

# Ocena wytrenowanego modelu (średnia nagroda z 10 epizodów)
mean_reward, _ = evaluate_policy(model, env, n_eval_episodes=10)
print(f"Średnia nagroda: {mean_reward:.2f}")

# Demonstracja działania wytrenowanego agenta
demo_env = gym.make('CartPole-v1', render_mode='human')
obs, _ = demo_env.reset()

for _ in range(1000):  # Maksymalnie 1000 kroków
    action, _ = model.predict(obs, deterministic=True)  # Wybór akcji
    obs, reward, done, _, _ = demo_env.step(action)  # Wykonanie akcji

    if done:  # Reset środowiska jeśli epizod zakończony
        obs, _ = demo_env.reset()

demo_env.close()