class RouteTrieNode(object):
    def __init__(self):
        self.handler = None
        self.children = {}


class RouteTrie(object):
    def __init__(self, roothandler, notfoundhandler):
        self.root = RouteTrieNode()
        children = RouteTrieNode()
        children.handler = roothandler
        self.root.children[""] = children
        self.notfoundhandler = notfoundhandler

    def insert(self, words, handler):
        """
        Add `word` to trie
        """
        current_node = self.root

        for word in words:
            if word not in current_node.children:
                current_node.children[word] = RouteTrieNode()
            current_node = current_node.children[word]

        current_node.handler = handler

    def exists(self, words):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for word in words:
            if word not in current_node.children:
                return self.notfoundhandler
            current_node = current_node.children[word]

        if current_node.handler == None:
            return self.notfoundhandler
        return current_node.handler

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, roothandler, notfoundhandler):
        self.routes = RouteTrie(roothandler, notfoundhandler)

    def add_handler(self, path,handler):
        words = self.split_path(path)
        self.routes.insert(words, handler)

    def lookup(self, path):
        if "/" not in path:
            print("Invalid path")
            return
        words = self.split_path(path)
        return self.routes.exists(words)


    def split_path(self, path):
        if path.endswith("/"):
            path = path[:-1]
        return path.split('/')

router = Router("root handler","not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("aa"))