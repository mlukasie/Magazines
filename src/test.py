from EvolutionAlgorithm import EvolutionAlgorithm


def get_best_eval_func_factors():
    vertices = [(0, 0), (0, 3), (5, 5), (5, 7), (0, 7), (0, 10), (12, 12), (12, 0)]
    wares_data = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                  (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                  (2, 3), (4, 3), (3, 3), (3, 3), (3, 3), (3, 3)]
    test_values = {
        # 'test11': [5, 7, 3, 2],
        # 'test12': [5, 7, 3, 3],
        # 'test13': [5, 7, 5, 3],
        # 'test14': [5, 10, 5, 3],
        # 'test15': [5, 7, 2, 2],
        # 'test16': [5, 10, 2, 2],
        'test17': [5, 7, 4, 2]
    #   'test18': [5, 10, 4, 2],
    }
    for key in test_values.keys():
        name = key
        eval_func_factors = test_values[key]
        algorithm = EvolutionAlgorithm(vertices=vertices,
                                      wares_data=wares_data,
                                      population_size=3000,
                                      tournament_size=3,
                                      elite_size=1,
                                      mutation_rate=0.1,
                                      mutation_weights=[0.4, 0.4, 0.1, 0.2],
                                      crossover_rate=0.4,
                                      episodes=100,
                                      name=name,
                                      eval_func_factors=eval_func_factors
                                      )
        algorithm.run()

def check():
    vertices = [(0, 0), (0, 3), (5, 5), (5, 7), (0, 7), (0, 10), (12, 12), (12, 0)]
    wares_data = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (9, 9)]
    algorithm = EvolutionAlgorithm(vertices=vertices,
                                   wares_data=wares_data,
                                   population_size=1000,
                                   tournament_size=3,
                                   elite_size=1,
                                   mutation_rate=0.1,
                                   mutation_weights=[0.4, 0.4, 0.2, 0.2],
                                   crossover_rate=0.4,
                                   episodes=50,
                                   name='moderate',
                                   eval_func_factors=[5, 2, 2, 3]
                                   )
    algorithm.run()





if __name__ == '__main__':
    get_best_eval_func_factors()