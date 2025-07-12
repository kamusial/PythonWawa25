import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import EvalCallback
import torch
import torch.nn as nn

# 1. Tworzenie środowiska - Wahadło (Pendulum)
env = make_vec_env("Pendulum-v1", n_envs=4)  # 4 równoległe środowiska

# 2. Konfiguracja modelu PPO z rozbudowanymi parametrami
model = PPO(
    # Podstawowe parametry
    policy="MlpPolicy",  # Wielowarstwowy perceptron
    env=env,  # Środowisko treningowe
    device="auto",  # Automatyczny wybór CPU/GPU

    # Parametry sieci neuronowej
    policy_kwargs={
        "net_arch": [dict(pi=[256, 128], vf=[256, 128])],  # Architektura sieci
        "activation_fn": nn.Tanh,  # Funkcja aktywacji
        "ortho_init": True  # Inicjalizacja ortogonalna
    },

    # Parametry algorytmu
    learning_rate=4e-4,  # Szybkość uczenia (może być liniowo malejąca)
    n_steps=1024,  # Kroki na środowisko przed aktualizacją
    batch_size=64,  # Rozmiar batcha do optymalizacji
    n_epochs=10,  # Liczba epok na aktualizację
    gamma=0.99,  # Współczynnik dyskontowania
    gae_lambda=0.95,  # Parametr GAE (Generalized Advantage Estimation)
    clip_range=0.2,  # Zakres klipsowania dla PPO
    clip_range_vf=None,  # Klipsowanie dla funkcji wartości
    normalize_advantage=True,  # Normalizacja przewagi
    ent_coef=0.01,  # Współczynnik entropii (zachęta do eksploracji)
    vf_coef=0.5,  # Waga funkcji wartości w funkcji kosztu
    max_grad_norm=0.5,  # Maksymalna norma gradientu
    use_sde=False,  # State-dependent exploration (nie używane w Pendulum)

    # Logowanie
    tensorboard_log="./ppo_pendulum_tensorboard/",  # Logi dla TensorBoard
    verbose=2  # Poziom szczegółowości (0-2)
)

# 3. Callback do okresowej ewaluacji
eval_callback = EvalCallback(
    env,
    best_model_save_path="./best_model/",
    log_path="./logs/",
    eval_freq=5000,  # Co 5000 kroków ewaluacja
    deterministic=True,
    render=False
)

# 4. Trening
total_timesteps = 100000
model.learn(
    total_timesteps=total_timesteps,
    callback=eval_callback,
    tb_log_name="PPO_Pendulum_run"
)

# 5. Ewaluacja końcowa
mean_reward, std_reward = evaluate_policy(
    model,
    env,
    n_eval_episodes=10,
    deterministic=True
)
print(f"\nKońcowa średnia nagroda: {mean_reward:.2f} ± {std_reward:.2f}")

# 6. Testowanie modelu
test_env = gym.make("Pendulum-v1", render_mode='human')
obs, _ = test_env.reset()
episode_reward = 0
max_steps = 200

for _ in range(max_steps):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, _, _ = test_env.step(action)
    episode_reward += reward

    if done:
        break

print(f"Nagroda testowa: {episode_reward:.2f}")
test_env.close()