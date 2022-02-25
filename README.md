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

Das Spiel ist ein NP-Problem, d.h. es kann in polynomial time gelöst werden (also "sehr sehr schnell").

> Um das Problem durch einen SAT Solver (z.B. https://msoos.github.io/cryptominisat_web/) zu lösen, benötigt man eine Wissensbasis. Eine Wissensbasis enthält alle Klauseln, die alle möglichen Ausgangzustände in Variablen mit True oder False, angeben.


