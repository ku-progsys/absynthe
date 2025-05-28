import pandas as pd
import matplotlib.pyplot as plt
import glob


def plotLines(files: list[str], legend: list[str], title):
    # Get a list of CSV files in the current directory.
    csv_files = files
    legend = ["Global", "Window 3", "Window 5", "Window 9"]

    # Create a colormap that will cycle through distinct colors.
    colors = plt.cm.get_cmap("tab10", len(csv_files))

    # Create a figure
    plt.figure(figsize=(10, 6))

    for i, csv_file in enumerate(csv_files):
        try:
            # Read csv file assuming the first row contains headers.
            df = pd.read_csv(csv_file)
        except Exception as e:
            print(f"Error reading file {csv_file}: {e}")
            continue

        # Drop rows where "Time Median (s)" is missing "-".
        df = df[df["Time Median (s)"] != "-"]

        # Convert the "Time Median (s)" column to numeric.
        df["Time Median (s)"] = pd.to_numeric(df["Time Median (s)"], errors='coerce')
        df.dropna(subset=["Time Median (s)"], inplace=True)

        # Sort rows by "Time Median (s)" in ascending order.
        df = df.sort_values("Time Median (s)", ascending=True).reset_index(drop=True)

        # Prepare x-axis as integers from 0 to the number of rows minus one.
        x = list(range(len(df)))
        # y-axis: the "Time Median (s)" values.
        y = df["Time Median (s)"].tolist()

        # Plot while assigning each file a different color.
        plt.plot(x, y, marker='o', label=legend[i], color=colors(i))
        
        # Immediately after plotting with plt.plot(), add whiskers for the endpoint.
        # Ensure that you've already converted "Time SIQR (s)" to numeric:
        #   df["Time SIQR (s)"] = pd.to_numeric(df["Time SIQR (s)"], errors="coerce")
        siqr_val = df["Time SIQR (s)"].iloc[-1]
        if pd.notna(siqr_val):
            siqr_val = float(siqr_val)
            plt.errorbar(x[-1], y[-1], yerr=siqr_val, fmt='none', color=colors(i),
                capsize=5, elinewidth=1.5)

    # Configure the plot.
    plt.xlabel("# Progs Found")
    plt.ylabel("Time Median(s)")
    plt.title(title)
    plt.legend(title="Legend")
    plt.grid(True)
    plt.tight_layout()

    # Display the plot.
    plt.savefig(f"{title}.pdf", bbox_inches="tight")
    plt.close()


