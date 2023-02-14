package com.example.todo;

import android.os.Bundle;
import android.util.Log;
import android.widget.ListView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import com.example.todo.Adapters.RecyclerTodoAdapter;
import com.example.todo.Models.TodoModel;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;


public class MainActivity extends AppCompatActivity {

    String BASE_URL = "https://django-todo-v1.herokuapp.com/api/todo/";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ArrayList<TodoModel> todo_items = new ArrayList<>();

        RequestQueue queue = Volley.newRequestQueue(this);

        JsonArrayRequest jsonArrayRequest = new JsonArrayRequest(Request.Method.GET, BASE_URL, null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        try{
                            for (int i=0; i<response.length(); i++){
                                JSONObject obj = response.getJSONObject(i);
                                todo_items.add(new TodoModel(obj.getInt("id"), obj.getString("task"), obj.getBoolean("is_completed")));
                                Log.d("API", "RESPONSE : " + i);
                            }
                        } catch (JSONException e){
                            Log.d("API", "ERROR : " + e);
                            e.printStackTrace();
                        }
                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.d("API", "ERROR : " + error.toString());
                    }
                });
        queue.add(jsonArrayRequest);

        RecyclerView recyclerView = findViewById(R.id.all_todos);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        RecyclerTodoAdapter adapter = new RecyclerTodoAdapter(this, todo_items);
        recyclerView.setAdapter(adapter);

    }
}