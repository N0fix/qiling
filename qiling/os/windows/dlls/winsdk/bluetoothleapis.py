bluetoothleapis_data = {'BluetoothGATTGetServices': {'hDevice': 'HANDLE', 'ServicesBufferCount': 'USHORT', 'ServicesBuffer': 'PBTH_LE_GATT_SERVICE', 'ServicesBufferActual': 'USHORT', 'Flags': 'ULONG'}, 'BluetoothGATTGetIncludedServices': {'hDevice': 'HANDLE', 'ParentService': 'PBTH_LE_GATT_SERVICE', 'IncludedServicesBufferCount': 'USHORT', 'IncludedServicesBuffer': 'PBTH_LE_GATT_SERVICE', 'IncludedServicesBufferActual': 'USHORT', 'Flags': 'ULONG'}, 'BluetoothGATTGetCharacteristics': {'hDevice': 'HANDLE', 'Service': 'PBTH_LE_GATT_SERVICE', 'CharacteristicsBufferCount': 'USHORT', 'CharacteristicsBuffer': 'PBTH_LE_GATT_CHARACTERISTIC', 'CharacteristicsBufferActual': 'USHORT', 'Flags': 'ULONG'}, 'BluetoothGATTGetDescriptors': {'hDevice': 'HANDLE', 'Characteristic': 'PBTH_LE_GATT_CHARACTERISTIC', 'DescriptorsBufferCount': 'USHORT', 'DescriptorsBuffer': 'PBTH_LE_GATT_DESCRIPTOR', 'DescriptorsBufferActual': 'USHORT', 'Flags': 'ULONG'}, 'BluetoothGATTGetCharacteristicValue': {'hDevice': 'HANDLE', 'Characteristic': 'PBTH_LE_GATT_CHARACTERISTIC', 'CharacteristicValueDataSize': 'ULONG', 'CharacteristicValue': 'PBTH_LE_GATT_CHARACTERISTIC_VALUE', 'CharacteristicValueSizeRequired': 'USHORT', 'Flags': 'ULONG'}, 'BluetoothGATTGetDescriptorValue': {'hDevice': 'HANDLE', 'Descriptor': 'PBTH_LE_GATT_DESCRIPTOR', 'DescriptorValueDataSize': 'ULONG', 'DescriptorValue': 'PBTH_LE_GATT_DESCRIPTOR_VALUE', 'DescriptorValueSizeRequired': 'USHORT', 'Flags': 'ULONG'}, 'BluetoothGATTBeginReliableWrite': {'hDevice': 'HANDLE', 'ReliableWriteContext': 'PBTH_LE_GATT_RELIABLE_WRITE_CONTEXT', 'Flags': 'ULONG'}, 'BluetoothGATTSetCharacteristicValue': {'hDevice': 'HANDLE', 'Characteristic': 'PBTH_LE_GATT_CHARACTERISTIC', 'CharacteristicValue': 'PBTH_LE_GATT_CHARACTERISTIC_VALUE', 'ReliableWriteContext': 'BTH_LE_GATT_RELIABLE_WRITE_CONTEXT', 'Flags': 'ULONG'}, 'BluetoothGATTEndReliableWrite': {'hDevice': 'HANDLE', 'ReliableWriteContext': 'BTH_LE_GATT_RELIABLE_WRITE_CONTEXT', 'Flags': 'ULONG'}, 'BluetoothGATTAbortReliableWrite': {'hDevice': 'HANDLE', 'ReliableWriteContext': 'BTH_LE_GATT_RELIABLE_WRITE_CONTEXT', 'Flags': 'ULONG'}, 'BluetoothGATTSetDescriptorValue': {'hDevice': 'HANDLE', 'Descriptor': 'PBTH_LE_GATT_DESCRIPTOR', 'DescriptorValue': 'PBTH_LE_GATT_DESCRIPTOR_VALUE', 'Flags': 'ULONG'}, 'BluetoothGATTRegisterEvent': {'hService': 'HANDLE', 'EventType': 'BTH_LE_GATT_EVENT_TYPE', 'EventParameterIn': 'PVOID', 'Callback': 'PFNBLUETOOTH_GATT_EVENT_CALLBACK', 'CallbackContext': 'PVOID', 'pEventHandle': 'BLUETOOTH_GATT_EVENT_HANDLE', 'Flags': 'ULONG'}, 'BluetoothGATTUnregisterEvent': {'EventHandle': 'BLUETOOTH_GATT_EVENT_HANDLE', 'Flags': 'ULONG'}}