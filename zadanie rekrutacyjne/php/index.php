<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zadanie Rekrutacyjne</title>
</head>
<body>

    <?php

//klasa Pipeline
class Pipeline
{
    public static function make(...$functions)
    {
        return function ($arg) use ($functions) {
            $result = $arg;  
            foreach ($functions as $function) {
                $result = $function($result);
            }
            return $result;
        };
    }
}
//klasa TextInput
class TextInput{
    public $container = '';

    public function add($text) {
        $this->container .= $text;
    }
    
    public function getValue() {
        return $this->container;
    }   
}
class NumericInput extends TextInput { // Funkcja rozszerza Class TextInput i jezeli Uzytkownik wpisze w input wartość tekstową to go ignoruje
    public function add($text) {
        if (is_numeric($text)) {
            parent::add($text);
        }
    }
}



// wywołanie 
$pipeline = Pipeline::make( //przykładowe uzycie metody zawarte w zadaniu
    function($var) { return $var * 3; },
    function($var) { return $var + 1; },
    function($var) { return $var / 2; }
);
echo 'Wartość z Zadania pierwszego : ', $pipeline(3);

$input = new NumericInput();

    ?>

    <h1>hello world!</h1>

    <form action="index.php" method="post">
    <label for="text">1</label>
    <input type="text" name="text"><br><br>

    <label >2</label>
    <input type="number" name="numer"><br><br>
    <input type="submit" value="Submit">
    </form>

    <p>Podana wartość: <?php echo $_POST["text"]; $input->add($_POST["text"]); ?><?php echo $_POST["numer"]; $input->add($_POST["numer"]);?>  </p>


    <p>Podana wartość tylko liczby <?php echo $input->getValue();?> </p>
</body>
</html>
