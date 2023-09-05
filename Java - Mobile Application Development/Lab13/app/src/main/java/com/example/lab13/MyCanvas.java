package com.example.lab13;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.Log;
import android.view.View;
public class MyCanvas extends View {
    int ballX, ballY, ballWidth, ballHeight, ballDeltaX, ballDeltaY;
    int tabX, tabY, tabWidth, tabHeight, tabDeltaX, tabDeltaY;
    int width, height;
    boolean gameOver;
    public MyCanvas (Context context){
        super(context);
        ballX = ballY = 100;
        ballWidth = 100;
        ballHeight = 100;
        ballDeltaX = ballDeltaY = 10;
        tabX = tabY = 100;
        tabWidth = 400;
        tabHeight = 50;
        tabDeltaX = tabDeltaY = 0;
        gameOver = false;
    }
    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        width = canvas.getWidth();
        height = canvas.getHeight();
        tabY = height - 200;
        canvas.drawColor(Color.WHITE);
        Paint red = new Paint();
        red.setColor(Color.RED);
        Paint blue = new Paint();
        blue.setColor(Color.BLUE);
        Paint textPaint = new Paint();
        textPaint.setColor(Color.BLACK);
        textPaint.setTextSize(150);
        Log.d("***", "*** "+width+" - "+height);
        canvas.drawCircle(ballX,ballY,ballWidth/2,red);
        canvas.drawRect(tabX,tabY,tabX + tabWidth,tabY + tabHeight,blue);
//canvas.drawText("Hello",50,50, textPaint);
        if(gameOver == true){
            canvas.drawText("Game Over", 50, 250, textPaint);
        }
    }
}