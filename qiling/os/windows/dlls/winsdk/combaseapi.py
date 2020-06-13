combaseapi_data = {'CoGetMalloc': {'dwMemContext': 'DWORD', 'ppMalloc': 'LPMALLOC'}, 'CreateStreamOnHGlobal': {'hGlobal': 'HGLOBAL', 'fDeleteOnRelease': 'BOOL', 'ppstm': 'LPSTREAM'}, 'GetHGlobalFromStream': {'pstm': 'LPSTREAM', 'phglobal': 'HGLOBAL'}, 'CoUninitialize': {'VOID': 'void'}, 'CoGetCurrentProcess': {'VOID': 'void'}, 'CoInitializeEx': {'pvReserved': 'LPVOID', 'dwCoInit': 'DWORD'}, 'CoGetCallerTID': {'lpdwTID': 'LPDWORD'}, 'CoGetCurrentLogicalThreadId': {'pguid': 'GUID'}, 'CoGetContextToken': {'pToken': 'ULONG_PTR'}, 'CoGetDefaultContext': {'aptType': 'APTTYPE', 'riid': 'IID', 'ppv': 'void'}, 'CoGetApartmentType': {'pAptType': 'APTTYPE', 'pAptQualifier': 'APTTYPEQUALIFIER'}, 'CoDecodeProxy': {'dwClientPid': 'DWORD', 'ui64ProxyAddress': 'UINT64', 'pServerInformation': 'PServerInformation'}, 'CoIncrementMTAUsage': {'pCookie': 'CO_MTA_USAGE_COOKIE'}, 'CoDecrementMTAUsage': {'Cookie': 'CO_MTA_USAGE_COOKIE'}, 'CoAllowUnmarshalerCLSID': {'clsid': 'IID'}, 'CoGetObjectContext': {'riid': 'IID', 'ppv': 'LPVOID'}, 'CoGetClassObject': {'rclsid': 'IID', 'dwClsContext': 'DWORD', 'pvReserved': 'LPVOID', 'riid': 'IID', 'ppv': 'LPVOID'}, 'CoRegisterClassObject': {'rclsid': 'IID', 'pUnk': 'LPUNKNOWN', 'dwClsContext': 'DWORD', 'flags': 'DWORD', 'lpdwRegister': 'LPDWORD'}, 'CoRevokeClassObject': {'dwRegister': 'DWORD'}, 'CoResumeClassObjects': {'VOID': 'void'}, 'CoSuspendClassObjects': {'VOID': 'void'}, 'CoAddRefServerProcess': {'VOID': 'void'}, 'CoReleaseServerProcess': {'VOID': 'void'}, 'CoGetPSClsid': {'riid': 'IID', 'pClsid': 'CLSID'}, 'CoRegisterPSClsid': {'riid': 'IID', 'rclsid': 'IID'}, 'CoRegisterSurrogate': {'pSurrogate': 'LPSURROGATE'}, 'CoGetMarshalSizeMax': {'pulSize': 'ULONG', 'riid': 'IID', 'pUnk': 'LPUNKNOWN', 'dwDestContext': 'DWORD', 'pvDestContext': 'LPVOID', 'mshlflags': 'DWORD'}, 'CoMarshalInterface': {'pStm': 'LPSTREAM', 'riid': 'IID', 'pUnk': 'LPUNKNOWN', 'dwDestContext': 'DWORD', 'pvDestContext': 'LPVOID', 'mshlflags': 'DWORD'}, 'CoUnmarshalInterface': {'pStm': 'LPSTREAM', 'riid': 'IID', 'ppv': 'LPVOID'}, 'CoMarshalHresult': {'pstm': 'LPSTREAM', 'hresult': 'HRESULT'}, 'CoUnmarshalHresult': {'pstm': 'LPSTREAM', 'phresult': 'HRESULT'}, 'CoReleaseMarshalData': {'pStm': 'LPSTREAM'}, 'CoDisconnectObject': {'pUnk': 'LPUNKNOWN', 'dwReserved': 'DWORD'}, 'CoLockObjectExternal': {'pUnk': 'LPUNKNOWN', 'fLock': 'BOOL', 'fLastUnlockReleases': 'BOOL'}, 'CoGetStandardMarshal': {'riid': 'IID', 'pUnk': 'LPUNKNOWN', 'dwDestContext': 'DWORD', 'pvDestContext': 'LPVOID', 'mshlflags': 'DWORD', 'ppMarshal': 'LPMARSHAL'}, 'CoGetStdMarshalEx': {'pUnkOuter': 'LPUNKNOWN', 'smexflags': 'DWORD', 'ppUnkInner': 'LPUNKNOWN'}, 'CoIsHandlerConnected': {'pUnk': 'LPUNKNOWN'}, 'CoMarshalInterThreadInterfaceInStream': {'riid': 'IID', 'pUnk': 'LPUNKNOWN', 'ppStm': 'LPSTREAM'}, 'CoGetInterfaceAndReleaseStream': {'pStm': 'LPSTREAM', 'iid': 'IID', 'ppv': 'LPVOID'}, 'CoCreateFreeThreadedMarshaler': {'punkOuter': 'LPUNKNOWN', 'ppunkMarshal': 'LPUNKNOWN'}, 'CoFreeUnusedLibraries': {'VOID': 'void'}, 'CoFreeUnusedLibrariesEx': {'dwUnloadDelay': 'DWORD', 'dwReserved': 'DWORD'}, 'CoDisconnectContext': {'dwTimeout': 'DWORD'}, 'CoInitializeSecurity': {'pSecDesc': 'PSECURITY_DESCRIPTOR', 'cAuthSvc': 'LONG', 'asAuthSvc': 'SOLE_AUTHENTICATION_SERVICE', 'pReserved1': 'void', 'dwAuthnLevel': 'DWORD', 'dwImpLevel': 'DWORD', 'pAuthList': 'void', 'dwCapabilities': 'DWORD', 'pReserved3': 'void'}, 'CoGetCallContext': {'riid': 'IID', 'ppInterface': 'void'}, 'CoQueryProxyBlanket': {'pProxy': 'IUnknown', 'pwAuthnSvc': 'DWORD', 'pAuthzSvc': 'DWORD', 'pServerPrincName': 'LPOLESTR', 'pAuthnLevel': 'DWORD', 'pImpLevel': 'DWORD', 'pAuthInfo': 'RPC_AUTH_IDENTITY_HANDLE', 'pCapabilites': 'DWORD'}, 'CoSetProxyBlanket': {'pProxy': 'IUnknown', 'dwAuthnSvc': 'DWORD', 'dwAuthzSvc': 'DWORD', 'pServerPrincName': 'OLECHAR', 'dwAuthnLevel': 'DWORD', 'dwImpLevel': 'DWORD', 'pAuthInfo': 'RPC_AUTH_IDENTITY_HANDLE', 'dwCapabilities': 'DWORD'}, 'CoCopyProxy': {'pProxy': 'IUnknown', 'ppCopy': 'IUnknown'}, 'CoQueryClientBlanket': {'pAuthnSvc': 'DWORD', 'pAuthzSvc': 'DWORD', 'pServerPrincName': 'LPOLESTR', 'pAuthnLevel': 'DWORD', 'pImpLevel': 'DWORD', 'pPrivs': 'RPC_AUTHZ_HANDLE', 'pCapabilities': 'DWORD'}, 'CoImpersonateClient': {'VOID': 'void'}, 'CoRevertToSelf': {'VOID': 'void'}, 'CoQueryAuthenticationServices': {'pcAuthSvc': 'DWORD', 'asAuthSvc': 'SOLE_AUTHENTICATION_SERVICE'}, 'CoSwitchCallContext': {'pNewObject': 'IUnknown', 'ppOldObject': 'IUnknown'}, 'CoCreateInstance': {'rclsid': 'IID', 'pUnkOuter': 'LPUNKNOWN', 'dwClsContext': 'DWORD', 'riid': 'IID', 'ppv': 'LPVOID'}, 'CoCreateInstanceEx': {'Clsid': 'IID', 'punkOuter': 'IUnknown', 'dwClsCtx': 'DWORD', 'pServerInfo': 'COSERVERINFO', 'dwCount': 'DWORD', 'pResults': 'MULTI_QI'}, 'CoCreateInstanceFromApp': {'Clsid': 'IID', 'punkOuter': 'IUnknown', 'dwClsCtx': 'DWORD', 'reserved': 'PVOID', 'dwCount': 'DWORD', 'pResults': 'MULTI_QI'}, 'CoRegisterActivationFilter': {'pActivationFilter': 'IActivationFilter'}, 'CoGetCancelObject': {'dwThreadId': 'DWORD', 'iid': 'IID', 'ppUnk': 'void'}, 'CoSetCancelObject': {'pUnk': 'IUnknown'}, 'CoCancelCall': {'dwThreadId': 'DWORD', 'ulTimeout': 'ULONG'}, 'CoTestCancel': {'VOID': 'void'}, 'CoEnableCallCancellation': {'pReserved': 'LPVOID'}, 'CoDisableCallCancellation': {'pReserved': 'LPVOID'}, 'StringFromCLSID': {'rclsid': 'IID', 'lplpsz': 'LPOLESTR'}, 'CLSIDFromString': {'lpsz': 'LPCOLESTR', 'pclsid': 'LPCLSID'}, 'StringFromIID': {'rclsid': 'IID', 'lplpsz': 'LPOLESTR'}, 'IIDFromString': {'lpsz': 'LPCOLESTR', 'lpiid': 'LPIID'}, 'ProgIDFromCLSID': {'clsid': 'IID', 'lplpszProgID': 'LPOLESTR'}, 'CLSIDFromProgID': {'lpszProgID': 'LPCOLESTR', 'lpclsid': 'LPCLSID'}, 'StringFromGUID2': {'rguid': 'GUID', 'lpsz': 'LPOLESTR', 'cchMax': 'int'}, 'CoCreateGuid': {'pguid': 'GUID'}, 'PropVariantCopy': {'pvarDest': 'PROPVARIANT', 'pvarSrc': 'PROPVARIANT'}, 'PropVariantClear': {'pvar': 'PROPVARIANT'}, 'FreePropVariantArray': {'cVariants': 'ULONG', 'rgvars': 'PROPVARIANT'}, 'CoWaitForMultipleHandles': {'dwFlags': 'DWORD', 'dwTimeout': 'DWORD', 'cHandles': 'ULONG', 'pHandles': 'LPHANDLE', 'lpdwindex': 'LPDWORD'}, 'CoWaitForMultipleObjects': {'dwFlags': 'DWORD', 'dwTimeout': 'DWORD', 'cHandles': 'ULONG', 'pHandles': 'HANDLE', 'lpdwindex': 'LPDWORD'}, 'CoGetTreatAsClass': {'clsidOld': 'IID', 'pClsidNew': 'LPCLSID'}, 'CoInvalidateRemoteMachineBindings': {'pszMachineName': 'LPOLESTR'}, 'RoGetAgileReference': {'options': {'name': 'AgileReferenceOptions', 'data_type': 'Enum', 'enumerators': []}, 'riid': 'IID', 'pUnk': 'IUnknown', 'ppAgileReference': 'IAgileReference'}, 'CoTaskMemAlloc': {'cb': 'SIZE_T'}, 'CoTaskMemRealloc': {'pv': 'LPVOID', 'cb': 'SIZE_T'}, 'CoTaskMemFree': {'pv': 'LPVOID'}, 'CoFileTimeNow': {'lpFileTime': 'FILETIME'}, 'CLSIDFromProgIDEx': {'lpszProgID': 'LPCOLESTR', 'lpclsid': 'LPCLSID'}}