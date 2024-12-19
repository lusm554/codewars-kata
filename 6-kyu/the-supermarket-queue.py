# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

def queue_time(customers, n):
  threads_exec_time = [0] * n         
  for c in customers:
    thread_i_with_lower_load = threads_exec_time.index(min(threads_exec_time))
    threads_exec_time[thread_i_with_lower_load] += c
  return max(threads_exec_time)
