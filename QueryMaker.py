class QueryMaker:
    @classmethod
    def construct_best_search_query(self):
        conditions = []
        # Loop for input terms
        while True:
            input_terms = input(
                "Enter terms for TITLE-ABS-KEY separated by commas (press Enter to skip or type 'q' to quit): ").strip()
            if input_terms == '' or input_terms == 'q':
                break
            print("Do you want to join terms with OR or AND?")
            join_type = input("Type 'OR' or 'AND': ").strip().lower()
            term_list = [f'"{term.strip()}"' for term in input_terms.split(",")]
            conditions.append(
                f'TITLE-ABS-KEY({" OR ".join(term_list) if join_type == "or" else " AND ".join(term_list)})')

        # Ask for the start year and end year
        start_year = input("Enter the start year (e.g.,   2012) or press Enter to skip: ").strip()
        end_year = input("Enter the end year (e.g.,   2024) or press Enter to skip: ").strip()

        # Add start year condition if provided
        if start_year:
            conditions.append(f'PUBYEAR > {start_year}')

        # Add end year condition if provided
        if end_year:
            conditions.append(f'PUBYEAR < {end_year}')

        # Join all conditions with 'AND'
        search_query = ' AND '.join(conditions)
        return search_query.strip()
