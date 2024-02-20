class QueryMaker3:
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
            # Use the join_type variable here
            conditions.append(f'KEY({" OR ".join(keyword_terms) if join_type == "or" else " AND ".join(keyword_terms)})')

# Usage:
query_maker = QueryMaker3()
search_query = query_maker()
print(search_query)
