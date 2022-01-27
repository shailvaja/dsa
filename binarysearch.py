import re


class BinarySearch:
    def __init__(self, list, element) -> None:
        self.search_list = list
        self.location_list = [range(0,len(self.search_list)-1, 1)]
        self.element = element

    def getmidpoint(self, list):
        list_len = len(list)
        return list_len//2

    def compare_element(self, current_element, element):
        if current_element > element:
            return 0
        elif current_element < element:
            return 1 
        else:
            return current_element
    
    def getlocation(self):
        self.getmidpoint(self.search_list)

    def print_one(self):
        print(self.search_list)


if __name__ == "__main__":
    bs = BinarySearch([1,23,4,5,6,7], 23)
    bs.print_one()


    


    
