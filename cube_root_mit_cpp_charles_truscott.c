#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;
/* Charles Thomas Wallace Truscott at github.com/ctwtruscottwatters taking a C++ sabbatical from MIT XSeries Computational Thinking in Python 
/* Hope I can pass to earn my MIT certificate from June 2nd 6.001 and 6.002 ending on December 12th */
/* Tough road */
/* Even saw there was a 7 unit edX offering from MIT in CompSci which would be equivalent to a year of undergrad education from the worlds' consistently #1 college in Mathematics and Computer Science */
int main(void) {
	int cube = 27;
	long double guess = 0;
	long double epsilon = 0.0001;
	int guesses = 0;
	while (!(((guess * guess * guess) - cube) >= epsilon)) {
		guess += epsilon;
		guesses += 1;
	}
	cout << "The guess is: " << guess << " and guess cubed is " << abs((int)(guess * guess * guess)) << endl;
	cout << "It took " << guesses << " guesses " << "to find the answer." << endl;
	return 0;
}