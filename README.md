# Winchester DB Update Tool

This tool automates the transfer of feature datasets from a source SQL Server environment to a staging SQL Server environment, ensuring data consistency between environments. This script uses the ArcGIS Python API and `arcpy` to handle geospatial data management tasks effectively.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Script Details](#script-details)
- [Error Handling](#error-handling)

## Overview
The Winchester DB Update Tool performs the following:
1. Connects to a source SQL Server database to retrieve a feature dataset.
2. Copies the dataset from the source environment.
3. Connects to the target (staging) SQL Server database.
4. Clears the existing data in the target feature dataset and replaces it with the new data from the source.

## Prerequisites
- **Python environment with `conda`**: Ensure you have an Anaconda environment set up.
- **ArcGIS Pro**: `arcpy` requires an ArcGIS Pro installation and licensing.
- **ArcGIS Python API**: This tool uses the ArcGIS Python API for database connections and dataset manipulation.

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gershom-ejoni/Winchester_DB_Update.git
   cd Winchester_DB_Update
2. **Create and activate a Conda environment:**
   ```bash
   conda create -n arcvenv python=3.8
   conda activate arcvenv
3. **Install Required Packages:**
   ```bash
   conda create -n arcvenv python=3.8
   conda activate arcvenv
4. **Database Connection Files:**

   Ensure you have .sde connection files for both the source and target databases, with read and write permissions respectively. Place these files in an accessible directory and update the paths in the script accordingly.
## Usage
Run the script with ArcGIS Pro as a geoprocessing tool to view the progress through `arcpy.AddMessage` output.

### Parameters
- **Source Feature Dataset**: Path to the source feature dataset.
- **Target Feature Dataset**: Path to the target feature dataset in the staging environment.

### Parameters
- **Source Feature Dataset**: Path to the source feature dataset.
- **Target Feature Dataset**: Path to the target feature dataset in the staging environment.


## Script Details
The script follows these core steps:

1. **Connect to Source Environment**: Establishes a connection to the source SQL Server database and retrieves the specified dataset.
2. **Copy Dataset to Memory**: Uses `arcpy.CopyFeatures_management` to copy the source dataset into memory for efficient processing.
3. **Connect to Target Environment**: Connects to the staging SQL Server environment, where the dataset will be updated.
4. **Delete Existing Data in Target**: Clears any existing records in the target feature dataset to prepare for the new data.
5. **Insert New Data**: Appends the data copied from the source dataset into the target feature dataset.

## Error Handling
The script uses `try-except` blocks to manage errors and logs messages in ArcGIS Pro using `arcpy.AddMessage` and `arcpy.AddError` to capture:

- **ArcGIS-Specific Errors**: Catches exceptions related to ArcGIS processes, providing specific error messages for troubleshooting.
- **General Errors**: Handles any other runtime errors, ensuring they are captured and output in the ArcGIS environment for review.

### Running the Script
```bash
python main.py

