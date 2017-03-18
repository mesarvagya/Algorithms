
def HanoiTower(n, origin, destination, helper):
	if n > 1:
		HanoiTower(n-1, origin, helper, destination)
		print "Moved a plate from Origin(peg# {0}) to Destination(peg# {1})".format(origin, destination)
		HanoiTower(n-1, helper, destination, origin)
	else:
		print "Moved a plate from Origin(peg# {0}) to Destination(peg# {1})".format(origin, destination)

print HanoiTower(3, 1, 2, 3)