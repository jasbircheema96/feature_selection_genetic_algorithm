import constant
import time
from generation import next_generation
from generation import best_individual
from generation import average_fitness
from fitness import compute_fitness
def main():
    prev_gen=None
    average_file = open("average.txt", "a")
    best_file=open("best.txt","a")
    features_file=open("features.txt","a")
    time_file=open("time.txt","a")
    start_time=time.time()
    for i in range(constant.num_iterations):
        # print start time for a generation
        next_gen=next_generation(prev_gen)
        compute_fitness(next_gen)
        print("best individual's fitness in "+str(i)+ "th generation : " + str(best_individual(next_gen).fitness))
        best_file.write(str(best_individual(next_gen).fitness)+"\n")
        print(str(best_individual(next_gen).features))
        features_file.write(str(best_individual(next_gen).features)+"\n")
        print("Average generation's fitness "+str(average_fitness(next_gen)))
        average_file.write(str(average_fitness(next_gen))+"\n")
        prev_gen=next_gen
        end_time=time.time()
        time_interval=end_time-start_time
        print(time_interval)
        time_file.write(str(time_interval)+"\n")
        # print end time for generation and compute the time taken by that generation
    average_file.close()
    best_file.close()
    features_file.close()
if __name__ == "__main__":
    main()