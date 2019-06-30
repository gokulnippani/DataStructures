import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # Let us print the files in the directory in which you are running this script
    current_paths = os.listdir(path)

    for curr_path in current_paths:
        full_path = f"{path}/{curr_path}"
        if os.path.isfile(full_path):
            if full_path.endswith(suffix):
                print(full_path)
        else:
            find_files(suffix, full_path)


    return None

find_files('.c','./testdir')