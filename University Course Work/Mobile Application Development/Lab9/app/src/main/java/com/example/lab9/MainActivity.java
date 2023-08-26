package com.example.lab9;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import android.app.Activity;

import android.content.ClipData;
import android.content.ContentValues;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

    //Permission Code Variables
    int MY_CAMERA_PERMISSION_CODE = 555, CAMERA_REQUEST = 999, requestCode = 000
            , resultCode = 100, PICK_FROM_GALLERY = 333, RESULT_LOAD_IMAGE = 111;

    Uri imageUri;
    Button camera, gallery;

    ImageView photo;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        photo = findViewById(R.id.showPicture);
        camera = findViewById(R.id.btnCamera);
        gallery = findViewById(R.id.btnUpload);

        //Camera Permissions Granted
        if (ActivityCompat.checkSelfPermission(MainActivity.this,
                android.Manifest.permission.CAMERA)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(MainActivity.this,
                    new String[]{android.Manifest.permission.CAMERA},
                    MY_CAMERA_PERMISSION_CODE);
        }

        //External Storage Permissions Granted
        if (ActivityCompat.checkSelfPermission(MainActivity.this,
                android.Manifest.permission.READ_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(MainActivity.this,
                    new String[]{
                            android.Manifest.permission.READ_EXTERNAL_STORAGE,
                            android.Manifest.permission.WRITE_EXTERNAL_STORAGE},
                    PICK_FROM_GALLERY);
        }

        //intent to open camera and take photograph
        camera.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ContentValues values = new ContentValues();
                //values.put(MediaStore.Images.Media.TITLE, "Test Photo Title");
                //values.put(MediaStore.Images.Media.DESCRIPTION, "From your Camera");
                imageUri = getContentResolver().insert(
                        MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values);
                Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                intent.putExtra(MediaStore.EXTRA_OUTPUT, imageUri);
                startActivityForResult(intent, CAMERA_REQUEST);
            }
        });

        //intent to open external storage and bring a photograph
        gallery.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent();
                intent.setType("image/*");
                intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true);
                intent.setAction(Intent.ACTION_GET_CONTENT);
                startActivityForResult(Intent.createChooser(intent,"Select Picture"),
                        RESULT_LOAD_IMAGE);
            }
        });



    }

    //Function to display photograph in the ImageView
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        // receive photo from camera here???

        //To take image form camera
        if (requestCode == CAMERA_REQUEST && resultCode == Activity.RESULT_OK) {
            Bitmap thumbnail;
            String imageurl = "";
            try {
                thumbnail = MediaStore.Images.Media.getBitmap(getContentResolver(), imageUri);
                photo.setImageBitmap(thumbnail);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        //To take image form external storage
        if (requestCode == RESULT_LOAD_IMAGE && resultCode == RESULT_OK && null != data) {
            ClipData mClipData = data.getClipData();
            if (data.getData() != null) {
                Uri selectedImage = data.getData();
                Bitmap bitmap;
                try {
                    bitmap = MediaStore.Images.Media.getBitmap(this.getContentResolver(), selectedImage);
                    photo.setImageBitmap(bitmap);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }

    }
}