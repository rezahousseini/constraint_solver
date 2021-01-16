module ConstraintSolver where

import qualified Algebra.Graph as Alga

greet :: String -> String
greet who = "Hello, " <> who <> "!"

--type Point = (Double, Double)
data Point = Point Float Float deriving (Show, Eq, Ord)  

data Constraint = Distance Point Point | Angle Point Point Point
  deriving (Show, Eq, Ord)

data Triangle = Triangle3 Constraint Constraint Constraint |
                Triangle4 Constraint Constraint Constraint Constraint |
                Triangle5 Constraint Constraint Constraint Constraint Constraint |
                Triangle6 Constraint Constraint Constraint Constraint Constraint Constraint

-- |Assemble a list of constraints into a graph.
-- It takes one argument, of type [Constraint]
constraintsToGraph :: [Constraint] -> Alga.Graph Point
constraintsToGraph [] = Alga.Empty
constraintsToGraph ((Distance p1 p2):xs) = Alga.overlay 
  (Alga.connect (Alga.Vertex p1) (Alga.Vertex p2))
  (constraintsToGraph xs)
constraintsToGraph ((Angle p1 p2 p3):xs) = Alga.overlay
  (Alga.overlay
    (Alga.connect (Alga.Vertex p1) (Alga.Vertex p2))
    (Alga.connect (Alga.Vertex p2) (Alga.Vertex p3)))
  (constraintsToGraph xs)

-- |Extract a list of valid triangles from a constraint graph.
constraintsToTriangles :: Alga.Graph Point -> [Triangle]
constraintsToTriangles Alga.Empty = []
-- constraintsToTriangles 

