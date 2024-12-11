#include <string>
#include <vector>

class cpu {
private:
    std::string brand;
    std::string model;
    unsigned short core_count;
    unsigned short logical_processor_count;
    unsigned short max_freq;
    unsigned short base_freq;
    std::vector<unsigned short> cache;
    unsigned short max_bits;
public:
    cpu(/* args */);
};
