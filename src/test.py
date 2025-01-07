from EvolutionAlgorithm import EvolutionAlgorithm


def get_best_eval_func_factors():
    vertices = [(0, 0), (0, 10), (10, 10), (10, 0)]
    wares_data = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                  (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                  (2, 3), (4, 3), (3, 3)]
    test_values = {
        'high_fill_space1': [5, 3, 3, 2],
        'high_fill_space2': [5, 2, 2, 3],
        'high_fill_space3': [5, 3, 2, 3],
        'high_collisions1': [3, 5, 5, 2],
        'high_collisions2': [3, 5, 5, 4],
        'high_something_nearby1': [3, 2, 2, 4],
        'high_something_nearby2': [3, 4, 4, 4],
        'moderate1': [3, 3, 3, 3],
        'moderate2': [3, 2, 2, 3],
        'moderate3': [3, 2, 2, 2],
        'moderate4': [2, 3, 3, 3]
    }
    for key in test_values.keys():
        name = key
        eval_func_factors = test_values[key]
        algorithm = EvolutionAlgorithm(vertices=vertices,
                                      wares_data=wares_data,
                                      population_size=250,
                                      tournament_size=3,
                                      elite_size=1,
                                      mutation_rate=0.1,
                                      mutation_weights=[0.4, 0.4, 0.15, 0.05],
                                      crossover_rate=0.4,
                                      episodes=10,
                                      name=name,
                                      eval_func_factors=eval_func_factors
                                      )
        algorithm.run()

def check():
    vertices = [(0, 0), (0, 10), (10, 10), (10, 0)]
    wares_data = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                  (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                  (2, 3), (4, 3), (3, 3)]
    algorithm = EvolutionAlgorithm(vertices=vertices,
                                   wares_data=wares_data,
                                   population_size=250,
                                   tournament_size=3,
                                   elite_size=1,
                                   mutation_rate=0.1,
                                   mutation_weights=[0.4, 0.4, 0.15, 0.05],
                                   crossover_rate=0.4,
                                   episodes=50,
                                   name='moderate',
                                   eval_func_factors=[5, 2, 2, 3]
                                   )
    algorithm.run()





if __name__ == '__main__':
    check()