# Copyright 2024 (c) BlazeInferno64 --> https://github.com/blazeinferno64
""" 
 **Decription**: ScarapyPy is a powerful yet handy web scraper made using pure python!
 
 **Author**: BlazeInferno64
 
 Copyright 2024 (c) BlazeInferno64 --> https://github.com/blazeinferno64
"""
import requests
import time
import datetime
import tabulate
import json
import xml.dom.minidom
import os
from bs4 import BeautifulSoup
from src.tools.url import validateURL

app_name = "ScrapyPy"
app_description = "ScrapyPy is a powerful yet handy web scraper made using pure python"

def web_scrapper(url, optional_input, optional_name):
    """
    This function scraps the response from a given URL and formats it.
    It also provides an option to save the response in a separate file.
    """
    start_time = time.time()
    try:
        print(f"ScrapyPy is scraping response from '{url}'...")
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()
        # Get the headers of the response
        headers = response.headers
        # Format the response
        end_time = time.time()
        total_time = end_time - start_time
        beautified_response = format_response(url, response.text, headers, total_time)

        if optional_input:
            # If the user wants to save the response in a separate file
            if optional_name:
                # Use the provided filename
                with open(optional_name, "w", encoding="utf-8") as file:
                    file.write(beautified_response)
                    file.close()
                return print(f"Successfully scraped the response from '{url}' and saved it to '{optional_name}' file at '{os.getcwd()}'")
            else:
                # Use the default filename 'response.txt'
                print(f"\nNo filename provided therefore the scraped response would be saved as 'response.txt' file at '{os.getcwd()}'\n")
                with open("response.txt", "w", encoding="utf-8") as file:
                    file.write(beautified_response)
                    file.close()
                return print(f"Successfully scraped the response from '{url}' and saved it to 'response.txt' file at '{os.getcwd()}'")
        else:
            # If the user doesn't want to save the response in a separate file
            return print(beautified_response)
    except requests.exceptions.ConnectionError as err:
        return print(f"\nA connection error occured while scraping response from '{url}'\nMost likely ScrapyPy wasn't able to resolve '{url}'\n")
    except requests.exceptions.TooManyRedirects:
        return print(f"\nToo many redirects while scraping response from '{url}'\n")
    except requests.exceptions.RequestException as err:
        return print(f"\nAn exception occured while scraping '{url}': {err}\n")
            

def main():
    """
    This is the main function which takes input from the user, including the URL and options for saving the response.
    """
    url = input("Enter the URL for scraping: ")
    if validateURL(url):
        optional_input = input("Do you want to save the scraped response in a seperate file? (Y/N): ")
        if optional_input.lower() == "y" or optional_input.lower() == "yes":
            optional_name = input("What should be the name of the file: ")
            return web_scrapper(url, optional_input, optional_name)
        elif optional_input.lower() == "n" or optional_input.lower() == "no":
            return web_scrapper(url, None, None)
        else:
            return print(f"Invalid option: '{optional_input}' Please input either Y or N")
    else:
        return print(f"Invalid URL provided for scraping!")

def format_response(url, text, headers, time_taken):
    """
    This function formats the response from the URL.
    It checks if the response is JSON, HTML, or XML data and formats it accordingly.
    """
    table = [(key, value) for key, value in headers.items()]
    formatted_headers = tabulate.tabulate(table, headers=["Key", "Value"], tablefmt="flex")
    
    # Check if the response is JSON data
    try:
        json_data = json.loads(text)
        formatted_response = json.dumps(json_data, indent=4)
    except ValueError:
        # Check if the response is HTML data
        if headers.get("Content-Type") == "text/html":
            try:
                soup = BeautifulSoup(text, "html.parser")
                formatted_response = soup.prettify()
            except Exception as err:
                return print(f"An exception occured: \n\n{err}")
        # Check if the response is XML data
        elif headers.get("Content-Type") == "application/xml":
            try:
                xml_dom = xml.dom.minidom.parseString(text)
                formatted_response = xml_dom.toprettyxml(indent="  ")
            except Exception as err:
                return print(f"An error occured: \n\n{err}")
        else:
            # If it's not JSON, HTML, or XML data, just use the original response text
            formatted_response = text
    
    formatted_response = f"Scraped by {app_name} from '{url}' at '{datetime.datetime.now()}'\nEstimated Time taken for scraping: {time_taken:.2f} seconds\n\nHeaders:\n{formatted_headers}\n\nResponse:\n{formatted_response}"
    return formatted_response