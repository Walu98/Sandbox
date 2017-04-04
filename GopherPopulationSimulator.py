
import random
print("Welcome to the Gopher Population Simulator!")
STARTING_POPULATION = 1000
total_population = 1000

print("Starting population:", STARTING_POPULATION,"\n")

year = 0
for year in range(10):
    STARTING_POPULATION = total_population
    gophers_born = round(random.uniform(0.10, 0.20) * 1000)# 10%
    gophers_died = round(random.uniform(0.05, 0.25) * 1000)
    total_population = STARTING_POPULATION + gophers_born - gophers_died
    print("Year",year+1,"\n*****")
    print("{} gophers were born. {} died\nPopulation:{}\n".format(gophers_born,gophers_died,total_population))



"""
print("Welcome to the Gopher Population Simulator!")
STARTING_POPULATION = 1000
gophers_born = 0.15 * 1000
gophers_died = 0.08 * 1000
print("Starting population:", STARTING_POPULATION,"\n")

year = 0
for year in range(10):
    total_population = STARTING_POPULATION - gophers_died
    print("Year",year+1,"\n*****")
    print("{} gophers were born. {} died\nPopulation:{}\n".format(gophers_born,gophers_died,total_population))

"""