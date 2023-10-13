CREATE DATABASE IF NOT EXISTS air_pollution;

USE air_pollution;

CREATE TABLE components(
	id varchar(10),
    name varchar(50),
    units varchar(5),
    PRIMARY KEY (id)
);

INSERT INTO components(id, name, units)
VALUES
("co", "Carbon Monoxide", "μg/m3"),
("no", "Nitrogen Monoxide", "μg/m3"),
("no2", "Nitrogen Dioxide", "μg/m3"),
("o3", "Ozone", "μg/m3"),
("so2", "Sodium Dioxide", "μg/m3"),
("pm2_5", "Fine Particle Matter", "μg/m3"),
("pm10", "Coarse Particle Matter", "μg/m3"),
("nh3", "Ammonia", "μg/m3");

CREATE TABLE concentration(
    concentration_id INT AUTO_INCREMENT,
    component_id varchar(10),
    value FLOAT,
    measurement_date DATE DEFAULT (CURRENT_DATE),
    PRIMARY KEY (concentration_id),
    FOREIGN KEY (component_id) REFERENCES components(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

SELECT * FROM concentration;




