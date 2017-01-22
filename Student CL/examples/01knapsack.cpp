#include <vector>
#include <string>
#include <iostream>
#include <boost/tuple/tuple.hpp>
#include <set>


int findBestPack( const std::vector<boost::tuple<std::string , int , int> > & items ,std::set<int> & bestItems , const int weightlimit ) {
	//dynamic programming approach sacrificing storage space for execution
	//time , creating a table of optimal values for every weight and a 
	//second table of sets with the items collected so far in the knapsack
	//the best value is in the bottom right corner of the values table,
	//the set of items in the bottom right corner of the sets' table.
@@ begin question optimal_knapsack
@@ description: use dynamic programming to find the best assingment of weights to the knapsack
@@ points: 100
@@ time: 40 minutes






































@@ end question
	bestItems.swap( solutionSets[ n - 1][ weightlimit - 1 ] ) ;
	return bestValues[ n - 1 ][ weightlimit - 1 ] ;
}
