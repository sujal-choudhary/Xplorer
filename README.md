# Xplorer - IP Information Tool

Xplorer is a tool designed to fetch and display geolocation and ISP information for a given IP address.

## Features

- Fetches information such as country, region, city, ZIP code, latitude, longitude, timezone, ISP, organization, and AS number for a given IP address.
- Displays information with colored text for better readability.
- Clears the terminal screen and displays a banner at the start.

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Sujal74756/Xplorer.git
    cd IPInfoXplorer
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the tool using the command:
    ```sh
    python xplorer.py
    ```

2. When prompted, enter the IP address you want to look up.

3. The tool will display detailed information about the IP address, including:

    - Country
    - Region
    - City
    - ZIP code
    - Latitude
    - Longitude
    - Timezone
    - ISP
    - Organization
    - AS number
## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

> "Developed by Sujal Choudhary"
## Warning

**Warning:** Use of this tool must comply with all applicable laws. Do not use this tool for illegal activities. The developers are not responsible for any misuse of this tool.

## Example

```sh
$ python xplorer.py
Enter the IP address to lookup: 8.8.8.8

██╗  ██╗██████╗ ██╗      ██████╗ ██████╗ ███████╗██████╗ 
╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██╔══██╗██╔════╝██╔══██╗
 ╚███╔╝ ██████╔╝██║     ██║   ██║██████╔╝█████╗  ██████╔╝
 ██╔██╗ ██╔═══╝ ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗
██╔╝ ██╗██║     ███████╗╚██████╔╝██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

Welcome to Xplorer - IP Information Tool

IP Information:
IP Address: 8.8.8.8
Country: United States
Region: California
City: Mountain View
ZIP: 94035
Latitude: 37.386
Longitude: -122.084
Timezone: America/Los_Angeles
ISP: Google LLC
Organization: Google LLC
AS: AS15169 Google LLC
'''

