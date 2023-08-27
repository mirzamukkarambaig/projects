package com.example.lab4;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;

public class MainActivity extends AppCompatActivity {

    EditText userText;
    ImageButton btnSaveChanges, btnReset;
    SharedPreferences pref;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        try {
            InputStream in = getResources().openRawResource(R.raw.datafile);
            BufferedReader br = new BufferedReader(new InputStreamReader(in));
            String str = br.readLine();
            Log.d("*****","*****DATA FROM RESOURCE FILE:"+str);
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }

    @Override
    protected void onResume() {
        super.onResume();

        userText = findViewById(R.id.editTextTypeYourMessage);
        btnReset = findViewById(R.id.btnReset);
        btnSaveChanges = findViewById(R.id.btnSaveChanges);

        /*try {


            FileInputStream fileIn = openFileInput("LocalBackUp.txt");
            BufferedReader buffer = new BufferedReader(new InputStreamReader(fileIn));
            String userTxt = buffer.readLine();
            userText.setText(userTxt);
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }*/
        pref = getSharedPreferences("myOwnData", MODE_PRIVATE);
        String getUserTxt = pref.getString("myData", "Data nahi de raha koi!");
        Log.d("****","****DATA LOADED: " + getUserTxt);
        userText.setText(getUserTxt);

        btnReset.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                userText.setText("Write Your Text Here");
            }
        });
    }

    @Override
    protected void onPause() {
        super.onPause();

        /*try {
            FileOutputStream fileOut = openFileOutput("LocalBackUp.txt", MODE_PRIVATE);
            fileOut.write(userText.getText().toString().getBytes());
            fileOut.close();
            Log.d("*****","******DATA WRITTEN TO FILE SUCCESSFULLY ");
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }*/

        SharedPreferences.Editor editor = pref.edit();
        editor.putString("myData", userText.getText().toString());
        editor.commit();
    }
}





