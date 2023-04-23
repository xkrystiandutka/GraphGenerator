import os
import unittest
from unittest.mock import patch
import matplotlib.pyplot as plt
from main import PlotGeneratorPrototype


class TestPlotGeneratorPrototype(unittest.TestCase):

    def setUp(self):
        self.plot_generator = PlotGeneratorPrototype()

    def test_validate_data(self):
        # Test validating correct data
        valid_data = ['1,2', '2,4', '3,6']
        self.assertTrue(self.plot_generator._validate_data(valid_data))

        # Test validating incorrect data with less than two lines
        invalid_data = ['1,2']
        self.assertFalse(self.plot_generator._validate_data(invalid_data))

        # Test validating incorrect data with a line that does not contain a comma-separated values
        invalid_data = ['1,2', '34']
        self.assertFalse(self.plot_generator._validate_data(invalid_data))

        # Test validating incorrect data with a line that contains non-numeric values
        invalid_data = ['1,2', '3,abc']
        self.assertFalse(self.plot_generator._validate_data(invalid_data))

    def test_validate_file_extension(self):
        # Test validating correct extension
        valid_extension = 'test.txt'
        self.assertTrue(self.plot_generator._validate_file_extension(valid_extension))

        # Test validating file with .xlsx extension
        invalid_extension = 'test.xlsx'
        self.assertFalse(self.plot_generator._validate_file_extension(invalid_extension))

        # Test validating file with non-existing extension that starts with .txt
        invalid_extension = 'test.txt.xlsx'
        self.assertFalse(self.plot_generator._validate_file_extension(invalid_extension))

    def test_plot_line(self):
        # Test plotting a line chart
        self.plot_generator.file_path = 'data/data1.txt'
        self.plot_generator.plot_line(x_label='X', y_label='Y', title='Line Chart')
        self.assertIsNotNone(self.plot_generator.current_plot)

        # Test when input file is not selected
        self.plot_generator.current_plot.clf()
        self.plot_generator.file_path = None
        self.assertFalse(self.plot_generator.plot_line())

        # Test when data in input file is invalid
        self.plot_generator.current_plot.clf()
        self.plot_generator.file_path = 'data/data3wrongfile.txt'
        self.assertFalse(self.plot_generator.plot_line())

    def test_plot_bar(self):
        # Test plotting a bar chart
        self.plot_generator.file_path = 'data/data1.txt'
        self.plot_generator.plot_bar(x_label='X', y_label='Y', title='Bar Chart')
        self.assertIsNotNone(self.plot_generator.current_plot)

        # Test when input file is not selected
        self.plot_generator.file_path = None
        self.assertFalse(self.plot_generator.plot_bar())

        # Test when data in input file is invalid
        self.plot_generator.file_path = 'data/data3wrongfile.txt'
        self.assertFalse(self.plot_generator.plot_bar())

    def test_plot_pie(self):
        # Test plotting a pie chart
        self.plot_generator.file_path = 'data/data1.txt'
        self.plot_generator.plot_pie(title='Pie Chart')
        self.assertIsNotNone(self.plot_generator.current_plot)

        # Test when input file is not selected
        self.plot_generator.file_path = None
        self.assertFalse(self.plot_generator.plot_pie())

        # Test when data in input file is invalid
        self.plot_generator.file_path = 'data/data3wrongfile.txt'
        self.assertFalse(self.plot_generator.plot_pie())

    def test_choose_file(self):
        # Test setting a file path value
        with patch('tkinter.filedialog.askopenfilename', return_value='data.txt'):
            self.plot_generator.choose_file()
            self.assertEqual(self.plot_generator.file_path, 'data.txt')

    def test_save_current_plot(self):
        # Test when current_plot is None
        self.plot_generator.current_plot = None
        self.plot_generator.save_current_plot('test_save_current_plot_1')
        self.assertFalse(os.path.exists('plots/test_save_current_plot_1.png'))

        # Test when current_plot is not None
        self.plot_generator.current_plot = plt.figure()
        self.plot_generator.save_current_plot('test_save_current_plot_2')
        self.assertTrue(os.path.exists('plots/test_save_current_plot_2.png'))
        os.remove('plots/test_save_current_plot_2.png')
        os.removedirs('plots')

    def test_clone(self):
        # Test returning a new instance of the PlotGeneratorPrototype class
        clone = self.plot_generator.clone()
        self.assertIsInstance(clone, PlotGeneratorPrototype)
