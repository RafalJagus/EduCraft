<?php

class Thesaurus {
    public $thesaurus; //przechowuje słowa

    public function __construct($thesaurus) { //konstruktor
        $this->thesaurus = $thesaurus;
    }

    public function getSynonyms($word) {  // zwraca synonimy dla podanego słowa
        if (isset($this->thesaurus[$word])) {
            $synonyms = $this->thesaurus[$word];
        } else {
            $synonyms = array();
        }

        $result = array(
            "word" => $word,
            "synonyms" => $synonyms
        );

        return json_encode($result); // zwraca tablicę  
    }
}
$thesaurus = new Thesaurus(array( // słownik
    "market" => array("trade"),
    "small" => array("little", "compact")
));

echo $thesaurus->getSynonyms("small"); 
echo $thesaurus->getSynonyms("asleast");
?>
