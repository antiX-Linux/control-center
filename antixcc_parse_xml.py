#!/usr/bin/python

from xml.dom.minidom import parse

filename = "antixcc.xml"

class AntixccTool:

    def __init__(self, label, icon, action):
        self.label = label
        self.icon = icon
        self.action = action
        pass

    def to_string(self):
        str = "    tool: label: %s icon: %s action: [%s]" % (self.label, self.icon, self.action)
        return str

class AntixccCategory:

    def __init__(self, title, icon):
        self.title = title
        self.icon = icon
        self.tools = []
        pass

    def to_string(self):
        str = "category: title: %s icon: %s\n" % (self.title, self.icon)
        for tool in self.tools:
            str += tool.to_string() + '\n'
        return str

class Antixcc:

    def __init__(self, xml_filename=""):
        self.categories = []
        if xml_filename:
            self.parse(xml_filename)
        
    def parse(self, xml_filename):
        self.dom = parse(xml_filename)
        root = self.dom.getElementsByTagName("antixcc")[0]
        self.title = root.getAttribute('title')
        self.icon = root.getAttribute('icon')
        category_nodes = self.dom.getElementsByTagName("category")
        for n1 in category_nodes:
            attrs = n1.attributes
            title = n1.getAttribute('title')
            icon = n1.getAttribute('icon')
            # print title + " " + icon
            category = AntixccCategory(title, icon)
            self.categories.append(category)
            tool_nodes = n1.getElementsByTagName("tool")
            for n2 in tool_nodes:
                label = n2.getAttribute('label')
                icon = n2.getAttribute('icon')
                action = n2.getAttribute('action')
                tool = AntixccTool(label, icon, action)
                category.tools.append(tool)

    def to_string(self):
        str = ""
        for cat in self.categories:
            str += cat.to_string()
        return str
            
    def list_categories(self):
        pass
        

if __name__ == "__main__":
    antixcc = Antixcc("antixcc.xml")
    print antixcc.to_string()
