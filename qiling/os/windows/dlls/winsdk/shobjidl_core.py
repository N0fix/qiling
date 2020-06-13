shobjidl_core_data = {'SHSimpleIDListFromPath': {'pszPath': 'PCWSTR'}, 'SHCreateItemFromIDList': {'pidl': 'LPCITEMIDLIST', 'riid': 'IID', 'ppv': 'void'}, 'SHCreateItemFromParsingName': {'pszPath': 'PCWSTR', 'pbc': 'IBindCtx', 'riid': 'IID', 'ppv': 'void'}, 'SHCreateItemWithParent': {'pidlParent': 'LPCITEMIDLIST', 'psfParent': 'IShellFolder', 'pidl': 'LPCITEMIDLIST', 'riid': 'IID', 'ppvItem': 'void'}, 'SHCreateItemFromRelativeName': {'psiParent': 'IShellItem', 'pszName': 'PCWSTR', 'pbc': 'IBindCtx', 'riid': 'IID', 'ppv': 'void'}, 'SHCreateItemInKnownFolder': {'kfid': 'KNOWNFOLDERID', 'dwKFFlags': 'DWORD', 'pszItem': 'PCWSTR', 'riid': 'IID', 'ppv': 'void'}, 'SHGetIDListFromObject': {'punk': 'IUnknown', 'ppidl': 'LPITEMIDLIST'}, 'SHGetItemFromObject': {'punk': 'IUnknown', 'riid': 'IID', 'ppv': 'void'}, 'SHGetPropertyStoreFromIDList': {'pidl': 'LPCITEMIDLIST', 'flags': 'GETPROPERTYSTOREFLAGS', 'riid': 'IID', 'ppv': 'void'}, 'SHGetPropertyStoreFromParsingName': {'pszPath': 'PCWSTR', 'pbc': 'IBindCtx', 'flags': 'GETPROPERTYSTOREFLAGS', 'riid': 'IID', 'ppv': 'void'}, 'SHGetNameFromIDList': {'pidl': 'LPCITEMIDLIST', 'sigdnName': 'SIGDN', 'ppszName': 'PWSTR'}, 'SHGetItemFromDataObject': {'pdtobj': 'IDataObject', 'dwFlags': 'DATAOBJ_GET_ITEM_FLAGS', 'riid': 'IID', 'ppv': 'void'}, 'SHCreateShellItemArray': {'pidlParent': 'LPCITEMIDLIST', 'psf': 'IShellFolder', 'cidl': 'UINT', 'ppidl': 'LPCITEMIDLIST', 'ppsiItemArray': 'IShellItemArray'}, 'SHCreateShellItemArrayFromDataObject': {'pdo': 'IDataObject', 'riid': 'IID', 'ppv': 'void'}, 'SHCreateShellItemArrayFromIDLists': {'cidl': 'UINT', 'rgpidl': 'LPCITEMIDLIST', 'ppsiItemArray': 'IShellItemArray'}, 'SHCreateShellItemArrayFromShellItem': {'psi': 'IShellItem', 'riid': 'IID', 'ppv': 'void'}, 'SHCreateAssociationRegistration': {'riid': 'IID', 'ppv': 'void'}, 'SHCreateDefaultExtractIcon': {'riid': 'IID', 'ppv': 'void'}, 'SetCurrentProcessExplicitAppUserModelID': {'AppID': 'PCWSTR'}, 'GetCurrentProcessExplicitAppUserModelID': {'AppID': 'PWSTR'}, 'SHGetTemporaryPropertyForItem': {'psi': 'IShellItem', 'propkey': 'PROPERTYKEY', 'ppropvar': 'PROPVARIANT'}, 'SHSetTemporaryPropertyForItem': {'psi': 'IShellItem', 'propkey': 'PROPERTYKEY', 'propvar': 'PROPVARIANT'}, 'SHShowManageLibraryUI': {'psiLibrary': 'IShellItem', 'hwndOwner': 'HWND', 'pszTitle': 'LPCWSTR', 'pszInstruction': 'LPCWSTR', 'lmdOptions': 'LIBRARYMANAGEDIALOGOPTIONS'}, 'SHResolveLibrary': {'psiLibrary': 'IShellItem'}, 'SHAssocEnumHandlers': {'pszExtra': 'PCWSTR', 'afFilter': 'ASSOC_FILTER', 'ppEnumHandler': 'IEnumAssocHandlers'}, 'SHAssocEnumHandlersForProtocolByApplication': {'protocol': 'PCWSTR', 'riid': 'IID', 'enumHandlers': 'void'}}