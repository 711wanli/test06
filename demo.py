from base import analyze_file


# [("1", "2"), ("3", "4")]
# [{'username': 'xiaoming', 'password': 'xiaoming123'}, {'username': 'xiaohong', 'password': 'xiaohong'}]
def analyze_file_with_key(key):
    script_data = analyze_file("search_data")[key]
    script_list = list()
    for i in script_data.values():
        script_list.append(i)
    print(script_list)




    # list_data = list()
    # for i in script_data.values():
    #     script_list_data = list()
    #     for j in i.values():
    #         script_list_data.append(j)
    #     list_data.append(script_list_data)
    # print(list_data)

    # for j in i.values():
    #     script_list_data.append(j)
    #
    # # list_data.append(script_list_data)
    # print(script_list_data)


    # return



if __name__ == '__main__':
    analyze_file_with_key("test_login")
