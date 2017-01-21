@@ begin hide
main :: IO ()
main = do
	getLine
	xs <- getLine >>= return . map read . words
	print $ qsort xs
@@ end hide

qsort :: [Int] -> [Int]
@@ begin question quicksort_hs
@@ description: Why does anyone like haskell?
@@ points: 100000
qsort [] = []
qsort (x:xs) = qsort [y | y <- xs, y < x] ++ [x] ++ qsort [y | y <- xs, y >= x]
@@ end question
