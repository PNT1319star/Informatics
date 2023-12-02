<?php
header('Content-Type: text/html; charset=utf-8');
$a = 10;
$b = 20;
echo "<h2>1.<br></h2>a = $a<br>";
echo "\tb = $b<br>";
$c = $a + $b;
echo "<h2>2.</h2> c = a + b = $c<br>";
$c = $c * 3;
echo "<h2>3.</h2> c = $c<br>";
$c = $c / ($b - $a);
echo "<h2>4.</h2> c = $c<br>";
$p = "Программа";
$b = "работает";
$result = $p ." ". $b;
echo "<h2>6.</h2> $result<br>";
$result .= " "."хорошо";
echo "<h2>7.</h2> $result<br>";
$q = 5;
$w = 7;
// Используем временную переменную для обмена значениями
$temp = $q;
$q = $w;
$w = $temp;
// Выводим результат на экран
echo "<h2>8.</h2> После обмена: \$q = $q, \$w = $w<br>";
//PHP цикл, который выводит числа от 23 до 78.
echo "<h2>9.<br></h2>"; 
for( $i = 23;$i < 79; $i++ )
{
    echo "$i ";
}
echo "<br>";
//PHP цикл, который выводит ненумерованный список из 10 пунктов. 
$items = array();
echo "<h2>10.<br></h2>";
for ($i = 1; $i <= 10; $i++) {
    $items[] = 'Пункт ' . $i;
}

// Перемешиваем массив
shuffle($items);

// Выводим перемешанный массив
foreach ($items as $item) {
    echo '<li>' . $item . '</li>';
}
//Создайте массив из 100 случайных чисел.  Вывести массив, при помощи цикла while, а потом при помощи foreach.
$randomNumbers = array();
for ($i = 0; $i < 100; $i++) {
    $randomNumbers[] = rand(1, 1000); // Генерация случайного числа от 1 до 1000
}

// Выводим массив с использованием цикла while
echo '<h2>11. Вывод массива с использованием цикла while:</h2>';
$counter = 0;
while ($counter < count($randomNumbers)) {
    echo $randomNumbers[$counter] . ', ';
    $counter++;
}

// Выводим массив с использованием цикла foreach
echo '<h2>Вывод массива с использованием цикла foreach:</h2>';

foreach ($randomNumbers as $number) {
    echo  "$number, ";
}
echo "<br>";
//Напишите скрипт, который будет, в зависимости от дня недели, выводить надпись. Например: сегодня среда. Примечание: используйте оператор switch
// Получаем текущий день недели
$dayOfWeek = date("l");

// Используем оператор switch для вывода надписи в зависимости от дня недели
switch ($dayOfWeek) {
    case "Monday":
        $message = "Сегодня понедельник.";
        break;
    case "Tuesday":
        $message = "Сегодня вторник.";
        break;
    case "Wednesday":
        $message = "Сегодня среда.";
        break;
    case "Thursday":
        $message = "Сегодня четверг.";
        break;
    case "Friday":
        $message = "Сегодня пятница.";
        break;
    case "Saturday":
        $message = "Сегодня суббота.";
        break;
    case "Sunday":
        $message = "Сегодня воскресенье.";
        break;
    default:
        $message = "Не удалось определить текущий день недели.";
}

// Выводим сообщение
echo "<h2>12.</h2>";
echo "$message<br>";
//Создать функцию в PHP — getPlus10(), которая будет принимать число и распечатывать сумму этого числа и 10. Выведите результат расчетов на экран.
echo "<h2>13.</h2>";
function getPlus10($number){
    $result = $number + 10;
    return $result;
}
$sum = getPlus10(20);
echo "Result of function getPlus10(20) is $sum<br>";
?>
