from time import time, sleep

def ft_progress(lst):
    start_time = time()
    current_progress = 0
    final_progress = len(lst)

    for i in lst:
        yield i
        current_progress += 1
        passed_time = (time() - start_time)
        expected_time = (passed_time * (final_progress / current_progress))
        remaining_time = ((final_progress - current_progress) * passed_time / current_progress) if (expected_time - passed_time) < 0 else (expected_time - passed_time)
        bar_size = 20
        filled_size = int((bar_size * current_progress) / final_progress)
        filling_element = '='
        final_element = '>' if current_progress == current_progress else ''
        unfilled_element = ' '
        bar = filling_element * (filled_size - 1) + final_element + unfilled_element * (bar_size - filled_size)
        print(f"ETA: {remaining_time:.2f}s [{bar}] {current_progress}/{final_progress} | total time {passed_time:.2f}s", end='\r')
    print()


# Example 1
listy = range(1000)
ret = 0
for elem in ft_progress(list(listy)):
    ret += (elem + 3) % 5
    sleep(0.01)
print()

'''
# Example 2
listy = range(3333)
ret = 0
for elem in ft_progress(list(listy)):
    ret += elem
    sleep(0.005)
print()
print(ret)'''
