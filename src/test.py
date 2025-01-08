from EvolutionAlgorithm import EvolutionAlgorithm
from os import path, makedirs
import json

def get_best_eval_func_factors():
    vertices = [(0, 0), (0, 3), (5, 5), (5, 7), (0, 7), (0, 10), (12, 12), (12, 0)]
    wares_data = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                  (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                  (2, 3), (4, 3), (3, 3), (3, 3), (3, 3), (3, 3)]
    test_values = {
        'test1': [5, 7, 3, 2],
        'test2': [5, 7, 3, 3],
        'test3': [5, 7, 5, 3],
        'test4': [5, 10, 5, 3],
        'test5': [5, 7, 2, 2],
        'test6': [5, 10, 2, 2],
        'test7': [5, 7, 4, 2],
        'test8': [5, 10, 4, 2],
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


def test_best_eval_func_factors():
    vertices = [(0, 0), (0, 3), (5, 5), (5, 7), (0, 7), (0, 10), (12, 12), (12, 0)]
    wares_data = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                  (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                  (2, 3), (4, 3), (3, 3), (3, 3), (3, 3), (3, 3)]
    test_values = {
        'test17': [5, 7, 4, 2],
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
                                       eval_func_factors=eval_func_factors,
                                       selection_func=EvolutionAlgorithm._tournament_selection,
                                       crossover_func=EvolutionAlgorithm.two_point_crossover
                                       )
        algorithm.run()


def test_crossover_selection_methods():
    vertices = [(0, 0), (0, 3), (5, 5), (5, 7), (0, 7), (0, 10), (12, 12), (12, 0)]
    wares_data = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                  (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                  (2, 3), (4, 3), (3, 3), (3, 3), (3, 3), (3, 3)]

    test_values = {
        'tournament_two_point': (EvolutionAlgorithm._tournament_selection, EvolutionAlgorithm.two_point_crossover),
        'tournament_single_point': (EvolutionAlgorithm._tournament_selection, EvolutionAlgorithm.single_point_crossover),
        'roulette_two_point': (EvolutionAlgorithm._roulette_selection, EvolutionAlgorithm.two_point_crossover),
        'roulette_single_point': (EvolutionAlgorithm._roulette_selection, EvolutionAlgorithm.single_point_crossover),
    }


    for key in test_values.keys():
        for iteration in range(5):
            name = key
            selection_func = test_values[key][0]
            crossover_func = test_values[key][1]

            print(f'{name}: iteration {iteration}')

            algorithm = EvolutionAlgorithm(vertices=vertices,
                                           wares_data=wares_data,
                                           population_size=1500,
                                           tournament_size=3,
                                           elite_size=1,
                                           mutation_rate=0.1,
                                           mutation_weights=[0.4, 0.4, 0.1, 0.2],
                                           crossover_rate=0.4,
                                           episodes=50,
                                           name=name,
                                           eval_func_factors=[5, 7, 4, 2],
                                           selection_func=selection_func,
                                           crossover_func=crossover_func
                                           )

            best_dict, avg_quality_dict = algorithm.run(verbose=True)

            results_directory = f'output/results/'
            if not path.exists(results_directory):
                makedirs(results_directory)

            best_dict_filename = path.join(results_directory, f"{name}_{iteration}_best_dict.json")
            avg_quality_dict_filename = path.join(results_directory, f"{name}_{iteration}_avg_quality_dict.json")

            with open(best_dict_filename, 'w') as best_file:
                json.dump(best_dict, best_file, indent=4)

            with open(avg_quality_dict_filename, 'w') as avg_quality_file:
                json.dump(avg_quality_dict, avg_quality_file, indent=4)

            print(f"Results for {name} have been saved")


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
    test_crossover_selection_methods()
