module Main where

import System.Environment
import ConstraintSolver

main = mapM_ (putStrLn . greet) =<< getArgs
