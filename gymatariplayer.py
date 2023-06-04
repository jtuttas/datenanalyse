import os
import gym
import numpy as np


# Erstelle die Breakout-Umgebung
env = gym.make('Breakout-v0',render_mode='human')

print("Starte Training, lade alte Trainigsdaten")
if os.path.exists("training.txt"):
    qtable = np.loadtxt("training.txt")
else:
    print("keine Trainigsdaten gefunden")
    exit();


# Nutze den trainierten Agenten, um das Spiel zu spielen
state = env.reset()
state = np.reshape(state, (state_size,))
step = 0
done = False
max_steps = 100   
state_size = env.observation_space.shape[0] * env.observation_space.shape[1] * env.observation_space.shape[2]

while True:
    for step in range(max_steps):
        # Wähle die Aktion mit dem höchsten Q-Wert
        action = np.argmax(qtable[state,:])
        # Führe die Aktion aus und aktualisiere den Zustand
        new_state, reward, done, info = env.step(action)
        new_state = np.reshape(new_state, (state_size,))
        state = new_state
        
               
        if done == True:
            break

print ("Done")
env.close()
