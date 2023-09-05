package com.example.lab13;

import androidx.appcompat.app.AppCompatActivity;

import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        MyCanvas c = new MyCanvas(getApplicationContext());

        SensorManager sm = (SensorManager)getSystemService(SENSOR_SERVICE);

        Sensor accelerometer = sm.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        sm.registerListener(new SensorEventListener() {
            @Override
            public void onSensorChanged(SensorEvent sensorEvent) {
                float[] v = sensorEvent.values;
                if(v[0] < -2) {
                    if (c.tabX + c.tabWidth < c.width)
                        c.tabDeltaX = 10;
                    else
                        c.tabDeltaX = 0;
                }
                if(v[0] > 2) {
                    if (c.tabX > 10)
                        c.tabDeltaX = -10;
                    else
                        c.tabDeltaX = 0;
                }
                if(v[0] < 2 && v[0] > -2)
                    c.tabDeltaX = 0;
            }

            @Override
            public void onAccuracyChanged(Sensor sensor, int i) {

            }
        }, accelerometer, sm.SENSOR_DELAY_GAME);

        setContentView(c);

        Thread t = new Thread(new Runnable() {
            @Override
            public void run() {
                while(true){
                    try {
                        Thread.sleep(42);
                    }catch (InterruptedException e){
                        throw new RuntimeException(e);
                    }

                    c.tabX = c.tabX + c.tabDeltaX;
                    c.ballX += c.ballDeltaX;
                    if(c.ballX+c.ballWidth/2 > c.width)
                        c.ballDeltaX *= -1;
                    if(c.ballX < 0)
                        c.ballDeltaX *= -1;

                    c.ballY += c.ballDeltaY;
                    if(c.ballY > c.height)
                        c.gameOver = true;
                    else
                        c.gameOver = false;
                    if(c.ballY+c.ballHeight < 0)
                        c.ballDeltaY *= -1;

                    if(c.ballY + c.ballHeight/2 >= c.tabY && c.ballY - c.ballHeight/2 < c.tabY + c.tabHeight){
                        if(c.ballX > c.tabX && c.ballX < (c.tabX + c.tabWidth)){
                            c.ballDeltaY *= -1;
                        }
                    }

                    c.invalidate();
                }
            }
        });
        t.start();
    }
}