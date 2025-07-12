import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

# Tworzenie środowiska CartPole
# Środowisko symuluje wózek z zamocowanym odwrotnym wahadłem
env = make_vec_env('CartPole-v1', n_envs=1)

model = DQN(
    'MlpPolicy',
    env,
    learning_rate=1e-3,
    buffer_size=10000,
    learning_starts=1000,
    verbose=0,
)

model.learn(total_timesteps=5000)

evaluate_policy(model, env, n_eval_episodes=10)

