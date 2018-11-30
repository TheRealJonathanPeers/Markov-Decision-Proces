import numpy as np


class MDP(object):
    def __init__(self, n_states, n_actions, discount):
        self.__n_states = n_states
        self.__n_actions = n_actions
        self.__r = np.array([[[.0 for _ in range(n_states)] for _ in range(n_actions)] for _ in range(n_states)])
        self.__nsa = np.array([[0 for _ in range(n_actions)] for _ in range(n_states)])
        self.__ntsa = np.array([[[0 for _ in range(n_states)] for _ in range(n_actions)] for _ in range(n_states)])
        self.__ptsa = np.array([[[.0 for _ in range(n_states)] for _ in range(n_actions)] for _ in range(n_states)])
        self.__discount = discount

    @property
    def n_states(self):
        return self.__n_states

    @property
    def n_actions(self):
        return self.__n_actions

    @property
    def r(self):
        return self.__r

    @property
    def nsa(self):
        return self.__nsa

    @property
    def ntsa(self):
        return self.__ntsa

    @property
    def ptsa(self):
        return self.__ptsa

    @property
    def discount(self):
        return self.__discount

    def update(self, percept):
        s = percept.cur_state
        a = percept.action
        ss = percept.next_state

        self.r[s][a][ss] = percept.reward
        self.nsa[s][a] += 1
        self.ntsa[s][a][ss] += 1
        self.ptsa[s][a][ss] = 1.0 * self.ntsa[s][a][ss] / self.nsa[s][a]

    def __str__(self):
        f = '| {0:>2} | {1:>2} | {2:>2} | {3:>4.4} | {4:>4.4} |\n'
        output = f.format('S', 'A', 'S\'', 'P', 'R')
        output += f.format('=', '=', '=', '=', '=').replace(' ', '=')

        s = 0
        for states in self.ptsa:
            a = 0
            for actions in states:
                ss = 0
                for probability in actions:
                    if probability > 0:
                        output += f.format(str(s), str(a), str(ss), str(probability), str(self.r[s][a][ss]))
                    ss += 1
                a += 1
            s += 1
        return output
