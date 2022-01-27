


class BinarySearch:
    def __init__(self, list, element) -> None:
        self.search_list = sorted(list)
        self.element = element
        self.lower = 0
        self.upper = len(list)-1

    def getmidpoint(self):
        return (self.lower + self.upper + 1) // 2 

    def compare_element(self, midpoint):
        if self.search_list[midpoint] > self.element:
            return "Lesser"
        elif self.search_list[midpoint] < self.element:
            return "Greater" 
        else:
            return midpoint 

    def binary_search(self):
        mp = self.getmidpoint()
        result = self.compare_element(mp)
        while True:
            if result == "Greater":
                self.lower = mp
            elif result == "Lesser":
                self.upper= mp
            else:
                return result
            mp = self.getmidpoint()
            result = self.compare_element(mp)



if __name__ == "__main__":
    bs = BinarySearch([1,23,4,5,6,7], 23)
    print(bs.binary_search())


    


    
