import pickle

class Stack():
    def __init__(self):
        self.data=[]
    def push(self,a):
        self.data.append(a)
    def size(self):
        return len(self.data)
    def pop(self):
        if len(self.data)==0:
            raise 'stack is empty'
        else:
            return self.data.pop()
    def is_empty(self):
        return self.size==0

class BinaryTree():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def insert_left(self,new_data):
        if self.left is None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.left = self.left
            self.left = t
    def insert_right(self,new_data):
        if self.right is None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.right = self.right
            self.right = t
    def setRoot(self,val):
        self.data=val
    def getRightChild(self):
        return self.right
    def getLeftChild(self):
        return self.left
    def getRoot(self):
        return self.data

def build_tree(list):  # bulid a tree of your expression
    stack=Stack()
    final_tree=BinaryTree('')
    stack.push(final_tree)

    for i in list:
        if i == '(':
            final_tree.insert_left('')
            stack.push(final_tree)
            final_tree = final_tree.getLeftChild()
        elif i not in ['+','-','*','/'] and i != ')':
            j=int(i)
            final_tree.setRoot(j)
            final_tree = stack.pop()

        elif i in ['+','-','*','/']:
            final_tree.setRoot(i)
            final_tree.insert_right('')
            stack.push(final_tree)
            final_tree = final_tree.getRightChild()
        elif i == ')':
            final_tree = stack.pop()
        else:
            raise ValueError
    return final_tree


import operator
def evaluate(parseTree):     # to calculate the result
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = opers[parseTree.getRoot()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRoot()

def print_exampleTree(list1):    # to visualise the generated binary tree
    a = 0
    for i in range(len(list1)):
        if list1[i] == '(':
            a += 1
        elif list1[i] == ')':
            a -= 1
        elif list1[i] in ['+','-','*','/']:
            print('  '*(a-1)+list1[i])
        elif list1[i] not in ['+','-','*','/','(',')']:
            print('  '*a+list1[i])

def is_matched(list1):   # determine whether brackets are matched
    a = 0
    b = 0
    c = 0
    for i in range(len(list1)):
        if list1[i] == '(':
            a += 1
        if list1[i] == ')':
            b += 1
        if list1[i] in ['+','-','*','/']:
            c+=1
    if a==c and a==b:
        return ''
    else:
        return 'Not a valid expression, brackets mismatched.'


def is_valid(list1):
    for i in range(1,len(list1)):
        if (list1[i] not in ['+','-','*','/','(',')']) and (list1[i-1] in ['+','-','*','/']) and (list1[i+1] in ['+','-','*','/']):
            return 'Not a valid expression, wrong number of operands'
        if (list1[i] not in ['+','-','*','/','(',')']) and (list1[i-1]=='(') and (list1[i+1]==')'):
            return 'Not a valid expression, wrong number of operands'
        if (list1[i] not in ['+','-','*','/','(',')']) and (list1[i-1]=='(') and (list1[i+1]=='('):
            return 'Not a valid expression, operator missing'
    else:
        return ''

class Call_func():
    def call(self):
        list1 = []
        equation = input('please input a equation')
        for a in equation:
            list1.append(a)
        print(list1)

        test1=is_matched(list1)
        print(test1)
        test2=is_valid(list1)
        print(test2)

        if test1=='' and test2=='':
            example1=build_tree(list1)
            outcome=evaluate(example1)
            print('the result is {}'.format(outcome))
            print_exampleTree(list1)

        f = pickle.dumps(build_tree(list1))
        read_f=pickle.loads(f)
        print(read_f)

if __name__=='__main__':
    a=Call_func()
    a.call()
