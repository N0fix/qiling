processthreadsapi_data = {'QueueUserAPC': {'pfnAPC': 'PAPCFUNC', 'hThread': 'HANDLE', 'dwData': 'ULONG_PTR'}, 'GetProcessTimes': {'hProcess': 'HANDLE', 'lpCreationTime': 'LPFILETIME', 'lpExitTime': 'LPFILETIME', 'lpKernelTime': 'LPFILETIME', 'lpUserTime': 'LPFILETIME'}, 'GetCurrentProcess': {'VOID': 'void'}, 'GetCurrentProcessId': {'VOID': 'void'}, 'ExitProcess': {'uExitCode': 'UINT'}, 'TerminateProcess': {'hProcess': 'HANDLE', 'uExitCode': 'UINT'}, 'GetExitCodeProcess': {'hProcess': 'HANDLE', 'lpExitCode': 'LPDWORD'}, 'SwitchToThread': {'VOID': 'void'}, 'CreateThread': {'lpThreadAttributes': 'LPSECURITY_ATTRIBUTES', 'dwStackSize': 'SIZE_T', 'lpStartAddress': 'LPTHREAD_START_ROUTINE', 'lpParameter': 'LPVOID', 'dwCreationFlags': 'DWORD', 'lpThreadId': 'LPDWORD'}, 'CreateRemoteThread': {'hProcess': 'HANDLE', 'lpThreadAttributes': 'LPSECURITY_ATTRIBUTES', 'dwStackSize': 'SIZE_T', 'lpStartAddress': 'LPTHREAD_START_ROUTINE', 'lpParameter': 'LPVOID', 'dwCreationFlags': 'DWORD', 'lpThreadId': 'LPDWORD'}, 'GetCurrentThread': {'VOID': 'void'}, 'GetCurrentThreadId': {'VOID': 'void'}, 'OpenThread': {'dwDesiredAccess': 'DWORD', 'bInheritHandle': 'BOOL', 'dwThreadId': 'DWORD'}, 'SetThreadPriority': {'hThread': 'HANDLE', 'nPriority': 'int'}, 'SetThreadPriorityBoost': {'hThread': 'HANDLE', 'bDisablePriorityBoost': 'BOOL'}, 'GetThreadPriorityBoost': {'hThread': 'HANDLE', 'pDisablePriorityBoost': 'PBOOL'}, 'GetThreadPriority': {'hThread': 'HANDLE'}, 'ExitThread': {'dwExitCode': 'DWORD'}, 'TerminateThread': {'hThread': 'HANDLE', 'dwExitCode': 'DWORD'}, 'GetExitCodeThread': {'hThread': 'HANDLE', 'lpExitCode': 'LPDWORD'}, 'SuspendThread': {'hThread': 'HANDLE'}, 'ResumeThread': {'hThread': 'HANDLE'}, 'TlsAlloc': {'VOID': 'void'}, 'TlsGetValue': {'dwTlsIndex': 'DWORD'}, 'TlsSetValue': {'dwTlsIndex': 'DWORD', 'lpTlsValue': 'LPVOID'}, 'TlsFree': {'dwTlsIndex': 'DWORD'}, 'CreateProcessA': {'lpApplicationName': 'LPCSTR', 'lpCommandLine': 'LPSTR', 'lpProcessAttributes': 'LPSECURITY_ATTRIBUTES', 'lpThreadAttributes': 'LPSECURITY_ATTRIBUTES', 'bInheritHandles': 'BOOL', 'dwCreationFlags': 'DWORD', 'lpEnvironment': 'LPVOID', 'lpCurrentDirectory': 'LPCSTR', 'lpStartupInfo': 'LPSTARTUPINFOA', 'lpProcessInformation': 'LPPROCESS_INFORMATION'}, 'CreateProcessW': {'lpApplicationName': 'LPCWSTR', 'lpCommandLine': 'LPWSTR', 'lpProcessAttributes': 'LPSECURITY_ATTRIBUTES', 'lpThreadAttributes': 'LPSECURITY_ATTRIBUTES', 'bInheritHandles': 'BOOL', 'dwCreationFlags': 'DWORD', 'lpEnvironment': 'LPVOID', 'lpCurrentDirectory': 'LPCWSTR', 'lpStartupInfo': 'LPSTARTUPINFOW', 'lpProcessInformation': 'LPPROCESS_INFORMATION'}, 'SetProcessShutdownParameters': {'dwLevel': 'DWORD', 'dwFlags': 'DWORD'}, 'GetProcessVersion': {'ProcessId': 'DWORD'}, 'GetStartupInfoW': {'lpStartupInfo': 'LPSTARTUPINFOW'}, 'CreateProcessAsUserW': {'hToken': 'HANDLE', 'lpApplicationName': 'LPCWSTR', 'lpCommandLine': 'LPWSTR', 'lpProcessAttributes': 'LPSECURITY_ATTRIBUTES', 'lpThreadAttributes': 'LPSECURITY_ATTRIBUTES', 'bInheritHandles': 'BOOL', 'dwCreationFlags': 'DWORD', 'lpEnvironment': 'LPVOID', 'lpCurrentDirectory': 'LPCWSTR', 'lpStartupInfo': 'LPSTARTUPINFOW', 'lpProcessInformation': 'LPPROCESS_INFORMATION'}, 'SetThreadToken': {'Thread': 'PHANDLE', 'Token': 'HANDLE'}, 'OpenProcessToken': {'ProcessHandle': 'HANDLE', 'DesiredAccess': 'DWORD', 'TokenHandle': 'PHANDLE'}, 'OpenThreadToken': {'ThreadHandle': 'HANDLE', 'DesiredAccess': 'DWORD', 'OpenAsSelf': 'BOOL', 'TokenHandle': 'PHANDLE'}, 'SetPriorityClass': {'hProcess': 'HANDLE', 'dwPriorityClass': 'DWORD'}, 'GetPriorityClass': {'hProcess': 'HANDLE'}, 'SetThreadStackGuarantee': {'StackSizeInBytes': 'PULONG'}, 'ProcessIdToSessionId': {'dwProcessId': 'DWORD', 'pSessionId': 'DWORD'}, 'GetProcessId': {'Process': 'HANDLE'}, 'GetThreadId': {'Thread': 'HANDLE'}, 'FlushProcessWriteBuffers': {'VOID': 'void'}, 'GetProcessIdOfThread': {'Thread': 'HANDLE'}, 'InitializeProcThreadAttributeList': {'lpAttributeList': 'LPPROC_THREAD_ATTRIBUTE_LIST', 'dwAttributeCount': 'DWORD', 'dwFlags': 'DWORD', 'lpSize': 'PSIZE_T'}, 'DeleteProcThreadAttributeList': {'lpAttributeList': 'LPPROC_THREAD_ATTRIBUTE_LIST'}, 'UpdateProcThreadAttribute': {'lpAttributeList': 'LPPROC_THREAD_ATTRIBUTE_LIST', 'dwFlags': 'DWORD', 'Attribute': 'DWORD_PTR', 'lpValue': 'PVOID', 'cbSize': 'SIZE_T', 'lpPreviousValue': 'PVOID', 'lpReturnSize': 'PSIZE_T'}, 'SetProcessAffinityUpdateMode': {'hProcess': 'HANDLE', 'dwFlags': 'DWORD'}, 'QueryProcessAffinityUpdateMode': {'hProcess': 'HANDLE', 'lpdwFlags': 'LPDWORD'}, 'CreateRemoteThreadEx': {'hProcess': 'HANDLE', 'lpThreadAttributes': 'LPSECURITY_ATTRIBUTES', 'dwStackSize': 'SIZE_T', 'lpStartAddress': 'LPTHREAD_START_ROUTINE', 'lpParameter': 'LPVOID', 'dwCreationFlags': 'DWORD', 'lpAttributeList': 'LPPROC_THREAD_ATTRIBUTE_LIST', 'lpThreadId': 'LPDWORD'}, 'GetCurrentThreadStackLimits': {'LowLimit': 'PULONG_PTR', 'HighLimit': 'PULONG_PTR'}, 'GetThreadContext': {'hThread': 'HANDLE', 'lpContext': 'LPCONTEXT'}, 'GetProcessMitigationPolicy': {'hProcess': 'HANDLE', 'MitigationPolicy': 'PROCESS_MITIGATION_POLICY', 'lpBuffer': 'PVOID', 'dwLength': 'SIZE_T'}, 'SetThreadContext': {'hThread': 'HANDLE', 'lpContext': 'CONTEXT'}, 'SetProcessMitigationPolicy': {'MitigationPolicy': 'PROCESS_MITIGATION_POLICY', 'lpBuffer': 'PVOID', 'dwLength': 'SIZE_T'}, 'FlushInstructionCache': {'hProcess': 'HANDLE', 'lpBaseAddress': 'LPCVOID', 'dwSize': 'SIZE_T'}, 'GetThreadTimes': {'hThread': 'HANDLE', 'lpCreationTime': 'LPFILETIME', 'lpExitTime': 'LPFILETIME', 'lpKernelTime': 'LPFILETIME', 'lpUserTime': 'LPFILETIME'}, 'OpenProcess': {'dwDesiredAccess': 'DWORD', 'bInheritHandle': 'BOOL', 'dwProcessId': 'DWORD'}, 'IsProcessorFeaturePresent': {'ProcessorFeature': 'DWORD'}, 'GetProcessHandleCount': {'hProcess': 'HANDLE', 'pdwHandleCount': 'PDWORD'}, 'GetCurrentProcessorNumber': {'VOID': 'void'}, 'SetThreadIdealProcessorEx': {'hThread': 'HANDLE', 'lpIdealProcessor': 'PPROCESSOR_NUMBER', 'lpPreviousIdealProcessor': 'PPROCESSOR_NUMBER'}, 'GetThreadIdealProcessorEx': {'hThread': 'HANDLE', 'lpIdealProcessor': 'PPROCESSOR_NUMBER'}, 'GetCurrentProcessorNumberEx': {'ProcNumber': 'PPROCESSOR_NUMBER'}, 'GetProcessPriorityBoost': {'hProcess': 'HANDLE', 'pDisablePriorityBoost': 'PBOOL'}, 'SetProcessPriorityBoost': {'hProcess': 'HANDLE', 'bDisablePriorityBoost': 'BOOL'}, 'GetThreadIOPendingFlag': {'hThread': 'HANDLE', 'lpIOIsPending': 'PBOOL'}, 'GetSystemTimes': {'lpIdleTime': 'PFILETIME', 'lpKernelTime': 'PFILETIME', 'lpUserTime': 'PFILETIME'}, 'GetThreadInformation': {'hThread': 'HANDLE', 'ThreadInformationClass': 'THREAD_INFORMATION_CLASS', 'ThreadInformation': 'LPVOID', 'ThreadInformationSize': 'DWORD'}, 'SetThreadInformation': {'hThread': 'HANDLE', 'ThreadInformationClass': 'THREAD_INFORMATION_CLASS', 'ThreadInformation': 'LPVOID', 'ThreadInformationSize': 'DWORD'}, 'IsProcessCritical': {'hProcess': 'HANDLE', 'Critical': 'PBOOL'}, 'SetProtectedPolicy': {'PolicyGuid': 'LPCGUID', 'PolicyValue': 'ULONG_PTR', 'OldPolicyValue': 'PULONG_PTR'}, 'QueryProtectedPolicy': {'PolicyGuid': 'LPCGUID', 'PolicyValue': 'PULONG_PTR'}, 'SetThreadIdealProcessor': {'hThread': 'HANDLE', 'dwIdealProcessor': 'DWORD'}, 'SetProcessInformation': {'hProcess': 'HANDLE', 'ProcessInformationClass': 'PROCESS_INFORMATION_CLASS', 'ProcessInformation': 'LPVOID', 'ProcessInformationSize': 'DWORD'}, 'GetProcessInformation': {'hProcess': 'HANDLE', 'ProcessInformationClass': 'PROCESS_INFORMATION_CLASS', 'ProcessInformation': 'LPVOID', 'ProcessInformationSize': 'DWORD'}, 'CreateProcessAsUserA': {'hToken': 'HANDLE', 'lpApplicationName': 'LPCSTR', 'lpCommandLine': 'LPSTR', 'lpProcessAttributes': 'LPSECURITY_ATTRIBUTES', 'lpThreadAttributes': 'LPSECURITY_ATTRIBUTES', 'bInheritHandles': 'BOOL', 'dwCreationFlags': 'DWORD', 'lpEnvironment': 'LPVOID', 'lpCurrentDirectory': 'LPCSTR', 'lpStartupInfo': 'LPSTARTUPINFOA', 'lpProcessInformation': 'LPPROCESS_INFORMATION'}, 'GetProcessShutdownParameters': {'lpdwLevel': 'LPDWORD', 'lpdwFlags': 'LPDWORD'}, 'SetThreadDescription': {'hThread': 'HANDLE', 'lpThreadDescription': 'PCWSTR'}, 'GetThreadDescription': {'hThread': 'HANDLE', 'ppszThreadDescription': 'PWSTR'}, 'GetStartupInfoA': {'lpStartupInfo': 'LPSTARTUPINFOA'}}