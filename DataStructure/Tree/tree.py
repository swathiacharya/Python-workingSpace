class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def levelNode(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printNode(self):
        spaces = ' ' * self.levelNode() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printNode()
        '''
        print('DATA -->        ',self.data)
        print('CHILDREN LIST-->',self.children)
        # print('PARENT-->       ',self.parent)
        level = self.levelNode()
        print(level)
        '''
    def addChild(self, *childArg):
        for child in childArg:
            self.children.append(child)
            child.parent = self


def buildCompleteTree():
    root  = TreeNode('Electronics')

    # childrens of root node Electronics
    laptop = TreeNode('Laptop')
    mobile = TreeNode('Mobile')
    tab = TreeNode('Tap')
    #root --> 1st child
    '''
    root.addChild(laptop)
    root.addChild(mobile)
    root.addChild(tab)
    '''
    root.addChild(laptop, mobile, tab)

    # add child to the laptop ,mobile ,tap
    # laptop child
    laptop.addChild(TreeNode('Mac'), TreeNode('Ubuntu'), TreeNode('Windows'))
    # laptop.printNode()
    '''
    laptop.addChild(TreeNode('Mac'))
    laptop.addChild(TreeNode('Ubuntu'))
    laptop.addChild(TreeNode('Windows'))
    '''

    # mobile
    mobile.addChild(TreeNode('Android'), TreeNode('Iphone'))
    '''
    mobile.printNode()
    mobile.addChild(TreeNode('Android'))
    mobile.addChild(TreeNode('Iphone'))
    '''

    #Tap
    
    tab.addChild(TreeNode('AndroidVersion'), TreeNode('Ipad'))
    # print(tab.children)
    '''
    tab.printNode()
    tab.addChild(TreeNode('AndroidVersion'))
    tab.addChild(TreeNode('Ipad'))
    '''

    # Ipad.printNode()

    root.printNode()

if __name__ == '__main__':
    buildCompleteTree()
    # print(root.children)
    # # TreeNode.printNode(root)