class QueryMaker:
    def construct_search_query(self):
        conditions = []
        print("This is QueryMaker")

        # Affiliation
        affiliations = input("Enter affiliations separated by commas (press Enter to skip): ").strip()
        if affiliations:
            affiliation_conditions = [f'AFFIL("{affiliation.strip()}")' for affiliation in affiliations.split(",")]
            conditions.append("(" + " OR ".join(affiliation_conditions) + ")")

        # Keywords
        keywords = input("Enter keywords (press Enter to skip): ").strip()
        if keywords:
            conditions.append(f'KEY("{keywords}")')

        # Title
        title = input("Enter title (press Enter to skip): ").strip()
        if title:
            conditions.append(f'TITLE("{title}")')

        # Abstract
        abstract = input("Enter abstract (press Enter to skip): ").strip()
        if abstract:
            abstract_conditions = [f'ABSTRACT("{term.strip()}")' for term in abstract.split(",")]
            conditions.append("(" + " OR ".join(abstract_conditions) + ")")

        # Language
        language = input("Enter language (press Enter to skip): ").strip()
        if language:
            conditions.append(f'LANGUAGE("{language}")')

        search_query = " AND ".join(conditions)
        return search_query.strip()

    def construct_search_query_concise(self):
        conditions =[]
        print ("This is querymaker.construct_search_query_concise()")

        title_abs_key = input("Enter the title_abs_key (keywords for Title, Abstract and Keywords alltogether) (press Enter to skip): ").strip()
        if title_abs_key:
            conditions.append(f'TITLE-ABS-KEY("{title_abs_key}")')

        #Language
        language = input("Enter language (press Enter to skip): ").strip()
        if language:
            conditions.append(f'LANGUAGE("{language}")')

        # PUBYEAR
        if_pubyear = input("Do you want to enter a date/timeframe? (press Enter to skip at input anything to start entering a date): ").strip()
        if if_pubyear:
            start_year = input("Enter the start year you want to search FROM...")
            end_year = input("Enter the end year you want to search UNTIL...")
            conditions.append(f'PUBYEAR > {start_year}')
            conditions.append(f'PUBYEAR < {end_year}')

        search_query = " AND ".join(conditions)
        return search_query.strip()

if __name__ == "__main__":
    query_maker = QueryMaker()
    search_query = query_maker.construct_search_query()
    print("Constructed search query:", search_query)
