import qualified Data.Set as Set

type Point = String

data Constraint = Distance Point Point | Angle Point Point Point
  deriving (Show, Eq, Ord)

type Triangle = [Constraint] --deriving(Show, Eq, Ord)

isDistanceInAngle :: Constraint -> Constraint -> Bool
isDistanceInAngle (Distance pd1 pd2) (Angle pa1 pa2 pa3) = Set.fromList [pd1, pd2] 
                                                           `Set.isSubsetOf`
                                                           Set.fromList [pa1, pa2, pa3]

findAngleTriangles :: [Constraint] -> [Constraint] -> [Triangle]
findAngleTriangles [] _ = []
findAngleTriangles (a:as) ds = 
    let distances = [d | d <- ds, d `isDistanceInAngle` a]
        numDistances = length distances
    in if numDistances < 2 then [] else [a:distances] ++ findAngleTriangles as ds

distances = [Distance "p1" "p2",
             Distance "p1" "p3",
             Distance "p2" "p4",
             Distance "p3" "p4",
             Distance "p2" "p3"]
 
angles = [Angle "p2" "p1" "p3", Angle "p2" "p3" "p4"]

triangles = findAngleTriangles angles distances


-- class Triangle:
--     def __init__(self, points: Set[str], dist_constraints: List[DistanceConstraint],
--                  angle_constraints: List[AngleConstraint]) -> None:
--         self.points = points
--         self.given_dist_constraints = dist_constraints
--         self.given_angle_constraints = angle_constraints
--         num_dist_constraints = len(dist_constraints)
--         num_angle_constraints = len(angle_constraints)
--         num_constraints = (num_dist_constraints, num_angle_constraints)
--         if   num_constraints == (1, 2):
--             self.derived_angle_constraint = self.given_angle_constraints[0]
--         #elif num_constraints == (1, 3):
--         #elif num_constraints == (2, 1):
--         #elif num_constraints == (2, 2):
--         #elif num_constraints == (2, 3):
--         #elif num_constraints == (3, 0):
--         #elif num_constraints == (3, 1):
--         #elif num_constraints == (3, 2):
--         #elif num_constraints == (3, 3):
--         #else:
--         #    raise ValueError("Too few constraints, triangle is undefined")
--         #self.derived_constraints
-- 
--     def __repr__(self):
--         return "%s, %s, %s" % (self.points, self.given_dist_constraints,
--                                self.given_angle_constraints)

isDistanceAdjacent :: Constraint -> Constraint -> Bool
isDistanceAdjacent (Distance pd1 pd2) (Distance pd3 pd4) = 
    let sharedPoints = Set.fromList [pd1, pd2] `Set.intersection` Set.fromList [pd3, pd4]
    in length sharedPoints == 1

getDifferencePoints :: Constraint -> Constraint -> Set
getDifferencePoints (Distance pd1 pd2) (Distance pd3 pd4) = Set.fromList [pd1, pd2] 
                                                            `Set.difference` 
                                                            Set.fromList [pd3, pd4]

findDistanceTriangles :: [Constraint] -> [Constraint] -> [Triangle]
findDistanceTriangles [] _ = []
findDistanceTriangles (d:ds) as = 
  [x | x <- ds, size differencePoints == 2, let differencePoints = getDifferencePoints d x]
-- def find_tri(dist_constraints, angle_constraints):
--     triangles = find_angle_triangles(dist_constraints, angle_constraints)
--     # find triangles only consisting of dist constraints
--     while len(dist_constraints) > 0:
--         dc1 = dist_constraints.pop(0)
--         temp_dist_constraints = dist_constraints.copy()
--         # cycle through the remaining constraints to find a match
--         for dc2 in temp_dist_constraints:
--             # continue if dist constraints c1 and c2 share a common point
--             if len(dc1.points & dc2.points) == 1:
--                 # only continue if triangle was not already found above
--                 if not any([True for triangle in triangles
--                             if dc1.points | dc2.points == triangle.points]):
--                     # search the missing side in the remaining constraints
--                     dc3 = DistanceConstraint(dc1.points ^ dc2.points)
--                     for dc3 in temp_dist_constraints:
--                         if (dc1.points ^ dc2.points) == dc3.points:
--                             triangles.append(Triangle(dc1.points | dc2.points | dc3.points,
--                                                       [dc1, dc2, dc3], []))
--                             temp_dist_constraints.remove(dc3)
--     return triangles
-- 
-- def find_angle_triangles(dist_constraints, angle_constraints):
--     triangles = []
--     # find triangles formed by angle and dist constraints
--     for ca in angle_constraints:
--         additional_constraints = []
--         # find dist constraints which belong to the same triangle as the angle constraint
--         for cd in dist_constraints:
--             if set(ca.points).issuperset(cd.points):
--                 additional_constraints.append(cd)
--         # if only one dist constraint found triangle is not complete
--         if len(additional_constraints) > 1:
--             triangles.append(Triangle(set(ca.points), [ca], additional_constraints))
--     return triangles
-- 
-- triangles = find_tri(dist, angle)
-- print(triangles)
