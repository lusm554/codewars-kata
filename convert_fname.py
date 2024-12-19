#!/usr/bin/env python3
import sys
#task_name = input('Enter task name: ')
task_name = ' '.join(sys.argv[1:])
task_name = task_name.replace('.', '')
task_name = task_name.replace('!', '')
task_name = task_name.replace(',', '')
task_name = task_name.replace(':', '')
task_name = task_name.replace('_', ' ')
task_name = '-'.join(task_name.split(' '))
task_name += '.py'
task_name = task_name.lower()
print(task_name)
