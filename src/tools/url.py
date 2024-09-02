# Copyright 2024 (c) BlazeInferno64 --> https://github.com/blazeinferno64
import urllib.parse

def validateURL(url):
    """
    This function validates a given URL.
    It checks if the URL is empty, and if it has a scheme and a network location.
    """
    if url == "":
        print("ScrapyPy cannot scrap empty url!")
        return False
    try:
        # Parse the URL into its components
        parsed_url = urllib.parse.urlparse(url)
        # Check if the URL has a scheme and a network location
        if not all([parsed_url.scheme, parsed_url.netloc]):
            return False
        return True
    except Exception as e:
        # Handle any exceptions that occur during URL parsing
        print(f"An error occurred while parsing the URL: {e}")
        return False
    
if __name__ == "__main__":
    # This is not necessary, as validateURL is a function that takes a URL as an argument
    # validateURL()
    pass