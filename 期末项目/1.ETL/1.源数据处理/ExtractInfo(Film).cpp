#include <iostream>
#include <fstream>
#include <string>
using namespace std;

/**
 * Extract product/productId,review/score,review/time according to film IDs
 * @return
 */
int main() {
    ifstream in("/Users/logan/Desktop/DataFactory/movies.txt");
    ofstream ou("/Users/logan/Desktop/cpp/DataFactory/movieout.txt");
    string line;
    if(in) {
        int t = 1;
        while (getline(in, line)) {
            if (!line.find("product/productId:") || !line.find("review/score:") || !line.find("review/time:")) {
                num++;
                t++;
                //t->tabs 判断换行
                ou << line << endl;
                cout << num << endl;
            }
            if (t % 4 == 0) {
                t = 1;
                ou << endl;
            }
        }
    }
    cout << num/3 << endl;
}