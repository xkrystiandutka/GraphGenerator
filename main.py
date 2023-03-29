import matplotlib.pyplot as plt


class GraphGenerator:
    def __init__(self, file_path):
        self.file_path = file_path

    def plot_line(self, x_label='', y_label='', title=''):
        with open(self.file_path, encoding='utf-8-sig') as file:
            data = file.read().splitlines()
            x = [float(d.split(',')[0]) for d in data]
            y = [float(d.split(',')[1]) for d in data]
            plt.plot(x, y)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.show()

    def plot_bar(self, x_label='', y_label='', title=''):
        with open(self.file_path, encoding='utf-8-sig') as file:
            data = file.read().splitlines()
            x = [d.split(',')[0] for d in data]
            y = [float(d.split(',')[1]) for d in data]
            plt.bar(x, y)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.show()

    def pie_chart(self, title=''):
        with open(self.file_path, encoding='utf-8-sig') as file:
            data = file.read().splitlines()
            labels = [d.split(',')[0] for d in data]
            values = [float(d.split(',')[1]) for d in data]
            plt.pie(values, labels=labels)
            plt.title(title)
            plt.show()


def main():
    plot = GraphGenerator('data.csv')
    plot.plot_line(x_label='X-axis', y_label='Y-axis', title='Line Plot')
    plot.plot_bar(x_label='Categories', y_label='Values', title='Bar Chart')
    plot.pie_chart(title='Pie Chart')


if __name__ == '__main__':
    main()