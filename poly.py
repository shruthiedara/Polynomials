"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Shruthi Edara, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: se22895
"""

class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        if coeff == 0:
            return 
        if self.head is None or exp > self.head.exp:
            self.head = Node(coeff, exp, self.head)
            return
        previous_term = None
        current_term = self.head
        while current_term is not None and current_term.exp > exp:
            previous_term = current_term
            current_term = current_term.next

        if current_term is not None and current_term.exp == exp:
            current_term.coeff += coeff
            if current_term.coeff == 0:
                if previous_term is None:
                    self.head = current_term.next
                else:
                    previous_term.next = current_term.next
        else:
            add_node = Node(coeff, exp, current_term)
            if previous_term is None:
                self.head = add_node
            else:
                previous_term.next = add_node
                
    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        result = LinkedList()
        poly1 = self.head
        while poly1:
            result.insert_term(poly1.coeff, poly1.exp)
            poly1 = poly1.next
        poly2 = p.head
        while poly2:
            result.insert_term(poly2.coeff, poly2.exp)
            poly2 = poly2.next
        return result


    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        result = LinkedList()
        poly1 = self.head
        while poly1:
            poly2 = p.head
            while poly2:
                coefficient = poly1.coeff * poly2.coeff
                exponent = poly1.exp + poly2.exp
                result.insert_term(coefficient, exponent)
                poly2 = poly2.next
            poly1 = poly1.next
        return result

    # Return a string representation of the polynomial.
    def __str__(self):
        polynomial = self.head
        if polynomial is None:
            return ""
        poly = ""
        while polynomial:
            if polynomial.coeff != 0:
                if poly:
                    poly += " + "
                poly += f"({polynomial.coeff}, {polynomial.exp})"
            polynomial = polynomial.next
        return poly

#def main():
    # read data from stdin (terminal/file) using input() and create polynomial p

    # read data from stdin (terminal/file) using input() and create polynomial q

    # get sum of p and q as a new linked list and print sum

    # get product of p and q as a new linked list and print product
        

#if __name__ == "__main__":
  #  main()
