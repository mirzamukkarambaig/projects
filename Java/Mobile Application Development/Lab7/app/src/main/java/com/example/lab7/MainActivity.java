package com.example.lab7;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class MainActivity extends AppCompatActivity {

    Button btnEnter;
    TextView viewCityName, viewTemperature, viewFeelsLike, viewMaxTemperature,
            viewMinTemperature, viewHumidity, viewVisibility, viewWindSpeed, viewWindDirection,
            viewSunriseTime, viewSunsetTime, viewLongitudeValue, viewLatitudeValue,
            viewAltitudeValue, viewSpeedValue;

    double jsonTemperature, jsonFeelsLike, jsonMinTemperature, jsonMaxTemperature,
            jsonHumidity, jsonWindSpeed, jsonWindDirection;

    String  strTemperature, strFeelsLike, strMin, strMax, strHumidity, strWindSp,
            strWindDirec;

    int jsonVisibility, jsonSunrise, jsonSunset, permisisonCode = 555;

    LocationManager lm;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnEnter = findViewById(R.id.btnGetCityName);
        viewCityName = findViewById(R.id.txtgetCityName);
        viewTemperature = findViewById(R.id.getTemperature);
        viewFeelsLike = findViewById(R.id.getFeelsLike);
        viewMaxTemperature = findViewById(R.id.getMaxTemperature);
        viewMinTemperature = findViewById(R.id.getMinTemperature);
        viewHumidity = findViewById(R.id.getHumidity);
        viewVisibility = findViewById(R.id.getVisibility);
        viewWindSpeed = findViewById(R.id.getWindSpeed);
        viewWindDirection = findViewById(R.id.getWindDirection);
        viewSunriseTime = findViewById(R.id.getSunriseTime);
        viewSunsetTime = findViewById(R.id.getSunsetTime);
        viewLongitudeValue = findViewById(R.id.txtViewLongitudeValue);
        viewLatitudeValue = findViewById(R.id.txtViewLatitudeValue);
        viewAltitudeValue = findViewById(R.id.txtViewAltitudeValue);
        viewSpeedValue = findViewById(R.id.txtViewSpeedValue);

        int a = ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION);
        int b = ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION);

        if( a!= PackageManager.PERMISSION_GRANTED && b!= PackageManager.PERMISSION_GRANTED)
        {
            String[] thepermissions = new String[1];
            thepermissions[0]= android.Manifest.permission.ACCESS_FINE_LOCATION;
            this.requestPermissions(thepermissions,permisisonCode);
            return;

        }
        lm = (LocationManager) getSystemService(LOCATION_SERVICE);

        Location loc = lm.getLastKnownLocation(LocationManager.GPS_PROVIDER);
        lm.requestLocationUpdates(LocationManager.GPS_PROVIDER, 1000, 1, new LocationListener() {
            @Override
            public void onLocationChanged(@NonNull Location location) {
                viewLongitudeValue.setText(""+location.getLatitude());
                viewLatitudeValue.setText(""+location.getLongitude());
                viewAltitudeValue.setText(""+location.getAltitude());
                viewSpeedValue.setText(""+(location.getSpeed()*3.6));

                //Runnable Thread from Lab 3
                Runnable r = new Runnable() {
                    @Override
                    public void run() {
                        char[] data = new char[5000];
                        try {
                            URL url = new URL("https://api.openweathermap.org/data/2.5/weather?lat="+location.getLatitude()+"&lon="+location.getLongitude()+"&appid=5f7edfdffa55150b54e76a700a4003fd");
                            InputStream i = url.openStream();
                            BufferedReader buffer = new BufferedReader(new InputStreamReader(i));
                            int dataCount = buffer.read(data);
                            String response = new String(data, 0, dataCount);
                            Log.d("*****OpenWeatherMap API*****", "********** " + response);
                            JSONObject json = new JSONObject(response);
                            JSONObject jsonMain = json.getJSONObject("main");
                            jsonTemperature = jsonMain.getDouble("temp");
                            jsonTemperature = jsonTemperature - 273.15;
                            DecimalFormat decimalFormat = new DecimalFormat("#.##");
                            strTemperature = decimalFormat.format(jsonTemperature);
                            jsonFeelsLike = jsonMain.getDouble("feels_like");
                            jsonFeelsLike = jsonFeelsLike - 273.15;
                            strFeelsLike = decimalFormat.format(jsonFeelsLike);
                            jsonMaxTemperature = jsonMain.getDouble("temp_max");
                            jsonMaxTemperature = jsonMaxTemperature - 273.15;
                            strMax = decimalFormat.format(jsonMaxTemperature);
                            jsonMinTemperature = jsonMain.getDouble("temp_min");
                            jsonMinTemperature = jsonMinTemperature - 273.15;
                            strMin = decimalFormat.format(jsonMinTemperature);
                            jsonHumidity = jsonMain.getDouble("humidity");
                            strHumidity = decimalFormat.format(jsonHumidity);
                            jsonVisibility = json.getInt("visibility");
                            JSONObject jsonWind = json.getJSONObject("wind");
                            jsonWindSpeed = jsonWind.getDouble("speed");
                            strWindSp = decimalFormat.format(jsonWindSpeed);
                            jsonWindDirection = jsonWind.getDouble("deg");
                            strWindDirec = decimalFormat.format(jsonWindDirection);
                            JSONObject jsonSys = json.getJSONObject("sys");
                            jsonSunrise = jsonSys.getInt("sunrise");
                            Date sunRise = new Date(jsonSunrise * 1000L);
                            SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
                            String formattedSunrise = formatter.format(sunRise);
                            jsonSunset = jsonSys.getInt("sunset");
                            Date sunSet = new Date(jsonSunset * 1000L);
                            String formattedSunset = formatter.format(sunSet);
                            //Log.d("*****OpenWeatherMap API*****", "********** Temperature " + jsonTemperature);
                            runOnUiThread(new Runnable() {
                                @Override
                                public void run() {
                                    viewTemperature.setText(strTemperature);
                                    viewFeelsLike.setText(strFeelsLike);
                                    viewMaxTemperature.setText(strMax);
                                    viewMinTemperature.setText(strMin);
                                    viewHumidity.setText(strHumidity);
                                    viewVisibility.setText(""+jsonVisibility);
                                    viewWindSpeed.setText(strWindSp);
                                    viewWindDirection.setText(strWindDirec);
                                    viewSunriseTime.setText(formattedSunrise);
                                    viewSunsetTime.setText(formattedSunset);
                                }
                            });
                        } catch (Exception e) {
                            Log.e("OpenWeatherMap API", "Error fetching data", e);
                        }
                    }
                };
                new Thread(r).start();
            }
        });
    }
}









































