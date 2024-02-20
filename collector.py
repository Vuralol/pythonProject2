def query_finalizer(operation, given_string, string_list):
    if operation == "AND":
        result = 'AND'.join([' ' + word + ' ' for word in string_list])

    elif operation == "OR":
        result = 'OR'.join([' ' + word + ' ' for word in string_list])

    elif operation == "NOT":
        result = f" NOT ({'OR'.join([' ' + word + ' ' for word in string_list])})"

    else:
        # Default to returning the original list as a string if the operation is unknown
        result = " ".join(string_list)

    # Add the given string before and after the result
    result = f"{result}"
    result_not = "NOT"+result

    return '(' + result + ')' + given_string


def termcollector():
    include = True
    parameterlist = []
    while include:
        user_include = input()
        if user_include == 'done':
            include = False
        else:
            parameterlist.append(user_include)
            include = True
    return parameterlist