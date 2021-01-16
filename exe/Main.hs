module Main where

import System.Environment
import ConstraintSolver

--main = mapM_ (putStrLn . greet) =<< getArgs
main = do
  print $ constraintsToGraph [Distance (Point 0 0) (Point 1 0),
                              Distance (Point 0 0) (Point 1 1),
                              Distance (Point 1 0) (Point 1 1)]
--  print $ Graph.edgeCount (Graph.vertices [0, 1])
