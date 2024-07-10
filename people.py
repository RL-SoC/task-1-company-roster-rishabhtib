"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############

engineer_roster = []  # A list of all instantiated engineer objects
sales_roster = []     # List of all instantiated sales objects
branchmap = {         # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str    # Type hints : provides the information about the type of variable
    age : int     # Type hints : indicates age is expected to be integer
    ID : int
    city : str
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 
    # '\' indicates that argument list continues on the next line: line continuation characacter       
    def __init__(self, name, age, ID, city, branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:   # Return annotations : '-> bool' indicates that the function returns a boolean value
        if self.city!= new_city:      # Change the city 
            self.city = new_city 
            return True
        return False       # Return true if city change, successful, return false if city same as old city
        

    def migrate_branch(self, new_code:int) -> bool:
        if len(self.branches) == 1:
            old_branch = self.branches[0]                            # Should work only on those employees who have a single 
            if branchmap[old_branch]["city"] == branchmap[new_code]["city"]:   # branch to report to. Fail for others.
                self.branches = [new_code]                                   # Change old branch to new if it is in the same city, else return false.
                return True
        return False          
    
    

    def increment(self, increment_amt: int) -> None:
        self.salary += increment_amt # Increment salary by amount specified.
    




class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        if position in ["Junior", "Senior", "Team Lead", "Director"]:
            self.position = position
        else:
            self.position = "Junior"
 
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 

    
    def increment(self, amt:int) -> None:
        bonus =  amt*0.1  # While other functions are the same for and engineer,
        super.increment(amt+bonus)       # and increment to an engineer's salary should add a 10% bonus on to "amt"
        
        
    def promote(self, position:str) -> bool:
      hierarchy = ["Junior", "Senior", "Team Lead", "Director"]
      if position in hierarchy and hierarchy.index(position) > hierarchy.index(self.position):
        self.position = position
        self.increment(0.3 * self.salary)
        return True
      return False  # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
       



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to

    def __init__(self, name, age, ID, city, branchcodes, superior=None, position="Rep", salary=None):
        super().__init__(name, age, ID, city, branchcodes, salary)
        self.superior = superior
        if position in ["Rep", "Manager", "Head"]:
            self.position = position
        else:
            self.position = "Rep"     # Complete all this! Add arguments
        
    
    # def promote 
    def promote(self, position: str) -> bool:
        hierarchy = ["Rep", "Manager", "Head"]
        if position in hierarchy and hierarchy.index(position) > hierarchy.index(self.position):
            self.position = position
            self.increment(0.3 * self.salary)
            return True
        return False
    
    # def increment
    def increment(self, amt: int) -> None:
        bonus = amt * 0.05
        super().increment(amt + bonus) 

    def find_superior(self) -> tuple[int, str]:
         if self.superior is not None:
            for employee in engineer_roster + sales_roster:
                if employee.ID == self.superior:
                    return employee.ID, employee.name
         return None, None

        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        

    def add_superior(self) -> bool:
        hierarchy = ["Rep", "Manager", "Head"]
        next_position = hierarchy[hierarchy.index(self.position) + 1] if self.position != "Head" else None
        if next_position:
            for employee in sales_roster:
                if employee.position == next_position and employee.city == self.city:
                    self.superior = employee.ID
                    return True
        return False # Add superior of immediately higher rank.
                     # If superior doesn't exist return false,
       


    def migrate_branch(self, new_code: int) -> bool:
        self.branches.append(new_code)
        return True      # This should simply add a branch to the list; even different cities are fine
        

    





    
    