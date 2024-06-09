#include "geometry.h"
#include "model.h"
#include "tgaimage.h"

#include <pybind11/operators.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <string>

namespace py = pybind11;

template<typename T>
void bind_vec2(py::module &m, const std::string &typestr) {
  std::string class_name = "Vec2<" + typestr + ">";
  py::class_<Vec2<T>>(m, class_name.c_str())
    .def(py::init<>())
    .def(py::init<T, T>())
    .def_readwrite("x", &Vec2<T>::x)
    .def_readwrite("y", &Vec2<T>::y)
    .def(py::self + py::self)
    .def(py::self - py::self)
    .def(py::self * float());
}

template<typename T>
void bind_vec3(py::module &m, const std::string &typestr) {
  std::string class_name = "Vec3<" + typestr + ">";
  py::class_<Vec3<T>>(m, class_name.c_str())
    .def(py::init<>())
    .def(py::init<T, T, T>())
    .def_readwrite("x", &Vec3<T>::x)
    .def_readwrite("y", &Vec3<T>::y)
    .def_readwrite("z", &Vec3<T>::z)
    .def(py::self + py::self)
    .def(py::self - py::self)
    .def(py::self ^ py::self)
    .def(py::self * py::self)
    .def(py::self * float())
    .def("norm", &Vec3<T>::norm)
    .def("normalize", &Vec3<T>::normalize);
}

PYBIND11_MODULE(tgaimage, m) {
  bind_vec2<float>(m, "float");
  bind_vec2<int>(m, "int");
  bind_vec3<float>(m, "float");
  bind_vec3<int>(m, "int");
  py::class_<TGAImage>(m, "TGAImage")
    .def(py::init<int, int, int>())
    .def("__copy__", [](const TGAImage &self) { return TGAImage(self); })
    .def("__deepcopy__", [](const TGAImage &self, py::dict) { return TGAImage(self); })
    .def("assign",
         [](TGAImage &self, const TGAImage &other) {
           self = other;
           return self;
         })
    .def("read_tga_file", &TGAImage::read_tga_file)
    .def("write_tga_file", &TGAImage::write_tga_file)
    .def("flip_horizontally", &TGAImage::flip_horizontally)
    .def("flip_vertically", &TGAImage::flip_vertically)
    .def("scale", &TGAImage::scale)
    .def("get", &TGAImage::get)
    .def("set", &TGAImage::set)
    .def("get_width", &TGAImage::get_width)
    .def("get_height", &TGAImage::get_height)
    .def("get_bytespp", &TGAImage::get_bytespp)
    .def("buffer", &TGAImage::buffer)
    .def("clear", &TGAImage::clear);

  py::class_<TGAColor>(m, "TGAColor")
    .def(py::init<unsigned char, unsigned char, unsigned char, unsigned char>())
    .def(py::init<int, int>())
    .def_readwrite("b", &TGAColor::b)
    .def_readwrite("g", &TGAColor::g)
    .def_readwrite("r", &TGAColor::r)
    .def_readwrite("a", &TGAColor::a)
    .def_readwrite("bytespp", &TGAColor::bytespp);

  py::enum_<TGAImage::Format>(m, "Format")
    .value("GRAYSCALE", TGAImage::Format::GRAYSCALE)
    .value("RGB", TGAImage::Format::RGB)
    .value("RGBA", TGAImage::Format::RGBA);

  py::class_<Model>(m, "Model")
    .def(py::init<const char *>())
    .def("nverts", &Model::nverts)
    .def("nfaces", &Model::nfaces)
    .def("vert", &Model::vert)
    .def("face", &Model::face);
}
