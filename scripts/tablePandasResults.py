import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import sys


def format_value(val, col_header, time_columns):
    """
    Formats a cell value based on the column name.
    - For cells equal to a dash, return a dash.
    - For time columns, format as a float with 3 decimal places.
    - For all other numeric cells, format as an integer.
    - Otherwise, return string representation.
    """
    if val == "-":
        return "-"
    try:
        num = float(val)
        if col_header in time_columns:
            return f"{num:.3f}"
        else:
            # Format all non-time numeric values as integers
            return f"{int(round(num))}"
    except (ValueError, TypeError):
        return str(val)
    

def tablePandasResults(entropycsv: str, noentcsv: str):

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.precision', 2)
    #display(merged.to_string())

    entdata = entropycsv
    noentdata = noentcsv
    
    df1 = pd.read_csv(entdata)
    df2 = pd.read_csv(noentdata)
    
    
    # Read the CSV files into DataFrames.
    df1 = pd.read_csv(entdata)
    df2 = pd.read_csv(noentdata)
    
    # Convert string numbers to numeric types for the columns that will be used in calculations.
    numeric_columns = ["Time Median (s)", "Time SIQR (s)", "Depth", "Size", "Tested Progs"]
    for col in numeric_columns:
        df1[col] = pd.to_numeric(df1[col], errors="coerce")
        df2[col] = pd.to_numeric(df2[col], errors="coerce")
    
    
    # Merge the two dataframes on the 'Name' column.
    merged = pd.merge(df1, df2, on="Name",how="outer", suffixes=("_abs_on", "_abs_off"))
    #merged.sort_values("Name", inplace=True)

    
    
    # Calculate the difference between Time Medians (SIQR is NOT included for difference calculation).
    merged["Difference_Times"] = merged["Time Median (s)_abs_on"] - merged["Time Median (s)_abs_off"]
    

    
    # Now calculate the full time values that include SIQR.
    merged["Time_plus_SIQR_abs_on"] = merged["Time Median (s)_abs_on"] + merged["Time SIQR (s)_abs_on"]
    merged["Time_plus_SIQR_abs_off"] = merged["Time Median (s)_abs_off"] + merged["Time SIQR (s)_abs_off"]

    
    
    # Calculate the difference for Tested Progs.
    merged["Difference_Tested_Progs"] = merged["Tested Progs_abs_on"] - merged["Tested Progs_abs_off"]
    

    # Construct the final output DataFrame with the required headers.
    output = pd.DataFrame({
        "#ID": range(1, len(merged) + 1),
        "Benchmark": merged["Name"],
        "Depth": merged["Depth_abs_on"],  # Assumed identical across files.
        "Time+SIQR Abs": merged["Time_plus_SIQR_abs_on"],
        "Time+SIQR no Abs": merged["Time_plus_SIQR_abs_off"],
        "Time Diff": merged["Difference_Times"],
        "size": merged["Size_abs_on"],  # Assumed identical across files.
        "#Tested Abs": merged["Tested Progs_abs_on"],
        "#Tested noAbs": merged["Tested Progs_abs_off"],
        "#Tested Diff.": merged["Difference_Tested_Progs"]
    })

    output = output.fillna("-")
    
    # Specify which columns are the time columns (these will be rounded to 3 decimals)
    timecolumns = {"Time+SIQR Abs", "Time+SIQR no Abs", "Time Diff"}

    
    # Build the header (flat) from the DataFrame's columns.
    header = list(output.columns)

    # Build the table data.
    # The first row in table_data is the header.
    table_data = [header]
    # Then add each row, applying the appropriate formatting.
    for _, row in output.iterrows():
        formatted_row = []
        for i, cell in enumerate(row):
            formatted_row.append(format_value(cell, header[i], timecolumns))
        table_data.append(formatted_row)

    # Determine number of rows and columns
    nrows = len(table_data)
    ncols = len(header)

    # Create a matplotlib figure; adjust size as needed.
    fig, ax = plt.subplots(figsize=(ncols, nrows * .02))
    ax.axis('tight')
    ax.axis('off')

    # Create the table from table_data.
    tbl = ax.table(cellText=table_data, cellLoc='center', loc='bottom')

    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)
    # Adjust column widths based on content.
    tbl.auto_set_column_width(col=list(range(ncols)))

    # Apply conditional formatting for the difference columns:
    # For this layout assume index 5 ("difference between times") and index 9 ("difference between tested progs").
    diff_columns = [5, 9]
    for r in range(1, nrows):  # data rows (skip header row at index 0)
        for c in diff_columns:
            # Get the formatted text for the cell.
            cell_text = table_data[r][c]
            try:
                num = float(cell_text)
                if num > 0:
                    tbl[(r, c)].set_facecolor("lightgreen")
                elif num < 0:
                    tbl[(r, c)].set_facecolor("lightcoral")
            except ValueError:
                continue

    # Save the rendered table directly as a PDF.
    plt.title("Autopandas Comparison Absynth vs AbsEnt", fontsize=14, fontweight="bold")

    plt.savefig("./Plots/pandas_ent_vs_baseline_table.pdf", bbox_inches="tight")
    plt.close()

