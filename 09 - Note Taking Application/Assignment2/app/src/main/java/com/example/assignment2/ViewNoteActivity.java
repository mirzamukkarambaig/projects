package com.example.assignment2;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdView;
import com.google.android.gms.ads.LoadAdError;
import com.google.android.gms.ads.MobileAds;
import com.google.android.gms.ads.initialization.InitializationStatus;
import com.google.android.gms.ads.initialization.OnInitializationCompleteListener;
import com.google.android.gms.ads.interstitial.InterstitialAd;
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class ViewNoteActivity extends AppCompatActivity {

    private static final String TAG = "ViewNoteActivity";
    String noteStr;
    EditText note;
    Button delete, save, back;
    private AdView mAdView;
    private InterstitialAd mInterstitialAd;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_note);

        note = findViewById(R.id.editNote);
        delete = findViewById(R.id.btnDelete);
        save = findViewById(R.id.btnSave);
        back = findViewById(R.id.btnBack);

        Bundle bundle = getIntent().getExtras();
        String fileName = bundle.getString("FileName");

        //File file = new File(this.getFilesDir(), fileName);

        try
        {
            FileInputStream fis = openFileInput(fileName);
            BufferedReader br = new BufferedReader(new InputStreamReader(fis));
            noteStr = br.readLine();
            note.setText(noteStr);
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }

        save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try
                {
                    FileOutputStream fout = openFileOutput(fileName,MODE_PRIVATE);
                    fout.write(note.getText().toString().getBytes());
                    fout.close();
                    Toast.makeText(ViewNoteActivity.this, "Note Saved Successfully", Toast.LENGTH_SHORT).show();
                }
                catch (Exception e)
                {
                    e.printStackTrace();
                }
                finish();
            }
        });
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
        delete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                File file = new File(getFilesDir(), fileName);
                file.delete();
                Toast.makeText(ViewNoteActivity.this, "Note Deleted Successfully", Toast.LENGTH_SHORT).show();
                finish();
            }
        });
        mAdView = findViewById(R.id.adView3);
        AdRequest adRequest = new AdRequest.Builder().build();
        mAdView.loadAd(adRequest);

        MobileAds.initialize(this, new OnInitializationCompleteListener() {
            @Override
            public void onInitializationComplete(InitializationStatus initializationStatus) {}
        });

        AdRequest adRequest1 = new AdRequest.Builder().build();
        InterstitialAd.load(this,"ca-app-pub-3940256099942544/1033173712", adRequest1,
                new InterstitialAdLoadCallback() {
                    @Override
                    public void onAdLoaded(@NonNull InterstitialAd interstitialAd) {
                        mInterstitialAd = interstitialAd;
                        mInterstitialAd.show(ViewNoteActivity.this);
                    }

                    @Override
                    public void onAdFailedToLoad(@NonNull LoadAdError loadAdError) {
                        mInterstitialAd = null;
                    }
                });
    }
}