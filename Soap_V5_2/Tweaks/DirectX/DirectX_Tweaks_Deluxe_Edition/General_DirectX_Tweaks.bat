@Echo Off
cd %systemroot%\system32
call :IsAdmin

Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_PREEMPTION_MODE" /t REG_DWORD /d "3" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_FRAME_LATENCY_WAITABLE_OBJECT" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_SWAP_CHAIN_WAITABLE_OBJECT" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_FORCE_FLIP_DISCARD" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_SWAP_CHAIN_SCALE" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_SWAP_CHAIN_ALLOW_MODE_SWITCH" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_SWAP_CHAIN_FULLSCREEN_FLIP_MODE" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_DISABLE_DWM_THROTTLING" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_FORCE_FLIP_SEQUENTIAL" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_FORCE_FULLSCREEN_FLIP_MODE" /t REG_DWORD /d "3" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_MAX_FRAME_LATENCY" /t REG_DWORD /d "2" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectX" /v "DXGI_USE_OPTIMIZED_SWAP_CHAIN" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "CreateGdiPrimaryOnSlaveGPU" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DriverSupportsCddDwmInterop" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkCddSyncDxAccess" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkCddSyncGPUAccess" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkCddWaitForVerticalBlankEvent" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkCreateSwapChain" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkFreeGpuVirtualAddress" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkOpenSwapChain" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkShareSwapChainObject" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkWaitForVerticalBlankEvent" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "DxgkWaitForVerticalBlankEvent2" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "SwapChainBackBuffer" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\DXGKrnl" /v "TdrResetFromTimeoutAsync" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectDraw" /v "DisableAGPSupport" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectDraw" /v "UseNonLocalVidMem" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectDraw" /v "DisableDDSCAPSInDDSD" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectDraw" /v "EmulatePointSprites" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\DirectDraw" /v "EmulateStateBlocks" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\DirectDraw" /v "DisableAGPSupport" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\DirectDraw" /v "UseNonLocalVidMem" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\DirectDraw" /v "DisableDDSCAPSInDDSD" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\DirectDraw" /v "EmulatePointSprites" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\DirectDraw" /v "EmulateStateBlocks" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "ForceRgbRasterizer" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "EnumReference" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "EnumSeparateMMX" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "EnumRamp" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "EnumNullDevice" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D\Drivers" /v "UseMMXForRGB" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "ForceRgbRasterizer" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "EnumReference" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "EnumSeparateMMX" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "EnumRamp" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "EnumNullDevice" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Wow6432Node\Microsoft\Direct3D\Drivers" /v "UseMMXForRGB" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D" /v "UseNonLocalVidMem" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D" /v "FullDebug" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D" /v "DisableDM" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D" /v "EnableMultimonDebugging" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D" /v "LoadDebugRuntime" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D" /v "FewVertices" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D" /v "DisableMMX" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D" /v "UseMMXForRGB" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Microsoft\Direct3D" /v "DisableVidMemVBs" /t REG_DWORD /d "0" /f


:IsAdmin
Reg.exe query "HKU\S-1-5-19\Environment"
If Not %ERRORLEVEL% EQU 0 (
 Cls & Echo You must have administrator rights to continue ... 

)
Cls
goto:eof
