from EvolutionAlgorithm import EvolutionAlgorithm
from os import path, makedirs
import json
import matplotlib.pyplot as plt
import os

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
                                           episodes=75,
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


def test_parameters():
    vertices = [(0, 0), (0, 3), (5, 5), (5, 7), (0, 7), (0, 10), (12, 12), (12, 0)]
    wares_data = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                  (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                  (2, 3), (4, 3), (3, 3), (3, 3), (3, 3), (3, 3)]

    test_values = {
        'high_mutation_high_existance': [0.3, [0.4, 0.4, 0.2, 0.4], 0.4],
        'high_mutation_low_existance': [0.3, [0.4, 0.4, 0.2, 0.1], 0.4],
        'high_crossover': [0.1, [0.4, 0.4, 0.25, 0.15], 0.75],
        'high_crossover_high_mutation_high_existance': [0.3, [0.4, 0.4, 0.2, 0.4], 0.75],
        'high_crossover_high_mutation_low_existance': [0.3, [0.4, 0.4, 0.2, 0.1], 0.75],
    }


    for key in test_values.keys():
        for iteration in range(5):
            name = key
            mutation_rate = test_values[key][0]
            mutation_weights = test_values[key][1]
            crossover_rate = test_values[key][2]

            print(f'{name}: iteration {iteration}')

            algorithm = EvolutionAlgorithm(vertices=vertices,
                                           wares_data=wares_data,
                                           population_size=1500,
                                           tournament_size=3,
                                           elite_size=1,
                                           mutation_rate=mutation_rate,
                                           mutation_weights=mutation_weights,
                                           crossover_rate=crossover_rate,
                                           episodes=50,
                                           name=name,
                                           eval_func_factors=[5, 7, 4, 2],
                                           selection_func=EvolutionAlgorithm._roulette_selection,
                                           crossover_func=EvolutionAlgorithm.two_point_crossover
                                           )

            best_dict, avg_quality_dict = algorithm.run(verbose=True)

            results_directory = f'output/results_parameters/'
            if not path.exists(results_directory):
                makedirs(results_directory)

            best_dict_filename = path.join(results_directory, f"{name}_{iteration}_best_dict.json")
            avg_quality_dict_filename = path.join(results_directory, f"{name}_{iteration}_avg_quality_dict.json")

            with open(best_dict_filename, 'w') as best_file:
                json.dump(best_dict, best_file, indent=4)

            with open(avg_quality_dict_filename, 'w') as avg_quality_file:
                json.dump(avg_quality_dict, avg_quality_file, indent=4)

            print(f"Results for {name} have been saved")


