import matplotlib.pyplot as plt
import os

class Plotter:
  @staticmethod
  def plot_data(x: any, y: any, title: str, xlabel: str, ylabel: str,
                output_filename : str = None):
      plt.figure(figsize=(16,8))
      plt.title(title)
      plt.xlabel(xlabel)
      plt.ylabel(ylabel)
      plt.grid()

      plt.plot(x, y)
      if output_filename:
          directory = os.path.dirname(output_filename)
          if not os.path.exists(directory):
            os.makedirs(directory)
          plt.savefig(output_filename)

  @staticmethod
  def scatter_data(x: any, y: any, title: str, xlabel: str, ylabel: str,
                   output_filename : str = None):
      plt.figure(figsize=(16,8))
      plt.title(title)
      plt.xlabel(xlabel)
      plt.ylabel(ylabel)
      plt.grid()

      plt.scatter(x, y)
      if output_filename:
          directory = os.path.dirname(output_filename)
          if not os.path.exists(directory):
            os.makedirs(directory)
          plt.savefig(output_filename)

