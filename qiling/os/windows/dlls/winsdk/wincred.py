wincred_data = {'CredWriteW': {'Credential': 'PCREDENTIALW', 'Flags': 'DWORD'}, 'CredWriteA': {'Credential': 'PCREDENTIALA', 'Flags': 'DWORD'}, 'CredReadW': {'TargetName': 'LPCWSTR', 'Type': 'DWORD', 'Flags': 'DWORD', 'Credential': 'PCREDENTIALW'}, 'CredReadA': {'TargetName': 'LPCSTR', 'Type': 'DWORD', 'Flags': 'DWORD', 'Credential': 'PCREDENTIALA'}, 'CredEnumerateW': {'Filter': 'LPCWSTR', 'Flags': 'DWORD', 'Count': 'DWORD', 'Credential': 'PCREDENTIALW'}, 'CredEnumerateA': {'Filter': 'LPCSTR', 'Flags': 'DWORD', 'Count': 'DWORD', 'Credential': 'PCREDENTIALA'}, 'CredWriteDomainCredentialsW': {'TargetInfo': 'PCREDENTIAL_TARGET_INFORMATIONW', 'Credential': 'PCREDENTIALW', 'Flags': 'DWORD'}, 'CredWriteDomainCredentialsA': {'TargetInfo': 'PCREDENTIAL_TARGET_INFORMATIONA', 'Credential': 'PCREDENTIALA', 'Flags': 'DWORD'}, 'CredReadDomainCredentialsW': {'TargetInfo': 'PCREDENTIAL_TARGET_INFORMATIONW', 'Flags': 'DWORD', 'Count': 'DWORD', 'Credential': 'PCREDENTIALW'}, 'CredReadDomainCredentialsA': {'TargetInfo': 'PCREDENTIAL_TARGET_INFORMATIONA', 'Flags': 'DWORD', 'Count': 'DWORD', 'Credential': 'PCREDENTIALA'}, 'CredDeleteW': {'TargetName': 'LPCWSTR', 'Type': 'DWORD', 'Flags': 'DWORD'}, 'CredDeleteA': {'TargetName': 'LPCSTR', 'Type': 'DWORD', 'Flags': 'DWORD'}, 'CredRenameW': {'OldTargetName': 'LPCWSTR', 'NewTargetName': 'LPCWSTR', 'Type': 'DWORD', 'Flags': 'DWORD'}, 'CredRenameA': {'OldTargetName': 'LPCSTR', 'NewTargetName': 'LPCSTR', 'Type': 'DWORD', 'Flags': 'DWORD'}, 'CredGetTargetInfoW': {'TargetName': 'LPCWSTR', 'Flags': 'DWORD', 'TargetInfo': 'PCREDENTIAL_TARGET_INFORMATIONW'}, 'CredGetTargetInfoA': {'TargetName': 'LPCSTR', 'Flags': 'DWORD', 'TargetInfo': 'PCREDENTIAL_TARGET_INFORMATIONA'}, 'CredMarshalCredentialW': {'CredType': 'CRED_MARSHAL_TYPE', 'Credential': 'PVOID', 'MarshaledCredential': 'LPWSTR'}, 'CredMarshalCredentialA': {'CredType': 'CRED_MARSHAL_TYPE', 'Credential': 'PVOID', 'MarshaledCredential': 'LPSTR'}, 'CredUnmarshalCredentialW': {'MarshaledCredential': 'LPCWSTR', 'CredType': 'PCRED_MARSHAL_TYPE', 'Credential': 'PVOID'}, 'CredUnmarshalCredentialA': {'MarshaledCredential': 'LPCSTR', 'CredType': 'PCRED_MARSHAL_TYPE', 'Credential': 'PVOID'}, 'CredIsMarshaledCredentialW': {'MarshaledCredential': 'LPCWSTR'}, 'CredIsMarshaledCredentialA': {'MarshaledCredential': 'LPCSTR'}, 'CredUnPackAuthenticationBufferW': {'dwFlags': 'DWORD', 'pAuthBuffer': 'PVOID', 'cbAuthBuffer': 'DWORD', 'pszUserName': 'LPWSTR', 'pcchMaxUserName': 'DWORD', 'pszDomainName': 'LPWSTR', 'pcchMaxDomainName': 'DWORD', 'pszPassword': 'LPWSTR', 'pcchMaxPassword': 'DWORD'}, 'CredUnPackAuthenticationBufferA': {'dwFlags': 'DWORD', 'pAuthBuffer': 'PVOID', 'cbAuthBuffer': 'DWORD', 'pszUserName': 'LPSTR', 'pcchlMaxUserName': 'DWORD', 'pszDomainName': 'LPSTR', 'pcchMaxDomainName': 'DWORD', 'pszPassword': 'LPSTR', 'pcchMaxPassword': 'DWORD'}, 'CredPackAuthenticationBufferW': {'dwFlags': 'DWORD', 'pszUserName': 'LPWSTR', 'pszPassword': 'LPWSTR', 'pPackedCredentials': 'PBYTE', 'pcbPackedCredentials': 'DWORD'}, 'CredPackAuthenticationBufferA': {'dwFlags': 'DWORD', 'pszUserName': 'LPSTR', 'pszPassword': 'LPSTR', 'pPackedCredentials': 'PBYTE', 'pcbPackedCredentials': 'DWORD'}, 'CredProtectW': {'fAsSelf': 'BOOL', 'pszCredentials': 'LPWSTR', 'cchCredentials': 'DWORD', 'pszProtectedCredentials': 'LPWSTR', 'pcchMaxChars': 'DWORD', 'ProtectionType': 'CRED_PROTECTION_TYPE'}, 'CredProtectA': {'fAsSelf': 'BOOL', 'pszCredentials': 'LPSTR', 'cchCredentials': 'DWORD', 'pszProtectedCredentials': 'LPSTR', 'pcchMaxChars': 'DWORD', 'ProtectionType': 'CRED_PROTECTION_TYPE'}, 'CredUnprotectW': {'fAsSelf': 'BOOL', 'pszProtectedCredentials': 'LPWSTR', 'cchProtectedCredentials': 'DWORD', 'pszCredentials': 'LPWSTR', 'pcchMaxChars': 'DWORD'}, 'CredUnprotectA': {'fAsSelf': 'BOOL', 'pszProtectedCredentials': 'LPSTR', 'cchProtectedCredentials': 'DWORD', 'pszCredentials': 'LPSTR', 'pcchMaxChars': 'DWORD'}, 'CredIsProtectedW': {'pszProtectedCredentials': 'LPWSTR', 'pProtectionType': 'CRED_PROTECTION_TYPE'}, 'CredIsProtectedA': {'pszProtectedCredentials': 'LPSTR', 'pProtectionType': 'CRED_PROTECTION_TYPE'}, 'CredFindBestCredentialW': {'TargetName': 'LPCWSTR', 'Type': 'DWORD', 'Flags': 'DWORD', 'Credential': 'PCREDENTIALW'}, 'CredFindBestCredentialA': {'TargetName': 'LPCSTR', 'Type': 'DWORD', 'Flags': 'DWORD', 'Credential': 'PCREDENTIALA'}, 'CredGetSessionTypes': {'MaximumPersistCount': 'DWORD', 'MaximumPersist': 'LPDWORD'}, 'CredFree': {'Buffer': 'PVOID'}, 'CredUIPromptForCredentialsW': {'pUiInfo': 'PCREDUI_INFOW', 'pszTargetName': 'PCWSTR', 'pContext': 'PCtxtHandle', 'dwAuthError': 'DWORD', 'pszUserName': 'PWSTR', 'ulUserNameBufferSize': 'ULONG', 'pszPassword': 'PWSTR', 'ulPasswordBufferSize': 'ULONG', 'save': 'BOOL', 'dwFlags': 'DWORD'}, 'CredUIPromptForCredentialsA': {'pUiInfo': 'PCREDUI_INFOA', 'pszTargetName': 'PCSTR', 'pContext': 'PCtxtHandle', 'dwAuthError': 'DWORD', 'pszUserName': 'PSTR', 'ulUserNameBufferSize': 'ULONG', 'pszPassword': 'PSTR', 'ulPasswordBufferSize': 'ULONG', 'save': 'BOOL', 'dwFlags': 'DWORD'}, 'CredUIPromptForWindowsCredentialsW': {'pUiInfo': 'PCREDUI_INFOW', 'dwAuthError': 'DWORD', 'pulAuthPackage': 'ULONG', 'pvInAuthBuffer': 'LPCVOID', 'ulInAuthBufferSize': 'ULONG', 'ppvOutAuthBuffer': 'LPVOID', 'pulOutAuthBufferSize': 'ULONG', 'pfSave': 'BOOL', 'dwFlags': 'DWORD'}, 'CredUIPromptForWindowsCredentialsA': {'pUiInfo': 'PCREDUI_INFOA', 'dwAuthError': 'DWORD', 'pulAuthPackage': 'ULONG', 'pvInAuthBuffer': 'LPCVOID', 'ulInAuthBufferSize': 'ULONG', 'ppvOutAuthBuffer': 'LPVOID', 'pulOutAuthBufferSize': 'ULONG', 'pfSave': 'BOOL', 'dwFlags': 'DWORD'}, 'CredUIParseUserNameW': {'UserName': 'PCWSTR', 'user': 'WCHAR', 'userBufferSize': 'ULONG', 'domain': 'WCHAR', 'domainBufferSize': 'ULONG'}, 'CredUIParseUserNameA': {'userName': 'PCSTR', 'user': 'CHAR', 'userBufferSize': 'ULONG', 'domain': 'CHAR', 'domainBufferSize': 'ULONG'}, 'CredUICmdLinePromptForCredentialsW': {'pszTargetName': 'PCWSTR', 'pContext': 'PCtxtHandle', 'dwAuthError': 'DWORD', 'UserName': 'PWSTR', 'ulUserBufferSize': 'ULONG', 'pszPassword': 'PWSTR', 'ulPasswordBufferSize': 'ULONG', 'pfSave': 'PBOOL', 'dwFlags': 'DWORD'}, 'CredUICmdLinePromptForCredentialsA': {'pszTargetName': 'PCSTR', 'pContext': 'PCtxtHandle', 'dwAuthError': 'DWORD', 'UserName': 'PSTR', 'ulUserBufferSize': 'ULONG', 'pszPassword': 'PSTR', 'ulPasswordBufferSize': 'ULONG', 'pfSave': 'PBOOL', 'dwFlags': 'DWORD'}, 'CredUIConfirmCredentialsW': {'pszTargetName': 'PCWSTR', 'bConfirm': 'BOOL'}, 'CredUIConfirmCredentialsA': {'pszTargetName': 'PCSTR', 'bConfirm': 'BOOL'}, 'CredUIStoreSSOCredW': {'pszRealm': 'PCWSTR', 'pszUsername': 'PCWSTR', 'pszPassword': 'PCWSTR', 'bPersist': 'BOOL'}, 'CredUIReadSSOCredW': {'pszRealm': 'PCWSTR', 'ppszUsername': 'PWSTR'}}