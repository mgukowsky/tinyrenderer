#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "tgaimage.h"

namespace py = pybind11;

PYBIND11_MODULE(tgaimage, m) {
    py::class_<TGAImage>(m, "TGAImage")
        .def(py::init<int, int, int>())
        .def("__copy__", [](const TGAImage &self){ return TGAImage(self); })
        .def("__deepcopy__", [](const TGAImage &self, py::dict){
            return TGAImage(self);
        })
        .def("assign", [](TGAImage &self, const TGAImage &other) {
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
}
