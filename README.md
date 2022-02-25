# Logic-based-SAT-Clause-Creater
***
This algorithms computes the clauses needed, to solve Minesweeper or check for satisfiability.
***

### SAT-Solver, die auf dem Prinzip der lokalen Suche basieren, führen im Grunde folgende Schritte aus:

    1. Weise jeder Variable einen Zufallswert true oder false zu. 
    2. Wenn alle Klauseln erfüllt sind, terminiere und gebe die Variablenbelegung zurück.
    3. Ansonsten negiere eine Variable und wiederhole.
