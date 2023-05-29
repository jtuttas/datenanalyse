import gymnasium as gym
#env = gym.make("Taxi-v3", render_mode="human")
env = gym.make("Taxi-v3")
observation, info = env.reset()
done = False

steps=0;

while not done:
   action = env.action_space.sample()  # this is where you would insert your policy
   observation, reward, done, truncated, info = env.step(action)
   steps=steps+1


print ("We are done in ",steps, " Steps")
env.close()