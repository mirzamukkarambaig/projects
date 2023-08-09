# Weather Mobile Application

## Introduction

This Android application retrieves and displays weather information for a given location. It utilizes the OpenWeatherMap API to fetch weather data such as temperature, humidity, wind speed, sunrise and sunset times, etc. Users can view weather details for their current location using the GPS functionality of their device.

## Features

- **Current Location Weather:** Get weather details for the user's current location.
- **Temperature Details:** View current temperature, feels-like temperature, maximum, and minimum temperatures.
- **Wind Information:** Get wind speed and wind direction details.
- **Sunrise and Sunset Times:** View sunrise and sunset times for the current location.
- **Visibility:** View visibility details.
- **Location Details:** Display longitude, latitude, altitude, and speed values for the current location.

## Permissions

The application requires the following permissions:

- `ACCESS_FINE_LOCATION`: To access the precise location of the device using GPS.
- `ACCESS_COARSE_LOCATION`: To access the approximate location of the device.

## Dependencies

- **OpenWeatherMap API:** The application fetches weather data from the OpenWeatherMap API.
- **AndroidX Libraries:** Uses AndroidX for backward compatibility of features.

## How to Use

1. **Enter City Name:** Users can enter the name of the city they want to view weather details for.
2. **View Weather Details:** Click the "Enter" button to view the weather details for the given city or current location.
3. **Location Permissions:** Users must grant location permissions to allow the app to access the device's location.

## Layout

The layout is designed using ConstraintLayout and includes EditText for city name input, a Button to trigger the weather data fetch, and a TableLayout to display weather details.

## Development

This project is developed using Java for the Android platform.

### Build & Run

You'll need Android Studio to build and run the project. Open the project in Android Studio, connect a suitable debugging-enabled device or emulator, and run the application.

## License

This project is open-source. Feel free to modify and distribute it as per your requirements.

## Support & Contribution

For support, feature requests, or contributions, please open an issue or pull request.