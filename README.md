________________________________________

Project Title
Amazon SA Report Combine App Read Me
Description
Self help tool when you are doing your daily job
Usage
Put into the folder with your raw data files.
Version Control
V1 to V5
Contributions
Not available at the moment
License
No license required for distribution
________________________________________

Version Control Log
v1
Overview
This script processes four types of raw data files by running the code in four distinct folders for each report type. The reports are identified by specific naming patterns, including numeric suffixes.
Report Types
1.	Files containing "Sponsored Products Search term report" with suffixes like (1), (2).
2.	Files containing "Sponsored Products Advertised product report" with suffixes like (1), (2).
3.	Files containing "Sponsored Display Advertised product report" with suffixes like (1), (2).
4.	Files containing "Sponsored Brands Search term report" with suffixes like (1), (2).
Key Changes and Improvements
1.	Functionality Encapsulation: Created the combine_excel_files function to encapsulate the logic for combining Excel files, enhancing modularity for easier debugging and maintenance.
2.	Dynamic File Pattern Matching: Updated the glob pattern to match files with report names followed by numeric suffixes, allowing for flexible matching (e.g., "file (1).xlsx", "file (2).xlsx").
3.	Centralized Report Management: The report_names list now contains all report names, simplifying the addition or modification of reports without altering the core logic.
4.	Output Files: Each combined output file is named according to the corresponding report type for clarity and organization.
5.	Glob Pattern Update: The updated glob pattern (*).xlsx captures various suffix variations like "(1)", "(2)", "(a)", etc.
6.	Flexibility: Ensures inclusion of any valid file matching the report name with any suffix in the combination process.
________________________________________
v2
Overview
Addressed exceptions related to column names during normalization.
Remaining Exceptions
1.	"14-Day Total Sales - (Click)" separated from "14 Day Total Sales".
2.	"14-Day Total Orders (#) - (Click)" separated from "14 Day Total Orders (#)".
3.	"14-Day Total Units (#) - (Click)" separated from "14 Day Total Units (#)".
Key Additions for Column Normalization
1.	Function to Normalize Column Names: The normalize_column_names function uses regex to:
○	Replace instances of the en dash (–) with a standard hyphen (-).
○	Replace multiple spaces with a single space.
○	Strip leading and trailing whitespace.
○	Convert column names to title case for standardization.
2.	Integration in File Loading: The normalization function is called immediately after loading each DataFrame to ensure standardization before concatenation.
________________________________________
v3
Overview
Continued to refine column normalization.
Remaining Exceptions
1.	"14-Day Total Sales - (Click)" separated from "14 Day Total Sales".
2.	"14-Day Total Orders (#) - (Click)" separated from "14 Day Total Orders (#)".
3.	"14-Day Total Units (#) - (Click)" separated from "14 Day Total Units (#)".
Key Modifications
1.	Removing Suffixes: Added a line to remove the "- (Click)" suffix from any column names to merge related columns.
2.	Standardizing "14-Day": Standardized instances of "14-Day" to "14 Day" for consistency across column names.
________________________________________
v4
Overview
Identified issues with caching leading to double counting.
Issues Encountered
●	The script was combining files with cached data leading to double counting.
Key Changes
1.	Check for Existing Combined File: Implemented a check to remove the existing combined file before proceeding to combine new files to avoid duplication.
2.	Improved Reporting: Added print statements indicating when an existing combined file is removed.
Additional Key Changes
1.	Unique File Selection: Used a set to ensure all files are unique, preventing duplicates during processing.
2.	Comprehensive File Handling: Handled both file types (with and without suffixes) while avoiding duplicates.
________________________________________
v5
Overview
Addressed remaining issues with column separation and errors during file combination.
Issues Encountered
●	Observed three columns remained separated due to trailing spaces after normalization.
●	Encountered an error related to reindexing during file combination.
Key Changes
1.	Additional Stripping: Added another stripping operation after normalization to remove any remaining trailing spaces.
2.	Unique Column Names: Enhanced the normalize_column_names function to ensure that duplicated column names have a suffix (e.g., _1, _2) appended to them.
3.	Robustness: Improved the script's robustness to prevent errors during concatenation of DataFrames with similar column names.

