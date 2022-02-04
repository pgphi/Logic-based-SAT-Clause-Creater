from corner_clauses import distinct_corner_clauses
from side_clauses import distinct_side_clauses
from middle_clauses import distinct_middle_clauses


def calc_no_of_clauses():
    no_of_clauses = len(distinct_corner_clauses()) \
                    + len(distinct_side_clauses()) \
                    + len(distinct_middle_clauses())
    return no_of_clauses