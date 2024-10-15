from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import random
import random_word  # Import the random word generator script

# Path to your ChromeDriver
DRIVER_PATH = "./resources/chromewin64/chromedriver.exe"

# Path to your existing Chrome profile
CHROME_PROFILE_PATH = "C:/Users/lucii/AppData/Local/Google/Chrome/User Data"
PROFILE_DIRECTORY = "Default"  # The specific profile you use, usually 'Default'

def open_bing():
    # Create ChromeOptions to load the existing Chrome profile
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")
    chrome_options.add_argument(f"profile-directory={PROFILE_DIRECTORY}")
# Add options to avoid the DevToolsActivePort issue
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems in containers
    chrome_options.add_argument("--remote-debugging-port=9222")  # Open remote debugging port
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--start-maximized")  # Start maximized
    chrome_options.add_argument("--disable-gpu")  # Applicable to Windows OS
    chrome_options.add_argument("--headless=new")  # Run in headless mode if needed (new API)

    # Create a Service object and pass the path to the ChromeDriver
    service = Service(executable_path=DRIVER_PATH)

    # Set up the Chrome driver with options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open Bing
    driver.get("https://www.bing.com")

    # Wait for the page to load
    time.sleep(2)

    return driver

def perform_search(driver, search_query):
    # Find the search box using the "q" name attribute
    search_box = driver.find_element(By.NAME, "q")
    
    # Clear any previous searches
    search_box.clear()
    
    # Enter the search query and hit ENTER
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the results page to load
    time.sleep(3)

    print(f"Performed search for: {search_query}")

if __name__ == "__main__":
    # Open Bing
    driver = open_bing()

    # Fetch 35 random words using the API
    search_queries = random_word.get(35)

    # Loop through each search term and perform the search
    for query in search_queries:
        perform_search(driver, query)
        
        # Introduce a random delay between searches (e.g., between 1 to 5 seconds)
        time.sleep(random.uniform(1, 5))

    # Close the browser after all searches
    driver.quit()
