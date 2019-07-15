<?php
require 'DBWorker.php';
if (isset($_GET['code'])){
    $code = $_GET['code'];
    $data = json_decode(file_get_contents("https://oauth.vk.com/access_token?client_id=6949573&client_secret=yTy9ne0P6B0MmzZLDLPr&redirect_uri=http://icyftl.ru/ZalgoBot/GetAccess.php&code=$code"));
    $db = new DBWorker();
    $db->user_add($data->{'user_id'}, $data->{'access_token'});
    header('Location: https://vk.com/im?sel=-181269537');
}
else die('Bad args.');

