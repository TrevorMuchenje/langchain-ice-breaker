import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from linkedin profiles,
    manually scrape the infor from the linkedin profile
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/TrevorMuchenje/4422f660cfc8933a54b51b6652b9ad60/raw/9a9e99a0749385d1d4a37fe89d772333ead15783/trevor-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )
    data = response.json().get("person")
    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/trevor-muchenje-42a0bb175"
        ),
    )
