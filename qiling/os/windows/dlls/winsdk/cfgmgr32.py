cfgmgr32_data = {'CM_Add_Empty_Log_Conf': {'plcLogConf': 'PLOG_CONF', 'dnDevInst': 'DEVINST', 'Priority': 'PRIORITY', 'ulFlags': 'ULONG'}, 'CM_Add_Empty_Log_Conf_Ex': {'plcLogConf': 'PLOG_CONF', 'dnDevInst': 'DEVINST', 'Priority': 'PRIORITY', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Add_Res_Des': {'prdResDes': 'PRES_DES', 'lcLogConf': 'LOG_CONF', 'ResourceID': 'RESOURCEID', 'ResourceData': 'PCVOID', 'ResourceLen': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Add_Res_Des_Ex': {'prdResDes': 'PRES_DES', 'lcLogConf': 'LOG_CONF', 'ResourceID': 'RESOURCEID', 'ResourceData': 'PCVOID', 'ResourceLen': 'ULONG', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Delete_Class_Key': {'ClassGuid': 'LPGUID', 'ulFlags': 'ULONG'}, 'CM_Delete_DevNode_Key': {'dnDevNode': 'DEVNODE', 'ulHardwareProfile': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Disable_DevNode': {'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Disconnect_Machine': {'hMachine': 'HMACHINE'}, 'CM_Enable_DevNode': {'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Enumerate_Classes': {'ulClassIndex': 'ULONG', 'ClassGuid': 'LPGUID', 'ulFlags': 'ULONG'}, 'CM_Enumerate_Classes_Ex': {'ulClassIndex': 'ULONG', 'ClassGuid': 'LPGUID', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Free_Log_Conf': {'lcLogConfToBeFreed': 'LOG_CONF', 'ulFlags': 'ULONG'}, 'CM_Free_Log_Conf_Ex': {'lcLogConfToBeFreed': 'LOG_CONF', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Free_Log_Conf_Handle': {'lcLogConf': 'LOG_CONF'}, 'CM_Free_Res_Des': {'prdResDes': 'PRES_DES', 'rdResDes': 'RES_DES', 'ulFlags': 'ULONG'}, 'CM_Free_Res_Des_Ex': {'prdResDes': 'PRES_DES', 'rdResDes': 'RES_DES', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Free_Res_Des_Handle': {'rdResDes': 'RES_DES'}, 'CM_Get_Child': {'pdnDevInst': 'PDEVINST', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Get_Child_Ex': {'pdnDevInst': 'PDEVINST', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Depth': {'pulDepth': 'PULONG', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Get_Depth_Ex': {'pulDepth': 'PULONG', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Device_IDW': {'dnDevInst': 'DEVINST', 'Buffer': 'PWSTR', 'BufferLen': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Device_ID_ListA': {'pszFilter': 'PCSTR', 'Buffer': 'PZZSTR', 'BufferLen': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Device_ID_ListW': {'pszFilter': 'PCWSTR', 'Buffer': 'PZZWSTR', 'BufferLen': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Device_ID_List_SizeA': {'pulLen': 'PULONG', 'pszFilter': 'PCSTR', 'ulFlags': 'ULONG'}, 'CM_Get_Device_ID_List_SizeW': {'pulLen': 'PULONG', 'pszFilter': 'PCWSTR', 'ulFlags': 'ULONG'}, 'CM_Get_Device_ID_Size': {'pulLen': 'PULONG', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Get_Device_ID_Size_Ex': {'pulLen': 'PULONG', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_DevNode_PropertyW': {'dnDevInst': 'DEVINST', 'PropertyKey': 'DEVPROPKEY', 'PropertyType': 'DEVPROPTYPE', 'PropertyBuffer': 'PBYTE', 'PropertyBufferSize': 'PULONG', 'ulFlags': 'ULONG'}, 'CM_Get_DevNode_Property_Keys': {'dnDevInst': 'DEVINST', 'PropertyKeyArray': 'DEVPROPKEY', 'PropertyKeyCount': 'PULONG', 'ulFlags': 'ULONG'}, 'CM_Get_DevNode_Property_Keys_Ex': {'dnDevInst': 'DEVINST', 'PropertyKeyArray': 'DEVPROPKEY', 'PropertyKeyCount': 'PULONG', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_DevNode_Registry_PropertyW': {'dnDevInst': 'DEVINST', 'ulProperty': 'ULONG', 'pulRegDataType': 'PULONG', 'Buffer': 'PVOID', 'pulLength': 'PULONG', 'ulFlags': 'ULONG'}, 'CM_Get_DevNode_Status': {'pulStatus': 'PULONG', 'pulProblemNumber': 'PULONG', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Get_DevNode_Status_Ex': {'pulStatus': 'PULONG', 'pulProblemNumber': 'PULONG', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_First_Log_Conf': {'plcLogConf': 'PLOG_CONF', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Get_First_Log_Conf_Ex': {'plcLogConf': 'PLOG_CONF', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Device_Interface_ListA': {'InterfaceClassGuid': 'LPGUID', 'pDeviceID': 'DEVINSTID_A', 'Buffer': 'PZZSTR', 'BufferLen': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Device_Interface_ListW': {'InterfaceClassGuid': 'LPGUID', 'pDeviceID': 'DEVINSTID_W', 'Buffer': 'PZZWSTR', 'BufferLen': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Device_Interface_List_SizeA': {'pulLen': 'PULONG', 'InterfaceClassGuid': 'LPGUID', 'pDeviceID': 'DEVINSTID_A', 'ulFlags': 'ULONG'}, 'CM_Get_Device_Interface_List_SizeW': {'pulLen': 'PULONG', 'InterfaceClassGuid': 'LPGUID', 'pDeviceID': 'DEVINSTID_W', 'ulFlags': 'ULONG'}, 'CM_Get_Device_Interface_PropertyW': {'pszDeviceInterface': 'LPCWSTR', 'PropertyKey': 'DEVPROPKEY', 'PropertyType': 'DEVPROPTYPE', 'PropertyBuffer': 'PBYTE', 'PropertyBufferSize': 'PULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Device_Interface_Property_ExW': {'pszDeviceInterface': 'LPCWSTR', 'PropertyKey': 'DEVPROPKEY', 'PropertyType': 'DEVPROPTYPE', 'PropertyBuffer': 'PBYTE', 'PropertyBufferSize': 'PULONG', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Device_Interface_Property_KeysW': {'pszDeviceInterface': 'LPCWSTR', 'PropertyKeyArray': 'DEVPROPKEY', 'PropertyKeyCount': 'PULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Log_Conf_Priority': {'lcLogConf': 'LOG_CONF', 'pPriority': 'PPRIORITY', 'ulFlags': 'ULONG'}, 'CM_Get_Log_Conf_Priority_Ex': {'lcLogConf': 'LOG_CONF', 'pPriority': 'PPRIORITY', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Next_Log_Conf': {'plcLogConf': 'PLOG_CONF', 'lcLogConf': 'LOG_CONF', 'ulFlags': 'ULONG'}, 'CM_Get_Next_Log_Conf_Ex': {'plcLogConf': 'PLOG_CONF', 'lcLogConf': 'LOG_CONF', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Parent': {'pdnDevInst': 'PDEVINST', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Get_Parent_Ex': {'pdnDevInst': 'PDEVINST', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Res_Des_Data': {'rdResDes': 'RES_DES', 'Buffer': 'PVOID', 'BufferLen': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Res_Des_Data_Ex': {'rdResDes': 'RES_DES', 'Buffer': 'PVOID', 'BufferLen': 'ULONG', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Res_Des_Data_Size': {'pulSize': 'PULONG', 'rdResDes': 'RES_DES', 'ulFlags': 'ULONG'}, 'CM_Get_Res_Des_Data_Size_Ex': {'pulSize': 'PULONG', 'rdResDes': 'RES_DES', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Sibling': {'pdnDevInst': 'PDEVINST', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Get_Sibling_Ex': {'pdnDevInst': 'PDEVINST', 'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Version': {'VOID': 'void'}, 'CM_Get_Version_Ex': {'hMachine': 'HMACHINE'}, 'CM_Is_Version_Available': {'wVersion': 'WORD'}, 'CM_Is_Version_Available_Ex': {'wVersion': 'WORD', 'hMachine': 'HMACHINE'}, 'CM_Locate_DevNodeA': {'pdnDevInst': 'PDEVINST', 'pDeviceID': 'DEVINSTID_A', 'ulFlags': 'ULONG'}, 'CM_Locate_DevNodeW': {'pdnDevInst': 'PDEVINST', 'pDeviceID': 'DEVINSTID_W', 'ulFlags': 'ULONG'}, 'CM_Modify_Res_Des': {'prdResDes': 'PRES_DES', 'rdResDes': 'RES_DES', 'ResourceID': 'RESOURCEID', 'ResourceData': 'PCVOID', 'ResourceLen': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Modify_Res_Des_Ex': {'prdResDes': 'PRES_DES', 'rdResDes': 'RES_DES', 'ResourceID': 'RESOURCEID', 'ResourceData': 'PCVOID', 'ResourceLen': 'ULONG', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Get_Next_Res_Des': {'prdResDes': 'PRES_DES', 'rdResDes': 'RES_DES', 'ForResource': 'RESOURCEID', 'pResourceID': 'PRESOURCEID', 'ulFlags': 'ULONG'}, 'CM_Get_Next_Res_Des_Ex': {'prdResDes': 'PRES_DES', 'rdResDes': 'RES_DES', 'ForResource': 'RESOURCEID', 'pResourceID': 'PRESOURCEID', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Open_Class_KeyW': {'ClassGuid': 'LPGUID', 'pszClassName': 'LPCWSTR', 'samDesired': 'REGSAM', 'Disposition': 'REGDISPOSITION', 'phkClass': 'PHKEY', 'ulFlags': 'ULONG'}, 'CM_Open_DevNode_Key': {'dnDevNode': 'DEVINST', 'samDesired': 'REGSAM', 'ulHardwareProfile': 'ULONG', 'Disposition': 'REGDISPOSITION', 'phkDevice': 'PHKEY', 'ulFlags': 'ULONG'}, 'CM_Open_Device_Interface_KeyA': {'pszDeviceInterface': 'LPCSTR', 'samDesired': 'REGSAM', 'Disposition': 'REGDISPOSITION', 'phkDeviceInterface': 'PHKEY', 'ulFlags': 'ULONG'}, 'CM_Open_Device_Interface_KeyW': {'pszDeviceInterface': 'LPCWSTR', 'samDesired': 'REGSAM', 'Disposition': 'REGDISPOSITION', 'phkDeviceInterface': 'PHKEY', 'ulFlags': 'ULONG'}, 'CM_Open_Device_Interface_Key_ExA': {'pszDeviceInterface': 'LPCSTR', 'samDesired': 'REGSAM', 'Disposition': 'REGDISPOSITION', 'phkDeviceInterface': 'PHKEY', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Open_Device_Interface_Key_ExW': {'pszDeviceInterface': 'LPCWSTR', 'samDesired': 'REGSAM', 'Disposition': 'REGDISPOSITION', 'phkDeviceInterface': 'PHKEY', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Delete_Device_Interface_KeyW': {'pszDeviceInterface': 'LPCWSTR', 'ulFlags': 'ULONG'}, 'CM_Query_And_Remove_SubTreeW': {'dnAncestor': 'DEVINST', 'pVetoType': 'PPNP_VETO_TYPE', 'pszVetoName': 'LPWSTR', 'ulNameLength': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Reenumerate_DevNode': {'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Reenumerate_DevNode_Ex': {'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Set_DevNode_Problem_Ex': {'dnDevInst': 'DEVINST', 'ulProblem': 'ULONG', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Set_DevNode_Problem': {'dnDevInst': 'DEVINST', 'ulProblem': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Set_DevNode_PropertyW': {'dnDevInst': 'DEVINST', 'PropertyKey': 'DEVPROPKEY', 'PropertyType': 'DEVPROPTYPE', 'PropertyBuffer': 'PBYTE', 'PropertyBufferSize': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Set_DevNode_Registry_PropertyW': {'dnDevInst': 'DEVINST', 'ulProperty': 'ULONG', 'Buffer': 'PCVOID', 'ulLength': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Set_Device_Interface_PropertyW': {'pszDeviceInterface': 'LPCWSTR', 'PropertyKey': 'DEVPROPKEY', 'PropertyType': 'DEVPROPTYPE', 'PropertyBuffer': 'PBYTE', 'PropertyBufferSize': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Is_Dock_Station_Present': {'pbPresent': 'PBOOL'}, 'CM_Is_Dock_Station_Present_Ex': {'pbPresent': 'PBOOL', 'hMachine': 'HMACHINE'}, 'CM_Request_Eject_PC': {'VOID': 'void'}, 'CM_Request_Eject_PC_Ex': {'hMachine': 'HMACHINE'}, 'CM_Setup_DevNode': {'dnDevInst': 'DEVINST', 'ulFlags': 'ULONG'}, 'CM_Uninstall_DevNode': {'dnDevInst': 'DEVNODE', 'ulFlags': 'ULONG'}, 'CM_Query_Resource_Conflict_List': {'pclConflictList': 'PCONFLICT_LIST', 'dnDevInst': 'DEVINST', 'ResourceID': 'RESOURCEID', 'ResourceData': 'PCVOID', 'ResourceLen': 'ULONG', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Free_Resource_Conflict_Handle': {'clConflictList': 'CONFLICT_LIST'}, 'CM_Get_Resource_Conflict_Count': {'clConflictList': 'CONFLICT_LIST', 'pulCount': 'PULONG'}, 'CM_Get_Class_PropertyW': {'ClassGUID': 'LPCGUID', 'PropertyKey': 'DEVPROPKEY', 'PropertyType': 'DEVPROPTYPE', 'PropertyBuffer': 'PBYTE', 'PropertyBufferSize': 'PULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Class_Property_Keys': {'ClassGUID': 'LPCGUID', 'PropertyKeyArray': 'DEVPROPKEY', 'PropertyKeyCount': 'PULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Class_Property_Keys_Ex': {'ClassGUID': 'LPCGUID', 'PropertyKeyArray': 'DEVPROPKEY', 'PropertyKeyCount': 'PULONG', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Set_Class_PropertyW': {'ClassGUID': 'LPCGUID', 'PropertyKey': 'DEVPROPKEY', 'PropertyType': 'DEVPROPTYPE', 'PropertyBuffer': 'PBYTE', 'PropertyBufferSize': 'ULONG', 'ulFlags': 'ULONG'}, 'CM_Get_Class_Registry_PropertyW': {'ClassGuid': 'LPGUID', 'ulProperty': 'ULONG', 'pulRegDataType': 'PULONG', 'Buffer': 'PVOID', 'pulLength': 'PULONG', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Set_Class_Registry_PropertyW': {'ClassGuid': 'LPGUID', 'ulProperty': 'ULONG', 'Buffer': 'PCVOID', 'ulLength': 'ULONG', 'ulFlags': 'ULONG', 'hMachine': 'HMACHINE'}, 'CM_Register_Notification': {'pFilter': 'PCM_NOTIFY_FILTER', 'pContext': 'PVOID', 'pCallback': 'PCM_NOTIFY_CALLBACK', 'pNotifyContext': 'PHCMNOTIFICATION'}, 'CM_Unregister_Notification': {'NotifyContext': 'HCMNOTIFICATION'}, 'CM_MapCrToWin32Err': {'CmReturnCode': 'CONFIGRET', 'DefaultErr': 'DWORD'}}