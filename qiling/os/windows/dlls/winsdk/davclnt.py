davclnt_data = {'DavAddConnection': {'ConnectionHandle': 'HANDLE', 'RemoteName': 'LPCWSTR', 'UserName': 'LPCWSTR', 'Password': 'LPCWSTR', 'ClientCert': 'PBYTE', 'CertSize': 'DWORD'}, 'DavDeleteConnection': {'ConnectionHandle': 'HANDLE'}, 'DavGetUNCFromHTTPPath': {'Url': 'LPCWSTR', 'UncPath': 'LPWSTR', 'lpSize': 'LPDWORD'}, 'DavGetHTTPFromUNCPath': {'UncPath': 'LPCWSTR', 'Url': 'LPWSTR', 'lpSize': 'LPDWORD'}, 'DavGetTheLockOwnerOfTheFile': {'FileName': 'LPCWSTR', 'LockOwnerName': 'PWSTR', 'LockOwnerNameLengthInBytes': 'PULONG'}, 'DavGetExtendedError': {'hFile': 'HANDLE', 'ExtError': 'DWORD', 'ExtErrorString': 'LPWSTR', 'cChSize': 'DWORD'}, 'DavFlushFile': {'hFile': 'HANDLE'}, 'DavInvalidateCache': {'URLName': 'LPCWSTR'}, 'DavCancelConnectionsToServer': {'lpName': 'LPWSTR', 'fForce': 'BOOL'}, 'DavRegisterAuthCallback': {'CallBack': 'PFNDAVAUTHCALLBACK', 'Version': 'ULONG'}, 'DavUnregisterAuthCallback': {'hCallback': 'DWORD'}}