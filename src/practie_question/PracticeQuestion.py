def solution(queries):
    value = list()
    response = list()

    add = "ADD"
    exist = "EXISTS"
    remove = "REMOVE"
    get_next = "GET_NEXT"

    for query in queries:
        if query[0] == add:
            value.append(query[1])
            value.sort(key=int)
            response.append("")
        elif query[0] == exist:
            response.append(bool_to__lower_case_string(in_query(query, value)))
        elif query[0] == remove:
            if in_query(query, value):
                value.remove(query[1])
                response.append(bool_to__lower_case_string(True))
            else:
                response.append(bool_to__lower_case_string((in_query(query, value))))
        elif query[0] == get_next:
            response.append(higher_in_query(query, value))

    print(response)

    return response


def in_query(query, value):
    if query[1] in value:
        return True
    else:
        return False


def higher_in_query(query, values):
    for value in values:
        if int(value) > int(query[1]):
            return value
    return ""


def bool_to__lower_case_string(bool):
    return str(bool).lower()
