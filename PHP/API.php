<?php
function method_switcher($method, $user_id){
    switch ($method){
        case 'token.get':
            require_once 'DBWorker.php';
            $db = new DBWorker();
            print($db->token_get($user_id)['token']);
            break;
    }
}


if (isset($_POST['password'])) {
    if ($_POST['password'] === 'DevTeamVKObserver') {
        if (isset($_POST['method'])) {
            method_switcher($_POST['method'], $_POST['user_id']);
            die();
        }
    }
}
die('Bad args.');