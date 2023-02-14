import Foundation

enum NetworkErrors: Error{
    case decodingError
    case badRequest
    case otherErrors(errorMessage: String)
}

struct TaskBody : Codable {
    let task : String
    let is_completed : Bool
}

struct TaskResponse : Codable {
    let id: Int
    let task : String
    let is_completed : Bool
}


class WebService{
    
    func getAllTodos(completion: @escaping (Result<[Todo], NetworkErrors>) -> Void){
        guard let url = URL(string: "https://django-todo-v1.herokuapp.com/api/todo/") else {
            completion(.failure(.otherErrors(errorMessage: "Incorrect URL")))
            return
        }
        URLSession.shared.dataTask(with: url) { data, response, error in
            guard let data=data, error == nil, (response as? HTTPURLResponse)?.statusCode == 200 else{
                completion(.failure(.badRequest))
                return
            }
            let todos = try?  JSONDecoder().decode([Todo].self, from: data)
            completion(.success(todos ?? []))
        }.resume()
    }
    
//    func fetchAllTodos() async throws -> [Todo]{
//        guard let url = URL(string: "https://django-todo-v1.herokuapp.com/api/todo/") else {
//            throw NetworkErrors.badRequest
//        }
//
//        let (data, _) = try await URLSession.shared.data(from: url)
//        let todoResponse = try? JSONDecoder().decode([Todo].self, from: data)
//        return todoResponse ?? []
//
//    }
    
    func addTodo(inp:String, completion: @escaping (Result<TaskResponse, NetworkErrors>) -> Void){
        guard let url = URL(string: "https://django-todo-v1.herokuapp.com/api/todo/") else {
            completion(.failure(.badRequest))
            return
        }
        let body = TaskBody(task: inp, is_completed: false)
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try? JSONEncoder().encode(body)
        URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data=data, error == nil else{
                completion(.failure(.otherErrors(errorMessage: "No Data")))
                return
            }
            guard let TaskResponse = try? JSONDecoder().decode(TaskResponse.self, from: data) else{
                completion(.failure(.badRequest))
                return
           }
            completion(.success(TaskResponse))
        }.resume()
        
    }
}
