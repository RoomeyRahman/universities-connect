import requests
import json


def get_data(url):
    # Define the API endpoint URL
    # Make a GET request to the API endpoint using requests.get()
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        posts = response.json()
        return posts
    else:
        print('Error:', response.status_code)
        return None


def main():
    posts = get_data('http://universities.hipolabs.com/search?country=australia')
    if posts:
        sorted_data = sorted(posts, key=lambda x: x['name'])
        with open('Australia.json', 'w') as json_file:
            json.dump(sorted_data, json_file, indent=4)
        # print('First Post Title:', len(posts))
    else:
        print('Failed to fetch posts from API.')

if __name__ == '__main__':
    main()