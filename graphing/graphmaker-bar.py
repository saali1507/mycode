#!usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# data from United Nations World Population Prospects (Revision 2019)
# https://population.un.org/wpp/, license: CC BY 3.0 IGO
year = [1970, 1980, 1990, 2000, 2010, 2018]
population_by_animal = {
    'panda': [1000, 1000, 1200, 1596, 1600, 1800],
    'whooping crane': [56, 76, 146, 177, 281, 400],
    'siberian tiger': [50, 50, 100, 75, 200, 400],
}

fig, ax = plt.subplots()
ax.stackplot(year, population_by_animal.values(),
             labels=population_by_animal.keys(), alpha=0.8)
ax.legend(loc='upper left')
ax.set_title('Animal population')
ax.set_xlabel('Year')
ax.set_ylabel('Number of animals')

plt.savefig("/home/student/static/pizzaparty.png")
