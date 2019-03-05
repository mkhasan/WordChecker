/*
 * test.cpp
 *
 *  Created on: Mar 5, 2019
 *      Author: usrc
 */

#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char argv[]) {


	char testStr[255] = "hello how are your \r\n";

	char *p = strtok(testStr, " ");
	cout << p << endl;
	p = strtok(NULL, "\r\n");

	cout << (!p ? "NULL" : p) << endl;
	return 0;
}


