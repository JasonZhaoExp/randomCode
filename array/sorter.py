import os
import timeit

def load_sorting_algorithms():
    sorting_algorithms = []
    sorts_dir = "sorts"
    for filename in os.listdir(sorts_dir):
        if filename.endswith(".py"):
            filepath = os.path.join(sorts_dir, filename)
            algorithm = {}
            with open(filepath, "r") as file:
                exec(file.read(), algorithm)
            if "name" in algorithm and "sort" in algorithm:
                sorting_algorithms.append(algorithm)
            else:
                print(f"Invalid format in {filename}. Skipping this algorithm.")
    return sorting_algorithms

def time_sorting_algorithm(sort_func, array, repetitions):
    total_time = 0
    for _ in range(repetitions):
        start_time = timeit.default_timer()
        try:
            sorted_array = sort_func(array.copy())
        except Exception as e:
            print(f"Error occurred during sorting with algorithm '{sort_func.__name__}': {e}")
            return None
        end_time = timeit.default_timer()

        if sorted_array is None or sorted_array != sorted(array):
            print(f"Warning: Sorting algorithm '{sort_func.__name__}' did not return a sorted array.")
            return None

        total_time += end_time - start_time
    return total_time / repetitions

def main():
    sorting_algorithms = load_sorting_algorithms()

    if not sorting_algorithms:
        print("No valid sorting algorithms found in the 'sorts' folder.")
        return

    try:
        repetitions = int(input("Enter the number of times to repeat each sorting algorithm: "))
        if repetitions <= 0:
            print("Please enter a positive integer for repetitions.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    array_to_sort = [5, 2, 7, 1, 3, 8, 4, 9, 6]  # You can change this array as per your requirements

    print("\nAverage time taken for each sorting algorithm:")
    for algorithm in sorting_algorithms:
        algorithm_name = algorithm["name"]()
        sort_func = algorithm["sort"]
        average_time = time_sorting_algorithm(sort_func, array_to_sort, repetitions)

        if average_time is not None:
            print(f"{algorithm_name}: {average_time:.6f} seconds")
        else:
            print(f"{algorithm_name}: Error occurred during sorting.")

if __name__ == "__main__":
    main()
