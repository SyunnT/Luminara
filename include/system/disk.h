#include <vector>
#include <string>

class disk {
private:
    class driver;
    std::vector<driver> disk_list;
public:
    disk(/* args */);
};

class disk::driver {
private:
    class portion;
    std::string brand;
    std::string model;
    unsigned short capacity;
    std::vector<portion> portions;
public:
    driver();
};

class disk::driver::portion {
private:
    std::string id;
    std::string path;
    unsigned short capacity;
    std::string file_system;
public:
    portion();
};