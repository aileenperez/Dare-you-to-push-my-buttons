from ddqn import *
import numpy as np
import random


class Lights:
    def __init__(self):
        self.m = 5  # rows
        self.n = 20  # cols
        # self.limit = (self.m - 1) * self.n
        self.grid = np.zeros(shape=(self.m, self.n))
        # self.grid[self.m - 1, random.randrange(0, self.n)] = 1

    def is_terminal(self, row, col):
        if row == self.m - 2 and self.grid[row + 1, col] == 1:
            terminal = True
            for i1 in range(1, self.m - 2):
                if self.grid[row - i1, col] != 1:
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
            # print("move " + str(80 - self.limit))
            print(self.grid)
            # or self.limit < 1
        return self.grid.ravel(), reward, test, None


class LightRow:
    def __init__(self):
        self.m = 4  # rows
        # self.limit = self.m - 1
        self.grid = np.zeros(self.m)

    def is_terminal(self, action):
        if action == self.m - 1:
            terminal = True
            for i1 in range(1, self.m - 1):
                if self.grid[action - i1] != 1:
                    terminal = False
                    break
            return terminal
        return False

    def reset(self):
        self.grid = np.zeros(self.m)
        # self.limit = (self.m - 1) * self.n
        return self.grid

    def step(self, action):
        reward = -1
        # self.limit -= 1
        test = False
        if self.grid[action] != 1:
            test = self.is_terminal(action)
            if action == 0:
                self.grid[0] = 1
            elif self.grid[action - 1] == 1:
                self.grid[action] = 1
            if test:
                reward = 0
            '''print("move " + str(80 - self.limit))
            print(self.grid)'''
        return self.grid, reward, test, None


class LightCol:
    def __init__(self):
        self.n = 20  # cols
        # self.limit = (self.m - 1) * self.n
        self.grid = np.zeros(self.n)
        self.grid[random.randrange(0, self.n)] = 1

    def reset(self):
        self.grid = np.zeros(self.n)
        self.grid[random.randrange(0, self.n)] = 1
        # self.limit = (self.m - 1) * self.n
        return self.grid

    def step(self, action):
        reward = -1
        # self.limit -= 1
        if self.grid[action] == 1:
            reward = 0
            '''print("move " + str(80 - self.limit))
            print(self.grid)'''
        return self.grid, reward, reward == 0, None


def learn_row():
    env = LightRow()
    ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=4, epsilon=0.0, batch_size=64, input_dims=4,
                           fname='ddqn_model1.h5')
    n_games = 1
    ddqn_agent.load_model()
    ddqn_scores = []
    eps_history = []
    x1 = []
    actions = []
    for i4 in range(n_games):
        print("game " + str(i4))
        done = False
        score = 0
        observation = env.reset()
        while not done:
            action1 = ddqn_agent.choose_action(observation)
            observation_, reward1, done, info = env.step(action1)
            actions.append(action1)
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
        filename = 'light-row-ddqn.png'
        plot_learning(x1, avg_scores, eps_history, filename)
    return actions


def learn_col():
    env = LightCol()
    ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=20, epsilon=0.0, batch_size=64, input_dims=20,
                           fname='ddqn_model2.h5')
    n_games = 1
    ddqn_agent.load_model()
    ddqn_scores = []
    eps_history = []
    x1 = []
    actions = []
    for i4 in range(n_games):
        print("game " + str(i4))
        done = False
        score = 0
        observation = env.reset()
        while not done:
            action1 = ddqn_agent.choose_action(observation)
            observation_, reward1, done, info = env.step(action1)
            actions.append(action1)
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
        filename = 'light-col-ddqn.png'
        plot_learning(x1, avg_scores, eps_history, filename)
    loc = 0
    for i1 in range(env.n):
        if env.grid[i1] == 1:
            loc = i1
            break
    return actions, loc


def run_light(row_actions, col_actions, loc):
    env = Lights()
    env.grid[env.m - 1, loc] = 1
    done = False
    counter = 0
    while not done:
        action1 = 20 * row_actions[counter] + col_actions[counter]
        observation_, reward1, done, info = env.step(action1)
        counter += 1


if __name__ == '__main__':
    rows = learn_row()
    cols, loc = learn_col()
    print(rows)
    print(cols)
    # need to merge rows and cols
    '''r1 = [0] * (len(cols) - 1)
    if len(rows) > len(cols):
        for i in range(len(rows) - len(cols)):
            cols.append(cols[-1])
    elif len(rows) < len(cols):
        for i in range(len(cols) - len(rows)):
            rows.append(rows[-1])
    run_light(rows, cols, loc)'''
