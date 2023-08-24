package com.example.assignment2;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.google.android.gms.ads.AdError;
import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdView;
import com.google.android.gms.ads.FullScreenContentCallback;
import com.google.android.gms.ads.LoadAdError;
import com.google.android.gms.ads.appopen.AppOpenAd;
import com.google.android.gms.ads.interstitial.InterstitialAd;
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    private static MyApplication myApplication;
    private AdView mAdView;
    private AppOpenAd mAppOpenAd;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageButton add = findViewById(R.id.btnAdd);

        add.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent addNewNote = new Intent(getApplicationContext(), AddNoteActivity.class);
                startActivity(addNewNote);
            }
        });
        mAdView = findViewById(R.id.adView);
        AdRequest adRequest = new AdRequest.Builder().build();
        mAdView.loadAd(adRequest);

        AdRequest request = new AdRequest.Builder().build();
        AppOpenAd.load(
                this, "ca-app-pub-3940256099942544/3419835294", request, new AppOpenAd.AppOpenAdLoadCallback() {

                    @Override
                    public void onAdLoaded(@NonNull AppOpenAd appOpenAd) {
                        mAppOpenAd = appOpenAd;
                        mAppOpenAd.show(MainActivity.this);
                    }

                    @Override
                    public void onAdFailedToLoad(@NonNull LoadAdError loadAdError) { }
                });
    }

    @Override
    protected void onPause() {
        super.onPause();
        LinearLayout l = findViewById(R.id.notesList);
        l.removeAllViews();
    }

    @Override
    protected void onResume() {
        super.onResume();
        LinearLayout l = findViewById(R.id.notesList);

        File root = this.getFilesDir();
        File[] files = root.listFiles();

        TextView[] tvs = new TextView[files.length];

        for (int i=0; i< files.length; i++)
        {
            try
            {
                String fileName = files[i].getName();
                FileInputStream fis = openFileInput(fileName);
                BufferedReader br = new BufferedReader(new InputStreamReader(fis));
                String noteStr = br.readLine();

                tvs[i] = new TextView(getApplicationContext());
                tvs[i].setText(noteStr);
                tvs[i].setTextColor(Color.WHITE);
                tvs[i].setPadding(30,30,30,30);
                tvs[i].setWidth(300);
                l.addView(tvs[i]);

                Bundle bundle = new Bundle();
                bundle.putString("FileName", fileName);
                tvs[i].setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        Intent viewNote = new Intent(getApplicationContext(), ViewNoteActivity.class);
                        viewNote.putExtras(bundle);
                        startActivity(viewNote);
                    }
                });
                Log.d("*********", fileName);
            }
            catch (Exception e)
            {
                e.printStackTrace();
            }
        }
    }
}