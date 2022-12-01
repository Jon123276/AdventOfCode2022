import System.IO  
import Control.Monad

main = do  
        contents <- readFile "input.txt"
        print . map readInt . words $ contents

readInt :: String -> Int
readInt = read
