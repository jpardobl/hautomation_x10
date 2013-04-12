import pkg_resources

ep = pkg_resources.load_entry_point("hautomation_x10", "cmds", "pl_switch")


ep("a1", "on")
