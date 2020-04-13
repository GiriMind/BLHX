#pragma once

#include <d3d11.h>
#include <atlbase.h>
#include <boost/python.hpp>
#include <boost/python/numpy.hpp>

namespace gc
{
	namespace py = boost::python;
	namespace np = boost::python::numpy;

	enum ByteOrder
	{
		BO_UNKNOWN,
		BO_BGR,		// B�ڵ�λ��R�ڸ�λ��OpenCVĬ�ϸ�ʽ
		BO_RGB,		// R�ڵ�λ��B�ڸ�λ
		BO_MAXCOUNT
	};

	class Image
	{
	public:
		Image();

		void convertFromD3D11Texture2D(CComPtr<ID3D11DeviceContext> deviceContext,
			CComPtr<ID3D11Texture2D> texture2D);

		np::ndarray toNdarray();

	private:
		int_t m_width;
		int_t m_height;
		int_t m_bpp;
		py::tuple m_shape;
		np::dtype m_dtype;
		np::ndarray m_ndarray;
	};
}
