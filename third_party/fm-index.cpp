#include <sdsl/suffix_arrays.hpp>
#include <string>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace sdsl;
using namespace std;

int main(int argc, char** argv)
{
    if (argc <  2) {
        cout << "Usage " << argv[0] << " text_file substrfile" << endl;
        cout << "    This program constructs a very compact FM-index" << endl;
        cout << "    which supports count, locate, and extract queries." << endl;
        cout << "    text_file      Original text file." << endl;
        cout << "    max_locations  Maximal number of location to report." <<endl;
        cout << "    post_context   Maximal length of the reported post-context." << endl;
        cout << "    pre_context    Maximal length of the pre-context." << endl;
        return 1;
    }
    size_t max_locations = 1;
    size_t post_context = 1;
    size_t pre_context = 1;


    string index_suffix = ".fm9";
    string index_file   = string(argv[1])+index_suffix;
//    csa_wt<wt_huff<rrr_vector<255> >, 1024, 2048> fm_index;
    csa_wt<wt_huff<rrr_vector<127> >, 512, 1024> fm_index;
    //csa_wt<wt_huff<rrr_vector<12700> >, 51200, 102400> fm_index;

    if (!load_from_file(fm_index, index_file)) {
        ifstream in(argv[1]);
        if (!in) {
            cout << "ERROR: File " << argv[1] << " does not exist. Exit." << endl;
            return 1;
        }
        cout << "No index "<<index_file<< " located. Building index now." << endl;
        construct(fm_index, argv[1], 1); // generate index
        store_to_file(fm_index, index_file); // save it
    }
    cout << "Index construction complete, index requires " << size_in_mega_bytes(fm_index) << " MiB." << endl;
    cout << "Input search terms and press Ctrl-D to exit." << endl;
    string prompt = "\e[0;32m>\e[0m ";
    cout << prompt;
    string query;


 ifstream myfile(argv[2]);
ofstream fout("issub");
ofstream occout("occsub");
    while (getline(myfile, query)) {
        size_t m  = query.size();
        size_t occs = sdsl::count(fm_index, query.begin(), query.end());
        occout<<occs<<endl;
	if(occs!=0){
	 fout<<"1"<<" " << query << endl;
	}else{
	 fout <<  occs<<" " << query << endl;
	}
    }
occout.close();
fout.close();
myfile.close();
    cout << endl;
}

