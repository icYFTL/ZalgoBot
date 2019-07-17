<?php


class DBWorker
{
    private $host = 'localhost';
    private $username = 'user7180_root';
    private $password = 'Frdf231968123';
    private $db = 'user7180_zalgobot';
    private $mysql;

    function __construct()
    {
        $this->mysql = new mysqli($this->host, $this->username, $this->password, $this->db);
    }

    function user_exists($user)
    {
        $arr = mysqli_fetch_array($this->mysql->query(sprintf("SELECT * FROM userdata WHERE user_id=%d", $user)));
        if (count($arr) > 0)
            return True;
        return False;
    }

    function user_add($user_id, $token)
    {
        if ($this->user_exists($user_id)) {
        $this->user_update($user_id, $token);
        return;
        }

        if ($this->mysql->query("INSERT INTO userdata (user_id, token)
VALUES ($user_id, '$token')") === TRUE) {
            echo "Successful added!";
        } else {
            echo "Error: " . "<br>" . $this->mysql->error;

        }
        $this->mysql->close();
    }

    function user_update($user_id, $token){
    if ($this->mysql->query("UPDATE userdata SET token = '$token' WHERE user_id=$user_id") === TRUE) {
            echo "Successful updated!";
        } else {
            echo "Error: " . "<br>" . $this->mysql->error;

        }
        $this->mysql->close();
    }

    function token_get($user_id){
        $data = mysqli_fetch_array($this->mysql->query(sprintf("SELECT token FROM userdata WHERE user_id=%d", $user_id)));
        $this->mysql->close();


        if ($data !== '')
            return $data;
        return false;
    }


}