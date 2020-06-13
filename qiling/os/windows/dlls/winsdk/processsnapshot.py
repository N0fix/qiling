processsnapshot_data = {'PssCaptureSnapshot': {'ProcessHandle': 'HANDLE', 'CaptureFlags': 'PSS_CAPTURE_FLAGS', 'ThreadContextFlags': 'DWORD', 'SnapshotHandle': 'HPSS'}, 'PssFreeSnapshot': {'ProcessHandle': 'HANDLE', 'SnapshotHandle': 'HPSS'}, 'PssQuerySnapshot': {'SnapshotHandle': 'HPSS', 'InformationClass': 'PSS_QUERY_INFORMATION_CLASS', 'Buffer': 'void', 'BufferLength': 'DWORD'}, 'PssWalkSnapshot': {'SnapshotHandle': 'HPSS', 'InformationClass': 'PSS_WALK_INFORMATION_CLASS', 'WalkMarkerHandle': 'HPSSWALK', 'Buffer': 'void', 'BufferLength': 'DWORD'}, 'PssDuplicateSnapshot': {'SourceProcessHandle': 'HANDLE', 'SnapshotHandle': 'HPSS', 'TargetProcessHandle': 'HANDLE', 'TargetSnapshotHandle': 'HPSS', 'Flags': 'PSS_DUPLICATE_FLAGS'}, 'PssWalkMarkerCreate': {'Allocator': 'PSS_ALLOCATOR', 'WalkMarkerHandle': 'HPSSWALK'}, 'PssWalkMarkerFree': {'WalkMarkerHandle': 'HPSSWALK'}, 'PssWalkMarkerGetPosition': {'WalkMarkerHandle': 'HPSSWALK', 'Position': 'ULONG_PTR'}, 'PssWalkMarkerSetPosition': {'WalkMarkerHandle': 'HPSSWALK', 'Position': 'ULONG_PTR'}, 'PssWalkMarkerSeekToBeginning': {'WalkMarkerHandle': 'HPSSWALK'}}