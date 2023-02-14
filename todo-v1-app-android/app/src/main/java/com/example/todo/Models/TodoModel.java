package com.example.todo.Models;

public class TodoModel{

    public int id;
    public String task;
    public boolean is_completed;

    public TodoModel(int i, String s, boolean b){
        this.id = i;
        this.task = s;
        this.is_completed = b;
    }

}
