import Foundation


struct TodoItemsViewMode: Identifiable{
    
    private let todo:Todo
    
    init(todo:Todo){
        self.todo = todo
    }
    
    var task: String {
        todo.task
    }
    
    var is_completed: Bool {
        todo.is_completed
    }
    
    var id: Int{
        todo.id
    }
    
}


class TodoListViewModel: ObservableObject {
    
    @Published var todoItems = [TodoItemsViewMode]()
    
    @Published var taskStatus = ""
    
    var newTask : String = ""
    
    func populateTodoItems(){

        WebService().getAllTodos() { result in
            switch result{
                case .success(let todos):
                DispatchQueue.main.async {
                    self.todoItems = todos.map(TodoItemsViewMode.init)
                }
                case .failure(let error):
                    print(error.localizedDescription)
            }
        }
    }
    
    func addTodoItem(){
        WebService().addTodo(inp: newTask){ result in
            switch result{
            case .success(let task):
                print(task)
            case.failure(let error):
                print(error.localizedDescription)
            }
        }
    }
}

