import os
import pandas as pd
from main import artist_name, max_count


def df_gen(data):
    # Create a DataFrame using the collected data
    df = pd.DataFrame(data)

    # Specify the path to the "data" folder
    data_folder = os.path.join(os.path.dirname(__file__), "..", "data")

    # Create the data folder if it doesn't exist
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Define the Excel file path within the "data" folder
    excel_file_path = os.path.join(
        data_folder, f"{artist_name}_{max_count}_tracks.xlsx"
    )

    # Save the DataFrame to an Excel file in the "data" folder
    df.to_excel(excel_file_path, sheet_name="Sheet1", index=False)

    print(f"DataFrame has been saved to '{excel_file_path}' in the 'data' folder.")
