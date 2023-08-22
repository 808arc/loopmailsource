# Music Data Processing Tool

This tool is designed to help you retrieve and process music-related data from various sources, including the Genius lyrics API and Instagram profiles. It consists of several Python scripts that work together to gather information about your favorite rapper's songs, their producers, and relevant Instagram data.

## Getting Started

To use this tool, follow these steps:

1. Clone this repository to your local machine.

2. Set up your environment variables:
   - Create a `.env` file in the root directory of the repository.
   - Add the following variables to the `.env` file and replace the values with your actual credentials:
        `api_key=<Your_Genius_API_Key>`
        `user_name=<Your_Instagram_Username>`
        `password=<Your_Instagram_Password>`

3. Install the required Python packages by running:

    `pip install -r requirements.txt`


4. Run the `main.py` script to start processing the data:

`python main.py`


## Files

- `genius.py`: This script contains functions to authenticate with the Genius API, retrieve artist and song data, and fetch artist information.

- `instagram_scraper.py`: This script uses the `instagram_private_api` library to scrape Instagram usernames for public email and bio information.

- `main.py`: The main script that orchestrates the data processing. It prompts the user for inputs, interacts with Genius and Instagram APIs, and saves the collected data to an Excel file.

- `song_list.py`: Contains lists used to store producer information, Instagram usernames, and other data.

- `song_processing.py`: Contains functions to process the fetched songs and their associated producers.

## Usage

1. When you run the `main.py` script, it will prompt you for the name of your favorite rapper and the maximum number of songs you want to process.

2. The script will authenticate with the Genius API using the provided API key and fetch information about the artist.

3. It will then retrieve a list of songs by the artist and process them using the custom processing functions.

4. The `scrape_instagram_usernames` function will be called to scrape Instagram usernames' public email and bio information.

5. Finally, a DataFrame will be created using the collected data, and the DataFrame will be saved to an Excel file.

## Notes

- The `requirements.txt` file contains the necessary Python packages. Install them using `pip install -r requirements.txt`.

- This tool is designed for educational and personal use. Make sure to review and comply with the terms of use for the Genius API and any other services you interact with.
