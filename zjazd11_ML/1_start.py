import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

from tmp import mean_reward

# Tworzenie środowiska CartPole
# Środowisko symuluje wózek z zamocowanym odwrotnym wahadłem
env = make_vec_env('CartPole-v1', n_envs=1)

model = DQN(
    'MlpPolicy',
    env,
    learning_rate=1e-3,
    buffer_size=10000,
    learning_starts=10,
    verbose=0,
)

model.learn(total_timesteps=5000)

mean_reward, _ = evaluate_policy(model, env, n_eval_episodes=10)
print(f'Średnia nagroda: {mean_reward:.2f}')

demo_env = gym.make('CartPole-v1', render_mode='human')
obs, _ = demo_env.reset()

for _ in range(1000):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, _, _ = demo_env.step(action)

    if done:
        obs, _ = demo_env.reset()

demo_env.close()