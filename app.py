import streamlit as st
import requests

def generate_itinerary(location, adventure, culture, outdoor_activities, num_days, driving_level):
    headers = {
        'authority': 'www.llama2.ai',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://www.llama2.ai',
        'referer': 'https://www.llama2.ai/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    driving_levels = {
        'low': 'less than 15 hours',
        'medium': 'between 15 and 30 hours',
        'high': 'more than 30 hours',
    }

    data = {
        "prompt": f"plan a {num_days} day trip to {location}. keep the adventure setting to {adventure * 100}%, culture exploration to {culture * 100}%, and outdoor activities to {outdoor_activities * 100}%. Also, I don't want to have a total drive {driving_levels[driving_level]} during the trip",
        "model": "meta/llama-2-70b-chat",
        "systemPrompt": "You are a helpful assistant.",
        "temperature": 0.75,
        "topP": 0.9,
        "maxTokens": 800,
    }

    response = requests.post('https://www.llama2.ai/api', headers=headers, json=data)
    return response.text

def main():
    st.title("Trip Planner")

    location = st.text_input("Enter the location:")
    adventure = st.slider("Adventure Setting", 0.0, 1.0, 0.5, 0.1)
    culture = st.slider("Culture Exploration", 0.0, 1.0, 0.5, 0.1)
    outdoor_activities = st.slider("Outdoor Activities", 0.0, 1.0, 0.5, 0.1)
    num_days = st.slider("Number of Days", 1, 7, 5, 1)
    driving_level = st.selectbox("Driving Level", ['low', 'medium', 'high'])

    # Information on Driving Levels
    st.subheader("Driving Level Information:")
    st.write(
        " - **Low:** This setting involves driving for less than 15 hours during the entire trip."
        "\n - **Medium:** This setting involves driving between 15 and 30 hours during the entire trip."
        "\n - **High:** This setting involves driving for more than 30 hours during the entire trip."
    )

    if st.button("Submit"):
        st.text("Generating Itinerary...")

        # Generate itinerary based on user input
        itinerary_response = generate_itinerary(location, adventure, culture, outdoor_activities, num_days, driving_level)

        # Display the response
        st.subheader("Generated Itinerary:")
        st.write(itinerary_response)

if __name__ == "__main__":
    main()
