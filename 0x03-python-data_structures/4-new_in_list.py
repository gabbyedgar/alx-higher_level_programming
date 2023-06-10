#!/usr/bin/python3
def new_in_list(my_list, idx, element):
  new_list = [i for i in my_list]

  if idx < len(new_list) and idx > -1:
      new_list[idx] = element
        return new_list
