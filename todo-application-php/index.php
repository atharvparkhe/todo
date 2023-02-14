<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "todo";
    
    $conn = mysqli_connect($servername, $username, $password, $dbname);
    
    if(!$conn){
        die(mysqli_connect_error());
    }
    
    $query = "select * from todo;";
    $result = mysqli_query($conn, $query);
    $num = mysqli_num_rows($result);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo App</title>
</head>
<body>
    <center>
        <h1>Todo Application</h1>
        <section id="add-todo">
            <form method="POST" action="">
                <input type="text" placeholder="New Task" name="new_task" required>
                <button type="SUBMIT" name="submit">ADD</button>
            </form>
            <?php
                if(isset($_POST["new_task"])){
                    $new_task = $_POST["new_task"];
                    $num += 1;
                    $insert_query = "INSERT INTO `todo` (`id`, `task`, `is_completed`) VALUES ('$num', '$new_task', '0');";
                    $final_result = mysqli_query($conn, $insert_query);
                    $result = mysqli_query($conn, $query);
                }
            ?>
        </section>
        <section id="todo-list">
            <ul>
                <?php
                    if ($num > 0) {
                        while ($data = mysqli_fetch_assoc($result)){
                            echo "<li>".$data["task"]."</li>";
                        }
                    }
                ?>
            </ul>
        </section>
    </center>
</body>
</html>
