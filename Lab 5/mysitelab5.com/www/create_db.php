<?php
header('Content-Type: text/html; charset=utf-8');
	//Создать соединение с сервером
	$link = mysqli_connect ("localhost", "root", "2210200313082003t");
	if ($link) {
		echo "Соединение с сервером установлено", "<br>";
	} else {
		echo "Нет соединения с сервером";
	}
	//Создать БД MySiteDB
	//Сначала формирование запроса на создание

	$db = "MySiteDB";
	$query = "CREATE DATABASE $db";
	//Затем реализация запроса на создание. Важна последовательность аргументов функции: соединение с сервером, SQL-запрос.
	$create_db = mysqli_query($link, $query);
	if ($create_db) {
		echo "База данных $db успешно создана";
	} else {
		echo "База не создана";
	}
	# FileName="Connection_php_mysql.htm"
	# Type="MYSQL"
	# HTTP="true"
	
	$localhost = "localhost";
	$db = "MySiteDB";
	$user = "root";
	$password = "2210200313082003t";
	$link = mysqli_connect($localhost, $user, $password) or
	trigger_error(mysql_error(),E_USER_ERROR);

	//trigger_error выводит на страницу сообщение об ошибке. Первый параметр-сообщение об ошибке
	//в строковом виде, в данном случае возвращается функция mysql_error(),	второй - числовой код //ошибки(почти всегда используется значение константы E_USER_ERROR, равное 256)
	//Следующие строки необходимы для того, чтобы MySQL воспринимал кириллицу.
	//Параметры функции mysqli_query(): идентификатор соединения с сервером и запрос SQL
	mysqli_query($link, "SET NAMES cp1251;") or die(mysql_error());
	mysqli_query($link, "SET CHARACTER SET cp1251;") or die(mysql_error());

?>
