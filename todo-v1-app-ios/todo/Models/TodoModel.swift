//
//  Todo.swift
//  todo
//
//  Created by Atharva Parkhe on 12/02/22.
//

import Foundation

struct Todo : Codable{
    let id: Int
    let task: String
    let is_completed: Bool
}

struct PostTodo: Codable {
    let task : String
}

struct PatchTodo: Codable {
    let is_completed : Bool
}
