#pragma once

#include <d3d11.h>
#include <atlbase.h>

namespace gc
{
	class Image
	{
	public:
		virtual ~Image() = default;

		virtual void convertFromD3D11Texture2D(CComPtr<ID3D11DeviceContext> deviceContext,
			CComPtr<ID3D11Texture2D> texture2D);
	};
}
