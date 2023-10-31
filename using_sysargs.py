import sys # sys is a reference to the platform in which Python is running
print(sys.platform, sys.version_info)

# sys.argv is a list
# sys.argv[0] is always the name of this module
# any further system arguments are additional members of tis list
# NB they are ALWAYS string values
print(sys.argv)