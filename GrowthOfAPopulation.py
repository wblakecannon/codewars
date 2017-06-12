def nb_year(p0, percent, aug, p):
    pop_list = []
    conv_percent = percent / 100.0
    population = p0 + p0 * conv_percent + aug
    pop_list.append(population)
    while population < p:
        population = population + population * conv_percent + aug
        pop_list.append(population)
        if population >= p:
            break
    print pop_list
    return len(pop_list)

print nb_year(1000, 2, 50, 1200)
