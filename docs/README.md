# Project Documentation: Music and Instagram Data Collector

## Table of Contents

- [Introduction](#introduction)
  - [Installation](#installation)
  - [Usage](#usage)
- [Configuration](#configuration)
  - [Insert your Genius API key](#Insert-your-Genius-API-key)
  - [Insert your Instagram credentials](Insert-your-Instagram-credentials)
  - [Getting API Keys](#getting-api-keys)
- [Documentation](#documentation)
  - [Project Structure](#project-structure)
    - [genius.py](#geniuspy)
    - [instagram_scraper.py](#instagram_scraperpy)
    - [log_manager.py](#log_managerpy)
    - [main.py](#mainpy)
    - [song_list.py](#song_listpy)
    - [song_processing.py](#song_processingpy)

## Introduction

"loopmailsource" is a Python project that allows you to collect information about your favorite music artist producers and scrape their open data contacts. It can fetch data about songs, producers, and artists while also gathering Instagram usernames, public email addresses, and biographies.

## Installation

To set up the project, follow these steps:

1. Clone the project repository from GitHub.
2. Create a virtual environment (recommended) and activate it.
3. Install the required packages listed in the `requirements.txt` file using `pip install -r requirements.txt`.
4. Create a `.env` file in the root directory (next to `requirements.txt`) and populate it with your API keys and Instagram credentials (see [Configuration](#configuration)).
5. You are now ready to use the project.

## Usage

To use the Music and Instagram Data Collector:

1. Run the `main.py` script.
2. Follow the prompts to input the artist's name and the maximum number of songs to process.
3. The script will collect data about the artist, their songs, producers, and Instagram-related information.
4. The results will be saved to a CSV file named `<artist_name>_<max_count>_tracks.csv`.

## Configuration

In the `.env` file, configure the following variables:

## Insert your Genius API key
api_key = 'your_genius_api_key'

## Insert your Instagram credentials
user_name = 'your_instagram_username'
password = 'your_instagram_password'

Make sure to replace 'your_genius_api_key', 'your_instagram_username', and 'your_instagram_password' with your actual API key and credentials.

- **Instagram Credentials:** Use your own Instagram username and password for Instagram data scraping.


## Getting API Keys

To obtain the necessary API keys:

- **Genius API Key:**
  1. Sign up on [Genius](https://genius.com/).
  2. Go to the [Genius API Clients](https://genius.com/api-clients) page.
  3. Obtain a CLIENT ACCESS TOKEN for your application.

With the API keys and credentials configured in the `.env` file, you can start using the Music and Instagram Data Collector to gather information about your favorite music artist and their Instagram presence.

## Documentation

## Project Structure

The project is organized into several Python files within the `src` directory:

- `genius.py`: Handles interaction with the Genius API for music-related data.
- `instagram_scraper.py`: Provides functions for scraping Instagram data.
- `log_manager.py`: Manages API keys and authentication for Genius and Instagram.
- `main.py`: The main script that orchestrates the data collection process.
- `song_list.py`: Defines lists for storing data related to songs, producers, Instagram usernames, emails, and biographies.
- `song_processing.py`: Contains functions for processing song-related data.

**genius.py**

This module handles interactions with the Genius API for music-related data. It includes functions for authentication, retrieving artist information, and fetching songs.

**instagram_scraper.py**

The `instagram_scraper.py` module provides functions for scraping Instagram data, including public email addresses and biographies, from Instagram usernames.

**log_manager.py**

`log_manager.py` manages API keys and authentication for both the Genius and Instagram APIs. It loads environment variables from the `.env` file and provides the `genius_auth` function for Genius API authentication.

**main.py**

The `main.py` script is the main entry point for the project. It prompts the user for input, fetches data about the artist and their songs, processes the data, scrapes Instagram information, and saves the results to a CSV file.

**song_list.py**

`song_list.py` defines lists for storing data related to songs, producers, Instagram usernames, public email addresses, and biographies. These lists are used to collect and organize the data during the execution of the project.

**song_processing.py**

`song_processing.py` contains functions for processing song-related data. It iterates through songs, retrieves information about producers, and calculates estimated time and progress during data collection.

