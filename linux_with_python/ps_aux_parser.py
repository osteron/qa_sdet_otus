import subprocess
import datetime
from collections import defaultdict


def get_processes():
    encoding = 'utf-8'
    _output = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).stdout.readlines()
    headers = _output[0].decode(encoding).strip().split()
    raw_data = map(lambda s: s.decode(encoding).strip().split(maxsplit=len(headers) - 1), _output[1:])
    return [dict(zip(headers, r)) for r in raw_data]


def output(message, file):
    print(message)
    file.write(message + "\n")


def get_and_save_report(processes):
    unique_users = set()
    user_process = defaultdict(int)
    max_mem_value, max_mem_command = (-1, '')
    max_cpu_value, max_cpu_command = (-1, '')

    sum_mem = 0
    sum_cpu = 0

    for item in processes:
        user = item['USER']
        mem = float(item['%MEM'])
        cpu = float(item['%CPU'])
        command = item['COMMAND']

        unique_users.add(user)
        user_process[user] += 1
        sum_mem += mem
        sum_cpu += cpu

        if max_mem_value < mem:
            max_mem_value, max_mem_command = mem, command

        if max_cpu_value < cpu:
            max_cpu_value, max_cpu_command = cpu, command

    now = datetime.datetime.now()
    date_time_string = now.strftime("%d-%m-%Y-%H:%M")
    filename = f"{date_time_string}-scan.txt"

    with open(filename, "w") as file:
        output('Отчёт о состоянии системы:', file)
        output('Пользователи системы: ' + ', '.join(map(lambda u: f"'{u}'", unique_users)), file)
        output('Процессов запущено: ' + str(len(processes)), file)

        output('Пользовательских процессов: ', file)
        for user_name, process_count in user_process.items():
            output(f'{user_name}: {process_count}', file)

        output(f'Всего памяти используется: {sum_mem:.1f}%', file)
        output(f'Всего CPU используется: {sum_cpu:.1f}%', file)

        output('Больше всего памяти использует: ' + max_mem_command[:20], file)
        output('Больше всего CPU использует: ' + max_cpu_command[:20], file)


if __name__ == '__main__':
    get_and_save_report(get_processes())
