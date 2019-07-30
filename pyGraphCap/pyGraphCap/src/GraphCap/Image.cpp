#include "GraphCap/Common.h"
#include "GraphCap/Image.h"

namespace gc
{
	void Image::convertFromD3D11Texture2D(CComPtr<ID3D11DeviceContext> deviceContext,
		CComPtr<ID3D11Texture2D> texture2D)
	{
		THROW_BASE_EXCEPTION(Exception() << err_str("Unimplemented function."));
	}
}
