package com.example.pdm_lab2;

import android.support.v7.app.AppCompatActivity;
import android.widget.ImageView;
import android.os.Bundle;
import android.widget.Button;
import android.view.View;

import java.util.Vector;
import android.view.ViewGroup;
import android.content.Context;
import android.view.LayoutInflater;
import android.widget.TextView;
import android.view.animation.AlphaAnimation;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    Button button1, button2;
    ImageView image;
    ViewGroup m_my_list;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        m_my_list = (ViewGroup) findViewById(R.id.list);
        LayoutInflater l = (LayoutInflater) getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        Vector<String> strings = new Vector<String>();
        for(int i=0; i<20; ++i) {
            strings.add("Item " + i);
        }

        for(String s : strings) {
            View item = l.inflate(R.layout.list_item, null);
            ((TextView) item.findViewById(R.id.itemtext)).setText(s);
            m_my_list.addView(item);
        }

        findViewById(R.id.button).setOnClickListener(this);

        button1 = (Button) findViewById(R.id.button2);
        button2 = (Button) findViewById(R.id.button3);
        image = (ImageView) findViewById(R.id.image);
    }

    public void onClick(View v) {
        Toast.makeText(getApplicationContext(),
                "You started searching",
                Toast.LENGTH_SHORT).show();
    }

    public void showImage(View v) {
        image = (ImageView) findViewById(R.id.image);

        AlphaAnimation animation1 = new AlphaAnimation(0.0f, 1.0f);
        animation1.setDuration(200);
        animation1.setFillAfter(true);

        image.startAnimation(animation1);
    }

    public void hideImage(View v) {
        image = (ImageView) findViewById(R.id.image);

        AlphaAnimation animation1 = new AlphaAnimation(1.0f, 0.0f);
        animation1.setDuration(200);
        animation1.setFillAfter(true);

        image.startAnimation(animation1);
    }
}
