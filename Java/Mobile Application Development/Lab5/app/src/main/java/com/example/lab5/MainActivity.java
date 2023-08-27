package com.example.lab5;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import java.io.File;
import java.io.FileWriter;

public class MainActivity extends AppCompatActivity {

    Button btnInternal, btnExternal, btnCache;
    char [] d;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnInternal = findViewById(R.id.btnInternal);
        btnExternal = findViewById(R.id.btnExternal);
        btnCache = findViewById(R.id.btnCache);

        d = new char[1048576]; // 1 MB = 1048576 B
        for( int i=0; i<d.length; i++)
        {
            d[i] = 'M';
        }
        String data = new String(d);

        btnInternal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {


                        try {
                            File dir = getFilesDir();
                            File internalFile = new File(dir, "myInternalFile.txt");
                            FileWriter fw = new FileWriter(internalFile);
                            for(int i=0; i<200; i++)
                                fw.write(data);
                            fw.close();
                        }
                        catch (Exception e){
                            e.printStackTrace();
                        }


            }
        });

        btnCache.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Thread t = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            File dir = getCacheDir();
                            File f = new File(dir,"myCacheFile.txt");
                            FileWriter fw = new FileWriter(f);
                            for(int i=0; i<100; i++)
                                fw.write(data);
                            fw.close();
                        }
                        catch (Exception e)
                        {
                            e.printStackTrace();
                        }
                    }
                });
            }
        });

        btnExternal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    File dir = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOCUMENTS);
                    File stringData = new File(dir, "mySuccessString.txt");
                    FileWriter fw = new FileWriter(stringData);
                    fw.write("Data Written Successfully");
                    fw.close();
                }
                catch(Exception e)
                {
                    e.printStackTrace();
                }

            }
        });
    }
}



