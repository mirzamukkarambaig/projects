package com.example.lab8;

import androidx.appcompat.app.AppCompatActivity;

import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    TextView accel, pressure, light;
    SensorManager sensorManager;
    Sensor pressureSensor;
    Sensor lightSensor;
    Sensor accelerometer;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        accel = findViewById(R.id.valDispAccel);
        pressure = findViewById(R.id.valDispPressure);
        light = findViewById(R.id.valDispLight);

        // Get the sensor service and sensors
        sensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);
        pressureSensor = sensorManager.getDefaultSensor(Sensor.TYPE_PRESSURE);
        lightSensor = sensorManager.getDefaultSensor(Sensor.TYPE_LIGHT);
        accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);

        // Register the sensor listeners
        sensorManager.registerListener(new SensorEventListener() {
            @Override
            public void onSensorChanged(SensorEvent sensorEvent) {
                float pressureValue = sensorEvent.values[0];
                pressure.setText("" + pressureValue + " KP");
            }

            @Override
            public void onAccuracyChanged(Sensor sensor, int i) {

            }
        }, pressureSensor, SensorManager.SENSOR_DELAY_NORMAL);

        sensorManager.registerListener(new SensorEventListener() {
            @Override
            public void onSensorChanged(SensorEvent sensorEvent) {
                float lightValue = sensorEvent.values[0];
                light.setText("" + lightValue + " Lux");
            }

            @Override
            public void onAccuracyChanged(Sensor sensor, int i) {

            }
        }, lightSensor, SensorManager.SENSOR_DELAY_NORMAL);

        sensorManager.registerListener(new SensorEventListener() {
            @Override
            public void onSensorChanged(SensorEvent sensorEvent) {
                float x = sensorEvent.values[0];
                float y = sensorEvent.values[1];
                float z = sensorEvent.values[2];
                accel.setText(" x = "+ x + "\n y = " + y + "\n z = " + z);
            }

            @Override
            public void onAccuracyChanged(Sensor sensor, int i) {

            }
        }, accelerometer, SensorManager.SENSOR_DELAY_NORMAL);

    }
}