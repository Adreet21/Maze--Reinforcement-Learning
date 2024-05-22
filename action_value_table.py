import numpy as np

class ActionValueTable():
    def __init__(self, dimension, num_actions):
        table_size = dimension + [num_actions]
        self.table = np.zeros(table_size)


    def get_index(self, state, action):
        '''
        Returns an index for self.table given a state and action
        '''
        index_list = [[state[i]] for i in range(len(state))]
        index_list.append([action])
        idx = np.ix_(*index_list)
        return idx


    def get_value(self, state, action):
        '''
        Returns the value for a (state, action) pair
        '''
        idx = self.get_index(state, action)
        return self.table[idx]


    def set_value(self, state, action, new_value):
        '''
        Set the value for a (state, action) pair to new_value
        '''
        idx = self.get_index(state, action)
        self.table[idx] = new_value
