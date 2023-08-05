# File System Comparison

This Jupyter notebook compares the performance of different file formats (CSV, Pickle, Parquet, Feather) for reading and writing large datasets using pandas. The comparison is based on file size, reading speed, writing speed, and maximum size.

## Metadata

The dataset used for this comparison is generated using a function within the code, which creates 10 million data points with the following specifications:

- 6 Columns: Size, Age, Team, Win, Date, Probability
- The data types of these columns are: 'category', 'int16', 'boolean', and 'float32'.

## Comparison

The comparison includes the following aspects:

### CSV
- File Size: 488,292 KB
- Advantages: Human readable, simple to use.
- Disadvantages: No type information, inefficient with large datasets, not suitable for complex data, lack of standardization.

### Pickle
- File Size: 166,018 KB
- Advantages: Python integration, flexibility.
- Disadvantages: Security issues, lack of interoperability, lack of backward compatibility.

### Parquet
- File Size: 66,624 KB
- Advantages: Efficient compression, columnar format, big data ecosystem, supports schema evolution.
- Disadvantages: Slower write speed, complex.

### Feather
- File Size: 100,123 KB
- Advantages: Fast, interoperability, stores data type information.
- Disadvantages: Larger file size, lack of support in big data systems.

## Summary

The notebook concludes with a summary table that compares the file systems based on file size, reading speed, writing speed, and maximum size. The summary also includes recommendations for when to use each file system, based on the specific use case, size of the dataset, complexity of the data, programming languages in use, and specific requirements of the project.

## Code Overview

The code in the notebook can be divided into three main sections:

- Importing Libraries: This part of the code imports the necessary Python libraries for the notebook, which are `pandas` and `numpy`.

- Dataset Creation and Type Definition: The `get_dataset` function is defined to create a fake dataset with the required specifications. The `set_dtypes` function is used to set the data types for the columns in the dataframe.

- Reading and Writing Operations: The notebook contains separate sections where the pandas dataframe is written to and read from the different file formats. The time taken for these operations is recorded and displayed.

## File Usage

To use this notebook:

1. Import the required libraries (`pandas` and `numpy`).
2. Run the `get_dataset` and `set_dtypes` functions to create the dataset and set the data types.
3. Perform reading and writing operations for each file format and observe the recorded times.
4. Analyze the results and select the best file format based on your specific use case and requirements.

## Acknowledgments

This notebook is based on the work of Rob Mulla. You can find his YouTube channel [here](https://www.youtube.com/@robmulla). The specific video that provided inspiration for this code is available [here](https://www.youtube.com/watch?v=u4rsA5ZiTls&t=446s&ab_channel=RobMulla).

Please note that the results shared in this README are relevant to my local machine and can vary from machine to machine. For the most accurate results, it is recommended to run the code on your own machine.

