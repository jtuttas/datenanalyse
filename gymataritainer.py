import os
import gym
import numpy as np


# Erstelle die Breakout-Umgebung
env = gym.make('Breakout-v0',render_mode='rgb_array')


# Definiere die Größe des Q-Tables
state_size = env.observation_space.shape[0] * env.observation_space.shape[1] * env.observation_space.shape[2]
action_size = env.action_space.n

# Definiere die Hyperparameter
total_episodes = 1000
learning_rate = 0.8         
max_steps = 100              
gamma = 0.95                

# Exploration parameters
epsilon = 1.0                
max_epsilon = 1.0           
min_epsilon = 0.01          
decay_rate = 0.001          

if os.path.exists("training.txt"):
    print("Starte Training, lade alte Trainigsdaten")
    qtable = np.loadtxt("training.txt")
else:
    print("Starte neues Training!")
    qtable = np.zeros((state_size, action_size))


# Implementiere den Q-Learning Algorithmus
for episode in range(total_episodes):
    # Setze die Umgebung für das neue Spiel zurück
    state = env.reset()
    state = np.reshape(state, (state_size,))
    step = 0
    done = False
    
    for step in range(max_steps):
        # Entscheide, ob wir eine zufällige Aktion ausführen oder diejenige mit dem höchsten Q-Wert wählen
        exp_exp_tradeoff = np.random.uniform(0, 1)
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(qtable[state,:])
        else:
            action = env.action_space.sample()
        
        # Führe die Aktion aus und erhalte den neuen Zustand, die Belohnung, ob das Spiel beendet ist, und zusätzliche Informationen
        new_state, reward, done, info = env.step(action)
        new_state = np.reshape(new_state, (state_size,))
        
        # Aktualisiere den Q-Wert des alten Zustands
        qtable[state, action] = qtable[state, action] + learning_rate * (reward + gamma * np.max(qtable[new_state, :]) - qtable[state, action])
        
        state = new_state
        
        if done == True:
            break
    
    # Reduziere epsilon im Laufe der Zeit, während wir unser Modell verbessern
    if episode%100==0:
        print("Episode "+str(episode))
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate*episode)


print("Training beendet")
np.savetxt("training.txt",qtable)
