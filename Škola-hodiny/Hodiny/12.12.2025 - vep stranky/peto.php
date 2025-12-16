<?php
    $a = $_REQUEST["a"];
    $b = $_REQUEST["b"];
    $c = $_REQUEST["c"];

    if (!is_int($a) and !is_int($b) and !is_int($c)) {
        die("Neboli to cisla");
    }

    $d = $b ** 2 - 4 * $a * $c;

    if ($d > 0) {
        $x1 = (-$b + $d ** 0.5) / 2 * $a;
        $x2 = (-$b - $d ** 0.5) / 2 * $a;
        echo $x1;
        echo "<br>";
        echo $x2;

    } else if ($d == 0) {
        $x1 = (-$b + $d ** 0.5) / 2 * $a;
        echo $x1;
    } else {
        echo "ZLOBA";
    }
?>