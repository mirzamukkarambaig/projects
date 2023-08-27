# Data Exploration of COVID-19 Deaths and Vaccinations

This SQL script provides an exploration of COVID-19 data, including the number of deaths and vaccinations, on a global scale, per continent, and per country.

The script is divided into several sections, each dealing with different aspects of the data:

## 1. Testing Tables

Checks whether the `DeathsCovid` and `VaccinationCovid` tables in the `PortfolioProject` database contain any records where `continent` is not NULL.

## 2. Selecting Relevant Data

Selects the location, date, total cases, new cases, total deaths, and population data from the `DeathsCovid` table.

## 3. Total Cases vs Total Deaths

Calculates the death percentage with respect to the total cases for Pakistan (can be modified for other locations).

## 4. Total Cases vs Population

Calculates the infected population percentage for Pakistan (can be modified for other locations).

## 5. Countries with Highest Infection Rate

Determines the countries with the highest COVID-19 infection rates compared to their populations.

## 6. Highest Deaths per Countries and Continents

Finds the countries and continents with the highest numbers of COVID-19 deaths.

## 7. Highest Cases per Continent's Population

Finds the continents with the highest COVID-19 cases relative to their populations.

## 8. Global and Total Numbers

Calculates global and total numbers for new cases, new deaths, and the death percentage of the infected.

## 9. Vaccinations

Analyzes vaccination data, including total population vs vaccinations, using a common table expression (CTE) and a temporary table.

## 10. Creating a View

Creates a view named `PopulationVaccinated` that shows the rolling sum of vaccinations per location and date.

## How to Run

To run this script, you'll need access to the `PortfolioProject` database that contains the `DeathsCovid` and `VaccinationCovid` tables. This script is designed to run on SQL Server Management Studio or a similar SQL Server environment.

Please note that the script contains several `DROP` statements that will remove any existing table or view with the same name before creating a new one. Ensure you have backed up any important data before running this script.

## Acknowledgment

This script was created while following along with one of my favorite YouTubers, [Alex Freberg](https://www.youtube.com/@AlexTheAnalyst). The specific video I coded along with can be found [here](https://www.youtube.com/watch?v=qfyynHBFOsM&list=PLUaB-1hjhk8H48Pj32z4GZgGWyylqv85f&index=1&t=25s&ab_channel=AlexTheAnalyst). I would like to express my gratitude to Alex for his clear and helpful tutorials, which contributed greatly to my understanding of SQL for data analysis.