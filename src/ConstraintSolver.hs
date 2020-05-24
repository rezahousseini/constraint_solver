module ConstraintSolver where

import qualified Algebra.Graph as Alga

greet :: String -> String
greet who = "Hello, " <> who <> "!"

type Point = Int

data Constraint = Distance Point Point | Angle Point Point Point
  deriving (Show, Eq, Ord)

constraintsToGraph :: [Constraint] -> Alga.Graph Point
constraintsToGraph [] = Alga.empty
constraintsToGraph ((Distance p1 p2):xs) = Alga.overlay 
  (Alga.connect (Alga.vertex p1) (Alga.vertex p2))
  (constraintsToGraph xs)
constraintsToGraph ((Angle p1 p2 p3):xs) = Alga.overlay
  (Alga.overlay
    (Alga.connect (Alga.vertex p1) (Alga.vertex p2))
    (Alga.connect (Alga.vertex p2) (Alga.vertex p3)))
  (constraintsToGraph xs)

--main = do
--  print $ Graph.edgeCount (Graph.vertices [0, 1])
