from serpapi import GoogleSearch
from csv import writer 

# Latitude and longitude (New York)
latitude = 40.7128
longitude = -74.0060

def UnfilteredData():
    '''
    Will print completely unfiltered data
    '''
    for result in data['local_results']:  
        print(result)

def ErrorMayRaise(tag):
    '''
    If the establishment, does not have a tag (phonenum, price, descrpition ... etc)
    None will be returned
    '''
    try:
        return result[tag]
    except Exception:
        return 'None'

# Set up the search parameters
params = {
    "engine": "google_maps", # Engine to use
    "q": "coffee", # Query
    "type": "search", # What action we would like to preform ...search
    "ll": f"@{latitude},{longitude},14z", # The Location (ll = lat,lon)
}

# Passes the parameters to GoogleSearch, the variable "data" then recieves the response    
client = GoogleSearch(params)
data = client.get_dict()

# Creates a csv file/Writes over existing csv file
with open("MapScrape.csv", "w", encoding="utf8", newline="") as f:
    thewriter = writer(f)
    header = ["Position", "Name", "Address", "Phone Number", "Price", "Description", "Rating", "Reviews"]
    thewriter.writerow(header)

    # For each search result the code attempts to pull the following elements. If an
    # element is not there to pull, "None" will fill its place
    for result in data["local_results"]:    

        position = ErrorMayRaise(tag='position')
        name = ErrorMayRaise(tag='title')
        address = ErrorMayRaise(tag='address')
        phonenumber = ErrorMayRaise(tag='phone')
        price = ErrorMayRaise(tag='price').replace("£","$")
        description = ErrorMayRaise(tag='description')
        rating = ErrorMayRaise(tag='rating')
        reviews = ErrorMayRaise(tag='reviews')

        # The data is then put into a list and written to a .csv file
        info = [position, name, address, phonenumber, price, description, rating, reviews]
        thewriter.writerow(info)

print("CSV file creation complete")
