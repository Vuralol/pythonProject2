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

if __name__ == "__main__":
    query_maker = QueryMaker()
    search_query = query_maker.construct_search_query()
    print("Constructed search query:", search_query)
