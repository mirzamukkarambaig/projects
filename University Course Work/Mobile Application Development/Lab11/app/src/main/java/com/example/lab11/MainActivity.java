package com.example.lab11;

import static android.content.ContentValues.TAG;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {
    Button b;
    TextView v1, v2, v3, v4, v5, v6;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Write a message to the database
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference myRef = database.getReference("Lab11Database");

        b = findViewById(R.id.button);
        v1 = findViewById(R.id.textView8);


        myRef.child("employees").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                // This method is called once with the initial value and again
                // whenever data at this location is updated.
                for (DataSnapshot messageSnapshot: snapshot.getChildren()) {
                    String name=(String)messageSnapshot.child("name").getValue();
                    Object o = messageSnapshot.child("salary").getValue();
                    String nn = o.getClass().getName();
                    Log.d("*****", "***** " + name);
                    v1.setText(name);
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                // Failed to read value
                Log.w(TAG, "Failed to read value.", error.toException());
            }
        });

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Employee e1 = new Employee(1,"Mukkaram","CS",5000.4);

                Employee e2 = new Employee(2,"Nadir","CE",5500.1);

                Employee e3 = new Employee(3,"Faizan","EE",4500.3);

                myRef.child("employees").child("1").setValue(e1);

                myRef.child("employees").child("2").setValue(e2);

                myRef.child("employees").child("3").setValue(e3);
            }
        });
    }
}