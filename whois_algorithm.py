from whois import whois
import datetime


def reformat_date(date_str: str) -> datetime.datetime:
    """
    Returns a datetime object containing the information in the formatted string

    @param date_str, a formatted string containing a date
    @return a datetime.datetime object containing the input date
    """
    if type(date_str) == type("str"):
        return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

    elif type(date_str) == type([]):
        return date_str[0]

    elif type(date_str) == type(datetime.datetime.now()):
        return date_str

    else:
        raise Exception("Incorrect date value passed")


def days_since_creation(date_str: str) -> int:
    """
    Returns the number of days since a given date

    @param date_str, a formatted string that contains the time when a website was registered
    @return diff_days.days, the number of days since the input date
    """
    date_obj = reformat_date(date_str)
    diff_days = datetime.datetime.now() - date_obj

    return diff_days.days


def get_whois_data(url: str) -> dict:
    """
    Gets the ICANN WHOIS information for a given website URL and returns a dictionary with the useful (for our purposes)
    information.

    @param url, a string containing the URL for an article to be checked
    @return refined_whois_dict, a dictionary containing information that is relevant to our algorithm
    """
    whois_dict = whois(url)
    refined_whois_dict = {
        "city": "",
        "state": "",
        "country": "",
        "creation_date": "",
        "name": ""
    }

    if "city" in whois_dict:
        refined_whois_dict["city"] = whois_dict["city"]

    if "state" in whois_dict:
        refined_whois_dict["state"] = whois_dict["state"]

    if "country" in whois_dict:
        refined_whois_dict["country"] = whois_dict["country"],

    if "creation_date" in whois_dict:
        refined_whois_dict["creation_date"] = reformat_date(whois_dict["creation_date"])

    if "name" in whois_dict:
        refined_whois_dict["name"] = whois_dict["name"]

    return refined_whois_dict


# TODO - Revamp to match changes made to the get whois info function
def get_whois_features(url: str) -> dict:
    """
    Returns a dictionary containing values for different WHOIS factors that our algorithm will use. The location of
    the website's registration (e.g. Macedonia), the age of the site, and whether it was registered using a WHOIS guard
    will all impact the results of the program.

    @param url, a string containing the URL of an article to be checked
    @return whois_values_dict, a dictionary containing the calculated values for each factor (e.g. location, age)
    """
    whois_data = get_whois_data(url)
    whois_values_dict = {
        "location_value": 0,
        "age_value": 0,
    }

    # Assigns an int to the location_value key depending on the history of fake news dissemination from a given country
    suspicious_countries = ("MK", "PA")
    suspicious_cities_us = (("SCOTTSDALE", "AZ"),)

    # Sanitize the country name
    if str(whois_data["country"]).upper() in suspicious_countries:
        whois_values_dict["location_value"] = 1

    elif (str(whois_data["city"]).upper(), str(whois_data["state"]).upper()) in suspicious_cities_us:
        whois_values_dict["location_value"] = 1

    # Assigns a float to the age_value key depending on the relative age of the website
    # TODO - Refine this value to get best results
    whois_values_dict["age_value"] = whois_data["creation_date"]

    # Assigns an int to the privacy_value key by checking if a privacy guard service was used
    if whois_data["name"] != None and "PRIVACY" in whois_data["name"].upper():
        whois_values_dict["location_value"] = 0.65

    return whois_values_dict
