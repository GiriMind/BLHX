#include "pyGraphCap/Common.h"
#include "pyGraphCap/pyImage.h"

#include "Base/ScopeGuard.h"

namespace pygc
{
	pyImage::pyImage() :
		m_width(16),
		m_height(9),
		m_bpp(4),
		m_shape(py::make_tuple(m_height, m_width, m_bpp)),
		m_dtype(np::dtype::get_builtin<uint8_t>()),
		m_ndarray(np::empty(m_shape, m_dtype))
	{
	}

	void pyImage::convertFromD3D11Texture2D(CComPtr<ID3D11DeviceContext> deviceContext,
		CComPtr<ID3D11Texture2D> texture2D)
	{
		D3D11_TEXTURE2D_DESC desc = {};
		texture2D->GetDesc(&desc);

		int_t bpp = 0;
		ByteOrder bo = BO_UNKNOWN;
		switch (desc.Format)
		{
		case DXGI_FORMAT_B8G8R8A8_UNORM:
		case DXGI_FORMAT_B8G8R8X8_UNORM:
			bpp = 4;
			bo = BO_BGR;
			break;

		default:
			THROW_BASE_EXCEPTION(Exception() << err_no(desc.Format) << err_str("Unsupported image format."));
			break;
		}

		if (m_width != desc.Width || m_height != desc.Height || m_bpp != bpp)
		{
			m_width = desc.Width;
			m_height = desc.Height;
			m_bpp = bpp;
			m_shape = py::make_tuple(m_height, m_width, m_bpp);
			//m_dtype = np::dtype::get_builtin<uint8_t>();
			m_ndarray = np::empty(m_shape, m_dtype);
		}

		UINT subresource = D3D11CalcSubresource(0, 0, 0);
		D3D11_MAPPED_SUBRESOURCE mapped = {};
		HRESULT hr = deviceContext->Map(texture2D, subresource, D3D11_MAP_READ, 0, &mapped);
		if (FAILED(hr))
			THROW_DIRECTX_HRESULT(hr);
		ON_SCOPE_EXIT([&]()
		{
			deviceContext->Unmap(texture2D, subresource);
		});

		byte_t* src = reinterpret_cast<byte_t*>(mapped.pData);
		byte_t* dst = reinterpret_cast<byte_t*>(m_ndarray.get_data());
		int_t pitch = m_width * m_bpp;
		//if (bo == BO_BGR)
		//{
		if (pitch == mapped.RowPitch)
		{
			memcpy_s(dst, pitch * m_height, src, pitch * m_height);
		}
		else
		{
			for (int_t h = 0; h < m_height; ++h)
			{
				memcpy_s(dst, pitch, src, pitch);
				src += mapped.RowPitch;
				dst += pitch;
			}
		}
		//}
		//else
		//{
		//}
	}

	np::ndarray pyImage::toNdarray()
	{
		return m_ndarray;
	}
}
