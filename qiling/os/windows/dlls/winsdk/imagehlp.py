imagehlp_data = {'BindImage': {'ImageName': 'PCSTR', 'DllPath': 'PCSTR', 'SymbolPath': 'PCSTR'}, 'BindImageEx': {'Flags': 'DWORD', 'ImageName': 'PCSTR', 'DllPath': 'PCSTR', 'SymbolPath': 'PCSTR', 'StatusRoutine': 'PIMAGEHLP_STATUS_ROUTINE'}, 'ReBaseImage': {'CurrentImageName': 'PCSTR', 'SymbolPath': 'PCSTR', 'fReBase': 'BOOL', 'fRebaseSysfileOk': 'BOOL', 'fGoingDown': 'BOOL', 'CheckImageSize': 'ULONG', 'OldImageSize': 'ULONG', 'OldImageBase': 'ULONG_PTR', 'NewImageSize': 'ULONG', 'NewImageBase': 'ULONG_PTR', 'TimeStamp': 'ULONG'}, 'ReBaseImage64': {'CurrentImageName': 'PCSTR', 'SymbolPath': 'PCSTR', 'fReBase': 'BOOL', 'fRebaseSysfileOk': 'BOOL', 'fGoingDown': 'BOOL', 'CheckImageSize': 'ULONG', 'OldImageSize': 'ULONG', 'OldImageBase': 'ULONG64', 'NewImageSize': 'ULONG', 'NewImageBase': 'ULONG64', 'TimeStamp': 'ULONG'}, 'CheckSumMappedFile': {'BaseAddress': 'PVOID', 'FileLength': 'DWORD', 'HeaderSum': 'PDWORD', 'CheckSum': 'PDWORD'}, 'MapFileAndCheckSumA': {'Filename': 'PCSTR', 'HeaderSum': 'PDWORD', 'CheckSum': 'PDWORD'}, 'MapFileAndCheckSumW': {'Filename': 'PCWSTR', 'HeaderSum': 'PDWORD', 'CheckSum': 'PDWORD'}, 'GetImageConfigInformation': {'LoadedImage': 'PLOADED_IMAGE', 'ImageConfigInformation': 'PIMAGE_LOAD_CONFIG_DIRECTORY'}, 'GetImageUnusedHeaderBytes': {'LoadedImage': 'PLOADED_IMAGE', 'SizeUnusedHeaderBytes': 'PDWORD'}, 'SetImageConfigInformation': {'LoadedImage': 'PLOADED_IMAGE', 'ImageConfigInformation': 'PIMAGE_LOAD_CONFIG_DIRECTORY'}, 'ImageGetDigestStream': {'FileHandle': 'HANDLE', 'DigestLevel': 'DWORD', 'DigestFunction': 'DIGEST_FUNCTION', 'DigestHandle': 'DIGEST_HANDLE'}, 'ImageAddCertificate': {'FileHandle': 'HANDLE', 'Certificate': 'LPWIN_CERTIFICATE', 'Index': 'PDWORD'}, 'ImageRemoveCertificate': {'FileHandle': 'HANDLE', 'Index': 'DWORD'}, 'ImageEnumerateCertificates': {'FileHandle': 'HANDLE', 'TypeFilter': 'WORD', 'CertificateCount': 'PDWORD', 'Indices': 'PDWORD', 'IndexCount': 'DWORD'}, 'ImageGetCertificateData': {'FileHandle': 'HANDLE', 'CertificateIndex': 'DWORD', 'Certificate': 'LPWIN_CERTIFICATE', 'RequiredLength': 'PDWORD'}, 'ImageGetCertificateHeader': {'FileHandle': 'HANDLE', 'CertificateIndex': 'DWORD', 'Certificateheader': 'LPWIN_CERTIFICATE'}, 'ImageLoad': {'DllName': 'PCSTR', 'DllPath': 'PCSTR'}, 'ImageUnload': {'LoadedImage': 'PLOADED_IMAGE'}, 'MapAndLoad': {'ImageName': 'PCSTR', 'DllPath': 'PCSTR', 'LoadedImage': 'PLOADED_IMAGE', 'DotDll': 'BOOL', 'ReadOnly': 'BOOL'}, 'UnMapAndLoad': {'LoadedImage': 'PLOADED_IMAGE'}, 'TouchFileTimes': {'FileHandle': 'HANDLE', 'pSystemTime': 'PSYSTEMTIME'}, 'SplitSymbols': {'ImageName': 'PSTR', 'SymbolsPath': 'PCSTR', 'SymbolFilePath': 'PSTR', 'Flags': 'ULONG'}, 'UpdateDebugInfoFile': {'ImageFileName': 'PCSTR', 'SymbolPath': 'PCSTR', 'DebugFilePath': 'PSTR', 'NtHeaders': 'PIMAGE_NT_HEADERS32'}, 'UpdateDebugInfoFileEx': {'ImageFileName': 'PCSTR', 'SymbolPath': 'PCSTR', 'DebugFilePath': 'PSTR', 'NtHeaders': 'PIMAGE_NT_HEADERS32', 'OldCheckSum': 'DWORD'}}