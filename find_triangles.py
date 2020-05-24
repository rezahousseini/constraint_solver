from typing import Set, List

#def law_of_sines(a,b,b,gamma<y):
#
#
#def law_of_cosines():

class Constraint:
    def __init__(self, points: Set[str]) -> None:
        self.points = points
        self.value = lambda v: v

    def __repr__(self):
        return "%s" % (self.points)

class AngleConstraint(Constraint):
    def __init__(self, direction: List[str]) -> None:
        self.direction = direction
        self.points = set(direction) # make a set

class DistanceConstraint(Constraint): pass


class Triangle:
    def __init__(self, points: Set[str], dist_constraints: List[DistanceConstraint],
                 angle_constraints: List[AngleConstraint]) -> None:
        self.points = points
        self.given_dist_constraints = dist_constraints
        self.given_angle_constraints = angle_constraints
        num_dist_constraints = len(dist_constraints)
        num_angle_constraints = len(angle_constraints)
        num_constraints = (num_dist_constraints, num_angle_constraints)
        if   num_constraints == (1, 2):
            self.derived_angle_constraint = self.given_angle_constraints[0]
        #elif num_constraints == (1, 3):
        #elif num_constraints == (2, 1):
        #elif num_constraints == (2, 2):
        #elif num_constraints == (2, 3):
        #elif num_constraints == (3, 0):
        #elif num_constraints == (3, 1):
        #elif num_constraints == (3, 2):
        #elif num_constraints == (3, 3):
        #else:
        #    raise ValueError("Too few constraints, triangle is undefined")
        #self.derived_constraints

    def __repr__(self):
        return "%s, %s, %s" % (self.points, self.given_dist_constraints,
                               self.given_angle_constraints)


def find_tri(dist_constraints, angle_constraints):
    triangles = find_angle_triangles(dist_constraints, angle_constraints)
    # find triangles only consisting of dist constraints
    while len(dist_constraints) > 0:
        dc1 = dist_constraints.pop(0)
        temp_dist_constraints = dist_constraints.copy()
        # cycle through the remaining constraints to find a match
        for dc2 in temp_dist_constraints:
            # continue if dist constraints c1 and c2 share a common point
            if len(dc1.points & dc2.points) == 1:
                # only continue if triangle was not already found above
                if not any([True for triangle in triangles
                            if dc1.points | dc2.points == triangle.points]):
                    # search the missing side in the remaining constraints
                    dc3 = DistanceConstraint(dc1.points ^ dc2.points)
                    for dc3 in temp_dist_constraints:
                        if (dc1.points ^ dc2.points) == dc3.points:
                            triangles.append(Triangle(dc1.points | dc2.points | dc3.points,
                                                      [dc1, dc2, dc3], []))
                            temp_dist_constraints.remove(dc3)
    return triangles

def find_angle_triangles(dist_constraints, angle_constraints):
    triangles = []
    # find triangles formed by angle and dist constraints
    for ca in angle_constraints:
        additional_constraints = []
        # find dist constraints which belong to the same triangle as the angle constraint
        for cd in dist_constraints:
            if set(ca.points).issuperset(cd.points):
                additional_constraints.append(cd)
        # if only one dist constraint found triangle is not complete
        if len(additional_constraints) > 1:
            triangles.append(Triangle(set(ca.points), [ca], additional_constraints))
    return triangles



dist = [DistanceConstraint({'p1', 'p2'}),
        DistanceConstraint({'p1', 'p3'}),
        DistanceConstraint({'p2', 'p4'}),
        DistanceConstraint({'p3', 'p4'}),
        DistanceConstraint({'p2', 'p3'})]

angle = [AngleConstraint(['p2', 'p1', 'p3'])]

triangles = find_tri(dist, angle)
print(triangles)
