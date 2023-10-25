# list --> array, mengakses dengan index
data_list = ['dudung','asep','caki']
print(f"data list: {data_list[1]}\n")

#dictionary (dict) --> associative array
#identifier --> key
data_dict = {
    'manggo' : 'mangga',
    'orange' : 'jeruk',
    'apple' : 'apel',
    'banana' : 'pisang',
    'list' : data_list
}
print(data_dict['key'])
print(data_dict['apple'])
print(data_dict['banana'])
print(data_dict['list'])