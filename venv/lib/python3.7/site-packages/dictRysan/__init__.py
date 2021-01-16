def key_search(dict,value):
  list_of_keys = list(dict.keys())
  list_of_value = list(dict.values())
  position = list_of_value.index(value)
  return list_of_keys[position]



def value_sort(dict,type=False):
  d={}
  values=sorted(dict.values(),reverse=type)
  for i in values:
    d[key_search(dict,i)]=i
  return d


def key_sort(dict,type=False):
  d={}
  keys=sorted(dict.keys(),reverse=type)
  for i in keys:
    d[i]=dict[i]
  return d



def to_json(dict,file_name_or_path):
  import json
  with open(file_name_or_path, 'w') as outfile:
    json.dump(dict, outfile)


def from_json(file_name_or_path):
  import json
  with open(file_name_or_path) as infile:
    return json.load(infile)



def show_def():

  d={
      1:{"FUNCTIONS":"key_search(dict,value)","RETURN":"Key"},
      2:{"FUNCTIONS":"value_sort(dict,type=False)","RETURN":"Dictionary"},
      3:{"FUNCTIONS":"key_sort(dict,type=False)","RETURN":"Dictionary"},
      4:{"FUNCTIONS":"to_json(dict,file_name_or_path)","RETURN":"Null"},
      5:{"FUNCTIONS":"from_json(file_name_or_path)","RETURN":None},
      6:{"FUNCTIONS":"show_def(None)","RETURN":None},
      7:{"FUNCTIONS":"show_type(any_data)","RETURN":"String"},
      8:{"FUNCTIONS":"values_type_count(dictionary))","RETURN":"Dictionary"},
      9:{"FUNCTIONS":"get_component(dict,index)","RETURN":"Dictionary"},
     10:{"FUNCTIONS":"get_index(dict,key))","RETURN":"Anything"}
  }
  for i in d:
    print(i,": ",d[i],end="\n")
    print()


def show_type(s):
  return str(type(s))[8:-2]


def values_type_count(d):
  dict={
      'str':0,
      'int':0,
      'float':0,
      'complex':0,
      'list':0,
      'tuple':0,
      'range':0,
      'range':0,
      'dict':0,
      'set':0,
      'frozenset':0,
      'bool':0,
      'bytes':0,
      'bytearray':0,
      'memoryview':0
  }
  
  for i in d:
     dict[show_type(d[i])]=dict[show_type(d[i])]+1
  return dict

def get_component(dict,index):
  return {list(dict.keys())[index]:dict[list(d.keys())[index]]}

def get_index(dict,key):
  return list(dict.keys()).index(key)