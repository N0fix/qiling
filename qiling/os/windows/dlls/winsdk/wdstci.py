wdstci_data = {'WdsTransportClientInitialize': {'VOID': 'void'}, 'WdsTransportClientInitializeSession': {'pSessionRequest': 'PWDS_TRANSPORTCLIENT_REQUEST', 'pCallerData': 'PVOID', 'hSessionKey': 'PHANDLE'}, 'WdsTransportClientRegisterCallback': {'hSessionKey': 'HANDLE', 'CallbackId': 'TRANSPORTCLIENT_CALLBACK_ID', 'pfnCallback': 'PVOID'}, 'WdsTransportClientStartSession': {'hSessionKey': 'HANDLE'}, 'WdsTransportClientCompleteReceive': {'hSessionKey': 'HANDLE', 'ulSize': 'ULONG', 'pullOffset': 'PULARGE_INTEGER'}, 'WdsTransportClientCancelSession': {'hSessionKey': 'HANDLE'}, 'WdsTransportClientWaitForCompletion': {'hSessionKey': 'HANDLE', 'uTimeout': 'ULONG'}, 'WdsTransportClientQueryStatus': {'hSessionKey': 'HANDLE', 'puStatus': 'PULONG', 'puErrorCode': 'PULONG'}, 'WdsTransportClientCloseSession': {'hSessionKey': 'HANDLE'}, 'WdsTransportClientAddRefBuffer': {'pvBuffer': 'PVOID'}, 'WdsTransportClientReleaseBuffer': {'pvBuffer': 'PVOID'}, 'WdsTransportClientShutdown': {'VOID': 'void'}}