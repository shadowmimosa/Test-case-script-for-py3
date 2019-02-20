import jsonpointer

### global variable
null = None
true = True
false = False


def use_jsonpointer(doc, pointer):

    if type(doc) == str and doc != '0':
        if doc == 'None':
            print('The data is null')
            # raise ValueError
            return 'null'
        doc = eval(doc)  ### Change str to dict
    elif type(doc) == dict:
        pass
    else:
        print('The parameter is \'0\'')
        doc_code = "0"
        return doc_code
    
    pointer_in_doc = jsonpointer.resolve_pointer(doc, pointer)

    print('The doc\'s type after change is', type(doc))
    print('The data\'s type after filtering is',
          type(pointer_in_doc))
    print('The data\'s after filtering is',
          pointer_in_doc)


    ### If the data return from Jsonpointer  is string, Changing it.
    if type(pointer_in_doc) == str:
        print('Change Python\'s string to Robot\'s string')
        print('The pointer_in_doc is str and it\'s', pointer_in_doc)
        pointer_in_doc = '\"' + pointer_in_doc + '\"'
        print('The pointer_in_doc is str and it\'s', pointer_in_doc)
    
    # int timestamps
    elif type(pointer_in_doc)==int:
        pass

    ### If the data return from Jsonpointer is null. Returning it.
    elif pointer_in_doc == None:
        print('It\'s Right!!!')
        return 'null'
    elif type(pointer_in_doc) == list:
        pointer_in_doc = str(pointer_in_doc)
        pass
    else:
        pointer_in_doc = str(pointer_in_doc)
        pointer_in_doc = '\"' + pointer_in_doc + '\"'


    print('The data\'s type after filtering and change is',
          type(pointer_in_doc))

    # pointer_in_doc = pointer_in_doc.replace('"', '\\"')
    # pointer_in_doc = pointer_in_doc.replace('\'', '\"')
    # print(pointer_in_doc[0])

    print('The data finally is', pointer_in_doc)

    return pointer_in_doc


def use_self_method(doc, pointer):

    return 'None'


def get_json_value(doc, pointer, change_type=None):

    print('The doc\'s type is', type(doc))
    print('The doc is', doc)
    print('The pointer\' type is', type(pointer))
    print('The pointer is', pointer)

    if change_type == None:
        filter_doc = use_jsonpointer(doc, pointer)
        return filter_doc
    elif change_type == 'self_use':
        filter_doc = use_self_method(doc, pointer)


def to_str(anything):

    print(type(anything))
    print(anything)

    if type(anything) == bytes:
        ### Change anything to str
        anything = anything.decode('utf-8')
        return anything
    elif type(anything) == dict:
        anything = str(anything)
        print(anything)
        return anything
    else:
        return 'YOU ARE WRONG!!'


def to_list(raw_string):

    print(type(raw_string))
    a = 'a'
    print(type(a))
    print(raw_string)

    try:
        obj_list = eval(raw_string)
    except Exception as e:
        print(e)
        print('eval is error')

    print(type(obj_list))

    return obj_list


def get_int(one=None, two=None, three=None, four=None, five=None):

    if two == None and type(one) == str:
        print(type(one))

        if one == '0':
            return one
        new_one = ''
        sign = False

        for word in one:
            print(type(word))
            if word == '0' and sign == False:
                continue
            elif word != '0':
                sign = True
                new_one += word
            else:
                new_one += word

        return new_one
    else:
        pass

    num_list = [one, two, three, four, five]
    new_list = []

    for index in range(len(num_list)):
        if num_list[index] != None:
            new_list.append(int(num_list[index]))
        else:
            continue

    return new_list[0], new_list[1], new_list[2], new_list[3], new_list[4]


def list_or_str(altitude):

    try:
        altitude = altitude.replace('\"', '')
        if type(eval(altitude)) == list or type(eval(altitude)) == str:
            print(
                'In the trying now, altitude\'s type is %s. \nAnd altitude is %s'
                % (type(altitude), altitude))
            length = len(eval(altitude))
            print(length)
            return length != 0
    except:
        print(
            'In the excepting now, altitude\'s type is %s. \nAnd altitude is %s'
            % (type(altitude), altitude))
        return len(altitude)


def log_json(content):
    pass
