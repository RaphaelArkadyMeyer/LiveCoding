@@ begin hide
main = do
	getLine
	xs <- getLine >>= return . map read . unwords
	print $ qsort xs
@@ begin hide

@@ begin problem
@@ description: Why does anyone like haskell?
@@ begin question quicksort
@@ points: 100000
qsort :: [Int] -> [Int]
qsort [] = []
qsort (x:xs) = qsort [y | y <- xs, y < x] ++ [x] ++ qsort [y | y <- xs, y >= x]
@@ end question
@@ end problem