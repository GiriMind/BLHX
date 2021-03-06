#include "pyGraphCap/Common.h"

#include <boost/exception/all.hpp>
#include <boost/python.hpp>
#include <boost/python/numpy.hpp>

#include "pyGraphCap/DesktopCapturer.h"
#include "pyGraphCap/Image.h"

namespace gc
{
	namespace py = boost::python;
	namespace np = boost::python::numpy;

	void Translator(const boost::exception& ex)
	{
		std::string what = boost::diagnostic_information(ex);
		PyErr_SetString(PyExc_RuntimeError, what.c_str());
	}

	BOOST_PYTHON_MEMBER_FUNCTION_OVERLOADS(DesktopCapturer_capture_overloads, capture, 2, 3)

	BOOST_PYTHON_MODULE(pyGraphCap)
	{
		Py_Initialize();
		np::initialize();

		py::register_exception_translator<boost::exception>(Translator);

		py::class_<Point>("Point", py::init<>())
			.def(py::init<Point::value_t, Point::value_t>())
			.def_readwrite("x", &Point::x)
			.def_readwrite("y", &Point::y);

		py::class_<Size>("Size", py::init<>())
			.def(py::init<Size::value_t, Size::value_t>())
			.def_readwrite("width", &Size::width)
			.def_readwrite("height", &Size::height);

		py::class_<Rect>("Rect", py::init<>())
			.def(py::init<Rect::value_t, Rect::value_t, Rect::value_t, Rect::value_t>())
			.def(py::init<const Point&, const Size&>())
			.def_readwrite("x", &Rect::x)
			.def_readwrite("y", &Rect::y)
			.def_readwrite("width", &Rect::width)
			.def_readwrite("height", &Rect::height);

		py::class_<Image, boost::noncopyable>("Image", py::init<>())
			.def("toNdarray", &Image::toNdarray/*, py::return_internal_reference<>()*/);

		py::class_<DesktopCapturer, boost::noncopyable>("DesktopCapturer", py::init<>())
			.def("capture", &DesktopCapturer::capture, DesktopCapturer_capture_overloads());
	}
}
