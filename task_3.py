import timeit
from pathlib import Path

from helpers.bmh import boyer_moore_search

# Import algorithmic search functions
from helpers.kmp import kmp_search
from helpers.rk import rabin_karp_search

# Log messages
from helpers.templates import (
    fastest_result,
    mgs_FileNotFound,
    mgs_WrongEncoding,
    output_head,
)

# Path to test files
path_text_1 = Path.cwd().joinpath("data/article_1.txt")
path_text_2 = Path.cwd().joinpath("data/article_2.txt")

pattern_result = "Література"
pattern_no_result = "Помʼятий"

results = {
    "kmp_search": 0,
    "boyer_moore_search": 0,
    "rabin_karp_search": 0,
}


if __name__ == "__main__":
    try:
        # Testing the performance of search algorithms. Approach 1
        with open(path_text_1, "r", encoding="utf-8") as file_path:
            test_text_1 = file_path.read()

        for key in results.keys():
            execution_time = timeit.timeit(
                f"{key}(test_text_1, pattern_result)", globals=globals(), number=100
            )
            results[key] = round(execution_time, 5)

        fastest_algorithm_1, fastest_time_1 = min(results.items(), key=lambda x: x[1])

        benchmark_res_1 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results.items()
        )

        print("APPROACH 1", end="\n")
        print(output_head, benchmark_res_1, end="\n")
        print(fastest_result.format(fastest_algorithm_1, fastest_time_1))

        for key in results.keys():
            execution_time = timeit.timeit(
                f"{key}(test_text_1, pattern_no_result)", globals=globals(), number=100
            )
            results[key] = round(execution_time, 5)

        fastest_algorithm_1, fastest_time_1 = min(results.items(), key=lambda x: x[1])

        benchmark_res_1 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results.items()
        )

        print(output_head, benchmark_res_1, end="\n")
        print(fastest_result.format(fastest_algorithm_1, fastest_time_1))

        # Testing the performance of search algorithms. Approach 2
        with open(path_text_2, "r", encoding="utf-8") as file_path:
            test_text_2 = file_path.read()

        for key in results.keys():
            execution_time = timeit.timeit(
                f"{key}(test_text_2, pattern_result)", globals=globals(), number=100
            )
            results[key] = round(execution_time, 5)

        fastest_algorithm_2, fastest_time_2 = min(results.items(), key=lambda x: x[1])

        benchmark_res_2 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results.items()
        )

        print("APPROACH 2", end="\n")
        print(output_head, benchmark_res_2, end="\n")
        print(fastest_result.format(fastest_algorithm_2, fastest_time_2))

        for key in results.keys():
            execution_time = timeit.timeit(
                f"{key}(test_text_2, pattern_no_result)", globals=globals(), number=100
            )
            results[key] = round(execution_time, 5)

        fastest_algorithm_2, fastest_time_2 = min(results.items(), key=lambda x: x[1])

        benchmark_res_2 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results.items()
        )

        print(output_head, benchmark_res_2, end="\n")
        print(fastest_result.format(fastest_algorithm_2, fastest_time_2))

    except FileNotFoundError as error:
        print(mgs_FileNotFound.format(type(error).__name__))
    except UnicodeDecodeError as error:
        print(mgs_WrongEncoding.format(type(error).__name__))
