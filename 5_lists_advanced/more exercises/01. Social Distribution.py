population_input = input().split(", ")
population = list(map(int, population_input))
min_wealth = int(input())

if sum(population) / len(population) < min_wealth:
    print('No equal distribution possible')
else:
    for i in range(len(population)):
        if population[i] < min_wealth:
            diff = abs(population[i] - min_wealth)
            population[i] += diff
            max_element = max(population)
            idx_max_element = population.index(max_element)
            population[idx_max_element] -= diff

    print(population)



