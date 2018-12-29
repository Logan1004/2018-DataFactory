#include <iostream>
#include <fstream>
#include <string>
using namespace std;
/**
 * 使用cpp处理原始数据
 * 自动去重
*/
int main() {
    ifstream in("/Users/logan/Desktop/DataFactory/movies.txt");
    ofstream ou("/Users/logan/Desktop/cpp/DataFactory/movieout.txt");
    //默认文件路径
    string line;
    string previous = "";
    long num=0;
    if(in) {
        while (getline(in, line)) {
             if (!line.find("product/productId: ")) {
                 line.erase(0,19);
                 if (previous!=line) {
                     previous = line;
                     //记录之前的line 用于去重
                     ou << "amazon.com/dp/"+previous << endl;
                     num++;
                 }
            }
        }
    }
    cout << num << endl;
}