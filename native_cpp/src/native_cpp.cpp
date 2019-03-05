#include <boost/python/class.hpp>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <iostream>
#include <string>

namespace { // Avoid cluttering the global namespace.

  // A friendly class.
  class hello
  {
    public:
      hello(const std::string& country) { this->country = country; }
      std::string greet() const { return "Hello from " + country; }
    private:
      std::string country;
  };

  // A function taking a hello object as an argument.
  std::string invite(const hello& w) {
    return w.greet() + "! Please come soon!";
  }

  class split {
  public:
	  std::string kor;
	  std::string eng;
	  int size;
  public:
	  split(const std::string& str): size(0) {
		  char *localStr = new char[str.length()+1];
		  strcpy(localStr, str.c_str());
		  char * p = strtok(localStr, " ");
		  if(p != NULL) {
			  kor = p;
			  size ++;
			  p = strtok(NULL, "\r\n");
			  if(p != NULL) {
				  eng = p;
				  size ++;
			  }

		  }
		  delete[] localStr;
	  }

	  std::string get(const std::string &k) const {

		  return std::string("test") + "|" + k;
	  }
  };

  std::string get(const split & s) {
	  return "test";
  }
}

BOOST_PYTHON_MODULE(native_cpp)
{
    using namespace boost::python;
    class_<hello>("hello", init<std::string>())
        // Add a regular member function.
        .def("greet", &hello::greet)
        // Add invite() as a member of hello!
        .def("invite", invite)

		;

    // Also add invite() as a regular function to the module.
    def("invite", invite);

    class_<split>("split", init<std::string>())
		.def("get", &split::get)
		.def_readonly("kor", &split::kor)
		.def_readonly("eng", &split::eng)
		.def_readonly("size", &split::size)
		;

    def("get", get);
}
