# Logic-based-SAT-Clause-Creater
***
This algorithms computes the clauses needed, to solve Minesweeper or check for satisfiability.
***

### SAT-Solver, die auf dem Prinzip der lokalen Suche basieren, führen im Grunde folgende Schritte aus:

    1. Weise jeder Variable einen Zufallswert true oder false zu. 
    2. Wenn alle Klauseln erfüllt sind, terminiere und gebe die Variablenbelegung zurück.
    3. Ansonsten negiere eine Variable und wiederhole.

## Verständliche Erklärung dieses Projekts

- Bei Minesweeper handelt es sich um ein Spiel mit NxM Felder. 
- Hinter jedem Feld ist entweder:
- Die Anzahl der benachbarten Felder mit einer Bombe, 
- oder eine Bombe.
- Das Spiel ist gewonnen, wenn alle Felder aufgedeckt sind, die keine Bombe enthalten.

#### Das Spiel ist ein NP-Problem, d.h. es kann in polynomial time gelöst werden (also "sehr sehr schnell").

> Um das Problem durch einen SAT Solver (z.B. https://msoos.github.io/cryptominisat_web/) zu lösen, benötigt man eine Wissensbasis. Eine Wissensbasis enthält alle Klauseln, die alle möglichen Ausgangzustände in Variablen mit True oder False, angeben. Die Klauseln werden in der KNF (Konjunktiven Normalform) angegeben. D.h. in einer Verknüpfung aller ODER Zeichen mit UND Zeichen. 

- Zum Beispiel Klausel XY := (A OR B) AND (C OR D) = True.

## Konkretes Beispiel

> Wir betrachten eine 6x6 Matrix (LängexBreite). Wir decken das oberste rechte Eckfeld 1x1 auf mit der Zahl 3. Das Eckfeld hat drei Nachbarfelder 1x2, 2x2 und 2x1. Wir wissen, dass jedes Nachbarfeld eine Bombe besitzt. Somit ist die Klausel für alle Eckfelder (drei Nachbarfelder) mit der Zahl 3 (3 Bomben in den Nachbarfelder), wie folgt definiert: Eckfeldklausel_mit_Zahl_3 := Feld_1x2 AND Feld_2x2 AND Feld_2x1 = True. D.h. wenn der beschriebene Fall eintritt, wissen wir, dass auf jeden Fall eine Bombe in den benachbarten Felder liegt.

> Dieses Script gibt all diese Klauseln, für alle möglichen Fälle aus.
