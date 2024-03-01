import ApiAccess
from querymaker5 import querymaker5
from searchtermmanager import SearchManager
from querymaker import QueryMaker  # Assuming your QueryMaker class is in querymaker.py

# Create an instance of QueryMaker and execute it
#query_maker = QueryMaker()
#search_query = query_maker.construct_search_query()
#print("Constructed search query:", search_query)


query_maker = querymaker5()
search_query2 = query_maker.construct_best_search_query()

ApiAccess.perform_search(search_query2)


# Continue with the rest of your program
search_manager = SearchManager()
search_manager.perform_search()
search_manager.display_results()


# print(querymaker.construct_search_query())
