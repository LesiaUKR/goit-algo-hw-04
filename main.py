import timeit
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort


if __name__ == "__main__":
    # Генерація тестових даних
   data_small = [random.randint(0, 1_000) for _ in range(100)]
   data_medium = [random.randint(0, 10_000) for _ in range(1_000)]
   data_large = [random.randint(0, 100_000) for _ in range(10_000)]
   
   # Тестування алгоритмів на малих масивах
   ts_insertion = timeit.timeit(lambda: insertion_sort(data_small), number=3)
   ts_merge = timeit.timeit(lambda: merge_sort(data_small), number=3)
   ts_timsorted = timeit.timeit(lambda: sorted(data_small[:]), number=3)
   ts_timsort = timeit.timeit(lambda: data_small[:].sort(), number=3)

   # Тестування алгоритмів на середніх масивах
   tm_insertion = timeit.timeit(lambda: insertion_sort(data_medium), number=3)
   tm_merge = timeit.timeit(lambda: merge_sort(data_medium), number=3)
   tm_timsorted = timeit.timeit(lambda: sorted(data_medium[:]), number=3)
   tm_timsort = timeit.timeit(lambda: data_medium[:].sort(), number=3)
 
   # Тестування алгоритмів на великих масивах
   tl_insertion = timeit.timeit(lambda: insertion_sort(data_large), number=1)
   tl_merge = timeit.timeit(lambda: merge_sort(data_large), number=1)
   tl_timsorted = timeit.timeit(lambda: sorted(data_large[:]), number=1)
   tl_timsort = timeit.timeit(lambda: data_large[:].sort(), number=1)
   
    # Вивід результатів тестування
   print(f"| {'Algorithm':<20} | {'Small':<20} | {'Medium':<20} | {'Large':<20} |")
   print(f"| {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")
   print(f"| {'Insertion Sort':<20} | {ts_insertion:20.5f} | {tm_insertion:20.5f} | {tl_insertion:20.5f} |")
   print(f"| {'Merge Sort':<20} | {ts_merge:20.5f} | {tm_merge:20.5f} | {tl_merge:20.5f} |")
   print(f"| {'Timsort (sorted)':<20} | {ts_timsorted:20.5f} | {tm_timsorted:20.5f} | {tl_timsorted:20.5f} |")
   print(f"| {'Timsort (sort)':<20} | {ts_timsort:20.5f} | {tm_timsort:20.5f} | {tl_timsort:20.5f} |")

   
