CREATE DATABASE AirQualityDB;

USE AirQualityDB;

CREATE TABLE locations(
    location_code VARCHAR(10) PRIMARY KEY,  -- Renamed from location_id for consistency
    location_name VARCHAR(20) NOT NULL,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL
);

CREATE TABLE components(
    component_id VARCHAR(10) PRIMARY KEY,
    description VARCHAR(50) NOT NULL,
    units VARCHAR(5) NOT NULL
);

CREATE TABLE air_quality(
    aqi_uuid CHAR(36) PRIMARY KEY,  
    location_code VARCHAR(10) NOT NULL,
    aqi_value INT NOT NULL,
    measured_at DATETIME NOT NULL,  
    FOREIGN KEY (location_code) REFERENCES locations(location_code),  -- Added foreign key reference
    UNIQUE (location_code, measured_at)
);

CREATE TABLE concentrations(
    concentration_id CHAR(36) PRIMARY KEY,
    aqi_id CHAR(36) NOT NULL,
    component_id VARCHAR(10) NOT NULL,  -- Renamed from component for consistency
    value FLOAT NOT NULL,
    FOREIGN KEY (aqi_id) REFERENCES air_quality(aqi_uuid),
    FOREIGN KEY (component_id) REFERENCES components(component_id),  -- Added foreign key reference
    UNIQUE (aqi_id, component_id)  -- Ensures one value per component for each AQI
);