def test_on_different_magazines():
    vertices1 = [(0, 0), (0, 3), (5, 5), (5, 7), (0, 7), (0, 10), (12, 12), (12, 0)]
    vertices2 = [(0, 0), (0, 10), (10, 10), (10, 0)]
    vertices3 = [(2, 0), (2, 2), (0, 2), (0, 5), (2, 5), (2, 8), (5, 8), (5, 5), (8, 5), (8, 2), (5, 2), (5, 0)]

    wares_data1 = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                  (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                  (2, 3), (4, 3), (3, 3), (3, 3), (3, 3), (3, 3)]

    wares_data2 = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                  (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                  (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                  (2, 3), (2, 3)
                  ]

    test_values = {
        'vertices1_wares1': (vertices1, wares_data1),
        'vertices2_wares1': (vertices2, wares_data1),
        'vertices3_wares1': (vertices3, wares_data1),
        'vertices1_wares2': (vertices1, wares_data2),
        'vertices2_wares2': (vertices2, wares_data2),
        'vertices3_wares2': (vertices3, wares_data2),
    }


    for key in test_values.keys():
        for iteration in range(5):
            name = key
            vertices = test_values[key][0]
            wares_data = test_values[key][1]
            print(f'{name}: iteration {iteration}')

            algorithm = EvolutionAlgorithm(vertices=vertices,
                                           wares_data=wares_data,
                                           population_size=3000,
                                           tournament_size=3,
                                           elite_size=1,
                                           mutation_rate=0.3,
                                           mutation_weights=[0.4, 0.4, 0.2, 0.4],
                                           crossover_rate=0.75,
                                           episodes=75,
                                           name=name,
                                           eval_func_factors=[5, 7, 4, 2],
                                           selection_func=EvolutionAlgorithm._roulette_selection,
                                           crossover_func=EvolutionAlgorithm.two_point_crossover
                                           )

            best_dict, avg_quality_dict = algorithm.run(verbose=True)

            results_directory = f'output/results_different_magazines/'
            if not path.exists(results_directory):
                makedirs(results_directory)

            best_dict_filename = path.join(results_directory, f"{name}_{iteration}_best_dict.json")
            avg_quality_dict_filename = path.join(results_directory, f"{name}_{iteration}_avg_quality_dict.json")

            with open(best_dict_filename, 'w') as best_file:
                json.dump(best_dict, best_file, indent=4)

            with open(avg_quality_dict_filename, 'w') as avg_quality_file:
                json.dump(avg_quality_dict, avg_quality_file, indent=4)

            print(f"Results for {name} have been saved")

def plot_results():
    results_directory = 'output/results_parameters/'

    if not os.path.exists(results_directory):
        print(f"Directory {results_directory} does not exist. Run the test first.")
        return

    all_best_scores = {}
    all_avg_qualities = {}

    for filename in os.listdir(results_directory):
        if filename.endswith("_best_dict.json"):
            method_name = '_'.join(filename.split("_")[:-3])
            with open(os.path.join(results_directory, filename), 'r') as f:
                best_dict = json.load(f)
            if method_name not in all_best_scores:
                all_best_scores[method_name] = []
            all_best_scores[method_name].append(best_dict)

        elif filename.endswith("_avg_quality_dict.json"):
            method_name = '_'.join(filename.split("_")[:-4])
            with open(os.path.join(results_directory, filename), 'r') as f:
                avg_quality_dict = json.load(f)
            if method_name not in all_avg_qualities:
                all_avg_qualities[method_name] = []
            all_avg_qualities[method_name].append(avg_quality_dict)

    max_episodes = max(
        max(int(k) for k in run.keys())
        for method_runs in all_best_scores.values()
        for run in method_runs
    )

    plt.figure(figsize=(12, 6))
    for method_name, runs in all_best_scores.items():
        avg_best_scores = []
        for ep in range(max_episodes + 1):
            ep_scores = []
            for run in runs:
                keys = sorted(int(k) for k in run.keys())
                if ep <= keys[-1]:
                    ep_scores.append(run.get(str(ep), 0))
                else:
                    ep_scores.append(run.get(str(keys[-1]), 0))
            avg_best_scores.append(sum(ep_scores) / len(ep_scores))

        plt.plot(range(max_episodes + 1), avg_best_scores, label=f"{method_name} (best score)")

    plt.title("Average Best Scores Across Methods")
    plt.xlabel("Episode")
    plt.ylabel("Average Best Score")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(results_directory, "avg_best_scores_comparison.png"))
    plt.close()

    plt.figure(figsize=(12, 6))
    for method_name, runs in all_avg_qualities.items():
        avg_qualities = []
        for ep in range(max_episodes + 1):
            ep_scores = []
            for run in runs:
                keys = sorted(int(k) for k in run.keys())
                if ep <= keys[-1]:
                    ep_scores.append(run.get(str(ep), 0))
                else:
                    ep_scores.append(run.get(str(keys[-1]), 0))
            avg_qualities.append(sum(ep_scores) / len(ep_scores))

        plt.plot(range(max_episodes + 1), avg_qualities, label=f"{method_name} (avg quality)")

    plt.title("Average Population Quality Across Methods")
    plt.xlabel("Episode")
    plt.ylabel("Average Population Quality")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(results_directory, "avg_quality_comparison.png"))
    plt.close()

    print("Plots have been saved to the results directory.")



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
                                   episodes=1,
                                   name='moderate',
                                   eval_func_factors=[5, 2, 2, 3]
                                   )
    algorithm.run()


if __name__ == '__main__':
    test_on_different_magazines()
