// 取出最早评论时间.cpp: 定义控制台应用程序的入口点。
//

// ConsoleApplication8.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
#include<string>
#include<windows.h>
using namespace std;


int main()
{
	int flag = 0;
	string *movie=new string[140000];
	ofstream outfile;
	string line;
	string a;
	ifstream infile;
	ifstream in;
	in.open("F:\\csvtest.txt", ios::in);
	for (int j =0;j <140000; j++) {
		getline(in, line);
		movie[j] = line;
	}
	in.close();
	string::size_type idx;
	outfile.open("F:\\re.txt", ios::app);
	infile.open("E:\\temp.txt", ios::in);
	while (!infile.eof()) {
		getline(infile, a);
		for (int j = 0; j < 140000; j++) {
			idx = movie[j].find(a);
			if (idx == string::npos)
			{
			}
			else {
				outfile << movie[j] << endl;
				flag = 1;
				break;
			}
		}
		if (flag == 0) {
			outfile << a << ",0,0" << endl;
		}
		flag = 0;
		
	}
	infile.close();
	outfile.close();
	cout << "success" << endl;
	return 0;
	
}



