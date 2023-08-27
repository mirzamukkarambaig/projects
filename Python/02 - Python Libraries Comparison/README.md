# Pandas vs Vaex vs Polars Comparison

This repository contains a Jupyter Notebook where we compare the performance of three popular Python libraries—Pandas, Vaex, and Polars—for common data analysis tasks. 

## Overview

The objective of this notebook is to benchmark the performance of Pandas, Vaex, and Polars in the context of the following operations:

1. Reading a file
2. Computing metrics (mean and standard deviation) of a column
3. Finding the unique count of a column
4. Performing a cumulative sum of a column
5. Conducting a group-by aggregation

Each operation is demonstrated and timed in the notebook using each of the three libraries. 

## Usage

To run the notebook, you will need to have Jupyter Notebook installed, along with the Pandas, Vaex, and Polars libraries. The notebook was created in a Google Colab environment, so the results may vary depending on your local system's hardware and software configurations.

## Code Overview

The code in the notebook is divided into separate sections for each library. Each section demonstrates the use of the library for the tasks listed above, and each operation is timed to provide a comparison of the performance of the three libraries.

## File Usage

The data file used in this notebook is a Parquet file named 'test.parquet'. It is read in the first step of each library's operations.

## Summary

The notebook provides a comprehensive comparison of the Pandas, Vaex, and Polars libraries in terms of speed and efficiency for common data analysis tasks. The results can be a valuable reference for anyone seeking to optimize their data analysis workflows.

## Contributing

Your contributions are always welcome! If you have suggestions for improving the code or you want to refactor the code, feel free to make a pull request. Let's work together to make this comparison more comprehensive and beneficial for everyone.

## Acknowledgements

Special thanks to [Rob Mulla](https://www.youtube.com/@robmulla) for the inspiration. Check out his original videos [here](https://www.youtube.com/watch?v=LEhMQhCv3Kg&t=334s&ab_channel=RobMulla) and [here](https://www.youtube.com/watch?v=VHqn7ufiilE&t=1s&ab_channel=RobMulla).
