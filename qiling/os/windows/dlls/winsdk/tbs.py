tbs_data = {'Tbsi_Context_Create': {'pContextParams': 'PCTBS_CONTEXT_PARAMS', 'phContext': 'PTBS_HCONTEXT'}, 'Tbsip_Context_Close': {'hContext': 'TBS_HCONTEXT'}, 'Tbsip_Submit_Command': {'hContext': 'TBS_HCONTEXT', 'Locality': 'TBS_COMMAND_LOCALITY', 'Priority': 'TBS_COMMAND_PRIORITY', 'pabCommand': 'PCBYTE', 'cbCommand': 'UINT32', 'pabResult': 'PBYTE', 'pcbResult': 'PUINT32'}, 'Tbsip_Cancel_Commands': {'hContext': 'TBS_HCONTEXT'}, 'Tbsi_Physical_Presence_Command': {'hContext': 'TBS_HCONTEXT', 'pabInput': 'PCBYTE', 'cbInput': 'UINT32', 'pabOutput': 'PBYTE', 'pcbOutput': 'PUINT32'}, 'Tbsi_Get_TCG_Log': {'hContext': 'TBS_HCONTEXT', 'pOutputBuf': 'PBYTE', 'pOutputBufLen': 'PUINT32'}, 'Tbsi_GetDeviceInfo': {'Size': 'UINT32', 'Info': 'PVOID'}, 'Tbsi_Get_OwnerAuth': {'hContext': 'TBS_HCONTEXT', 'ownerauthType': 'TBS_OWNERAUTH_TYPE', 'pOutputBuf': 'PBYTE', 'pOutputBufLen': 'PUINT32'}, 'Tbsi_Revoke_Attestation': {}, 'Tbsi_Get_TCG_Log_Ex': {'logType': 'UINT32', 'pbOutput': 'PBYTE', 'pcbOutput': 'PUINT32'}}