from Magazine import Magazine


def check_magazine():
    vertices = [(1, 1), (1, 4), (0, 4), (0, 20), (20, 20), (20, 1)]
    wares_data = [(1, 7), (8, 2), (1, 2), (1, 2), (3, 2), (5, 2), (4, 4), (6, 2), (1, 2), (3, 2), (5, 2), (4, 4), (6, 2)]
    magazine = Magazine(vertices=vertices)
    wares = magazine.generate_magazine_wares(wares_data=wares_data)
    for ware in wares:
        print(str(ware))
    new_matrix, collisions, wall_collisions = magazine.fill_magazine_with_wares(wares=wares)
    Magazine.show_magazine(magazine.matrix)
    print(f'Wall collisions: {wall_collisions}, collisions: {collisions}')
    Magazine.show_magazine(new_matrix, wares)


if __name__ == '__main__':
    check_magazine()