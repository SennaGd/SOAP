@Echo Off
cd %systemroot%\system32
call :IsAdmin

Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_PREEMPTION_MODE" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_FRAME_LATENCY_WAITABLE_OBJECT" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_SWAP_CHAIN_WAITABLE_OBJECT" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_FORCE_FLIP_DISCARD" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_SWAP_CHAIN_SCALE" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_SWAP_CHAIN_ALLOW_MODE_SWITCH" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_SWAP_CHAIN_FULLSCREEN_FLIP_MODE" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_DISABLE_DWM_THROTTLING" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_FORCE_FLIP_SEQUENTIAL" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_FORCE_FULLSCREEN_FLIP_MODE" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_MAX_FRAME_LATENCY" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_USE_OPTIMIZED_SWAP_CHAIN" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "CreateGdiPrimaryOnSlaveGPU" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DriverSupportsCddDwmInterop" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkCddSyncDxAccess" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkCddSyncGPUAccess" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkCddWaitForVerticalBlankEvent" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkCreateSwapChain" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkFreeGpuVirtualAddress" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkOpenSwapChain" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkShareSwapChainObject" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkWaitForVerticalBlankEvent" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkWaitForVerticalBlankEvent2" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "SwapChainBackBuffer" /f
Reg.exe delete "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "TdrResetFromTimeoutAsync" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectDraw" /v "DisableAGPSupport" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectDraw" /v "UseNonLocalVidMem" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectDraw" /v "DisableDDSCAPSInDDSD" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectDraw" /v "EmulatePointSprites" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\DirectDraw" /v "EmulateStateBlocks" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\DirectDraw" /v "DisableAGPSupport" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\DirectDraw" /v "UseNonLocalVidMem" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\DirectDraw" /v "DisableDDSCAPSInDDSD" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\DirectDraw" /v "EmulatePointSprites" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\DirectDraw" /v "EmulateStateBlocks" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "ForceRgbRasterizer" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "EnumReference" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "EnumSeparateMMX" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "EnumRamp" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "EnumNullDevice" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "UseMMXForRGB" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "ForceRgbRasterizer" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "EnumReference" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "EnumSeparateMMX" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "EnumRamp" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "EnumNullDevice" /f
Reg.exe delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "UseMMXForRGB" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D" /v "UseNonLocalVidMem" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D" /v "FullDebug" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D" /v "DisableDM" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D" /v "EnableMultimonDebugging" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D" /v "LoadDebugRuntime" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D" /v "FewVertices" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D" /v "DisableMMX" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D" /v "UseMMXForRGB" /f
Reg.exe delete "HKLM\SOFTWARE\Microsoft\Direct3D" /v "DisableVidMemVBs" /f


:IsAdmin
Reg.exe query "HKU\S-1-5-19\Environment"
If Not %ERRORLEVEL% EQU 0 (
    Cls & Echo You must have administrator rights to continue ... 
    
)
Cls
goto:eof
