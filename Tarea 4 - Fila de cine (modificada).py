"""Companion code to https://realpython.com/simulation-with-simpy/

'Simulating Real-World Processes With SimPy'

Python version: 3.7.3
SimPy version: 3.0.11
"""

import random
import statistics
import numpy
import simpy
from math import inf as infinite

wait_times = []

class Theater(object):
    def __init__(self, env, num_cashiers, num_servers, num_ushers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.server = simpy.Resource(env, num_servers)
        self.usher = simpy.Resource(env, num_ushers)

    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1, 3))

    def check_ticket(self, moviegoer):
        yield self.env.timeout(3 / 60)

    def sell_food(self, moviegoer):
        yield self.env.timeout(random.randint(1, 5))


def go_to_movies(env, moviegoer, theater):
    # Moviegoer arrives at the theater
    arrival_time = env.now

    if random.random() < 0.1 :  # Probabilidad del 10% de que un cliente solo vaya a dulcería.
        with theater.server.request() as request:
            yield request
            yield env.process(theater.sell_food(moviegoer))

    else:
        with theater.cashier.request() as request:
            yield request
            yield env.process(theater.purchase_ticket(moviegoer))

        if random.choice([True, False]):
            with theater.server.request() as request:
                yield request
                yield env.process(theater.sell_food(moviegoer))

        with theater.usher.request() as request:
            yield request
            yield env.process(theater.check_ticket(moviegoer))

    # Moviegoer heads into the theater
    wait_times.append(env.now - arrival_time)


def run_theater(env, num_cashiers, num_servers, num_ushers):
    theater = Theater(env, num_cashiers, num_servers, num_ushers)

    for moviegoer in range(3):
        env.process(go_to_movies(env, moviegoer, theater))

    while True:
        yield env.timeout(numpy.random.exponential(1))  # Wait a bit before generating a new person

        moviegoer += 1
        env.process(go_to_movies(env, moviegoer, theater))


def get_average_wait_time(wait_times):
    average_wait = statistics.mean(wait_times)
    # Pretty print the results
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)

def get_user_input():
    num_cashiers = input("Input # of cashiers working: ")
    num_servers = input("Input # of servers working: ")
    num_ushers = input("Input # of ushers working: ")
    params = [num_cashiers, num_servers, num_ushers]
    if all(str(i).isdigit() for i in params):  # Check input is valid
        params = [int(x) for x in params]
    else:
        print(
            "Could not parse input. Simulation will use default values:",
            
            "\n1 cashier, 1 server, 1 usher.",
        )
        params = [1, 1, 1]
    return params


def main():
    # Setup
    random.seed(42)

    a = 4
    b = 4
    c = 1

    time_counter_2 = 0
    first = True

    end = True
    while end:
        #print(f"Cashiers: {a-1}")

        scenarios = []
        for i in range(a, a + 1):
            for j in range(b, b + 1):
                for k in range(c, c + 1):
                    scenarios.append({
                        "cashiers": i,
                        "servers": j,
                        "ushers": k,
                        "average_time": None
                    })

        for set in scenarios:
            num_cashiers = set["cashiers"]
            num_servers = set["servers"]
            num_ushers = set["ushers"]

            times = []
            for l in range(100):
                # Run the simulation
                env = simpy.Environment()
                env.process(run_theater(env, num_cashiers, num_servers, num_ushers))
                #print(
                #    "Running simulation...",
                #)
                env.run(until=240)
                times.append(statistics.mean(wait_times))
                wait_times.clear()
            
            #set["average_time"] =  statistics.mean(times)
            print(statistics.mean(times))

        #scenarios.reverse()

        resources_counter = 27
        time_counter = infinite
        target_scenario = None
        #for new_set in scenarios:
        #    if new_set["cashiers"] + new_set["servers"] + new_set["ushers"] < resources_counter and new_set["average_time"] < time_counter:
        #        resources_counter = new_set["cashiers"] + new_set["servers"] + new_set["ushers"]
        #        time_counter = new_set["average_time"]
        #        target_scenario = new_set
    
        #print(f"Escenario óptimo es: {target_scenario}")
    
        #if first:
        #    time_counter_2 = time_counter
        #    first = False
        #if time_counter < 5:
        #    time_counter_2 = time_counter
        #    a -= 1
        #if a == 2:
        #    end = False

if __name__ == "__main__":
        main()