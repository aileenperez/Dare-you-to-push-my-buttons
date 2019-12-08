from ddqn import *
import time
import numpy as np
import random


class Lights:
    def __init__(self):
        self.m = 5  # rows
        self.n = 20  # cols
        # self.limit = (self.m - 1) * self.n
        self.grid = np.zeros(shape=(self.m, self.n))
        self.grid[self.m - 1, random.randrange(0, self.n)] = 1

    def is_terminal(self, row, col):
        if row == self.m - 2 and self.grid[row + 1, col] == 1:
            terminal = True
            for i in range(1, self.m - 2):
                if self.grid[row - i, col] != 1:
                    terminal = False
                    break
            return terminal
        return False

    def reset(self):
        self.grid = np.zeros(shape=(self.m, self.n))
        self.grid[self.m - 1, random.randrange(0, self.n)] = 1
        # self.limit = (self.m - 1) * self.n
        return self.grid.ravel()

    def step(self, action):
        reward = -1
        # self.limit -= 1
        row = action // self.n
        col = action % self.n
        test = False
        if self.grid[row, col] != 1:
            test = self.is_terminal(row, col)
            if action < self.n:
                self.grid[row, col] = 1
            elif self.grid[row - 1, col] == 1:
                self.grid[row, col] = 1
            if test:
                reward = 0
            print()
            print(self.grid)
        return self.grid.ravel(), reward, test, None


if __name__ == '__main__':
    env = Lights()
    ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=80, epsilon=0.0, batch_size=64, input_dims=100,
                           fname='ddqn_model.h5')
    n_games = 1
    ddqn_agent.load_model()
    ddqn_scores = []
    eps_history = []
    x1 = []
    start = time.time()
    for i4 in range(n_games):
        print("game " + str(i4))
        done = False
        score = 0
        observation = env.reset()
        while not done:
            action1 = ddqn_agent.choose_action(observation)
            observation_, reward1, done, info = env.step(action1)
            score += reward1
            ddqn_agent.remember(observation, action1, reward1, observation_, int(done))
            observation = observation_
            ddqn_agent.learn()
        x1.append(i4 + 1)
        eps_history.append(ddqn_agent.epsilon)
        ddqn_scores.append(score)
        if i4 % 10 == 0 and i4 > 0:
            ddqn_agent.save_model()
    if n_games > 100:
        sum1 = 0
        for i4 in range(101):
            sum1 += ddqn_scores[i4]
        avg_scores = [sum1 / 101]
        for i4 in range(101, n_games):
            avg_scores.append(avg_scores[i4 - 101] + (ddqn_scores[i4] - ddqn_scores[i4 - 101]) / 101)
        del x1[:50]
        del x1[-50:]
        del eps_history[:50]
        del eps_history[-50:]
        filename = 'light-ddqn.png'
        plot_learning(x1, avg_scores, eps_history, filename)
    time = time.time() - start
    print("time: " + str(int(time // 60)) + " minutes and " + str(round(time % 60)) + " seconds")
    print("games per minute: " + str(round(60 * n_games / time)))
