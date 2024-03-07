import ApiAccess
from QueryMaker import QueryMaker
from searchtermmanager import SearchManager
import FileSorter
# ------------------------------------------------------

query_maker = QueryMaker()
search_query2 = query_maker.construct_best_search_query()

ApiAccess.perform_search(search_query2)

sorter = FileSorter.FileSorter()
sorter()

# Continue with the rest of your program
#search_manager = SearchManager()
#search_manager.perform_search()
#search_manager.display_results()
