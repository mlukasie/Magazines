from EvolutionAlgorithm import EvolutionAlgorithm


def check_algorithm():
    #vertices = [(1, 1), (1, 4), (0, 4), (0, 5), (5, 5), (5, 1)]
    vertices = [(1, 1), (1, 4), (0, 4), (0, 20), (20, 20), (20, 1)]
    wares_data = [(2, 4), (8, 2), (1, 2), (3, 2), (1, 2), (5, 2), (4, 4), (6, 2), (1, 2), (3, 2), (5, 2), (4, 4), (6, 2),
                  (2, 4), (3, 4), (1, 2), (1, 2), (1, 2), (1, 2), (1, 1), (1, 2), (1, 3), (3, 2), (5, 2), (4, 4), (1, 4)]
    # wares_data = [(1, 2), (1, 3), (1, 4)]
    Algoritm = EvolutionAlgorithm(vertices=vertices,
                                  wares_data=wares_data,
                                  population_size=1000,
                                  tournament_size=3,
                                  elite_size=1,
                                  mutation_rate=0.1,
                                  mutation_weights=[0.35, 0.35, 0.25, 0.05],
                                  crossover_rate=0.4,
                                  episodes=50
                                  )
    Algoritm.run()




if __name__ == '__main__':
    check_algorithm()