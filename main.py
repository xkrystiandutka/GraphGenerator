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
        """
            Choose a file using a file dialog. Only text files with the .txt extension are allowed.
            Sets the 'file_path' attribute to the chosen file path.
        """
        root = tk.Tk()
        root.withdraw()
        self.file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])

    def plot_line(self, x_label='', y_label='', title=''):
        """
            Plot a line chart using data from the input file.
            :param x_label: label for the x-axis
            :param y_label: label for the y-axis
            :param title: title of the chart
            :return: False if the input file is not selected or the data is invalid, True otherwise
        """
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
        """
            Plot a bar chart using data from the input file.
            :param x_label: label for the x-axis
            :param y_label: label for the y-axis
            :param title: title of the chart
            :return: False if the input file is not selected or the data is invalid, True otherwise
        """
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
        """
            Plot a pie chart using data from the input file.
            :param title: title of the chart
            :return: False if the input file is not selected or the data is invalid, True otherwise
        """
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
            self.current_plot = plt.gcf()

    @staticmethod
    def _validate_data(data):
        """
        Validates the input data for a plotting function. It checks if the data contains at least two lines, if each
        line contains at least one comma-separated value, and if all values can be converted to floats. Prints error
        messages and returns False if any of these conditions are not met. Returns True otherwise.
        :param data: a list of strings representing the input data
        :return: True if the input data is valid, False otherwise
        """
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

    @staticmethod
    def _validate_file_extension(file_path):
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
        """
            Save the current plot to a file with the given title.
            If the current plot is None, print an error message and return.
            The plot is saved in a subdirectory 'plots' with the format 'title.png'.
            :param title: title of the saved file
        """
        if self.current_plot is None:
            print('Error: no chart to save')
            return
        if not os.path.exists('plots'):
            os.makedirs('plots')
        file_path = os.path.join('plots', f'{title}.png')
        self.current_plot.savefig(file_path, bbox_inches='tight')
        print(f'The chart was saved as a file {file_path}')

    def clone(self):
        """
            Create a deep copy of the object.
            :return: a new instance of the PlotGeneratorPrototype class with the same attributes
        """
        return copy.deepcopy(self)


def main():
    """
    The main function demonstrates the prototype design pattern using a PlotGeneratorPrototype class. It creates an
    instance of the class, allows the user to select a data file, clones the object to create new objects for line
    plot, pie chart, and bar plot generation, customizes each plot with specific parameters, and saves each plot with
    a corresponding file name.
    """
    plot_generator = PlotGeneratorPrototype()
    plot_generator.choose_file()
    line_plot_generator = plot_generator.clone()
    line_plot_generator.plot_line(x_label='X Label', y_label='Y Label', title='Line Plot')
    line_plot_generator.save_current_plot('Line Plot')

    pie_plot_generator = plot_generator.clone()  # Copy the object and change the parameters
    pie_plot_generator.plot_pie(title='Pie Chart')
    pie_plot_generator.save_current_plot('Pie Chart')

    bar_plot_generator = plot_generator.clone()  # Copy the object and change the parameters
    bar_plot_generator.plot_bar(x_label='X Label', y_label='Y Label', title='Bar Plot')
    bar_plot_generator.save_current_plot('Bar Plot')


if __name__ == '__main__':
    main()
