
/*
 * Stolen from RosettaCode.com
 * Michal Sikorski
 * 06/07/2016
 *
 */

#include <cstdlib>
#include <iostream>
#include <windows.h>
#include <string.h>
using namespace std;
int main(int argc, char *argv[])
{
	string inpt;
	char ascii[28] = " ABCDEFGHIJKLMNOPQRSTUVWXYZ", lwcAscii[28] = " abcdefghijklmnopqrstuvwxyz";
	string morse[27] = {"  ", ".- ", "-... ", "-.-. ", "-.. ", ". ", "..-. ", "--. ", ".... ", ".. ", ".--- ", "-.- ", ".-.. ", "-- ", "-. ", "--- ", ".--.", "--.- ", ".-. ", "... ", "- ", "..- ", "...- ", ".-- ", "-..- ", "-.-- ", "--.. "};
	getline(cin,inpt);
	int xx=0;
	int size = inpt.length();
	cout<<"Length:"<<size<<endl;

@@ begin question morse_loop
@@ description: Translate ascii to morse and print to std out
@@ points: 4
@@ time: 20 minutes
















@@ end question

		cout<<morse[x];
		xx++;
	}

	return EXIT_SUCCESS;
}
