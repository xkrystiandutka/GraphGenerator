# Plot Generator Prototype

The Plot Generator Prototype is a Python script that defines a class for generating line charts, bar charts, and pie charts using data from a text file.

## Getting Started

### Prerequisites

- Python 3.x
- Matplotlib

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/xkrystiandutka/GraphGenerator.git
    ```

2. Install Matplotlib:

    ```bash
    pip install matplotlib
    ```

### Usage

To use the Plot Generator Prototype, follow these steps:

1. Create an instance of the `PlotGeneratorPrototype` class:

    ```python
    plot_generator = PlotGeneratorPrototype()
    ```

2. Choose a data file using the `choose_file()` method:

    ```python
    plot_generator.choose_file()
    ```

3. Create a new object by copying the `plot_generator` instance:

    ```python
    line_plot_generator = plot_generator.clone()
    ```

4. Call the `plot_line()` method on the new object with specified parameters:

    ```python
    line_plot_generator.plot_line(x_label='X Label', y_label='Y Label', title='Line Chart')
    ```

5. Call the `save_current_plot()` method on the new object with a specified file title:

    ```python
    line_plot_generator.save_current_plot(title='line_chart')
    ```

6. Repeat steps 3-5 for the `plot_pie()` and `plot_bar()` methods:

    ```python
    pie_plot_generator = plot_generator.clone()
    pie_plot_generator.plot_pie(title='Pie Chart')
    pie_plot_generator.save_current_plot(title='pie_chart')

    bar_plot_generator = plot_generator.clone()
    bar_plot_generator.plot_bar(x_label='X Label', y_label='Y Label', title='Bar Chart')
    bar_plot_generator.save_current_plot(title='bar_chart')
    ```

### Contributors
This project was co-created by [Krystian Dutka](https://github.com/xkrystiandutka), [Weronika Przebięda](https://github.com/weronikaprzebieda) and [Jakub Bełtowski](https://github.com/JakBel). 

### License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/xkrystiandutka/GraphGenerator/blob/main/LICENSE) file for details.
