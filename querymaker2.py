class QueryMaker:
    def __init__(self):
        print("This is QueryMaker")

    def __call__(self):
        conditions = []
        print("This is QueryMaker")

        # Keywords
        while True:
            keywords = input(
                "Enter keywords separated by commas (press Enter to skip or type 'q' to quit): ").strip()
            if keywords == '':
                break
            if keywords == 'q':
                return ''
            print("Do you want to join keywords with OR or AND?")
            join_type = input("Type 'OR' or 'AND': ").strip().lower()
            keyword_terms = [f'"{keyword.strip()}"' for keyword in keywords.split(",")]
            conditions.append(f'KEY({" OR ".join(keyword_terms)})')

            # Title
            while True:
                title = input(
                    "Enter title(s) separated by commas (press Enter to skip or type 'q' to quit): ").strip()
                if title == '':
                    break
                if title == 'q':
                    return ''
                print("Do you want to join title terms with OR or AND?")
                join_type = input("Type 'OR' or 'AND': ").strip().upper()
                title_terms = [f'"{title_part.strip()}"' for title_part in title.split(",")]
                conditions.append(f'TITLE({" OR ".join(title_terms)})')

        # Abstract
        while True:
            abstract = input(
                "Enter abstract separated by commas (press Enter to skip or type 'q' to quit): ").strip()
            if abstract == '':
                break
            if abstract == 'q':
                return ''
            print("Do you want to join abstract terms with OR or AND?")
            join_type = input("Type 'OR' or 'AND': ").strip().lower()
            abstract_terms = [f'"{term.strip()}"' for term in abstract.split(",")]
            conditions.append(f'ABS({" OR ".join(abstract_terms)})')
        search_query = " AND ".join(conditions)

        return search_query.strip()


# Usage:
query_maker = QueryMaker()
search_query = query_maker()
print(search_query)
