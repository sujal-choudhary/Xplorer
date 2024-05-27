import os
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_terminal():
    # Clear command as function of OS
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def display_banner():
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
██╗  ██╗██████╗ ██╗      ██████╗ ██████╗ ███████╗██████╗     
╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██╔══██╗██╔════╝██╔══██╗    
 ╚███╔╝ ██████╔╝██║     ██║   ██║██████╔╝█████╗  ██████╔╝    
 ██╔██╗ ██╔═══╝ ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗    
██╔╝ ██╗██║     ███████╗╚██████╔╝██║  ██║███████╗██║  ██║    
╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    
                                                             
{Fore.YELLOW}{Style.BRIGHT}Welcome to Xplorer - IP Information Tool
Developed by Sujal Choudhary
    """
    print(banner)

def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return data
            else:
                print(Fore.RED + f"Failed to retrieve information: {data['message']}")
                return None
        else:
            print(Fore.RED + f"Failed to retrieve information for IP: {ip_address}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error fetching IP info: {e}")
        return None

def main():
    clear_terminal()
    display_banner()
    ip_address = input("Enter the IP address to lookup: ")
    ip_info = get_ip_info(ip_address)
    if ip_info:
        print(Fore.GREEN + "\nIP Information:")
        print(Fore.YELLOW + f"IP Address: {Fore.CYAN}{ip_info.get('query', 'N/A')}")
        print(Fore.YELLOW + f"Country: {Fore.CYAN}{ip_info.get('country', 'N/A')}")
        print(Fore.YELLOW + f"Region: {Fore.CYAN}{ip_info.get('regionName', 'N/A')}")
        print(Fore.YELLOW + f"City: {Fore.CYAN}{ip_info.get('city', 'N/A')}")
        print(Fore.YELLOW + f"ZIP: {Fore.CYAN}{ip_info.get('zip', 'N/A')}")
        print(Fore.YELLOW + f"Latitude: {Fore.CYAN}{ip_info.get('lat', 'N/A')}")
        print(Fore.YELLOW + f"Longitude: {Fore.CYAN}{ip_info.get('lon', 'N/A')}")
        print(Fore.YELLOW + f"Timezone: {Fore.CYAN}{ip_info.get('timezone', 'N/A')}")
        print(Fore.YELLOW + f"ISP: {Fore.CYAN}{ip_info.get('isp', 'N/A')}")
        print(Fore.YELLOW + f"Organization: {Fore.CYAN}{ip_info.get('org', 'N/A')}")
        print(Fore.YELLOW + f"AS: {Fore.CYAN}{ip_info.get('as', 'N/A')}")
    else:
        print(Fore.RED + "No information available.")

if __name__ == "__main__":
    main()
