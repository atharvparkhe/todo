package com.example.todo.Adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.todo.Models.TodoModel;
import com.example.todo.R;

import java.util.ArrayList;

public class RecyclerTodoAdapter extends RecyclerView.Adapter<RecyclerTodoAdapter.ViewHolder> {

    Context context;
    ArrayList<TodoModel> allTasks;

    public  RecyclerTodoAdapter(Context c, ArrayList<TodoModel> arr){
        this.context = c;
        this.allTasks = arr;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(context).inflate(R.layout.todo_row, parent, false);
        return new ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        holder.todo_textView.setText(allTasks.get(position).task);
        holder.todo_CheckBox.setChecked(allTasks.get(position).is_completed);
    }

    @Override
    public int getItemCount() {
        return allTasks.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder{

        TextView todo_textView;
        CheckBox todo_CheckBox;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            todo_textView = itemView.findViewById(R.id.task);
            todo_CheckBox = itemView.findViewById(R.id.todo_checkbox);
        }
    }

}
