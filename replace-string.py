import sys;print ''.join(map(lambda line: line.replace(str(sys.argv[1]), str(sys.argv[2])), sys.stdin.readlines()));
