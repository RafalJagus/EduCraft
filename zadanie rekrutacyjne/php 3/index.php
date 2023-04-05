<?php


class RankingTable
{
    private $players;

    public function __construct($players) //construktor gracza
    {
        $this->players = [];
        foreach ($players as $player) {
            $this->players[$player] = [
                'score' => 0,
                'gamesPlayed' => 0
            ];
        }
    }

    public function recordResult($playerName, $score) // zapisywanie danych gracza
    {
        if (!isset($this->players[$playerName])) {
            throw new Exception('Unknown player');
        }

        $this->players[$playerName]['score'] += $score;
        $this->players[$playerName]['gamesPlayed']++;
    }

    public function playerRank() //sortowanie wedle wytycznych czyli po punktach 
    {
        uasort($this->players, function($a, $b) {
            if ($a['score'] !== $b['score']) {
                return $b['score'] - $a['score'];
            } elseif ($a['gamesPlayed'] !== $b['gamesPlayed']) {
                return $a['gamesPlayed'] - $b['gamesPlayed'];
            } else {
                return 1;
            }
        });

        return array_keys($this->players);
        
    }


    
}




//wywołanie
$table = new RankingTable(array('Jan', 'Maks', 'Monika', 'Rafal' , 'mateusz'));
$table->recordResult('Jan', 2);
$table->recordResult('Maks', 3);
$table->recordResult('Rafal', 4);
$table->recordResult('mateusz', 1);
$table->recordResult('Monika', 5);
//echo $table->playerRank(1); 

echo " Ranking:\n";// zwraca liste graczy od najlepszego do najgorszego 
foreach ($table->playerRank() as $rank => $player) {
    echo $rank + 1 . ". " . $player . "\n";
}
?>


















