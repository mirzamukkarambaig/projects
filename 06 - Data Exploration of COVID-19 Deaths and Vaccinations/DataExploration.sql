-- Testing Tables are correct or not
Select *
From PortfolioProject..DeathsCovid
Where continent is not NULL
Order By 3,4

Select *
From PortfolioProject..VaccinationCovid
Where continent is not NULL
Order By 3,4

--Select Relevent Data
Select location, date, total_cases, new_cases, total_deaths, population
From PortfolioProject..DeathsCovid
Where continent is not NULL
Order By 1, 2

--Total Cases vs Total Deaths
Select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 AS Death_Perccenatge
From PortfolioProject..DeathsCovid
Where location = 'Pakistan' And continent is not NULL
Order By 1, 2
 
--Total Cases vs Population
Select location, date, total_cases, population, (total_cases/population)*100 AS Infected_Population_Percentage
From PortfolioProject..DeathsCovid
Where location = 'Pakistan' And continent is not NULL
Order By 1, 2

--Coutries with highest infection rate compare to population
Select location, population, MAX(total_cases) AS Highest_Infection_Count , MAX((total_cases/population)*100) AS Infected_Population_Percentage
From PortfolioProject..DeathsCovid
Where continent is not NULL
Group By location, population
Order By 4 DESC

--Hightest Deaths per Countries
Select location, MAX(cast(total_deaths AS int)) AS Highest_Death_Count 
From PortfolioProject..DeathsCovid
Where continent is not NULL
Group By location 
Order By 2 DESC
 
--Hightest Deaths per Continent
Select location, MAX(cast(total_deaths AS int)) AS Highest_Death_Count 
From PortfolioProject..DeathsCovid
Where continent is NULL
Group By location
Order By 2 DESC

--Hightest Cases  per Continent's Population
Select location, population,MAX(cast(total_cases AS int)) AS Highest_Cases_Count, MAX((total_cases/population)*100) AS Infected_Population_Percentage
From PortfolioProject..DeathsCovid
Where continent is NULL
Group By location, population
Order By 4 DESC


--Global Numbers
Select date, SUM(new_cases) AS Total_Cases, SUM(cast(new_deaths as int)) AS Total_Deaths, SUM(cast(new_deaths as int))/ NULLIF(SUM(new_cases),0)*100 AS Death_Percentage_of_Infected
From PortfolioProject..DeathsCovid
Where continent is NULL  
Group By date
Order By 1, 2

--Total Numbers
Select SUM(new_cases) AS Total_Cases, SUM(cast(new_deaths as int)) AS Total_Deaths, SUM(cast(new_deaths as int))/ NULLIF(SUM(new_cases),0)*100 AS Death_Percentage_of_Infected
From PortfolioProject..DeathsCovid
Where continent is NULL  
Order By 1, 2

--Vaccinations

--Total Population vs Vaccinations
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(bigint, vac.new_vaccinations)) OVER (Partition By dea.location Order By dea.location, dea.date ) As RollingVaccinationSum
--,(RollingVaccinationSum/population)*100
From PortfolioProject..DeathsCovid dea Join PortfolioProject..VaccinationCovid vac On dea.location = vac.location And dea.date = vac.date
Where dea.continent is not Null 
Order By 2, 3

--USE CTE
With PopVsVac (Continent, Location, Date, Population, New_Vaccinations, RollingVaccinationSum)
As
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(bigint, vac.new_vaccinations)) OVER (Partition By dea.location Order By dea.location, dea.date ) As RollingVaccinationSum
From PortfolioProject..DeathsCovid dea Join PortfolioProject..VaccinationCovid vac On dea.location = vac.location And dea.date = vac.date
Where dea.continent is not Null 
)
Select *, (RollingVaccinationSum/Population)*100
From PopVsVac

--Temp Tables
Drop Table if exists #PopulationVaccinated
Create Table #PopulationVaccinated(
	Continent nvarchar(255),
	Location nvarchar(255),
	Date datetime,
	Population float,
	New_Vaccinations nvarchar(255),
	RollingVaccinationSum bigint
)

Insert Into #PopulationVaccinated
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(bigint, vac.new_vaccinations)) OVER (Partition By dea.location Order By dea.location, dea.date ) As RollingVaccinationSum
From PortfolioProject..DeathsCovid dea Join PortfolioProject..VaccinationCovid vac On dea.location = vac.location And dea.date = vac.date
Where dea.continent is not Null 

Select *, (RollingVaccinationSum/Population)*100
From #PopulationVaccinated

--Creating View
Drop View if exists PopulationVaccinated
Go;
Create View PopulationVaccinated As
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(bigint, vac.new_vaccinations)) OVER (Partition By dea.location Order By dea.location, dea.date ) As RollingVaccinationSum
From PortfolioProject..DeathsCovid dea Join PortfolioProject..VaccinationCovid vac On dea.location = vac.location And dea.date = vac.date
Where dea.continent is not Null

Select *
From PopulationVaccinated