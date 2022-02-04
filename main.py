# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Import Modules
    from corner_clauses import distinct_corner_clauses
    from side_clauses import distinct_side_clauses
    from middle_clauses import distinct_middle_clauses
    from no_of_clauses import calc_no_of_clauses

    # Call Methods
    distinct_corner_clauses()
    distinct_side_clauses()
    distinct_middle_clauses()
    print("\nAnzahl aller Klauseln der Eck-, Seiten-, und Mittelzellen mit allen Bombemvariationen =",
          calc_no_of_clauses())