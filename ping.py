import os
import subprocess
import argparse

from datetime import datetime

import matplotlib.pyplot as plt



def run_ping(host, count, output_file):
    with open(output_file, 'w') as file:
        subprocess.run(['ping', '-c', str(count), host], stdout=file, text=True)

def read_ping_file(filename):
    times = []
    with open(filename, 'r') as file:
        for line in file:
            if 'time=' in line:
                time_str = line.split('time=')[1].split(' ')[0]
                times.append(float(time_str))
    return times

def plot_ping_times(times, output_image):
    plt.figure(figsize=(10, 5))
    plt.plot(times, marker='o', linestyle='-')
    plt.title('Ping Response Time Over Time')
    plt.xlabel('Ping Sequence Number')
    plt.ylabel('Response Time (ms)')
    plt.grid(True)
    plt.savefig(output_image)
    print(f'Plot saved as {output_image}')

def main():
    parser = argparse.ArgumentParser(description='Ping a host and plot the response times.')
    parser.add_argument('host', type=str, help='The host to ping')
    parser.add_argument('-c', '--count', type=int, default=100, help='Number of ping requests to send (default: 100)')
    
    args = parser.parse_args()
    
    # Получаем текущую дату и время
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H:%M:%S")
    
    # Проверяем и создаем папку results, если она не существует
    os.makedirs('results', exist_ok=True)
    
    # Формируем имена файлов по умолчанию
    output_file = f'./results/ping-{args.host}-{timestamp}.txt'
    plot_file = f'./results/ping-{args.host}-{timestamp}.png'

    parser.add_argument('-o', '--output', type=str, default=output_file, help='File to save ping results')
    parser.add_argument('-p', '--plot', type=str, default=plot_file, help='File to save the plot')

    args = parser.parse_args()

    # Выполнить ping и сохранить результаты в файл
    run_ping(args.host, args.count, args.output)

    # Прочитать файл и получить времена отклика
    times = read_ping_file(args.output)

    # Построить график
    plot_ping_times(times, args.plot)

if __name__ == "__main__":
    main()
