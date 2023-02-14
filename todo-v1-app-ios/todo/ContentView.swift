import SwiftUI

struct ContentView: View {
    
    @StateObject private var todoListVM = TodoListViewModel()
    
    var body: some View {
        NavigationView{
            VStack{
                Form{
                    Section(header: Text("Add Todo")){
                        HStack{
                            TextField("New Task", text: $todoListVM.newTask)
                            Button {
                                todoListVM.addTodoItem()
                                todoListVM.populateTodoItems()
                            } label: {
                                Text("ADD TODO")
                            }
                        }
                    }
                }.frame(height: 120)
                Spacer()

                Section(header: Text("Todo's")){
                    List(todoListVM.todoItems, id:\.id){ todoItem in
                        HStack{
                            Text(todoItem.task)
                        }
                    }
                }.onAppear{
                    todoListVM.populateTodoItems()
                }
                .refreshable {
                    todoListVM.populateTodoItems()
                }
                Spacer()
            }.navigationTitle("Todo Application")
            
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
