ioapiset_data = {'CreateIoCompletionPort': {'FileHandle': 'HANDLE', 'ExistingCompletionPort': 'HANDLE', 'CompletionKey': 'ULONG_PTR', 'NumberOfConcurrentThreads': 'DWORD'}, 'GetQueuedCompletionStatus': {'CompletionPort': 'HANDLE', 'lpNumberOfBytesTransferred': 'LPDWORD', 'lpCompletionKey': 'PULONG_PTR', 'lpOverlapped': 'LPOVERLAPPED', 'dwMilliseconds': 'DWORD'}, 'GetQueuedCompletionStatusEx': {'CompletionPort': 'HANDLE', 'lpCompletionPortEntries': 'LPOVERLAPPED_ENTRY', 'ulCount': 'ULONG', 'ulNumEntriesRemoved': 'PULONG', 'dwMilliseconds': 'DWORD', 'fAlertable': 'BOOL'}, 'PostQueuedCompletionStatus': {'CompletionPort': 'HANDLE', 'dwNumberOfBytesTransferred': 'DWORD', 'dwCompletionKey': 'ULONG_PTR', 'lpOverlapped': 'LPOVERLAPPED'}, 'DeviceIoControl': {'hDevice': 'HANDLE', 'dwIoControlCode': 'DWORD', 'lpInBuffer': 'LPVOID', 'nInBufferSize': 'DWORD', 'lpOutBuffer': 'LPVOID', 'nOutBufferSize': 'DWORD', 'lpBytesReturned': 'LPDWORD', 'lpOverlapped': 'LPOVERLAPPED'}, 'GetOverlappedResult': {'hFile': 'HANDLE', 'lpOverlapped': 'LPOVERLAPPED', 'lpNumberOfBytesTransferred': 'LPDWORD', 'bWait': 'BOOL'}, 'CancelIoEx': {'hFile': 'HANDLE', 'lpOverlapped': 'LPOVERLAPPED'}, 'CancelIo': {'hFile': 'HANDLE'}, 'GetOverlappedResultEx': {'hFile': 'HANDLE', 'lpOverlapped': 'LPOVERLAPPED', 'lpNumberOfBytesTransferred': 'LPDWORD', 'dwMilliseconds': 'DWORD', 'bAlertable': 'BOOL'}, 'CancelSynchronousIo': {'hThread': 'HANDLE'}}