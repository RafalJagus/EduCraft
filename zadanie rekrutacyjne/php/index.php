<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zadanie Rekrutacyjne</title>
</head>
<body>
    <h1>hello world!</h1>
    <?php

//klasa Pipeline
class Pipeline
{
    public static function make($functions)
    {
        return function ($arg) use ($functions) {  
            foreach ($functions as $function) {
                $result = $function($arg);
            }
            return $arg;
        };
    }
}

// przykładowe uzycie metody zawarte w zadaniu
$pipeline = Pipeline::make(
    function($var) { return $var * 3; },
    function($var) { return $var + 1; },
    function($var) { return $var / 2; }
);
// wywołanie 
echo $pipeline(3);


    ?>
</body>
</html>
