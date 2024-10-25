import arcpy
from arcgis.gis import GIS
import os
import sys


# SQL Server connections (using .sde connection files)
source_db = r"C:\Coding_Projects\Winchester_DB_Update\connections\SQLServer-gis-501sql2016-WinchesterCT(gis).sde"
target_db = r"C:\Coding_Projects\Winchester_DB_Update\connections\SQLServer-weblogisticsdbdev-WL_Winchester(sde).sde"

# Feature class details
source_fc = f"{source_db}\\WinchesterCT.GIS.INTERNAL"
target_fc = f"{target_db}\\WL_Winchester.SDE.INTERNAL"

try:
    # Step 1: Connect to the source environment (read only)
    arcpy.AddMessage("Connecting to the source environment...")
    arcpy.env.workspace = source_db

    # Step 2: Extract features from the source
    arcpy.AddMessage("Extracting features from the source environment...")
    source_features = arcpy.CopyFeatures_management(source_fc, "in_memory/temp_fc")

    # Step 3: Connect to the destination (staging) environment
    arcpy.AddMessage("Connecting to the destination environment...")
    arcpy.env.workspace = target_db

    # Step 4: Delete existing features in staging
    arcpy.AddMessage("Clearing existing features in the target environment...")
    arcpy.DeleteFeatures_management(target_fc)

    # Step 5: Insert new features into the destination (staging) environment
    arcpy.AddMessage("Inserting features into the destination environment...")
    arcpy.Append_management(source_features, target_fc, "NO_TEST")

    # Clean up in-memory data
    arcpy.Delete_management("in_memory/temp_fc")

    # Success message
    arcpy.AddMessage("Feature transfer completed successfully.")

except arcpy.ExecuteError:
    # Catch ArcPy-specific errors
    arcpy.AddError(f"ArcPy error occurred: {arcpy.GetMessages(2)}")

except Exception as e:
    # Catch general Python errors
    arcpy.AddError(f"An error occurred: {str(e)}")

finally:
    arcpy.AddMessage("Script execution completed.")
