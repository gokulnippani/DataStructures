class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is None:
        print('Invalid Group')
        return

    if not user:
        print('Invalid User.')
        return

    users = group.get_users()
    for u in users:
        if u == user:
            return True
    child_groups = group.get_groups()
    for child in child_groups:
        if is_user_in_group(user, child):
            return True
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", sub_child))
# Should return true
print(is_user_in_group("sub_child_user", child))
# Should return true
print(is_user_in_group("sub_child_user", parent))
# Should return true

print(is_user_in_group("sub_child_user", None))
# Should return invalid group

print(is_user_in_group("", parent))
# Should return invalid user