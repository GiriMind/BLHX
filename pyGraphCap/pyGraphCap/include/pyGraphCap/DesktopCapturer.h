#pragma once

#include <d3d11.h>
#include <dxgi1_2.h>
#include <atlbase.h>

#include "Base/Size.h"
#include "Base/Rect.h"
#include "pyGraphCap/Image.h"

namespace gc
{
	// Win8 or later
	class DesktopCapturer
	{
	public:
		DesktopCapturer();

		bool capture(Image& image, const Rect& rect, time_t timeout = 17);
		Size getDesktopSize() const;

	private:
		CComPtr<ID3D11Device> m_device;
		CComPtr<ID3D11DeviceContext> m_deviceContext;
		DXGI_OUTPUT_DESC m_outputDesc;
		CComPtr<IDXGIOutputDuplication> m_desktopDupl;
		CComPtr<ID3D11Texture2D> m_buffer;
		Size m_size;
	};
}
