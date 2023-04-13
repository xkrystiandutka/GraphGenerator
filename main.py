import copy
import tkinter as tk
from tkinter import filedialog
import os
import matplotlib.pyplot as plt


class PlotGeneratorPrototype:
    def __init__(self):
        self.file_path = None
        self.current_plot = None

    def choose_file(self):
        root = tk.Tk()
        root.withdraw()
        self.file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])

    def plot_line(self, x_label='', y_label='', title=''):
        if not self.file_path:
            print('Error: select file')
            return False
        with open(self.file_path) as file:
            data = file.read().splitlines()
            if not self._validate_data(data):
                return False
            if data[0].startswith('xlabel:'):
                x_label = data[0].split(':')[1]
                data = data[1:]
            x = [float(d.split(',')[0]) for d in data]
            y = [float(d.split(',')[1]) for d in data]
            plt.plot(x, y)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            self.current_plot = plt.gcf()

    def plot_bar(self, x_label='', y_label='', title=''):
        if not self.file_path:
            print('Error: select file')
            return False
        with open(self.file_path) as file:
            data = file.read().splitlines()
            if not self._validate_data(data):
                return False
            if data[0].startswith('xlabel:'):
                x_label = data[0].split(':')[1]
                data = data[1:]
            x = [d.split(',')[0] for d in data]
            y = [float(d.split(',')[1]) for d in data]
            fig, ax = plt.subplots()
            ax.bar(x, y)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.xticks(x, x)
            self.current_plot = fig

    def plot_pie(self, title=''):
        if not self.file_path:
            print('Error: select file')
            return False
        with open(self.file_path) as file:
            data = file.read().splitlines()
            if not self._validate_data(data):
                return False
            labels = [d.split(',')[0] for d in data]
            values = [float(d.split(',')[1]) for d in data]
            plt.pie(values, labels=labels)
            plt.title(title)


    def _validate_data(self, data):
        if len(data) < 2:
            print('Error: input file should contain at least 2 lines')
            return False
        if not all(',' in d for d in data):
            print('Error: each line of the input file should contain at least one value separated by a comma')
            return False
        try:
            for d in data:
                x, y = d.split(',')
                float(x)
                float(y)
        except ValueError:
            print('Error: values in input file should be numbers')
            return False
        return True


    def _validate_file_extension(self, file_path):
        """
        Validate the file extension of the input file. Only text files with the .txt extension are allowed.
        :param file_path: path to the input file
        :return: True if the file extension is valid, False otherwise
        """
        if not file_path.endswith('.txt'):
            print('Error: a file with an invalid extension was selected. The allowed file extension is .txt')
            return False
        return True

    def save_current_plot(self, title):
        if self.current_plot is None:
            print('Error: no chart to save')
            return
        if not os.path.exists('plots'):
            os.makedirs('plots')
        file_path = os.path.join('plots', f'{title}.png')
        self.current_plot.savefig(file_path, bbox_inches='tight')
        print(f'The chart was saved as a file {file_path}')

    def clone(self):
        return copy.deepcopy(self)

# Tworzymy nowy obiekt klasy PlotGeneratorPrototype
plot_generator = PlotGeneratorPrototype()
plot_generator.choose_file()

# Kopiujemy obiekt i zmieniamy parametry
line_plot_generator = plot_generator.clone()
line_plot_generator.plot_line(x_label='X Label', y_label='Y Label', title='Line Plot')
line_plot_generator.save_current_plot('Line Plot')

# Kopiujemy obiekt i zmieniamy parametry
bar_plot_generator = plot_generator.clone()
bar_plot_generator.plot_bar(x_label='X Label', y_label='Y Label', title='Bar Plot')
bar_plot_generator.save_current_plot('Bar Plot')

# Kopiujemy obiekt i zmieniamy parametry
pie_plot_generator = plot_generator.clone()
pie_plot_generator.plot_pie(title='Pie Chart')
pie_plot_generator.save_current_plot('Pie Chart')

