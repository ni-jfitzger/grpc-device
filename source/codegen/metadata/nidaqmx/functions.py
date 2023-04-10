functions = {
    'AddCDAQSyncConnection': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'portList',
                'type': 'const char[]'
            }
        ],
        'python_description': 'Adds a cDAQ Sync connection between devices. The connection is not verified.',
        'returns': 'int32'
    },
    'AddGlobalChansToTask': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'AddNetworkDevice': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'is_python_factory': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'ipAddress',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'attemptReservation',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'deviceNameOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'deviceNameOutBufferSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'deviceNameOutBufferSize',
                'type': 'uInt32'
            }
        ],
        'python_description': 'Adds a Network cDAQ device to the system and, if specified, attempts to reserve it.',
        'returns': 'int32'
    },
    'AreConfiguredCDAQSyncPortsDisconnected': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'chassisDevicesPorts',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'disconnectedPortsExist',
                'type': 'bool32'
            }
        ],
        'python_description': 'Verifies configured cDAQ Sync connections between devices. Failures generally indicate a specifying issue or that a device has been powered off or removed. Stop all NI-DAQmx tasks running on the devices prior to running this function because any running tasks cause the verification process to fail.',
        'returns': 'int32'
    },
    'AutoConfigureCDAQSyncConnections': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'chassisDevicesPorts',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            }
        ],
        'python_description': 'Detects and configures cDAQ Sync connections between devices. Stop all NI-DAQmx tasks running on the devices prior to running this function because any running tasks cause auto-configuration to fail.',
        'returns': 'int32'
    },
    'CalculateReversePolyCoeff': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'ctypes.c_char_p',
            'cvi_name': 'name',
            'python_accessor': 'self._name'
        },
        'parameters': [
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': False,
                'name': 'forwardCoeffs',
                'python_data_type': 'float',
                'python_description': 'Is the list of coefficients for the polynomial that computes y given a value of x. Each element of the list corresponds to a term of the equation.',
                'python_type_annotation': 'List[float]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numForwardCoeffsIn'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numForwardCoeffsIn',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minValX',
                'python_data_type': 'float',
                'python_default_value': '-5.0',
                'python_description': 'Is the minimum value of x for which you use the polynomial. This is the smallest value of x for which the function generates a y value in the table.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxValX',
                'python_data_type': 'float',
                'python_default_value': '5.0',
                'python_description': 'Is the maximum value of x for which you use the polynomial. This is the largest value of x for which the function generates a y value in the table.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'numPointsToCompute',
                'python_data_type': 'int',
                'python_default_value': '1000',
                'python_description': 'Is the number of points in the table of x versus y values. The function spaces the values evenly between **min_val_x** and **max_val_x**.',
                'python_type_annotation': 'Optional[int]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'reversePolyOrder',
                'python_data_type': 'int',
                'python_default_value': '-1',
                'python_description': 'Is the order of the reverse polynomial to compute. For example, an input of 3 indicates a 3rd order polynomial. A value of -1 indicates a reverse polynomial of the same order as the forward polynomial.',
                'python_type_annotation': 'Optional[int]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'out',
                'is_list': True,
                'is_optional_in_python': False,
                'name': 'reverseCoeffs',
                'python_data_type': 'float',
                'python_description': 'Is the list of coefficients for the reverse polynomial. Each element of the list corresponds to a term of the equation. For example, if index three of the list is 9, the fourth term of the equation is 9y^3.',
                'python_type_annotation': 'List[float]',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(reversePolyOrder < 0) ? numForwardCoeffsIn : reversePolyOrder + 1'
                },
                'type': 'float64[]'
            }
        ],
        'python_class_name': 'Scale',
        'python_description': 'Computes a set of coefficients for a polynomial that approximates the inverse of the polynomial with the coefficients you specify with the **forward_coeffs** input. This function generates a table of x versus y values over the range of x. This function then finds a polynomial fit, using the least squares method to compute a polynomial that computes x when given a value for y.',
        'returns': 'int32'
    },
    'CfgAnlgEdgeRefTrig': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'triggerSource',
                'python_data_type': 'str',
                'python_description': 'Is the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Slope1',
                'is_optional_in_python': True,
                'name': 'triggerSlope',
                'python_data_type': 'Slope',
                'python_default_value': 'Slope.RISING',
                'python_description': 'Specifies on which slope of the signal the Reference Trigger occurs.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Slope]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'triggerLevel',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies at what threshold to trigger. Specify this value in the units of the measurement or generation. Use **trigger_slope** to specify on which slope to trigger at this threshold.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_uint',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'pretriggerSamples',
                'python_data_type': 'int',
                'python_description': 'Specifies the minimum number of samples to acquire per channel before recognizing the Reference Trigger. The number of post-trigger samples per channel is equal to **number of samples per channel** in the DAQmx Timing function minus **pretrigger_samples**.',
                'python_type_annotation': 'int',
                'type': 'uInt32'
            }
        ],
        'python_class_name': 'ReferenceTrigger',
        'python_description': 'Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal reaches the level you specify; and the device acquires all post-trigger samples. When you use a Reference Trigger, the default for the read RelativeTo property is **first_pretrigger_sample** with a read Offset of 0.',
        'returns': 'int32'
    },
    'CfgAnlgEdgeStartTrig': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'triggerSource',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Is the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Slope1',
                'is_optional_in_python': True,
                'name': 'triggerSlope',
                'python_data_type': 'Slope',
                'python_default_value': 'Slope.RISING',
                'python_description': 'Specifies on which slope of the signal to start acquiring or generating samples when the signal crosses **trigger_level**.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Slope]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'triggerLevel',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies at what threshold to start acquiring or generating samples. Specify this value in the units of the measurement or generation. Use **trigger_slope** to specify on which slope to trigger at this threshold.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'StartTrigger',
        'python_description': 'Configures the task to start acquiring or generating samples when an analog signal crosses the level you specify.',
        'returns': 'int32'
    },
    'CfgAnlgMultiEdgeRefTrig': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'triggerSources',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'triggerSlopeArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const int32[]'
            },
            {
                'direction': 'in',
                'name': 'triggerLevelArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'pretriggerSamples',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'CfgAnlgMultiEdgeStartTrig': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'triggerSources',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'triggerSlopeArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const int32[]'
            },
            {
                'direction': 'in',
                'name': 'triggerLevelArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'CfgAnlgWindowRefTrig': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'triggerSource',
                'python_data_type': 'str',
                'python_description': 'Is the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'WindowTriggerCondition1',
                'is_optional_in_python': True,
                'name': 'triggerWhen',
                'python_data_type': 'WindowTriggerCondition1',
                'python_default_value': 'WindowTriggerCondition1.ENTERING_WINDOW',
                'python_description': 'Specifies whether the Reference Trigger occurs when the signal enters the window or when it leaves the window. Use **window_bottom** and **window_top** to specify the limits of the window.',
                'python_type_annotation': 'Optional[nidaqmx.constants.WindowTriggerCondition1]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'windowTop',
                'python_data_type': 'float',
                'python_description': 'Is the upper limit of the window. Specify this value in the units of the measurement or generation.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'windowBottom',
                'python_data_type': 'float',
                'python_description': 'Is the lower limit of the window. Specify this value in the units of the measurement or generation.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_uint',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'pretriggerSamples',
                'python_data_type': 'int',
                'python_description': 'Specifies the minimum number of samples to acquire per channel before recognizing the Reference Trigger. The number of post-trigger samples per channel is equal to **number of samples per channel** in the DAQmx Timing function minus **pretrigger_samples**.',
                'python_type_annotation': 'int',
                'type': 'uInt32'
            }
        ],
        'python_class_name': 'ReferenceTrigger',
        'python_description': 'Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal enters or leaves a range you specify; and the device acquires all post-trigger samples. When you use a Reference Trigger, the default for the read RelativeTo property is **first_pretrigger_sample** with a read Offset of 0.',
        'returns': 'int32'
    },
    'CfgAnlgWindowStartTrig': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'triggerSource',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Is the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'WindowTriggerCondition1',
                'is_optional_in_python': True,
                'name': 'triggerWhen',
                'python_data_type': 'WindowTriggerCondition1',
                'python_default_value': 'WindowTriggerCondition1.ENTERING_WINDOW',
                'python_description': 'Specifies whether the task starts measuring or generating samples when the signal enters the window or when it leaves the window. Use **window_bottom** and **window_top** to specify the limits of the window.',
                'python_type_annotation': 'Optional[nidaqmx.constants.WindowTriggerCondition1]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'windowTop',
                'python_data_type': 'float',
                'python_description': 'Is the upper limit of the window. Specify this value in the units of the measurement or generation.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'windowBottom',
                'python_data_type': 'float',
                'python_description': 'Is the lower limit of the window. Specify this value in the units of the measurement or generation.',
                'python_type_annotation': 'float',
                'type': 'float64'
            }
        ],
        'python_class_name': 'StartTrigger',
        'python_description': 'Configures the task to start acquiring or generating samples when an analog signal enters or leaves a range you specify.',
        'returns': 'int32'
    },
    'CfgBurstHandshakingTimingExportClock': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AcquisitionType',
                'is_optional_in_python': True,
                'name': 'sampleMode',
                'python_data_type': 'AcquisitionType',
                'python_default_value': 'AcquisitionType.FINITE',
                'python_description': 'Specifies if the task acquires or generates samples continuously or if it acquires or generates a finite number of samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AcquisitionType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_ulonglong',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sampsPerChan',
                'python_data_type': 'int',
                'python_default_value': '1000',
                'python_description': 'Specifies the number of samples to acquire or generate for each channel in the task if **sample_mode** is **FINITE_SAMPLES**. If **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses this value to determine the buffer size. This function returns an error if the specified value is negative.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'sampleClkRate',
                'python_data_type': 'float',
                'python_description': 'Specifies in hertz the rate of the Sample Clock.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'sampleClkOutpTerm',
                'python_data_type': 'str',
                'python_description': 'Specifies the terminal to which to export the Sample Clock.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Polarity2',
                'is_optional_in_python': True,
                'name': 'sampleClkPulsePolarity',
                'python_data_type': 'Polarity',
                'python_default_value': 'Polarity.ACTIVE_HIGH',
                'python_description': 'Specifies the polarity of the exported Sample Clock.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Polarity]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Level1',
                'is_optional_in_python': True,
                'name': 'pauseWhen',
                'python_data_type': 'Level',
                'python_default_value': 'Level.HIGH',
                'python_description': 'Specifies whether the task pauses while the trigger signal is high or low.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Level]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Polarity2',
                'is_optional_in_python': True,
                'name': 'readyEventActiveLevel',
                'python_data_type': 'Polarity',
                'python_default_value': 'Polarity.ACTIVE_HIGH',
                'python_description': 'Specifies the polarity of the Ready for Transfer Event.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Polarity]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'Timing',
        'python_description': 'Configures when the DAQ device transfers data to a peripheral device, using the onboard Sample Clock of the DAQ device to control burst handshake timing and exporting that clock for use by the peripheral device.',
        'returns': 'int32'
    },
    'CfgBurstHandshakingTimingImportClock': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AcquisitionType',
                'is_optional_in_python': True,
                'name': 'sampleMode',
                'python_data_type': 'AcquisitionType',
                'python_default_value': 'AcquisitionType.FINITE',
                'python_description': 'Specifies if the task acquires or generates samples continuously or if it acquires or generates a finite number of samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AcquisitionType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_ulonglong',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sampsPerChan',
                'python_data_type': 'int',
                'python_default_value': '1000',
                'python_description': 'Specifies the number of samples to acquire or generate for each channel in the task if **sample_mode** is **FINITE_SAMPLES**. If **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses this value to determine the buffer size. This function returns an error if the specified value is negative.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'sampleClkRate',
                'python_data_type': 'float',
                'python_description': 'Specifies in hertz the rate of the Sample Clock.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'sampleClkSrc',
                'python_data_type': 'str',
                'python_description': 'Specifies the source terminal of the Sample Clock. Leave this input unspecified to use the default onboard clock of the device.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'sampleClkActiveEdge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies on which edges of Sample Clock pulses to acquire or generate samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Level1',
                'is_optional_in_python': True,
                'name': 'pauseWhen',
                'python_data_type': 'Level',
                'python_default_value': 'Level.HIGH',
                'python_description': 'Specifies whether the task pauses while the trigger signal is high or low.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Level]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Polarity2',
                'is_optional_in_python': True,
                'name': 'readyEventActiveLevel',
                'python_data_type': 'Polarity',
                'python_default_value': 'Polarity.ACTIVE_HIGH',
                'python_description': 'Specifies the polarity of the Ready for Transfer Event.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Polarity]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'Timing',
        'python_description': 'Configures when the DAQ device transfers data to a peripheral device, using an imported sample clock to control burst handshake timing.',
        'returns': 'int32'
    },
    'CfgChangeDetectionTiming': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'risingEdgeChan',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the names of the digital lines or ports on which to detect rising edges. The DAQmx physical channel constant lists all lines and ports for devices installed in your system.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'fallingEdgeChan',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the names of the digital lines or ports on which to detect falling edges. The DAQmx physical channel constant lists all lines and ports for devices installed in your system.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AcquisitionType',
                'is_optional_in_python': True,
                'name': 'sampleMode',
                'python_data_type': 'AcquisitionType',
                'python_default_value': 'AcquisitionType.FINITE',
                'python_description': 'Specifies if the task acquires samples continuously or if it acquires a finite number of samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AcquisitionType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_ulonglong',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sampsPerChan',
                'python_data_type': 'int',
                'python_default_value': '1000',
                'python_description': 'Specifies the number of samples to acquire from each channel in the task if **sample_mode** is **FINITE_SAMPLES**. This function returns an error if the specified value is negative.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt64'
            }
        ],
        'python_class_name': 'Timing',
        'python_description': 'Configures the task to acquire samples on the rising and/or falling edges of the lines or ports you specify. To detect both rising and falling edges on a line or port, specify the name of that line or port to both **rising_edge_chan** and **falling_edge_chan**.',
        'returns': 'int32'
    },
    'CfgDigEdgeRefTrig': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'triggerSource',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of a terminal where there is a digital signal to use as the source of the trigger.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'triggerEdge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies on which edge of the digital signal the Reference Trigger occurs.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_uint',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'pretriggerSamples',
                'python_data_type': 'int',
                'python_description': 'Specifies the minimum number of samples to acquire per channel before recognizing the Reference Trigger. The number of post-trigger samples per channel is equal to **number of samples per channel** in the DAQmx Timing function minus **pretrigger_samples**.',
                'python_type_annotation': 'int',
                'type': 'uInt32'
            }
        ],
        'python_class_name': 'ReferenceTrigger',
        'python_description': 'Configures the task to stop the acquisition when the device acquires all pretrigger samples, detects a rising or falling edge of a digital signal, and acquires all posttrigger samples. When you use a Reference Trigger, the default for the read RelativeTo property is **first_pretrigger_sample** with a read Offset of 0.',
        'returns': 'int32'
    },
    'CfgDigEdgeStartTrig': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'triggerSource',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of a terminal where there is a digital signal to use as the source of the trigger.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'triggerEdge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies on which edge of the digital signal to start acquiring or generating samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'StartTrigger',
        'python_description': 'Configures the task to start acquiring or generating samples on a rising or falling edge of a digital signal.',
        'returns': 'int32'
    },
    'CfgDigPatternRefTrig': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'triggerSource',
                'python_data_type': 'str',
                'python_description': 'Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'triggerPattern',
                'python_data_type': 'str',
                'python_description': 'Specifies the digital pattern that must be met for the trigger to occur.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'DigitalPatternCondition1',
                'is_optional_in_python': True,
                'name': 'triggerWhen',
                'python_data_type': 'DigitalPatternCondition',
                'python_default_value': 'DigitalPatternCondition.PATTERN_MATCHES',
                'python_description': 'Specifies the condition under which the trigger occurs.',
                'python_type_annotation': 'Optional[nidaqmx.constants.DigitalPatternCondition]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_uint',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'pretriggerSamples',
                'python_data_type': 'int',
                'python_description': 'Specifies the minimum number of samples to acquire per channel before recognizing the Reference Trigger. The number of post-trigger samples per channel is equal to **number of samples per channel** in the DAQmx Timing function minus **pretrigger_samples**.',
                'python_type_annotation': 'int',
                'type': 'uInt32'
            }
        ],
        'python_class_name': 'ReferenceTrigger',
        'python_description': 'Configures the task to stop the acquisition when the device acquires all pretrigger samples, matches a digital pattern, and acquires all posttrigger samples. When you use a Reference Trigger, the default for the read RelativeTo property is First PretriggerSample with a read Offset of zero.',
        'returns': 'int32'
    },
    'CfgDigPatternStartTrig': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'triggerSource',
                'python_data_type': 'str',
                'python_description': 'Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'triggerPattern',
                'python_data_type': 'str',
                'python_description': 'Specifies the digital pattern that must be met for the trigger to occur.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'DigitalPatternCondition1',
                'is_optional_in_python': True,
                'name': 'triggerWhen',
                'python_data_type': 'DigitalPatternCondition',
                'python_default_value': 'DigitalPatternCondition.PATTERN_MATCHES',
                'python_description': 'Specifies the condition under which the trigger occurs.',
                'python_type_annotation': 'Optional[nidaqmx.constants.DigitalPatternCondition]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'StartTrigger',
        'python_description': 'Configures a task to start acquiring or generating samples when a digital pattern is matched.',
        'returns': 'int32'
    },
    'CfgHandshakingTiming': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AcquisitionType',
                'is_optional_in_python': True,
                'name': 'sampleMode',
                'python_data_type': 'AcquisitionType',
                'python_default_value': 'AcquisitionType.FINITE',
                'python_description': 'Specifies if the task acquires or generates samples continuously or if it acquires or generates a finite number of samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AcquisitionType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_ulonglong',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sampsPerChan',
                'python_data_type': 'int',
                'python_default_value': '1000',
                'python_description': 'Specifies the number of samples to acquire or generate for each channel in the task if **sample_mode** is **FINITE_SAMPLES**. If **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses this value to determine the buffer size. This function returns an error if the specified value is negative.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt64'
            }
        ],
        'python_class_name': 'Timing',
        'python_description': 'Determines the number of digital samples to acquire or generate using digital handshaking between the device and a peripheral device.',
        'returns': 'int32'
    },
    'CfgImplicitTiming': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AcquisitionType',
                'is_optional_in_python': True,
                'name': 'sampleMode',
                'python_data_type': 'AcquisitionType',
                'python_default_value': 'AcquisitionType.FINITE',
                'python_description': 'Specifies if the task acquires or generates samples continuously or if it acquires or generates a finite number of samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AcquisitionType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_ulonglong',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sampsPerChan',
                'python_data_type': 'int',
                'python_default_value': '1000',
                'python_description': 'Specifies the number of samples to acquire or generate for each channel in the task if **sample_mode** is **FINITE_SAMPLES**. If **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses this value to determine the buffer size. This function returns an error if the specified value is negative.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt64'
            }
        ],
        'python_class_name': 'Timing',
        'python_description': 'Sets only the number of samples to acquire or generate without specifying timing. Typically, you should use this instance when the task does not require sample timing, such as tasks that use counters for buffered frequency measurement, buffered period measurement, or pulse train generation. For finite counter output tasks, **samps_per_chan** is the number of pulses to generate.',
        'returns': 'int32'
    },
    'CfgInputBuffer': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'CfgOutputBuffer': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'CfgPipelinedSampClkTiming': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'source',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the source terminal of the Sample Clock. Leave this input unspecified to use the default onboard clock of the device.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'rate',
                'python_data_type': 'float',
                'python_description': 'Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'activeEdge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies on which edges of Sample Clock pulses to acquire or generate samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AcquisitionType',
                'is_optional_in_python': True,
                'name': 'sampleMode',
                'python_data_type': 'AcquisitionType',
                'python_default_value': 'AcquisitionType.FINITE',
                'python_description': 'Specifies if the task acquires or generates samples continuously or if it acquires or generates a finite number of samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AcquisitionType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_ulonglong',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sampsPerChan',
                'python_data_type': 'int',
                'python_default_value': '1000',
                'python_description': 'Specifies the number of samples to acquire or generate for each channel in the task if **sample_mode** is **FINITE_SAMPLES**. If **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses this value to determine the buffer size. This function returns an error if the specified value is negative.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt64'
            }
        ],
        'python_class_name': 'Timing',
        'python_description': 'Sets the source of the Sample Clock, the rate of the Sample Clock, and the number of samples to acquire or generate. The device acquires or generates samples on each Sample Clock edge, but it does not respond to certain triggers until a few Sample Clock edges later. Pipelining allows higher data transfer rates at the cost of increased trigger response latency. Refer to the device documentation for information about which triggers pipelining affects.  This timing type allows handshaking using the Pause trigger and either the Ready for Transfer event or the Data Active event. Refer to the device documentation for more information.  This timing type is supported only by the NI 6536 and NI 6537.',
        'returns': 'int32'
    },
    'CfgSampClkTiming': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'source',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the source terminal of the Sample Clock. Leave this input unspecified to use the default onboard clock of the device.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'rate',
                'python_data_type': 'float',
                'python_description': 'Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'activeEdge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies on which edges of Sample Clock pulses to acquire or generate samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AcquisitionType',
                'is_optional_in_python': True,
                'name': 'sampleMode',
                'python_data_type': 'AcquisitionType',
                'python_default_value': 'AcquisitionType.FINITE',
                'python_description': 'Specifies if the task acquires or generates samples continuously or if it acquires or generates a finite number of samples.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AcquisitionType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_ulonglong',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sampsPerChan',
                'python_data_type': 'int',
                'python_default_value': '1000',
                'python_description': 'Specifies the number of samples to acquire or generate for each channel in the task if **sample_mode** is **FINITE_SAMPLES**. If **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses this value to determine the buffer size. This function returns an error if the specified value is negative.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt64'
            }
        ],
        'python_class_name': 'Timing',
        'python_description': 'Sets the source of the Sample Clock, the rate of the Sample Clock, and the number of samples to acquire or generate.',
        'returns': 'int32'
    },
    'CfgTimeStartTrig': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': None,
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'when',
                'python_data_type': 'DateTime',
                'python_description': 'Specifies when to trigger.',
                'python_type_annotation': 'nidaqmx.constants.DateTime',
                'type': 'CVIAbsoluteTime'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Timescale2',
                'is_optional_in_python': True,
                'name': 'timescale',
                'python_data_type': 'Timescale',
                'python_default_value': 'Timescale.USE_HOST',
                'python_description': 'Specifies the start trigger timestamp time scale.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Timescale]',
                'type': 'int32'
            }
        ],
        'python_description': 'New Start Trigger',
        'returns': 'int32'
    },
    'CfgWatchdogAOExpirStates': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'expirStateArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'enum': 'WatchdogAOOutputType',
                'name': 'outputTypeArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        ],
        'python_description': 'Configures the expiration states for an analog watchdog timer task.',
        'returns': 'int32'
    },
    'CfgWatchdogCOExpirStates': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'WatchdogCOExpirState',
                'is_list': True,
                'name': 'expirStateArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        ],
        'python_description': 'Configures the expiration states for a counter watchdog timer task.',
        'returns': 'int32'
    },
    'CfgWatchdogDOExpirStates': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'DigitalLineState',
                'is_list': True,
                'name': 'expirStateArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        ],
        'python_description': 'Configures the expiration states for a digital watchdog timer task.',
        'returns': 'int32'
    },
    'ClearTEDS': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'ctypes.c_char_p',
            'cvi_name': 'physicalChannel',
            'python_accessor': 'self._name'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': '',
                'python_type_annotation': 'str',
                'type': 'const char[]',
                'use_in_python_api': False
            }
        ],
        'python_class_name': 'PhysicalChannel',
        'python_description': 'Removes TEDS information from the physical channel you specify. This function temporarily overrides any TEDS configuration for the physical channel that you performed in MAX.',
        'returns': 'int32'
    },
    'ClearTask': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            }
        ],
        'python_description': 'Clears the task. Before clearing, this function aborts the task, if necessary, and releases any resources the task reserved. You cannot use a task after you clear it unless you recreate the task.',
        'returns': 'int32'
    },
    'ConfigureLogging': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'LoggingMode',
                'name': 'loggingMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'groupName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'LoggingOperation',
                'name': 'operation',
                'type': 'int32'
            }
        ],
        'python_description': 'Configures TDMS file logging for the task.',
        'returns': 'int32'
    },
    'ConfigureTEDS': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'ctypes.c_char_p',
            'cvi_name': 'physicalChannel',
            'python_accessor': 'self._name'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': '',
                'python_type_annotation': 'str',
                'type': 'const char[]',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'filePath',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Is the path to a Virtual TEDS data sheet that you want to associate with the physical channel. If you do not specify anything for this input, this function attempts to find a TEDS sensor connected to the physical channel.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'PhysicalChannel',
        'python_description': 'Associates TEDS information with the physical channel you specify. If you do not specify the filename of a data sheet in the **file_path** input, this function attempts to find a TEDS sensor connected to the physical channel. This function temporarily overrides any TEDS configuration for the physical channel that you performed in MAX.',
        'returns': 'int32'
    },
    'ConnectTerms': {
        'calling_convention': 'StdCall',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'sourceTerminal',
                'python_data_type': 'str',
                'python_description': 'Specifies the originating terminal of the route. A DAQmx terminal constant lists all terminals available on devices installed in the system. You also can specify a source terminal by specifying a string that contains a terminal name.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'destinationTerminal',
                'python_data_type': 'str',
                'python_description': 'Specifies the receiving terminal of the route. A DAQmx terminal constant provides a list of all terminals available on devices installed in the system. You also can specify a destination terminal by specifying a string that contains a terminal name.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InvertPolarity',
                'is_optional_in_python': True,
                'name': 'signalModifiers',
                'python_data_type': 'SignalModifiers',
                'python_default_value': 'SignalModifiers.DO_NOT_INVERT_POLARITY',
                'python_description': 'Specifies whether to invert the signal this function routes from the source terminal to the destination terminal.',
                'python_type_annotation': 'Optional[nidaqmx.constants.SignalModifiers]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'System',
        'python_description': 'Creates a route between a source and destination terminal. The route can carry a variety of digital signals, such as triggers, clocks, and hardware events.',
        'returns': 'int32'
    },
    'ControlWatchdogTask': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'enum': 'WatchdogControlAction',
                'name': 'action',
                'type': 'int32'
            }
        ],
        'python_description': 'Controls the watchdog timer task according to the action you specify. This function does not program the watchdog timer on a real-time controller. Use the Real-Time Watchdog VIs to program the watchdog timer on a real-time controller.',
        'returns': 'int32'
    },
    'CreateAIAccel4WireDCVoltageChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-5.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '5.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AccelUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'AccelUnits',
                'python_default_value': 'AccelUnits.G',
                'python_description': 'Specifies the units to use to return acceleration measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AccelUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sensitivity',
                'python_data_type': 'float',
                'python_default_value': '1000.0',
                'python_description': 'Is the sensitivity of the sensor. This value is in the units you specify with the **sensitivity_units** input. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AccelSensitivityUnits1',
                'is_optional_in_python': True,
                'name': 'sensitivityUnits',
                'python_data_type': 'AccelSensitivityUnits',
                'python_default_value': 'AccelSensitivityUnits.MILLIVOLTS_PER_G',
                'python_description': 'Specifies the units of the **sensitivity** input.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AccelSensitivityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'c_bool32',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'useExcitForScaling',
                'python_data_type': 'bool',
                'python_default_value': False,
                'python_description': 'Specifies if NI-DAQmx divides the measurement by the excitation. You should typically set **use_excit_for_scaling** to True for ratiometric transducers. If you set **use_excit_for_scaling** to True, set **max_val** and **min_val** to reflect the scaling.',
                'python_type_annotation': 'Optional[bool]',
                'type': 'bool32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure acceleration. Use this instance for custom sensors that require excitation. You can use the excitation to scale the measurement.',
        'returns': 'int32'
    },
    'CreateAIAccelChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-5.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '5.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AccelUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'AccelUnits',
                'python_default_value': 'AccelUnits.G',
                'python_description': 'Specifies the units to use to return acceleration measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AccelUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sensitivity',
                'python_data_type': 'float',
                'python_default_value': '1000.0',
                'python_description': 'Is the sensitivity of the sensor. This value is in the units you specify with the **sensitivity_units** input. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AccelSensitivityUnits1',
                'is_optional_in_python': True,
                'name': 'sensitivityUnits',
                'python_data_type': 'AccelSensitivityUnits',
                'python_default_value': 'AccelSensitivityUnits.MILLIVOLTS_PER_G',
                'python_description': 'Specifies the units of the **sensitivity** input.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AccelSensitivityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.004',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an accelerometer to measure acceleration.',
        'returns': 'int32'
    },
    'CreateAIAccelChargeChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-5.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '5.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AccelUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'AccelUnits',
                'python_default_value': 'AccelUnits.G',
                'python_description': 'Specifies the units to use to return acceleration measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AccelUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sensitivity',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Is the sensitivity of the sensor. This value is in the units you specify with the **sensitivity_units** input. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AccelChargeSensitivityUnits',
                'is_optional_in_python': True,
                'name': 'sensitivityUnits',
                'python_data_type': 'AccelChargeSensitivityUnits',
                'python_default_value': 'AccelChargeSensitivityUnits.PICO_COULOMBS_PER_G',
                'python_description': 'Specifies the units of the **sensitivity** input.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AccelChargeSensitivityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a charge-based sensor to measure acceleration.',
        'returns': 'int32'
    },
    'CreateAIBridgeChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.002',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.002',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'BridgeUnits',
                'python_default_value': 'BridgeUnits.VOLTS_PER_VOLT',
                'python_description': 'Specifies in which unit to return voltage ratios from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.FULL_BRIDGE',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalBridgeResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that measure voltage ratios from a Wheatstone bridge. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support.',
        'returns': 'int32'
    },
    'CreateAIChargeChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.000000001',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.000000001',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ChargeUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'ChargeUnits',
                'python_default_value': 'ChargeUnits.COULOMBS',
                'python_description': 'Specifies the units to use to return charge measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ChargeUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a sensor with charge output.',
        'returns': 'int32'
    },
    'CreateAICurrentChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.01',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.01',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CurrentUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'CurrentUnits',
                'python_default_value': 'CurrentUnits.AMPS',
                'python_description': 'Specifies the units to use to return current measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CurrentUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CurrentShuntResistorLocationWithDefault',
                'is_optional_in_python': True,
                'name': 'shuntResistorLoc',
                'python_data_type': 'CurrentShuntResistorLocation',
                'python_default_value': 'CurrentShuntResistorLocation.LET_DRIVER_CHOOSE',
                'python_description': 'Specifies the location of the shunt resistor. For devices with built-in shunt resistors, specify the location as **INTERNAL**. For devices that do not have built-in shunt resistors, you must attach an external one, set this input to **EXTERNAL** and use the **ext_shunt_resistor_val** input to specify the value of the resistor.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CurrentShuntResistorLocation]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'extShuntResistorVal',
                'python_data_type': 'float',
                'python_default_value': '249.0',
                'python_description': 'Specifies in ohms the resistance of an external shunt resistor.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure current.',
        'returns': 'int32'
    },
    'CreateAICurrentRMSChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.01',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.01',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CurrentUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'CurrentUnits',
                'python_default_value': 'CurrentUnits.AMPS',
                'python_description': 'Specifies the units to use to return current measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CurrentUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CurrentShuntResistorLocationWithDefault',
                'is_optional_in_python': True,
                'name': 'shuntResistorLoc',
                'python_data_type': 'CurrentShuntResistorLocation',
                'python_default_value': 'CurrentShuntResistorLocation.LET_DRIVER_CHOOSE',
                'python_description': 'Specifies the location of the shunt resistor. For devices with built-in shunt resistors, specify the location as **INTERNAL**. For devices that do not have built-in shunt resistors, you must attach an external one, set this input to **EXTERNAL** and use the **ext_shunt_resistor_val** input to specify the value of the resistor.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CurrentShuntResistorLocation]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'extShuntResistorVal',
                'python_data_type': 'float',
                'python_default_value': '249.0',
                'python_description': 'Specifies in ohms the resistance of an external shunt resistor.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates a channel to measure current RMS, the average (mean) power of the acquired current.',
        'returns': 'int32'
    },
    'CreateAIForceBridgePolynomialChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ForceUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'ForceUnits',
                'python_default_value': 'ForceUnits.POUNDS',
                'python_description': 'Specifies in which unit to return force measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ForceUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.FULL_BRIDGE',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalBridgeResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'forwardCoeffs',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numForwardCoeffs'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numForwardCoeffs',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'reverseCoeffs',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numReverseCoeffs'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numReverseCoeffs',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'is_optional_in_python': True,
                'name': 'electricalUnits',
                'python_data_type': 'BridgeElectricalUnits',
                'python_default_value': 'BridgeElectricalUnits.MILLIVOLTS_PER_VOLT',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeElectricalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'is_optional_in_python': True,
                'name': 'physicalUnits',
                'python_data_type': 'BridgePhysicalUnits',
                'python_default_value': 'BridgePhysicalUnits.POUNDS',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgePhysicalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use the DAQmx Compute Reverse Polynomial Coefficients function to generate the other set.',
        'returns': 'int32'
    },
    'CreateAIForceBridgeTableChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ForceUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'ForceUnits',
                'python_default_value': 'ForceUnits.POUNDS',
                'python_description': 'Specifies in which unit to return force measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ForceUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.FULL_BRIDGE',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalBridgeResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'electricalVals',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numElectricalVals'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numElectricalVals',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'is_optional_in_python': True,
                'name': 'electricalUnits',
                'python_data_type': 'BridgeElectricalUnits',
                'python_default_value': 'BridgeElectricalUnits.MILLIVOLTS_PER_VOLT',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeElectricalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'physicalVals',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numPhysicalVals'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numPhysicalVals',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'is_optional_in_python': True,
                'name': 'physicalUnits',
                'python_data_type': 'BridgePhysicalUnits',
                'python_default_value': 'BridgePhysicalUnits.POUNDS',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgePhysicalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with **min_val** and **max_val** must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints.',
        'returns': 'int32'
    },
    'CreateAIForceBridgeTwoPointLinChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ForceUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'ForceUnits',
                'python_default_value': 'ForceUnits.POUNDS',
                'python_description': 'Specifies in which unit to return force measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ForceUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.FULL_BRIDGE',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalBridgeResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'firstElectricalVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'secondElectricalVal',
                'python_data_type': 'float',
                'python_default_value': '2.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'is_optional_in_python': True,
                'name': 'electricalUnits',
                'python_data_type': 'BridgeElectricalUnits',
                'python_default_value': 'BridgeElectricalUnits.MILLIVOLTS_PER_VOLT',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeElectricalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'firstPhysicalVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'secondPhysicalVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'is_optional_in_python': True,
                'name': 'physicalUnits',
                'python_data_type': 'BridgePhysicalUnits',
                'python_default_value': 'BridgePhysicalUnits.POUNDS',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgePhysicalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values.',
        'returns': 'int32'
    },
    'CreateAIForceIEPEChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-2000.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '2000.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ForceIEPEUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'ForceUnits',
                'python_default_value': 'ForceUnits.NEWTONS',
                'python_description': 'Specifies in which unit to return force measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ForceUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sensitivity',
                'python_data_type': 'float',
                'python_default_value': '2.25',
                'python_description': 'Is the sensitivity of the sensor. This value is in the units you specify with the **sensitivity_units** input. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ForceIEPESensorSensitivityUnits',
                'is_optional_in_python': True,
                'name': 'sensitivityUnits',
                'python_data_type': 'ForceIEPESensorSensitivityUnits',
                'python_default_value': 'ForceIEPESensorSensitivityUnits.MILLIVOLTS_PER_NEWTON',
                'python_description': 'Specifies the units of the **sensitivity** input.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ForceIEPESensorSensitivityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.004',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an IEPE force sensor to measure force or load.',
        'returns': 'int32'
    },
    'CreateAIFreqVoltageChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '1',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'FrequencyUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'FrequencyUnits',
                'python_default_value': 'FrequencyUnits.HZ',
                'python_description': 'Specifies the units to use to return frequency measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.FrequencyUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'thresholdLevel',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in volts the level at which to recognize waveform repetitions. You should select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'hysteresis',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in volts a window below **level**. The input voltage must pass below **threshold_level** minus **hysteresis** before NI-DAQmx recognizes a waveform repetition. Hysteresis can improve measurement accuracy when the signal contains noise or jitter.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a frequency-to-voltage converter to measure frequency.',
        'returns': 'int32'
    },
    'CreateAIMicrophoneChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'SoundPressureUnits1',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'SoundPressureUnits',
                'python_default_value': 'SoundPressureUnits.PA',
                'python_description': 'Specifies the units to use to return sound pressure measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.SoundPressureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'micSensitivity',
                'python_data_type': 'float',
                'python_default_value': '10.0',
                'python_description': 'Is the sensitivity of the microphone. Specify this value in mV/Pa.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxSndPressLevel',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Is the maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.004',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a microphone to measure sound pressure.',
        'returns': 'int32'
    },
    'CreateAIPosEddyCurrProxProbeChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.00254',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'LengthUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'LengthUnits',
                'python_default_value': 'LengthUnits.METERS',
                'python_description': 'Specifies the units to use to return position measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.LengthUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sensitivity',
                'python_data_type': 'float',
                'python_default_value': '200.0',
                'python_description': 'Is the sensitivity of the sensor. This value is in the units you specify with the **sensitivity_units** input. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'EddyCurrentProxProbeSensitivityUnits',
                'is_optional_in_python': True,
                'name': 'sensitivityUnits',
                'python_data_type': 'EddyCurrentProxProbeSensitivityUnits',
                'python_default_value': 'EddyCurrentProxProbeSensitivityUnits.MILLIVOLTS_PER_MIL',
                'python_description': 'Specifies the units of the **sensitivity** input.',
                'python_type_annotation': 'Optional[nidaqmx.constants.EddyCurrentProxProbeSensitivityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an eddy current proximity probe to measure position.',
        'returns': 'int32'
    },
    'CreateAIPosLVDTChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.1',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.1',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'LengthUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'LengthUnits',
                'python_default_value': 'LengthUnits.METERS',
                'python_description': 'Specifies the units to use to return linear position measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.LengthUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sensitivity',
                'python_data_type': 'float',
                'python_default_value': '50.0',
                'python_description': 'Is the sensitivity of the sensor. This value is in the units you specify with the **sensitivity_units** input. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'LVDTSensitivityUnits1',
                'is_optional_in_python': True,
                'name': 'sensitivityUnits',
                'python_data_type': 'LVDTSensitivityUnits',
                'python_default_value': 'LVDTSensitivityUnits.MILLIVOLTS_PER_VOLT_PER_MILLIMETER',
                'python_description': 'Specifies the units of the **sensitivity** input.',
                'python_type_annotation': 'Optional[nidaqmx.constants.LVDTSensitivityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '1.0',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitFreq',
                'python_data_type': 'float',
                'python_default_value': '2500.0',
                'python_description': 'Specifies in hertz the excitation frequency that the sensor requires. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ACExcitWireMode',
                'is_optional_in_python': True,
                'name': 'acExcitWireMode',
                'python_data_type': 'ACExcitWireMode',
                'python_default_value': 'ACExcitWireMode.FOUR_WIRE',
                'python_description': 'Is the number of leads on the sensor. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ACExcitWireMode]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an LVDT to measure linear position.',
        'returns': 'int32'
    },
    'CreateAIPosRVDTChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-70.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '70.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AngleUnits1',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'AngleUnits',
                'python_default_value': 'AngleUnits.DEGREES',
                'python_description': 'Specifies the units to use to return angular position measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AngleUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sensitivity',
                'python_data_type': 'float',
                'python_default_value': '50.0',
                'python_description': 'Is the sensitivity of the sensor. This value is in the units you specify with the **sensitivity_units** input. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'RVDTSensitivityUnits1',
                'is_optional_in_python': True,
                'name': 'sensitivityUnits',
                'python_data_type': 'RVDTSensitivityUnits',
                'python_default_value': 'RVDTSensitivityUnits.MILLIVOLTS_PER_VOLT_PER_DEGREE',
                'python_description': 'Specifies the units of the **sensitivity** input.',
                'python_type_annotation': 'Optional[nidaqmx.constants.RVDTSensitivityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '1.0',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitFreq',
                'python_data_type': 'float',
                'python_default_value': '2500.0',
                'python_description': 'Specifies in hertz the excitation frequency that the sensor requires. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ACExcitWireMode',
                'is_optional_in_python': True,
                'name': 'acExcitWireMode',
                'python_data_type': 'ACExcitWireMode',
                'python_default_value': 'ACExcitWireMode.FOUR_WIRE',
                'python_description': 'Is the number of leads on the sensor. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ACExcitWireMode]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an RVDT to measure angular position.',
        'returns': 'int32'
    },
    'CreateAIPowerChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'voltageSetpoint',
                'python_data_type': 'float',
                'python_description': 'Specifies, in volts, the constant output voltage.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'currentSetpoint',
                'python_data_type': 'float',
                'python_description': 'Specifies, in amperes, the output current.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'c_bool32',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'outputEnable',
                'python_data_type': 'bool',
                'python_description': 'Specifies whether to enable or disable the output.',
                'python_type_annotation': 'bool',
                'type': 'bool32'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure power.',
        'returns': 'int32'
    },
    'CreateAIPressureBridgePolynomialChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'PressureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'PressureUnits',
                'python_default_value': 'PressureUnits.POUNDS_PER_SQ_INCH',
                'python_description': 'Specifies in which unit to return pressure measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.PressureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.FULL_BRIDGE',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalBridgeResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'forwardCoeffs',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numForwardCoeffs'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numForwardCoeffs',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'reverseCoeffs',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numReverseCoeffs'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numReverseCoeffs',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'is_optional_in_python': True,
                'name': 'electricalUnits',
                'python_data_type': 'BridgeElectricalUnits',
                'python_default_value': 'BridgeElectricalUnits.MILLIVOLTS_PER_VOLT',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeElectricalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'is_optional_in_python': True,
                'name': 'physicalUnits',
                'python_data_type': 'BridgePhysicalUnits',
                'python_default_value': 'BridgePhysicalUnits.POUNDS_PER_SQ_INCH',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgePhysicalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use the DAQmx Compute Reverse Polynomial Coefficients function to generate the other set.',
        'returns': 'int32'
    },
    'CreateAIPressureBridgeTableChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'PressureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'PressureUnits',
                'python_default_value': 'PressureUnits.POUNDS_PER_SQ_INCH',
                'python_description': 'Specifies in which unit to return pressure measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.PressureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.FULL_BRIDGE',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalBridgeResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'electricalVals',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numElectricalVals'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numElectricalVals',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'is_optional_in_python': True,
                'name': 'electricalUnits',
                'python_data_type': 'BridgeElectricalUnits',
                'python_default_value': 'BridgeElectricalUnits.MILLIVOLTS_PER_VOLT',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeElectricalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'physicalVals',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numPhysicalVals'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numPhysicalVals',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'is_optional_in_python': True,
                'name': 'physicalUnits',
                'python_data_type': 'BridgePhysicalUnits',
                'python_default_value': 'BridgePhysicalUnits.POUNDS_PER_SQ_INCH',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgePhysicalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with **min_val** and **max_val** must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints.',
        'returns': 'int32'
    },
    'CreateAIPressureBridgeTwoPointLinChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'PressureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'PressureUnits',
                'python_default_value': 'PressureUnits.POUNDS_PER_SQ_INCH',
                'python_description': 'Specifies in which unit to return pressure measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.PressureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.FULL_BRIDGE',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalBridgeResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'firstElectricalVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'secondElectricalVal',
                'python_data_type': 'float',
                'python_default_value': '2.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'is_optional_in_python': True,
                'name': 'electricalUnits',
                'python_data_type': 'BridgeElectricalUnits',
                'python_default_value': 'BridgeElectricalUnits.MILLIVOLTS_PER_VOLT',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeElectricalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'firstPhysicalVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'secondPhysicalVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'is_optional_in_python': True,
                'name': 'physicalUnits',
                'python_data_type': 'BridgePhysicalUnits',
                'python_default_value': 'BridgePhysicalUnits.POUNDS_PER_SQ_INCH',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgePhysicalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values.',
        'returns': 'int32'
    },
    'CreateAIRTDChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TemperatureUnits',
                'python_default_value': 'TemperatureUnits.DEG_C',
                'python_description': 'Specifies the units to use to return temperature measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TemperatureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'RTDType1',
                'is_optional_in_python': True,
                'name': 'rtdType',
                'python_data_type': 'RTDType',
                'python_default_value': 'RTDType.PT_3750',
                'python_description': 'Specifies the type of RTD connected to the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.RTDType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'is_optional_in_python': True,
                'name': 'resistanceConfig',
                'python_data_type': 'ResistanceConfiguration',
                'python_default_value': 'ResistanceConfiguration.TWO_WIRE',
                'python_description': 'Specifies the number of wires to use for resistive measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ResistanceConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.EXTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.0025',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'r0',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Is the sensor resistance in ohms at 0 degrees Celsius. The Callendar-Van Dusen equation requires this value. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an RTD to measure temperature.',
        'returns': 'int32'
    },
    'CreateAIResistanceChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '1000.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ResistanceUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'ResistanceUnits',
                'python_default_value': 'ResistanceUnits.OHMS',
                'python_description': 'Specifies the units to use to return resistance measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ResistanceUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'is_optional_in_python': True,
                'name': 'resistanceConfig',
                'python_data_type': 'ResistanceConfiguration',
                'python_default_value': 'ResistanceConfiguration.TWO_WIRE',
                'python_description': 'Specifies the number of wires to use for resistive measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ResistanceConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.EXTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure resistance.',
        'returns': 'int32'
    },
    'CreateAIRosetteStrainGageChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create the strain gage virtual channels necessary to calculate the **rosette measurements** channels.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx creates a default channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.001',
                'python_description': 'Specifies the minimum strain you expect to measure. This value applies to each strain gage in the rosette.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Specifies the maximum strain you expect to measure. This value applies to each strain gage in the rosette.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'StrainGageRosetteType',
                'is_optional_in_python': False,
                'name': 'rosetteType',
                'python_data_type': 'StrainGageRosetteType',
                'python_description': 'Specifies information about the rosette configuration and measurements.',
                'python_type_annotation': 'nidaqmx.constants.StrainGageRosetteType',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'gageOrientation',
                'python_data_type': 'float',
                'python_description': 'Specifies information about the rosette configuration and measurements.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'numpy.int32',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': False,
                'name': 'rosetteMeasTypes',
                'python_data_type': 'int',
                'python_description': 'Specifies information about the rosette configuration and measurements.',
                'python_type_annotation': 'List[int]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numRosetteMeasTypes'
                },
                'type': 'const int32[]'
            },
            {
                'direction': 'in',
                'name': 'numRosetteMeasTypes',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'StrainGageBridgeType1',
                'is_optional_in_python': True,
                'name': 'strainConfig',
                'python_data_type': 'StrainGageBridgeType',
                'python_default_value': 'StrainGageBridgeType.QUARTER_BRIDGE_I',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.StrainGageBridgeType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'gageFactor',
                'python_data_type': 'float',
                'python_default_value': '2.0',
                'python_description': 'Contains information about the strain gage and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalGageResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Contains information about the strain gage and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'poissonRatio',
                'python_data_type': 'float',
                'python_default_value': '0.3',
                'python_description': 'Contains information about the strain gage and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'leadWireResistance',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channels to measure two-dimensional strain using a rosette strain gage.',
        'returns': 'int32'
    },
    'CreateAIStrainGageChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.001',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'StrainUnits1',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'StrainUnits',
                'python_default_value': 'StrainUnits.STRAIN',
                'python_description': 'Specifies the units to use to return strain measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.StrainUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'StrainGageBridgeType1',
                'is_optional_in_python': True,
                'name': 'strainConfig',
                'python_data_type': 'StrainGageBridgeType',
                'python_default_value': 'StrainGageBridgeType.FULL_BRIDGE_I',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.StrainGageBridgeType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'gageFactor',
                'python_data_type': 'float',
                'python_default_value': '2.0',
                'python_description': 'Contains information about the strain gage and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'initialBridgeVoltage',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalGageResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Contains information about the strain gage and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'poissonRatio',
                'python_data_type': 'float',
                'python_default_value': '0.30',
                'python_description': 'Contains information about the strain gage and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'leadWireResistance',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure strain.',
        'returns': 'int32'
    },
    'CreateAITempBuiltInSensorChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TemperatureUnits',
                'python_default_value': 'TemperatureUnits.DEG_C',
                'python_description': 'Specifies the units to use to return temperature measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TemperatureUnits]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use the built-in sensor of a terminal block or device to measure temperature. On SCXI modules, for example, the built-in sensor could be the CJC sensor.',
        'returns': 'int32'
    },
    'CreateAIThrmcplChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TemperatureUnits',
                'python_default_value': 'TemperatureUnits.DEG_C',
                'python_description': 'Specifies the units to use to return temperature measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TemperatureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ThermocoupleType1',
                'is_optional_in_python': True,
                'name': 'thermocoupleType',
                'python_data_type': 'ThermocoupleType',
                'python_default_value': 'ThermocoupleType.J',
                'python_description': 'Specifies the type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ThermocoupleType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CJCSource1',
                'is_optional_in_python': True,
                'name': 'cjcSource',
                'python_data_type': 'CJCSource',
                'python_default_value': 'CJCSource.CONSTANT_USER_VALUE',
                'python_description': 'Specifies the source of cold-junction compensation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CJCSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'cjcVal',
                'python_data_type': 'float',
                'python_default_value': '25.0',
                'python_description': 'Specifies in **units** the temperature of the cold junction if you set **cjc_source** to **CONSTANT_VALUE**.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'cjcChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the channel that acquires the temperature of the thermocouple cold-junction if you set **cjc_source** to **CHANNEL**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a thermocouple to measure temperature.',
        'returns': 'int32'
    },
    'CreateAIThrmstrChanIex': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TemperatureUnits',
                'python_default_value': 'TemperatureUnits.DEG_C',
                'python_description': 'Specifies the units to use to return temperature measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TemperatureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'is_optional_in_python': True,
                'name': 'resistanceConfig',
                'python_data_type': 'ResistanceConfiguration',
                'python_default_value': 'ResistanceConfiguration.FOUR_WIRE',
                'python_description': 'Specifies the number of wires to use for resistive measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ResistanceConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.EXTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.00015',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'a',
                'python_data_type': 'float',
                'python_default_value': '0.001295361',
                'python_description': 'Contains the constants for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'b',
                'python_data_type': 'float',
                'python_default_value': '0.0002343159',
                'python_description': 'Contains the constants for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'c',
                'python_data_type': 'float',
                'python_default_value': '0.0000001018703',
                'python_description': 'Contains the constants for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a thermistor to measure temperature. Use this instance when the thermistor requires current excitation.',
        'returns': 'int32'
    },
    'CreateAIThrmstrChanVex': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TemperatureUnits',
                'python_default_value': 'TemperatureUnits.DEG_C',
                'python_description': 'Specifies the units to use to return temperature measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TemperatureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'is_optional_in_python': True,
                'name': 'resistanceConfig',
                'python_data_type': 'ResistanceConfiguration',
                'python_default_value': 'ResistanceConfiguration.FOUR_WIRE',
                'python_description': 'Specifies the number of wires to use for resistive measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ResistanceConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.EXTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'a',
                'python_data_type': 'float',
                'python_default_value': '0.001295361',
                'python_description': 'Contains the constants for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'b',
                'python_data_type': 'float',
                'python_default_value': '0.0002343159',
                'python_description': 'Contains the constants for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'c',
                'python_data_type': 'float',
                'python_default_value': '0.0000001018703',
                'python_description': 'Contains the constants for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'r1',
                'python_data_type': 'float',
                'python_default_value': '5000.0',
                'python_description': 'Specifies in ohms the value of the reference resistor.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a thermistor to measure temperature. Use this instance when the thermistor requires voltage excitation.',
        'returns': 'int32'
    },
    'CreateAITorqueBridgePolynomialChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TorqueUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TorqueUnits',
                'python_default_value': 'TorqueUnits.INCH_POUNDS',
                'python_description': 'Specifies in which unit to return torque measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TorqueUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.FULL_BRIDGE',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalBridgeResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'forwardCoeffs',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numForwardCoeffs'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numForwardCoeffs',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'reverseCoeffs',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numReverseCoeffs'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numReverseCoeffs',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'is_optional_in_python': True,
                'name': 'electricalUnits',
                'python_data_type': 'BridgeElectricalUnits',
                'python_default_value': 'BridgeElectricalUnits.MILLIVOLTS_PER_VOLT',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeElectricalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'is_optional_in_python': True,
                'name': 'physicalUnits',
                'python_data_type': 'BridgePhysicalUnits',
                'python_default_value': 'BridgePhysicalUnits.INCH_POUNDS',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgePhysicalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure torque. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use the DAQmx Compute Reverse Polynomial Coefficients function to generate the other set.',
        'returns': 'int32'
    },
    'CreateAITorqueBridgeTableChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TorqueUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TorqueUnits',
                'python_default_value': 'TorqueUnits.INCH_POUNDS',
                'python_description': 'Specifies in which unit to return torque measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TorqueUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.FULL_BRIDGE',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalBridgeResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'electricalVals',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numElectricalVals'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numElectricalVals',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'is_optional_in_python': True,
                'name': 'electricalUnits',
                'python_data_type': 'BridgeElectricalUnits',
                'python_default_value': 'BridgeElectricalUnits.MILLIVOLTS_PER_VOLT',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeElectricalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'physicalVals',
                'python_data_type': 'float',
                'python_default_value': None,
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[List[float]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numPhysicalVals'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numPhysicalVals',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'is_optional_in_python': True,
                'name': 'physicalUnits',
                'python_data_type': 'BridgePhysicalUnits',
                'python_default_value': 'BridgePhysicalUnits.INCH_POUNDS',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgePhysicalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure torque. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with **min_val** and **max_val** must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints.',
        'returns': 'int32'
    },
    'CreateAITorqueBridgeTwoPointLinChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TorqueUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TorqueUnits',
                'python_default_value': 'TorqueUnits.INCH_POUNDS',
                'python_description': 'Specifies in which unit to return torque measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TorqueUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.FULL_BRIDGE',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nominalBridgeResistance',
                'python_data_type': 'float',
                'python_default_value': '350.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'firstElectricalVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'secondElectricalVal',
                'python_data_type': 'float',
                'python_default_value': '2.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'is_optional_in_python': True,
                'name': 'electricalUnits',
                'python_data_type': 'BridgeElectricalUnits',
                'python_default_value': 'BridgeElectricalUnits.MILLIVOLTS_PER_VOLT',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeElectricalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'firstPhysicalVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'secondPhysicalVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'is_optional_in_python': True,
                'name': 'physicalUnits',
                'python_data_type': 'BridgePhysicalUnits',
                'python_default_value': 'BridgePhysicalUnits.INCH_POUNDS',
                'python_description': 'Specifies how to scale electrical values from the sensor to physical units.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgePhysicalUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure torque. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values.',
        'returns': 'int32'
    },
    'CreateAIVelocityIEPEChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-50.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '50.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'VelocityUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'VelocityUnits',
                'python_default_value': 'VelocityUnits.INCHES_PER_SECOND',
                'python_description': 'Specifies in which unit to return velocity measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.VelocityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sensitivity',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Is the sensitivity of the sensor. This value is in the units you specify with the **sensitivity_units** input. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'VelocityIEPESensorSensitivityUnits',
                'is_optional_in_python': True,
                'name': 'sensitivityUnits',
                'python_data_type': 'VelocityIEPESensorSensitivityUnits',
                'python_default_value': 'VelocityIEPESensorSensitivityUnits.MILLIVOLTS_PER_INCH_PER_SECOND',
                'python_description': 'Specifies the units of the **sensitivity** input.',
                'python_type_annotation': 'Optional[nidaqmx.constants.VelocityIEPESensorSensitivityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.002',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an IEPE velocity sensor to measure velocity.',
        'returns': 'int32'
    },
    'CreateAIVoltageChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-5.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '5.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'VoltageUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'VoltageUnits',
                'python_default_value': 'VoltageUnits.VOLTS',
                'python_description': 'Specifies the units to use to return voltage measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.VoltageUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure voltage. If the measurement requires the use of internal excitation or you need excitation to scale the voltage, use the AI Custom Voltage with Excitation instance of this function.',
        'returns': 'int32'
    },
    'CreateAIVoltageChanWithExcit': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-10.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '10.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'VoltageUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'VoltageUnits',
                'python_default_value': 'VoltageUnits.VOLTS',
                'python_description': 'Specifies the units to use to return voltage measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.VoltageUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'is_optional_in_python': True,
                'name': 'bridgeConfig',
                'python_data_type': 'BridgeConfiguration',
                'python_default_value': 'BridgeConfiguration.NO_BRIDGE',
                'python_description': 'Specifies what type of Wheatstone bridge the sensor is.',
                'python_type_annotation': 'Optional[nidaqmx.constants.BridgeConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'c_bool32',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'useExcitForScaling',
                'python_data_type': 'bool',
                'python_default_value': False,
                'python_description': 'Specifies if NI-DAQmx divides the measurement by the excitation. You should typically set **use_excit_for_scaling** to True for ratiometric transducers. If you set **use_excit_for_scaling** to True, set **max_val** and **min_val** to reflect the scaling.',
                'python_type_annotation': 'Optional[bool]',
                'type': 'bool32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure voltage. Use this instance for custom sensors that require excitation. You can use the excitation to scale the measurement.',
        'returns': 'int32'
    },
    'CreateAIVoltageRMSChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-5.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '5.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'VoltageUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'VoltageUnits',
                'python_default_value': 'VoltageUnits.VOLTS',
                'python_description': 'Specifies the units to use to return voltage measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.VoltageUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure voltage RMS, the average (mean) power of the acquired voltage.',
        'returns': 'int32'
    },
    'CreateAOCurrentChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ao_channel.AOChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.02',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CurrentUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'CurrentUnits',
                'python_default_value': 'CurrentUnits.AMPS',
                'python_description': 'Specifies the units to use to generate current.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CurrentUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AOChannelCollection',
        'python_description': 'Creates channel(s) to generate current.',
        'returns': 'int32'
    },
    'CreateAOFuncGenChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ao_channel.AOChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'FuncGenType',
                'is_optional_in_python': True,
                'name': 'type',
                'python_data_type': 'FuncGenType',
                'python_default_value': 'FuncGenType.SINE',
                'python_description': 'Specifies the kind of waveform to generate.',
                'python_type_annotation': 'Optional[nidaqmx.constants.FuncGenType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'freq',
                'python_data_type': 'float',
                'python_default_value': '1000.0',
                'python_description': 'Is the frequency of the waveform to generate in hertz.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'amplitude',
                'python_data_type': 'float',
                'python_default_value': '5.0',
                'python_description': 'Is the zero-to-peak amplitude of the waveform to generate in volts. Zero and negative values are valid.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'offset',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Is the voltage offset of the waveform to generate.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'AOChannelCollection',
        'python_description': 'Creates a channel for continually generating a waveform on the selected physical channel.',
        'returns': 'int32'
    },
    'CreateAOVoltageChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ao_channel.AOChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-10.0',
                'python_description': 'Specifies in **units** the minimum value you expect to generate.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '10.0',
                'python_description': 'Specifies in **units** the maximum value you expect to generate.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'VoltageUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'VoltageUnits',
                'python_default_value': 'VoltageUnits.VOLTS',
                'python_description': 'Specifies the units to use to generate voltage.',
                'python_type_annotation': 'Optional[nidaqmx.constants.VoltageUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AOChannelCollection',
        'python_description': 'Creates channel(s) to generate voltage.',
        'returns': 'int32'
    },
    'CreateCIAngEncoderChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'EncoderType2',
                'is_optional_in_python': True,
                'name': 'decodingType',
                'python_data_type': 'EncoderType',
                'python_default_value': 'EncoderType.X_4',
                'python_description': 'Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. **X_1**, **X_2**, and **X_4** are valid for quadrature encoders only. **TWO_PULSE_COUNTING** is valid only for two-pulse encoders.',
                'python_type_annotation': 'Optional[nidaqmx.constants.EncoderType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'c_bool32',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'zidxEnable',
                'python_data_type': 'bool',
                'python_default_value': False,
                'python_description': 'Specifies whether to use Z indexing for the channel.',
                'python_type_annotation': 'Optional[bool]',
                'type': 'bool32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'zidxVal',
                'python_data_type': 'float',
                'python_default_value': '0',
                'python_description': 'Specifies in **units** the value to which to reset the measurement when signal Z is high and signal A and signal B are at the states you specify with **zidx_phase**.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'EncoderZIndexPhase1',
                'is_optional_in_python': True,
                'name': 'zidxPhase',
                'python_data_type': 'EncoderZIndexPhase',
                'python_default_value': 'EncoderZIndexPhase.AHIGH_BHIGH',
                'python_description': 'Specifies the states at which signal A and signal B must be while signal Z is high for NI-DAQmx to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than **A_HIGH_B_HIGH**.',
                'python_type_annotation': 'Optional[nidaqmx.constants.EncoderZIndexPhase]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AngleUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'AngleUnits',
                'python_default_value': 'AngleUnits.DEGREES',
                'python_description': 'Specifies the units to use to return angular position measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AngleUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_uint',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'pulsesPerRev',
                'python_data_type': 'int',
                'python_default_value': '24',
                'python_description': 'Is the number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'initialAngle',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Is the starting angle of the encoder. This value is in the units you specify with the **units** input.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel that uses an angular encoder to measure angular position. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signals to the default input terminals of the counter unless you select different input terminals.',
        'returns': 'int32'
    },
    'CreateCIAngVelocityChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '1.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'EncoderType2',
                'is_optional_in_python': True,
                'name': 'decodingType',
                'python_data_type': 'EncoderType',
                'python_default_value': 'EncoderType.X_4',
                'python_description': 'Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. **X_1**, **X_2**, and **X_4** are valid for quadrature encoders only. **TWO_PULSE_COUNTING** is valid only for two-pulse encoders.',
                'python_type_annotation': 'Optional[nidaqmx.constants.EncoderType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AngularVelocityUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'AngularVelocityUnits',
                'python_default_value': 'AngularVelocityUnits.RPM',
                'python_description': 'Specifies in which unit to return velocity measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AngularVelocityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_uint',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'pulsesPerRev',
                'python_data_type': 'int',
                'python_default_value': '24',
                'python_description': 'Is the number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel to measure the angular velocity of a digital signal. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the default input terminal of the counter unless you select a different input terminal.',
        'returns': 'int32'
    },
    'CreateCICountEdgesChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'edge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies on which edges of the input signal to increment or decrement the count.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_uint',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'initialCount',
                'python_data_type': 'int',
                'python_default_value': '0',
                'python_description': 'Is the value from which to start counting.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CountDirection1',
                'is_optional_in_python': True,
                'name': 'countDirection',
                'python_data_type': 'CountDirection',
                'python_default_value': 'CountDirection.COUNT_UP',
                'python_description': 'Specifies whether to increment or decrement the counter on each edge.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CountDirection]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel to count the number of rising or falling edges of a digital signal. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the default input terminal of the counter unless you select a different input terminal.',
        'returns': 'int32'
    },
    'CreateCIDutyCycleChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minFreq',
                'python_data_type': 'float',
                'python_default_value': '2.0',
                'python_description': 'Specifies the minimum frequency you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxFreq',
                'python_data_type': 'float',
                'python_default_value': '10000.0',
                'python_description': 'Specifies the maximum frequency you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'edge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies between which edges to measure the frequency or period of the signal.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates channel(s) to duty cycle of a digital pulse. Connect the input signal to the default input terminal of the counter unless you select a different input terminal. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter.',
        'returns': 'int32'
    },
    'CreateCIFreqChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '2.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'FrequencyUnits3',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'FrequencyUnits',
                'python_default_value': 'FrequencyUnits.HZ',
                'python_description': 'Specifies the units to use to return frequency measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.FrequencyUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'edge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies between which edges to measure the frequency or period of the signal.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CounterFrequencyMethod',
                'is_optional_in_python': True,
                'name': 'measMethod',
                'python_data_type': 'CounterFrequencyMethod',
                'python_default_value': 'CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER',
                'python_description': 'Specifies the method to use to calculate the period or frequency of the signal.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CounterFrequencyMethod]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'measTime',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Is the length of time in seconds to measure the frequency or period of the signal if **meas_method** is **HIGH_FREQUENCYWITH_2_COUNTERS**. Leave this input unspecified if **meas_method** is not **HIGH_FREQUENCYWITH_2_COUNTERS**.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_uint',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'divisor',
                'python_data_type': 'int',
                'python_default_value': '4',
                'python_description': 'Is the value by which to divide the input signal when **meas_method** is **LARGE_RANGEWITH_2_COUNTERS**. Leave this input unspecified if **meas_method** is not **LARGE_RANGEWITH_2_COUNTERS**.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel to measure the frequency of a digital signal. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the default input terminal of the counter unless you select a different input terminal.',
        'returns': 'int32'
    },
    'CreateCIGPSTimestampChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TimeUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TimeUnits',
                'python_default_value': 'TimeUnits.SECONDS',
                'python_description': 'Specifies the units to use to return the timestamp.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TimeUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'GpsSignalType1',
                'is_optional_in_python': True,
                'name': 'syncMethod',
                'python_data_type': 'GpsSignalType',
                'python_default_value': 'GpsSignalType.IRIGB',
                'python_description': 'Specifies the method to use to synchronize the counter to a GPS receiver.',
                'python_type_annotation': 'Optional[nidaqmx.constants.GpsSignalType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel that uses a special purpose counter to take a timestamp and synchronizes that counter to a GPS receiver. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signals to the default input terminals of the counter unless you select different input terminals.',
        'returns': 'int32'
    },
    'CreateCILinEncoderChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'EncoderType2',
                'is_optional_in_python': True,
                'name': 'decodingType',
                'python_data_type': 'EncoderType',
                'python_default_value': 'EncoderType.X_4',
                'python_description': 'Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. **X_1**, **X_2**, and **X_4** are valid for quadrature encoders only. **TWO_PULSE_COUNTING** is valid only for two-pulse encoders.',
                'python_type_annotation': 'Optional[nidaqmx.constants.EncoderType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'c_bool32',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'zidxEnable',
                'python_data_type': 'bool',
                'python_default_value': False,
                'python_description': 'Specifies whether to use Z indexing for the channel.',
                'python_type_annotation': 'Optional[bool]',
                'type': 'bool32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'zidxVal',
                'python_data_type': 'float',
                'python_default_value': '0',
                'python_description': 'Specifies in **units** the value to which to reset the measurement when signal Z is high and signal A and signal B are at the states you specify with **zidx_phase**.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'EncoderZIndexPhase1',
                'is_optional_in_python': True,
                'name': 'zidxPhase',
                'python_data_type': 'EncoderZIndexPhase',
                'python_default_value': 'EncoderZIndexPhase.AHIGH_BHIGH',
                'python_description': 'Specifies the states at which signal A and signal B must be while signal Z is high for NI-DAQmx to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than **A_HIGH_B_HIGH**.',
                'python_type_annotation': 'Optional[nidaqmx.constants.EncoderZIndexPhase]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'LengthUnits3',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'LengthUnits',
                'python_default_value': 'LengthUnits.METERS',
                'python_description': 'Specifies the units to use to return linear position measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.LengthUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'distPerPulse',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Is the distance to measure for each pulse the encoder generates on signal A or signal B. This value is in the units you specify with the **units** input.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'initialPos',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Is the position of the encoder when you begin the measurement. This value is in the units you specify with the **units** input.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel that uses a linear encoder to measure linear position. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signals to the default input terminals of the counter unless you select different input terminals.',
        'returns': 'int32'
    },
    'CreateCILinVelocityChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '1.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'EncoderType2',
                'is_optional_in_python': True,
                'name': 'decodingType',
                'python_data_type': 'EncoderType',
                'python_default_value': 'EncoderType.X_4',
                'python_description': 'Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. **X_1**, **X_2**, and **X_4** are valid for quadrature encoders only. **TWO_PULSE_COUNTING** is valid only for two-pulse encoders.',
                'python_type_annotation': 'Optional[nidaqmx.constants.EncoderType]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'VelocityUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'VelocityUnits',
                'python_default_value': 'VelocityUnits.METERS_PER_SECOND',
                'python_description': 'Specifies in which unit to return velocity measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.VelocityUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'distPerPulse',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Is the distance to measure for each pulse the encoder generates on signal A or signal B. This value is in the units you specify with the **units** input.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel that uses a linear encoder to measure linear velocity. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the default input terminal of the counter unless you select a different input terminal.',
        'returns': 'int32'
    },
    'CreateCIPeriodChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.000001',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.1',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TimeUnits3',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TimeUnits',
                'python_default_value': 'TimeUnits.SECONDS',
                'python_description': 'Specifies the units to use to return time or period measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TimeUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'edge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies between which edges to measure the frequency or period of the signal.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CounterFrequencyMethod',
                'is_optional_in_python': True,
                'name': 'measMethod',
                'python_data_type': 'CounterFrequencyMethod',
                'python_default_value': 'CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER',
                'python_description': 'Specifies the method to use to calculate the period or frequency of the signal.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CounterFrequencyMethod]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'measTime',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Is the length of time in seconds to measure the frequency or period of the signal if **meas_method** is **HIGH_FREQUENCYWITH_2_COUNTERS**. Leave this input unspecified if **meas_method** is not **HIGH_FREQUENCYWITH_2_COUNTERS**.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_uint',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'divisor',
                'python_data_type': 'int',
                'python_default_value': '4',
                'python_description': 'Is the value by which to divide the input signal when **meas_method** is **LARGE_RANGEWITH_2_COUNTERS**. Leave this input unspecified if **meas_method** is not **LARGE_RANGEWITH_2_COUNTERS**.',
                'python_type_annotation': 'Optional[int]',
                'type': 'uInt32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel to measure the period of a digital signal. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the default input terminal of the counter unless you select a different input terminal.',
        'returns': 'int32'
    },
    'CreateCIPulseChanFreq': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '1000',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '1000000',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'FrequencyUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'FrequencyUnits',
                'python_default_value': 'FrequencyUnits.HZ',
                'python_description': 'Specifies the units to use to return pulse specifications in terms of frequency.',
                'python_type_annotation': 'Optional[nidaqmx.constants.FrequencyUnits]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel to measure pulse specifications, returning the measurements as pairs of frequency and duty cycle. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the default input terminal of the counter unless you select a different input terminal.',
        'returns': 'int32'
    },
    'CreateCIPulseChanTicks': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'sourceTerminal',
                'python_data_type': 'str',
                'python_default_value': '"OnboardClock"',
                'python_description': 'Is the terminal to which you connect a signal to use as the source of ticks. A DAQmx terminal constant lists all terminals available on devices installed in the system. You also can specify a source terminal by specifying a string that contains a terminal name. If you specify OnboardClock, or do not specify any terminal, NI-DAQmx selects the fastest onboard timebase available on the device.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '1000',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '1000000',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel to measure pulse specifications, returning the measurements as pairs of high ticks and low ticks. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the default input terminal of the counter unless you select a different input terminal.',
        'returns': 'int32'
    },
    'CreateCIPulseChanTime': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.000001',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'DigitalWidthUnits3',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TimeUnits',
                'python_default_value': 'TimeUnits.SECONDS',
                'python_description': 'Specifies the units to use to return pulse specifications in terms of high time and low time.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TimeUnits]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel to measure pulse specifications, returning the measurements as pairs of high time and low time. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the default input terminal of the counter unless you select a different input terminal.',
        'returns': 'int32'
    },
    'CreateCIPulseWidthChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.000001',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.1',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TimeUnits3',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TimeUnits',
                'python_default_value': 'TimeUnits.SECONDS',
                'python_description': 'Specifies the units to use to return time or period measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TimeUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'startingEdge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies on which edge to begin measuring pulse width.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel to measure the width of a digital pulse. **starting_edge** determines whether to measure a high pulse or low pulse. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the default input terminal of the counter unless you select a different input terminal.',
        'returns': 'int32'
    },
    'CreateCISemiPeriodChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.000001',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.1',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TimeUnits3',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TimeUnits',
                'python_default_value': 'TimeUnits.SECONDS',
                'python_description': 'Specifies the units to use to return time or period measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TimeUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel to measure the time between state transitions of a digital signal. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the default input terminal of the counter unless you select a different input terminal.',
        'returns': 'int32'
    },
    'CreateCITwoEdgeSepChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ci_channel.CIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the name of the counter to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.000001',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '1.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TimeUnits3',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TimeUnits',
                'python_default_value': 'TimeUnits.SECONDS',
                'python_description': 'Specifies the units to use to return time or period measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TimeUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'firstEdge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.RISING',
                'python_description': 'Specifies on which edge of the first signal to start each measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Edge1',
                'is_optional_in_python': True,
                'name': 'secondEdge',
                'python_data_type': 'Edge',
                'python_default_value': 'Edge.FALLING',
                'python_description': 'Specifies on which edge of the second signal to stop each measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Edge]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'CIChannelCollection',
        'python_description': 'Creates a channel that measures the amount of time between the rising or falling edge of one digital signal and the rising or falling edge of another digital signal. With the exception of devices that support multi-counter tasks, you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signals to the default input terminals of the counter unless you select different input terminals.',
        'returns': 'int32'
    },
    'CreateCOPulseChanFreq': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.co_channel.COChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the counters to use to create the virtual channels. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'FrequencyUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'FrequencyUnits',
                'python_default_value': 'FrequencyUnits.HZ',
                'python_description': 'Specifies the units in which to define pulse frequency.',
                'python_type_annotation': 'Optional[nidaqmx.constants.FrequencyUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Level1',
                'is_optional_in_python': True,
                'name': 'idleState',
                'python_data_type': 'Level',
                'python_default_value': 'Level.LOW',
                'python_description': 'Specifies the resting state of the output terminal.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Level]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'initialDelay',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Is the amount of time in seconds to wait before generating the first pulse.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'freq',
                'python_data_type': 'float',
                'python_default_value': '1.0',
                'python_description': 'Specifies at what frequency to generate pulses.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'dutyCycle',
                'python_data_type': 'float',
                'python_default_value': '0.5',
                'python_description': 'Is the width of the pulse divided by the pulse period. NI-DAQmx uses this ratio combined with frequency to determine pulse width and the interval between pulses.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'COChannelCollection',
        'python_description': 'Creates channel(s) to generate digital pulses that **freq** and **duty_cycle** define. The pulses appear on the default output terminal of the counter unless you select a different output terminal.',
        'returns': 'int32'
    },
    'CreateCOPulseChanTicks': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.co_channel.COChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the counters to use to create the virtual channels. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'sourceTerminal',
                'python_data_type': 'str',
                'python_description': 'Is the terminal to which you connect an external timebase. A DAQmx terminal constant lists all terminals available on devices installed in the system. You also can specify a source terminal by specifying a string that contains a terminal name.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Level1',
                'is_optional_in_python': True,
                'name': 'idleState',
                'python_data_type': 'Level',
                'python_default_value': 'Level.LOW',
                'python_description': 'Specifies the resting state of the output terminal.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Level]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'initialDelay',
                'python_data_type': 'int',
                'python_default_value': '0',
                'python_description': 'Is the number of timebase ticks to wait before generating the first pulse.',
                'python_type_annotation': 'Optional[int]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'lowTicks',
                'python_data_type': 'int',
                'python_default_value': '100',
                'python_description': 'Is the number of ticks the pulse is low.',
                'python_type_annotation': 'Optional[int]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'highTicks',
                'python_data_type': 'int',
                'python_default_value': '100',
                'python_description': 'Is the number of ticks the pulse is high.',
                'python_type_annotation': 'Optional[int]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'COChannelCollection',
        'python_description': 'Creates channel(s) to generate digital pulses defined by the number of timebase ticks that the pulse is at a high state and the number of timebase ticks that the pulse is at a low state. The pulses appear on the default output terminal of the counter unless you select a different output terminal.',
        'returns': 'int32'
    },
    'CreateCOPulseChanTime': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(counter, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.co_channel.COChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'counter',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the counters to use to create the virtual channels. The DAQmx physical channel constant lists all physical channels, including counters, for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'DigitalWidthUnits3',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TimeUnits',
                'python_default_value': 'TimeUnits.SECONDS',
                'python_description': 'Specifies the units in which to define pulse high and low time.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TimeUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Level1',
                'is_optional_in_python': True,
                'name': 'idleState',
                'python_data_type': 'Level',
                'python_default_value': 'Level.LOW',
                'python_description': 'Specifies the resting state of the output terminal.',
                'python_type_annotation': 'Optional[nidaqmx.constants.Level]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'initialDelay',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Is the amount of time in seconds to wait before generating the first pulse.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'lowTime',
                'python_data_type': 'float',
                'python_default_value': '0.01',
                'python_description': 'Is the amount of time the pulse is low.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'highTime',
                'python_data_type': 'float',
                'python_default_value': '0.01',
                'python_description': 'Is the amount of time the pulse is high.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'COChannelCollection',
        'python_description': 'Creates channel(s) to generate digital pulses defined by the amount of time the pulse is at a high state and the amount of time the pulse is at a low state. The pulses appear on the default output terminal of the counter unless you select a different output terminal.',
        'returns': 'int32'
    },
    'CreateDIChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(lines, line_grouping, name_to_assign_to_lines)',
            'python_data_type': 'nidaqmx._task_modules.channels.di_channel.DIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'lines',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the digital lines or ports to use to create virtual channels. The DAQmx physical channel constant lists all lines and ports for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToLines',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'LineGrouping',
                'is_optional_in_python': True,
                'name': 'lineGrouping',
                'python_data_type': 'LineGrouping',
                'python_default_value': 'LineGrouping.CHAN_FOR_ALL_LINES',
                'python_description': 'Specifies how to group digital lines into one or more virtual channels. If you specify one or more entire ports with the **lines** input, you must set this input to **one channel for all lines**.',
                'python_type_annotation': 'Optional[nidaqmx.constants.LineGrouping]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'DIChannelCollection',
        'python_description': 'Creates channel(s) to measure digital signals. You can group digital lines into one digital channel or separate them into multiple digital channels. If you specify one or more entire ports in the **lines** input by using port physical channel names, you cannot separate the ports into multiple channels. To separate ports into multiple channels, use this function multiple times with a different port each time.',
        'returns': 'int32'
    },
    'CreateDOChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(lines, line_grouping, name_to_assign_to_lines)',
            'python_data_type': 'nidaqmx._task_modules.channels.do_channel.DOChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'lines',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the digital lines or ports to use to create virtual channels. The DAQmx physical channel constant lists all lines and ports for devices installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToLines',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'LineGrouping',
                'is_optional_in_python': True,
                'name': 'lineGrouping',
                'python_data_type': 'LineGrouping',
                'python_default_value': 'LineGrouping.CHAN_FOR_ALL_LINES',
                'python_description': 'Specifies how to group digital lines into one or more virtual channels. If you specify one or more entire ports with the **lines** input, you must set this input to **one channel for all lines**.',
                'python_type_annotation': 'Optional[nidaqmx.constants.LineGrouping]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'DOChannelCollection',
        'python_description': 'Creates channel(s) to generate digital signals. You can group digital lines into one digital channel or separate them into multiple digital channels. If you specify one or more entire ports in **lines** input by using port physical channel names, you cannot separate the ports into multiple channels. To separate ports into multiple channels, use this function multiple times with a different port each time.',
        'returns': 'int32'
    },
    'CreateLinScale': {
        'calling_convention': 'StdCall',
        'is_python_factory': True,
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'name',
                'python_data_type': 'str',
                'python_description': 'Identifies the custom scale for later use, such as with the DAQmx Create Virtual Channel VI',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'slope',
                'python_data_type': 'float',
                'python_description': 'Is the slope, m, in the equation.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'yIntercept',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Is the y-intercept, b, in the equation.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'UnitsPreScaled',
                'is_optional_in_python': True,
                'name': 'preScaledUnits',
                'python_data_type': 'UnitsPreScaled',
                'python_default_value': 'UnitsPreScaled.VOLTS',
                'python_description': 'Is the units of the values to scale.',
                'python_type_annotation': 'Optional[nidaqmx.constants.UnitsPreScaled]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'scaledUnits',
                'python_data_type': 'str',
                'python_default_value': None,
                'python_description': 'Is the units to use for the scaled value. You can use an arbitrary string. NI-DAQmx uses the units to label a graph or chart.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'Scale',
        'python_description': 'Creates a custom scale that uses the equation y=mx+b, where x is a pre-scaled value, and y is a scaled value. The equation is identical for input and output. If the equation is in the form x=my+b, you must first solve for y in terms of x.',
        'returns': 'int32'
    },
    'CreateMapScale': {
        'calling_convention': 'StdCall',
        'is_python_factory': True,
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'name',
                'python_data_type': 'str',
                'python_description': 'Identifies the custom scale for later use, such as with the DAQmx Create Virtual Channel VI',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'prescaledMin',
                'python_data_type': 'float',
                'python_description': 'Is the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to **scaled_min**.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'prescaledMax',
                'python_data_type': 'float',
                'python_description': 'Is the largest value in the range of pre-scaled values. NI-DAQmx maps this value to **scaled_max**.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'scaledMin',
                'python_data_type': 'float',
                'python_description': 'Is the smallest value in the range of scaled values. NI-DAQmx maps this value to **prescaled_min**. Read operations clip samples that are smaller than this value. Write operations generate errors for samples that are smaller than this value.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'scaledMax',
                'python_data_type': 'float',
                'python_description': 'Is the largest value in the range of scaled values. NI-DAQmx maps this value to **prescaled_max**. Read operations clip samples that are larger than this value. Write operations generate errors for samples that are larger than this value.',
                'python_type_annotation': 'float',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'UnitsPreScaled',
                'is_optional_in_python': True,
                'name': 'preScaledUnits',
                'python_data_type': 'UnitsPreScaled',
                'python_default_value': 'UnitsPreScaled.VOLTS',
                'python_description': 'Is the units of the values to scale.',
                'python_type_annotation': 'Optional[nidaqmx.constants.UnitsPreScaled]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'scaledUnits',
                'python_data_type': 'str',
                'python_default_value': None,
                'python_description': 'Is the units to use for the scaled value. You can use an arbitrary string. NI-DAQmx uses the units to label a graph or chart.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'Scale',
        'python_description': 'Creates a custom scale that scales values proportionally from a range of pre-scaled values to a range of scaled values.',
        'returns': 'int32'
    },
    'CreatePolynomialScale': {
        'calling_convention': 'StdCall',
        'is_python_factory': True,
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'name',
                'python_data_type': 'str',
                'python_description': 'Identifies the custom scale for later use, such as with the DAQmx Create Virtual Channel VI',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': False,
                'name': 'forwardCoeffs',
                'python_data_type': 'float',
                'python_description': 'Is an list of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the list corresponds to a term of the equation.',
                'python_type_annotation': 'List[float]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numForwardCoeffsIn'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numForwardCoeffsIn',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': False,
                'name': 'reverseCoeffs',
                'python_data_type': 'float',
                'python_description': 'Is an list of coefficients for the polynomial that converts scaled values to pre-scaled values. Each element of the list corresponds to a term of the equation.',
                'python_type_annotation': 'List[float]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numReverseCoeffsIn'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numReverseCoeffsIn',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'UnitsPreScaled',
                'is_optional_in_python': True,
                'name': 'preScaledUnits',
                'python_data_type': 'UnitsPreScaled',
                'python_default_value': 'UnitsPreScaled.VOLTS',
                'python_description': 'Is the units of the values to scale.',
                'python_type_annotation': 'Optional[nidaqmx.constants.UnitsPreScaled]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'scaledUnits',
                'python_data_type': 'str',
                'python_default_value': None,
                'python_description': 'Is the units to use for the scaled value. You can use an arbitrary string. NI-DAQmx uses the units to label a graph or chart.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'Scale',
        'python_description': 'Creates a custom scale that uses an nth order polynomial equation. NI-DAQmx requires both a polynomial to convert pre-scaled values to scaled values (forward) and a polynomial to convert scaled values to pre-scaled values (reverse). If you only know one set of coefficients, use the DAQmx Compute Reverse Polynomial Coefficients function to generate the other set.',
        'returns': 'int32'
    },
    'CreateTEDSAIAccelChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-5.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '5.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AccelUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'AccelUnits',
                'python_default_value': 'AccelUnits.G',
                'python_description': 'Specifies the units to use to return acceleration measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AccelUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.004',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an accelerometer to measure acceleration. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIBridgeChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.002',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.002',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TEDSUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TEDSUnits',
                'python_default_value': 'TEDSUnits.FROM_TEDS',
                'python_description': 'Specifies in which unit to return measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TEDSUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that measure a Wheatstone bridge. You must configure the physical channel(s) with TEDS information to use this function. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support.',
        'returns': 'int32'
    },
    'CreateTEDSAICurrentChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.01',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.01',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TEDSUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TEDSUnits',
                'python_default_value': 'TEDSUnits.FROM_TEDS',
                'python_description': 'Specifies the units to use to return measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TEDSUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CurrentShuntResistorLocationWithDefault',
                'is_optional_in_python': True,
                'name': 'shuntResistorLoc',
                'python_data_type': 'CurrentShuntResistorLocation',
                'python_default_value': 'CurrentShuntResistorLocation.LET_DRIVER_CHOOSE',
                'python_description': 'Specifies the location of the shunt resistor. For devices with built-in shunt resistors, specify the location as **INTERNAL**. For devices that do not have built-in shunt resistors, you must attach an external one, set this input to **EXTERNAL** and use the **ext_shunt_resistor_val** input to specify the value of the resistor.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CurrentShuntResistorLocation]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'extShuntResistorVal',
                'python_data_type': 'float',
                'python_default_value': '249.0',
                'python_description': 'Specifies in ohms the resistance of an external shunt resistor.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure current. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIForceBridgeChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ForceUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'ForceUnits',
                'python_default_value': 'ForceUnits.POUNDS',
                'python_description': 'Specifies in which unit to return force measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ForceUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure force or load. You must configure the physical channel(s) with TEDS information to use this function. NI-DAQmx scales electrical values to physical values according to that TEDS information.',
        'returns': 'int32'
    },
    'CreateTEDSAIForceIEPEChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-2000.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '2000.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ForceIEPEUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'ForceUnits',
                'python_default_value': 'ForceUnits.NEWTONS',
                'python_description': 'Specifies in which unit to return force measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ForceUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an IEPE force sensor to measure force or load. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIMicrophoneChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. You must use physical channels that you configured with TEDS information. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'SoundPressureUnits1',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'SoundPressureUnits',
                'python_default_value': 'SoundPressureUnits.PA',
                'python_description': 'Specifies the units to use to return sound pressure measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.SoundPressureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxSndPressLevel',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Is the maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.004',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a microphone to measure sound pressure. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIPosLVDTChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.1',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.1',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'LengthUnits2',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'LengthUnits',
                'python_default_value': 'LengthUnits.METERS',
                'python_description': 'Specifies the units to use to return linear position measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.LengthUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '1.0',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitFreq',
                'python_data_type': 'float',
                'python_default_value': '2500.0',
                'python_description': 'Specifies in hertz the excitation frequency that the sensor requires. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ACExcitWireMode',
                'is_optional_in_python': True,
                'name': 'acExcitWireMode',
                'python_data_type': 'ACExcitWireMode',
                'python_default_value': 'ACExcitWireMode.FOUR_WIRE',
                'python_description': 'Is the number of leads on the sensor. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ACExcitWireMode]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an LVDT to measure linear position. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIPosRVDTChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-70.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '70.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'AngleUnits1',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'AngleUnits',
                'python_default_value': 'AngleUnits.DEGREES',
                'python_description': 'Specifies the units to use to return angular position measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.AngleUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '1.0',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitFreq',
                'python_data_type': 'float',
                'python_default_value': '2500.0',
                'python_description': 'Specifies in hertz the excitation frequency that the sensor requires. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ACExcitWireMode',
                'is_optional_in_python': True,
                'name': 'acExcitWireMode',
                'python_data_type': 'ACExcitWireMode',
                'python_default_value': 'ACExcitWireMode.FOUR_WIRE',
                'python_description': 'Is the number of leads on the sensor. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ACExcitWireMode]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an RVDT to measure angular position. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIPressureBridgeChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'PressureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'PressureUnits',
                'python_default_value': 'PressureUnits.POUNDS_PER_SQ_INCH',
                'python_description': 'Specifies in which unit to return pressure measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.PressureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure pressure. You must configure the physical channel(s) with TEDS information to use this function. NI-DAQmx scales electrical values to physical values according to that TEDS information.',
        'returns': 'int32'
    },
    'CreateTEDSAIRTDChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TemperatureUnits',
                'python_default_value': 'TemperatureUnits.DEG_C',
                'python_description': 'Specifies the units to use to return temperature measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TemperatureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'is_optional_in_python': True,
                'name': 'resistanceConfig',
                'python_data_type': 'ResistanceConfiguration',
                'python_default_value': 'ResistanceConfiguration.TWO_WIRE',
                'python_description': 'Specifies the number of wires to use for resistive measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ResistanceConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.EXTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.0025',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use an RTD to measure temperature. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIResistanceChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '1000.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TEDSUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TEDSUnits',
                'python_default_value': 'TEDSUnits.FROM_TEDS',
                'python_description': 'Specifies the units to use to return measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TEDSUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'is_optional_in_python': True,
                'name': 'resistanceConfig',
                'python_data_type': 'ResistanceConfiguration',
                'python_default_value': 'ResistanceConfiguration.TWO_WIRE',
                'python_description': 'Specifies the number of wires to use for resistive measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ResistanceConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.EXTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure resistance. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIStrainGageChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-0.001',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '0.001',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'StrainUnits1',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'StrainUnits',
                'python_default_value': 'StrainUnits.STRAIN',
                'python_description': 'Specifies the units to use to return strain measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.StrainUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'initialBridgeVoltage',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'leadWireResistance',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies information about the bridge configuration and measurement.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure strain. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIThrmcplChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TemperatureUnits',
                'python_default_value': 'TemperatureUnits.DEG_C',
                'python_description': 'Specifies the units to use to return temperature measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TemperatureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'CJCSource1',
                'is_optional_in_python': True,
                'name': 'cjcSource',
                'python_data_type': 'CJCSource',
                'python_default_value': 'CJCSource.CONSTANT_USER_VALUE',
                'python_description': 'Specifies the source of cold-junction compensation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.CJCSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'cjcVal',
                'python_data_type': 'float',
                'python_default_value': '25.0',
                'python_description': 'Specifies in **units** the temperature of the cold junction if you set **cjc_source** to **CONSTANT_VALUE**.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'cjcChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the channel that acquires the temperature of the thermocouple cold-junction if you set **cjc_source** to **CHANNEL**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a thermocouple to measure temperature. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIThrmstrChanIex': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TemperatureUnits',
                'python_default_value': 'TemperatureUnits.DEG_C',
                'python_description': 'Specifies the units to use to return temperature measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TemperatureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'is_optional_in_python': True,
                'name': 'resistanceConfig',
                'python_data_type': 'ResistanceConfiguration',
                'python_default_value': 'ResistanceConfiguration.FOUR_WIRE',
                'python_description': 'Specifies the number of wires to use for resistive measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ResistanceConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'currentExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.EXTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'currentExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.00015',
                'python_description': 'Specifies in amperes the amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a thermistor to measure temperature. Use this instance when the thermistor requires current excitation. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIThrmstrChanVex': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TemperatureUnits',
                'python_default_value': 'TemperatureUnits.DEG_C',
                'python_description': 'Specifies the units to use to return temperature measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TemperatureUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'is_optional_in_python': True,
                'name': 'resistanceConfig',
                'python_data_type': 'ResistanceConfiguration',
                'python_default_value': 'ResistanceConfiguration.FOUR_WIRE',
                'python_description': 'Specifies the number of wires to use for resistive measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ResistanceConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.EXTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'r1',
                'python_data_type': 'float',
                'python_default_value': '5000.0',
                'python_description': 'Specifies in ohms the value of the reference resistor.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a thermistor to measure temperature. Use this instance when the thermistor requires voltage excitation. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTEDSAITorqueBridgeChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-100.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '100.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TorqueUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TorqueUnits',
                'python_default_value': 'TorqueUnits.INCH_POUNDS',
                'python_description': 'Specifies in which unit to return torque measurements from the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TorqueUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '2.5',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) that use a Wheatstone bridge to measure torque. You must configure the physical channel(s) with TEDS information to use this function. NI-DAQmx scales electrical values to physical values according to that TEDS information.',
        'returns': 'int32'
    },
    'CreateTEDSAIVoltageChan': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-5.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '5.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TEDSUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TEDSUnits',
                'python_default_value': 'TEDSUnits.FROM_TEDS',
                'python_description': 'Specifies the units to use to return measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TEDSUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure voltage. You must configure the physical channel(s) with TEDS information to use this function. If the measurement requires the use of internal excitation or you need excitation to scale the voltage, use the TEDS AI Custom Voltage with Excitation instance of this function.',
        'returns': 'int32'
    },
    'CreateTEDSAIVoltageChanWithExcit': {
        'adaptor_parameter': {
            'description': 'Indicates the newly created channel object.',
            'direction': 'output',
            'python_adaptor': 'self._create_chan(physical_channel, name_to_assign_to_channel)',
            'python_data_type': 'nidaqmx._task_modules.channels.ai_channel.AIChannel'
        },
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': 'Specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'nameToAssignToChannel',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies a name to assign to the virtual channel this function creates. If you do not specify a value for this input, NI-DAQmx uses the physical channel name as the virtual channel name.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'is_optional_in_python': True,
                'name': 'terminalConfig',
                'python_data_type': 'TerminalConfiguration',
                'python_default_value': 'TerminalConfiguration.DEFAULT',
                'python_description': 'Specifies the input terminal configuration for the channel.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TerminalConfiguration]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'minVal',
                'python_data_type': 'float',
                'python_default_value': '-10.0',
                'python_description': 'Specifies in **units** the minimum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'maxVal',
                'python_data_type': 'float',
                'python_default_value': '10.0',
                'python_description': 'Specifies in **units** the maximum value you expect to measure.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'TEDSUnits',
                'is_optional_in_python': True,
                'name': 'units',
                'python_data_type': 'TEDSUnits',
                'python_default_value': 'TEDSUnits.FROM_TEDS',
                'python_description': 'Specifies the units to use to return measurements.',
                'python_type_annotation': 'Optional[nidaqmx.constants.TEDSUnits]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'ExcitationSource',
                'is_optional_in_python': True,
                'name': 'voltageExcitSource',
                'python_data_type': 'ExcitationSource',
                'python_default_value': 'ExcitationSource.INTERNAL',
                'python_description': 'Specifies the source of excitation.',
                'python_type_annotation': 'Optional[nidaqmx.constants.ExcitationSource]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'voltageExcitVal',
                'python_data_type': 'float',
                'python_default_value': '0.0',
                'python_description': 'Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'customScaleName',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the name of a custom scale for the channel. If you want the channel to use a custom scale, specify the name of the custom scale to this input and set **units** to **FROM_CUSTOM_SCALE**.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'AIChannelCollection',
        'python_description': 'Creates channel(s) to measure voltage. Use this instance for custom sensors that require excitation. You can use the excitation to scale the measurement. You must configure the physical channel(s) with TEDS information to use this function.',
        'returns': 'int32'
    },
    'CreateTableScale': {
        'calling_convention': 'StdCall',
        'is_python_factory': True,
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'name',
                'python_data_type': 'str',
                'python_description': 'Identifies the custom scale for later use, such as with the DAQmx Create Virtual Channel VI',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': False,
                'name': 'prescaledVals',
                'python_data_type': 'float',
                'python_description': 'Is the list of pre-scaled values that map to the values in **scaled_vals**.',
                'python_type_annotation': 'List[float]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numPrescaledValsIn'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numPrescaledValsIn',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'numpy.float64',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': False,
                'name': 'scaledVals',
                'python_data_type': 'float',
                'python_description': 'Is the list of scaled values that map to the values in **prescaled_vals**.',
                'python_type_annotation': 'List[float]',
                'size': {
                    'mechanism': 'len',
                    'value': 'numScaledValsIn'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'numScaledValsIn',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'UnitsPreScaled',
                'is_optional_in_python': True,
                'name': 'preScaledUnits',
                'python_data_type': 'UnitsPreScaled',
                'python_default_value': 'UnitsPreScaled.VOLTS',
                'python_description': 'Is the units of the values to scale.',
                'python_type_annotation': 'Optional[nidaqmx.constants.UnitsPreScaled]',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'scaledUnits',
                'python_data_type': 'str',
                'python_default_value': None,
                'python_description': 'Is the units to use for the scaled value. You can use an arbitrary string. NI-DAQmx uses the units to label a graph or chart.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'Scale',
        'python_description': 'Creates a custom scale that maps an list of pre-scaled values to an list of corresponding scaled values. NI-DAQmx applies linear interpolation to values that fall between the values in the table. Read operations clip scaled samples that are outside the maximum and minimum scaled values found in the table. Write operations generate errors for samples that are outside the minimum and maximum scaled values found in the table.',
        'returns': 'int32'
    },
    'CreateTask': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'init_method': True,
        'is_python_factory': True,
        'parameters': [
            {
                'direction': 'in',
                'is_session_name': True,
                'name': 'sessionName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'python_description': 'Creates a task and adds virtual channels to that task if you specify them in the **globalvirtualchannels** input. If you specify a **tasktocopy**, this function duplicates the configuration of the specified task in the newly created task before it adds any additional global virtual channels.',
        'returns': 'int32'
    },
    'CreateWatchdogTimerTask': {
        'calling_convention': 'Cdecl',
        'codegen_method': 'grpc-only',
        'init_method': True,
        'is_python_factory': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'is_session_name': True,
                'name': 'sessionName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'lines',
                'repeating_argument': True,
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'DigitalLineState',
                'include_in_proto': False,
                'name': 'expState',
                'repeating_argument': True,
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated WatchdogExpChannelsAndState',
                'is_compound_type': True,
                'max_length': 96,
                'name': 'expStates',
                'repeated_var_args': True
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'python_description': "Creates and configures a task that controls the watchdog timer of a device. The timer activates when you start the task. Use the digital physical channel expiration states input to set expiration states for digital channels. If your device supports expiration states for other channel types, use the DAQmx Configure Watchdog Expiration States to configure those channels' expiration states. This function does not program the watchdog timer on a real-time controller. Use the Real-Time Watchdog VIs to program the watchdog timer on a real-time controller.",
        'returns': 'int32'
    },
    'CreateWatchdogTimerTaskEx': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'is_session_name': True,
                'name': 'sessionName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'int32'
    },
    'DeleteNetworkDevice': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            }
        ],
        'python_description': 'Deletes a Network DAQ device previously added to the host. If the device is reserved, it is unreserved before it is removed.',
        'returns': 'int32'
    },
    'DeleteSavedGlobalChan': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'const char[]'
            }
        ],
        'python_description': 'Deletes the specified global channel from MAX. This function does not remove the global channel from tasks that use it.',
        'returns': 'int32'
    },
    'DeleteSavedScale': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            }
        ],
        'python_description': 'Deletes the specified custom scale from MAX. This function does not remove the custom scale from virtual channels that use it.',
        'returns': 'int32'
    },
    'DeleteSavedTask': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'taskName',
                'type': 'const char[]'
            }
        ],
        'python_description': 'Deletes the specified task from MAX. This function does not clear the copy of the task stored in memory. Use the DAQmx Clear Task function to clear that copy of the task.',
        'returns': 'int32'
    },
    'DeviceSupportsCal': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'calSupported',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'DisableRefTrig': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            }
        ],
        'python_class_name': 'ReferenceTrigger',
        'python_description': 'Disables reference triggering for the measurement.',
        'returns': 'int32'
    },
    'DisableStartTrig': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            }
        ],
        'python_class_name': 'StartTrigger',
        'python_description': 'Configures the task to start acquiring or generating samples immediately upon starting the task.',
        'returns': 'int32'
    },
    'DisconnectTerms': {
        'calling_convention': 'StdCall',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'sourceTerminal',
                'python_data_type': 'str',
                'python_description': 'Specifies the originating terminal of the route. A DAQmx terminal constant lists all terminals available on devices installed in the system. You also can specify a source terminal by specifying a string that contains a terminal name.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'destinationTerminal',
                'python_data_type': 'str',
                'python_description': 'Specifies the receiving terminal of the route. A DAQmx terminal constant provides a list of all terminals available on devices installed in the system. You also can specify a destination terminal by specifying a string that contains a terminal name.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'System',
        'python_description': 'Removes signal routes you created by using the DAQmx Connect Terminals function. The DAQmx Disconnect Terminals function cannot remove task-based routes, such as those you create through timing and triggering configuration.',
        'returns': 'int32'
    },
    'ExportSignal': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'lib_importer.task_handle',
            'cvi_name': 'taskHandle',
            'python_accessor': 'self._handle'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'Signal',
                'is_optional_in_python': False,
                'name': 'signalID',
                'python_data_type': 'Signal',
                'python_description': 'Is the name of the trigger, clock, or event to export.',
                'python_type_annotation': 'nidaqmx.constants.Signal',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'outputTerminal',
                'python_data_type': 'str',
                'python_description': 'Is the destination of the exported signal. A DAQmx terminal constant lists all terminals on installed devices. You can also specify a string containing a comma-delimited list of terminal names.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'ExportSignals',
        'python_description': 'Routes a control signal to the terminal you specify. The output terminal can reside on the device that generates the control signal or on a different device. You can use this function to share clocks and triggers among multiple tasks and devices. The routes this function creates are task-based routes.',
        'returns': 'int32'
    },
    'GetAIChanCalCalDate': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'year',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'month',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'day',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'hour',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'minute',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetAIChanCalExpDate': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'year',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'month',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'day',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'hour',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'minute',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetAnalogPowerUpStates': {
        'calling_convention': 'Cdecl',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'channelName',
                'repeating_argument': True,
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'state',
                'repeating_argument': True,
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'PowerUpChannelType',
                'include_in_proto': False,
                'name': 'channelType',
                'repeating_argument': True,
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated AnalogPowerUpChannelAndType',
                'is_compound_type': True,
                'max_length': 96,
                'name': 'channels',
                'repeated_var_args': True
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated double',
                'max_length': 96,
                'name': 'powerUpStates',
                'repeated_var_args': True
            }
        ],
        'returns': 'int32'
    },
    'GetAnalogPowerUpStatesWithOutputType': {
        'calling_convention': 'Cdecl',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'stateArray',
                'size': {
                    'mechanism': 'passed-in-by-ptr',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'enum': 'PowerUpChannelType',
                'name': 'channelTypeArray',
                'size': {
                    'mechanism': 'passed-in-by-ptr',
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        ],
        'python_description': 'Gets the power up states for analog physical channels.',
        'returns': 'int32'
    },
    'GetArmStartTrigTimestampVal': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'GetArmStartTrigTrigWhen': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'GetAutoConfiguredCDAQSyncConnections': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'out',
                'name': 'portList',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'portListSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'portListSize',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetBufferAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetBufferAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'BufferAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetCalInfoAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetCalInfoAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'CalibrationInfoAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetCalInfoAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetCalInfoAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'CalibrationInfoAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetCalInfoAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetCalInfoAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'CalibrationInfoAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetCalInfoAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetCalInfoAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'CalibrationInfoAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetChanAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetChanAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetChanAttributeDoubleArray': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetChanAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetChanAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetChanAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetDeviceAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetDeviceAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'DeviceAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetDeviceAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetDeviceAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'DeviceAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetDeviceAttributeDoubleArray': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetDeviceAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'DeviceAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetDeviceAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetDeviceAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'DeviceAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetDeviceAttributeInt32Array': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetDeviceAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'DeviceAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetDeviceAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetDeviceAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'DeviceAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetDeviceAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetDeviceAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'DeviceAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetDeviceAttributeUInt32Array': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetDeviceAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'DeviceAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetDigitalLogicFamilyPowerUpState': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'logicFamily',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetDigitalPowerUpStates': {
        'calling_convention': 'Cdecl',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'channelName',
                'repeating_argument': True,
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'enum': 'PowerUpStates',
                'include_in_proto': False,
                'name': 'state',
                'repeating_argument': True,
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated string',
                'max_length': 96,
                'name': 'channelName',
                'repeated_var_args': True
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated PowerUpStates',
                'max_length': 96,
                'name': 'powerUpStates',
                'repeated_var_args': True
            }
        ],
        'returns': 'int32'
    },
    'GetDigitalPullUpPullDownStates': {
        'calling_convention': 'Cdecl',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'channelName',
                'repeating_argument': True,
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'enum': 'ResistorState',
                'include_in_proto': False,
                'name': 'state',
                'repeating_argument': True,
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated string',
                'max_length': 96,
                'name': 'channelName',
                'repeated_var_args': True
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated ResistorState',
                'max_length': 96,
                'name': 'pullUpPullDownStates',
                'repeated_var_args': True
            }
        ],
        'returns': 'int32'
    },
    'GetDisconnectedCDAQSyncPorts': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'out',
                'name': 'portList',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'portListSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'portListSize',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetErrorString': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'errorString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetExportedSignalAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetExportedSignalAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetExportedSignalAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetExportedSignalAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetExportedSignalAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetExportedSignalAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetExportedSignalAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetExportedSignalAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetExportedSignalAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetExportedSignalAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetExtendedErrorInfo': {
        'calling_convention': 'StdCall',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'out',
                'name': 'errorString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetFirstSampClkWhen': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'GetFirstSampTimestampVal': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'GetNthTaskChannel': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'index',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'buffer',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetNthTaskDevice': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'index',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'buffer',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetNthTaskReadChannel': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'index',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'buffer',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetPersistedChanAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPersistedChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PersistedChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPersistedChanAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPersistedChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PersistedChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPersistedScaleAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPersistedScaleAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PersistedScaleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPersistedScaleAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPersistedScaleAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PersistedScaleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPersistedTaskAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPersistedTaskAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'taskName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PersistedTaskAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPersistedTaskAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPersistedTaskAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'taskName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PersistedTaskAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPhysicalChanAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPhysicalChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PhysicalChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPhysicalChanAttributeBytes': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPhysicalChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PhysicalChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'uInt8[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPhysicalChanAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPhysicalChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PhysicalChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPhysicalChanAttributeDoubleArray': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPhysicalChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PhysicalChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPhysicalChanAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPhysicalChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PhysicalChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPhysicalChanAttributeInt32Array': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPhysicalChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PhysicalChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPhysicalChanAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPhysicalChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PhysicalChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPhysicalChanAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPhysicalChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PhysicalChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPhysicalChanAttributeUInt32Array': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetPhysicalChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'PhysicalChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetReadAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetReadAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetReadAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetReadAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetReadAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetReadAttributeUInt64': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetRealTimeAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetRealTimeAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'RealTimeAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetRealTimeAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetRealTimeAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'RealTimeAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetRealTimeAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetRealTimeAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'RealTimeAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetRefTrigTimestampVal': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'GetScaleAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetScaleAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ScaleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetScaleAttributeDoubleArray': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetScaleAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ScaleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetScaleAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetScaleAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ScaleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetScaleAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetScaleAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ScaleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetSelfCalLastDateAndTime': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'year',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'month',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'day',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'hour',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'minute',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetStartTrigTimestampVal': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'GetStartTrigTrigWhen': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'GetSyncPulseTimeWhen': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'GetSystemInfoAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetSystemInfoAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'grpc_type': 'SystemAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetSystemInfoAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetSystemInfoAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'grpc_type': 'SystemAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTaskAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTaskAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TaskAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTaskAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTaskAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TaskAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTaskAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTaskAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TaskAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeExBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeExDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeExInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeExString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeExTimestamp': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'CVIAbsoluteTime'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeExUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeExUInt64': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeTimestamp': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'CVIAbsoluteTime'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTimingAttributeUInt64': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTrigAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTrigAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTrigAttributeDoubleArray': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTrigAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTrigAttributeInt32Array': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTrigAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTrigAttributeTimestamp': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'CVIAbsoluteTime'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetTrigAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetWatchdogAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetWatchdogAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'lines',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'WatchdogAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetWatchdogAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetWatchdogAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'lines',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'WatchdogAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetWatchdogAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetWatchdogAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'lines',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'WatchdogAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetWatchdogAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetWatchdogAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'lines',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'WatchdogAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetWriteAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetWriteAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetWriteAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetWriteAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetWriteAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetWriteAttributeUInt64': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxGetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'IsTaskDone': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'isTaskDone',
                'type': 'bool32'
            }
        ],
        'python_description': 'Queries the status of the task and indicates if it completed execution. Use this function to ensure that the specified operation is complete before you stop the task.',
        'returns': 'int32'
    },
    'LoadTask': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'is_session_name': True,
                'name': 'sessionName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'int32'
    },
    'ReadAnalogF64': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadAnalogScalarF64': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadBinaryI16': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'int16[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadBinaryI32': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadBinaryU16': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'uInt16[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadBinaryU32': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCounterF64': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCounterF64Ex': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCounterScalarF64': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCounterScalarU32': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCounterU32': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCounterU32Ex': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCtrFreq': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'interleaved',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'readArrayFrequency',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'readArrayDutyCycle',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCtrFreqScalar': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'frequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dutyCycle',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCtrTicks': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'interleaved',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'readArrayHighTicks',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'out',
                'name': 'readArrayLowTicks',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCtrTicksScalar': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'highTicks',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'lowTicks',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCtrTime': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'interleaved',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'readArrayHighTime',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'readArrayLowTime',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadCtrTimeScalar': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'highTime',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'lowTime',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadDigitalLines': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInBytes'
                },
                'type': 'uInt8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInBytes',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'numBytesPerSamp',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadDigitalScalarU32': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadDigitalU16': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'uInt16[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadDigitalU32': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadDigitalU8': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'uInt8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadPowerBinaryI16': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'out',
                'name': 'readArrayVoltage',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'int16[]'
            },
            {
                'coerced': True,
                'direction': 'out',
                'name': 'readArrayCurrent',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'int16[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadPowerF64': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'fillMode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'readArrayVoltage',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'readArrayCurrent',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInSamps'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInSamps',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanRead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadPowerScalarF64': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'voltage',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'current',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ReadRaw': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'is_list': True,
                'name': 'readArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySizeInBytes'
                },
                'type': 'uInt8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInBytes',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'sampsRead',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'numBytesPerSamp',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'RegisterDoneEvent': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'options',
                'type': 'uInt32'
            },
            {
                'callback_params': [
                    {
                        'direction': 'out',
                        'include_in_proto': False,
                        'name': 'task',
                        'type': 'TaskHandle'
                    },
                    {
                        'direction': 'out',
                        'name': 'status',
                        'type': 'int32'
                    }
                ],
                'direction': 'in',
                'include_in_proto': False,
                'name': 'callbackFunction',
                'type': 'DAQmxDoneEventCallbackPtr'
            },
            {
                'callback_token': True,
                'direction': 'in',
                'include_in_proto': False,
                'name': 'callbackData',
                'pointer': True,
                'type': 'void'
            }
        ],
        'returns': 'int32',
        'stream_response': True
    },
    'RegisterEveryNSamplesEvent': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'enum': 'EveryNSamplesEventType',
                'name': 'everyNSamplesEventType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'nSamples',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'options',
                'type': 'uInt32'
            },
            {
                'callback_params': [
                    {
                        'direction': 'out',
                        'include_in_proto': False,
                        'name': 'task',
                        'type': 'TaskHandle'
                    },
                    {
                        'direction': 'out',
                        'enum': 'EveryNSamplesEventType',
                        'name': 'everyNSamplesEventType',
                        'type': 'int32'
                    },
                    {
                        'direction': 'out',
                        'name': 'nSamples',
                        'type': 'uInt32'
                    }
                ],
                'direction': 'in',
                'include_in_proto': False,
                'name': 'callbackFunction',
                'type': 'DAQmxEveryNSamplesEventCallbackPtr'
            },
            {
                'callback_token': True,
                'direction': 'in',
                'include_in_proto': False,
                'name': 'callbackData',
                'pointer': True,
                'type': 'void'
            }
        ],
        'returns': 'int32',
        'stream_response': True
    },
    'RegisterSignalEvent': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'enum': 'Signal2',
                'name': 'signalID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'options',
                'type': 'uInt32'
            },
            {
                'callback_params': [
                    {
                        'direction': 'out',
                        'include_in_proto': False,
                        'name': 'task',
                        'type': 'TaskHandle'
                    },
                    {
                        'direction': 'out',
                        'name': 'signalID',
                        'type': 'int32'
                    }
                ],
                'direction': 'in',
                'include_in_proto': False,
                'name': 'callbackFunction',
                'type': 'DAQmxSignalEventCallbackPtr'
            },
            {
                'callback_token': True,
                'direction': 'in',
                'include_in_proto': False,
                'name': 'callbackData',
                'pointer': True,
                'type': 'void'
            }
        ],
        'returns': 'int32',
        'stream_response': True
    },
    'RemoveCDAQSyncConnection': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'portList',
                'type': 'const char[]'
            }
        ],
        'python_description': 'Removes a cDAQ Sync connection between devices. The connection is not verified.',
        'returns': 'int32'
    },
    'ReserveNetworkDevice': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'overrideReservation',
                'type': 'bool32'
            }
        ],
        'python_description': 'Reserves the Network DAQ device for the current host. Reservation is required to run NI-DAQmx tasks, and the device must be added in MAX before it can be reserved.',
        'returns': 'int32'
    },
    'ResetBufferAttribute': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'BufferAttribute',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetChanAttribute': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetDevice': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'ctypes.c_char_p',
            'cvi_name': 'deviceName',
            'python_accessor': 'self._name'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'deviceName',
                'python_data_type': 'str',
                'python_description': '',
                'python_type_annotation': 'str',
                'type': 'const char[]',
                'use_in_python_api': False
            }
        ],
        'python_class_name': 'Device',
        'python_description': 'Immediately aborts all active tasks associated with a device, disconnects any routes, and returns the device to an initialized state. Aborting a task immediately terminates the currently active operation, such as a read or a write. Aborting a task puts the task into an unstable but recoverable state. To recover the task, use DAQmx Start to restart the task or use DAQmx Stop to reset the task without starting it.',
        'returns': 'int32'
    },
    'ResetExportedSignalAttribute': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'is_optional_in_python': False,
                'name': 'attribute',
                'python_data_type': 'int',
                'python_description': '',
                'python_type_annotation': 'int',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetReadAttribute': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetRealTimeAttribute': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'RealTimeAttribute',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetTimingAttribute': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'is_optional_in_python': False,
                'name': 'attribute',
                'python_data_type': 'int',
                'python_description': '',
                'python_type_annotation': 'int',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetTimingAttributeEx': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'deviceNames',
                'python_data_type': 'str',
                'python_description': '',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'is_optional_in_python': False,
                'name': 'attribute',
                'python_data_type': 'int',
                'python_description': '',
                'python_type_annotation': 'int',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetTrigAttribute': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'is_optional_in_python': False,
                'name': 'attribute',
                'python_data_type': 'int',
                'python_description': '',
                'python_type_annotation': 'int',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetWatchdogAttribute': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'lines',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'WatchdogAttribute',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetWriteAttribute': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SaveGlobalChan': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'saveAs',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'author',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'SaveOptions',
                'name': 'options',
                'type': 'uInt32'
            }
        ],
        'python_description': 'Saves the specified local or global channel to MAX as a global channel. You must specify both the local or global channel to save and a task that contains that channel.',
        'returns': 'int32'
    },
    'SaveScale': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'saveAs',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'author',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'SaveOptions',
                'name': 'options',
                'type': 'uInt32'
            }
        ],
        'python_description': 'Saves the specified custom scale to MAX.',
        'returns': 'int32'
    },
    'SaveTask': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'saveAs',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'author',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'SaveOptions',
                'name': 'options',
                'type': 'uInt32'
            }
        ],
        'python_description': 'Saves the specified task and any  local channels it contains to MAX. This function does not save global channels. Use the DAQmx Save Global Channel function to save global channels.',
        'returns': 'int32'
    },
    'SelfCal': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'SelfTestDevice': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'ctypes.c_char_p',
            'cvi_name': 'deviceName',
            'python_accessor': 'self._name'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'deviceName',
                'python_data_type': 'str',
                'python_description': '',
                'python_type_annotation': 'str',
                'type': 'const char[]',
                'use_in_python_api': False
            }
        ],
        'python_class_name': 'Device',
        'python_description': 'Performs a brief test of device resources. If a failure occurs, refer to your device documentation for more information.',
        'returns': 'int32'
    },
    'SetAIChanCalCalDate': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'year',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'month',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'day',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'hour',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'minute',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetAIChanCalExpDate': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'year',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'month',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'day',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'hour',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'minute',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetAnalogPowerUpStates': {
        'calling_convention': 'Cdecl',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'channelNames',
                'repeating_argument': True,
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'state',
                'repeating_argument': True,
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'PowerUpChannelType',
                'include_in_proto': False,
                'name': 'channelType',
                'repeating_argument': True,
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated AnalogPowerUpChannelsAndState',
                'is_compound_type': True,
                'max_length': 96,
                'name': 'powerUpStates',
                'repeated_var_args': True
            }
        ],
        'returns': 'int32'
    },
    'SetAnalogPowerUpStatesWithOutputType': {
        'calling_convention': 'Cdecl',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'stateArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'enum': 'PowerUpChannelType',
                'name': 'channelTypeArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        ],
        'python_description': 'Updates power up states for analog physical channels.',
        'returns': 'int32'
    },
    'SetArmStartTrigTrigWhen': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'SetBufferAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetBufferAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'BufferAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetCalInfoAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetCalInfoAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'CalibrationInfoAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetCalInfoAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetCalInfoAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'CalibrationInfoAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetCalInfoAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetCalInfoAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'CalibrationInfoAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetCalInfoAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetCalInfoAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'CalibrationInfoAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetChanAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetChanAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetChanAttributeDoubleArray': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetChanAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetChanAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetChanAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetChanAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ChannelAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetDigitalLogicFamilyPowerUpState': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'LogicFamily',
                'name': 'logicFamily',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetDigitalPowerUpStates': {
        'calling_convention': 'Cdecl',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'channelNames',
                'repeating_argument': True,
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'PowerUpStates',
                'include_in_proto': False,
                'name': 'state',
                'repeating_argument': True,
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated DigitalPowerUpChannelsAndState',
                'is_compound_type': True,
                'max_length': 96,
                'name': 'powerUpStates',
                'repeated_var_args': True
            }
        ],
        'returns': 'int32'
    },
    'SetDigitalPullUpPullDownStates': {
        'calling_convention': 'Cdecl',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'channelNames',
                'repeating_argument': True,
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'ResistorState',
                'include_in_proto': False,
                'name': 'state',
                'repeating_argument': True,
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated DigitalPullUpPullDownChannelsAndState',
                'is_compound_type': True,
                'max_length': 96,
                'name': 'pullUpPullDownStates',
                'repeated_var_args': True
            }
        ],
        'returns': 'int32'
    },
    'SetExportedSignalAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetExportedSignalAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetExportedSignalAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetExportedSignalAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetExportedSignalAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetExportedSignalAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetExportedSignalAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetExportedSignalAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetExportedSignalAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetExportedSignalAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ExportSignalAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetFirstSampClkWhen': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'SetReadAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetReadAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetReadAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetReadAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetReadAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetReadAttributeUInt64': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetReadAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'ReadAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetRealTimeAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetRealTimeAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'RealTimeAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetRealTimeAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetRealTimeAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'RealTimeAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetRealTimeAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetRealTimeAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'RealTimeAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetScaleAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetScaleAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ScaleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetScaleAttributeDoubleArray': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetScaleAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ScaleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetScaleAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetScaleAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ScaleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetScaleAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetScaleAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'ScaleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetStartTrigTrigWhen': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'SetSyncPulseTimeWhen': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeExBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeExDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeExInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeExString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeExTimestamp': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'CVIAbsoluteTime'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeExUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeExUInt64': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttributeEx',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeTimestamp': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'CVIAbsoluteTime'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTimingAttributeUInt64': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTimingAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TimingAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTrigAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTrigAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTrigAttributeDoubleArray': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTrigAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTrigAttributeInt32Array': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'const int32[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTrigAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTrigAttributeTimestamp': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'CVIAbsoluteTime'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetTrigAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetTrigAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'TriggerAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetWatchdogAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetWatchdogAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'lines',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'WatchdogAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetWatchdogAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetWatchdogAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'lines',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'WatchdogAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetWatchdogAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetWatchdogAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'lines',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'WatchdogAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetWatchdogAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetWatchdogAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'lines',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'WatchdogAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetWriteAttributeBool': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetWriteAttributeDouble': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetWriteAttributeInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetWriteAttributeString': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetWriteAttributeUInt32': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetWriteAttributeUInt64': {
        'calling_convention': 'Cdecl',
        'cname': 'DAQmxSetWriteAttribute',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'WriteAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt64'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0U',
                'include_in_proto': False,
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'StartNewFile': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'const char[]'
            }
        ],
        'python_description': 'Starts a new TDMS file the next time data is written to disk.',
        'returns': 'int32'
    },
    'StartTask': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            }
        ],
        'python_description': 'Transitions the task to the running state to begin the measurement or generation. Using this function is required for some applications and is optional for others.',
        'returns': 'int32'
    },
    'StopTask': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            }
        ],
        'python_description': 'Stops the task and returns it to the state the task was in before the DAQmx Start Task function ran or the DAQmx Write function ran with the **autostart** input set to True.',
        'returns': 'int32'
    },
    'TaskControl': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'enum': 'TaskControlAction',
                'name': 'action',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TristateOutputTerm': {
        'calling_convention': 'StdCall',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'outputTerminal',
                'python_data_type': 'str',
                'python_description': 'Specifies the terminal on the I/O connector to set to high-impedance state. A DAQmx terminal constant lists all available terminals on installed devices. You also can specify an output terminal by using a string that contains a terminal name.',
                'python_type_annotation': 'str',
                'type': 'const char[]'
            }
        ],
        'python_class_name': 'System',
        'python_description': 'Sets a terminal to high-impedance state. If you connect an external signal to a terminal on the I/O connector, the terminal must be in high-impedance state. Otherwise, the device could double-drive the terminal and damage the hardware. If you use this function on a terminal in an active route, the function fails and returns an error.',
        'returns': 'int32'
    },
    'UnreserveNetworkDevice': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            }
        ],
        'python_description': 'Unreserves or releases a Network DAQ device previously reserved by the host.',
        'returns': 'int32'
    },
    'WaitForNextSampleClock': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'isLate',
                'type': 'bool32'
            }
        ],
        'python_description': 'Waits until the next pulse of the Sample Clock occurs. If an extra Sample Clock pulse occurs between calls to this VI, the second call returns an error or warning and waits for the next Sample Clock pulse. Use the Convert Late Errors to Warnings DAQmx Real-Time property to specify whether this function returns errors or warnings. If that property is True, any warnings this function returns do not include the **source** string.  Use this function to ensure I/O cycles complete within Sample Clock periods. National Instruments recommends you use this function for certain applications only.',
        'returns': 'int32'
    },
    'WaitForValidTimestamp': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'enum': 'TimestampEvent',
                'name': 'timestampEvent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'timestamp',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'python_description': 'DAQmx Wait for Valid Timestamp',
        'returns': 'int32'
    },
    'WaitUntilTaskDone': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'timeToWait',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'WriteAnalogF64': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'is_list': True,
                'name': 'writeArray',
                'type': 'const float64[]'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteAnalogScalarF64': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteBinaryI16': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'in',
                'is_list': True,
                'name': 'writeArray',
                'type': 'const int16[]'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteBinaryI32': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'is_list': True,
                'name': 'writeArray',
                'type': 'const int32[]'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteBinaryU16': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'in',
                'is_list': True,
                'name': 'writeArray',
                'type': 'const uInt16[]'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteBinaryU32': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'is_list': True,
                'name': 'writeArray',
                'type': 'const uInt32[]'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteCtrFreq': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'frequency',
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'dutyCycle',
                'type': 'const float64[]'
            },
            {
                'direction': 'out',
                'name': 'numSampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteCtrFreqScalar': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'frequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dutyCycle',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteCtrTicks': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'highTicks',
                'type': 'const uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'lowTicks',
                'type': 'const uInt32[]'
            },
            {
                'direction': 'out',
                'name': 'numSampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteCtrTicksScalar': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'highTicks',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'lowTicks',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteCtrTime': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'highTime',
                'type': 'const float64[]'
            },
            {
                'direction': 'in',
                'name': 'lowTime',
                'type': 'const float64[]'
            },
            {
                'direction': 'out',
                'name': 'numSampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteCtrTimeScalar': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'highTime',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'lowTime',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteDigitalLines': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'is_list': True,
                'name': 'writeArray',
                'type': 'const uInt8[]'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteDigitalScalarU32': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteDigitalU16': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'in',
                'is_list': True,
                'name': 'writeArray',
                'type': 'const uInt16[]'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteDigitalU32': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'is_list': True,
                'name': 'writeArray',
                'type': 'const uInt32[]'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteDigitalU8': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSampsPerChan',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'GroupBy',
                'name': 'dataLayout',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'is_list': True,
                'name': 'writeArray',
                'type': 'const uInt8[]'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteRaw': {
        'calling_convention': 'StdCall',
        'codegen_method': 'grpc-only',
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'numSamps',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'autoStart',
                'type': 'bool32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'const uInt8[]'
            },
            {
                'direction': 'out',
                'name': 'sampsPerChanWritten',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'WriteToTEDSFromArray': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'ctypes.c_char_p',
            'cvi_name': 'physicalChannel',
            'python_accessor': 'self._name'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': '',
                'python_type_annotation': 'str',
                'type': 'const char[]',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'numpy.uint8',
                'direction': 'in',
                'has_explicit_buffer_size': True,
                'is_list': True,
                'is_optional_in_python': True,
                'name': 'bitStream',
                'python_data_type': 'int',
                'python_default_value': None,
                'python_description': 'Is the TEDS bitstream to write to the sensor. This bitstream must be constructed according to the IEEE 1451.4 specification.',
                'python_type_annotation': 'Optional[List[int]]',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'const uInt8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'WriteBasicTEDSOptions',
                'is_optional_in_python': True,
                'name': 'basicTEDSOptions',
                'python_data_type': 'WriteBasicTEDSOptions',
                'python_default_value': 'WriteBasicTEDSOptions.DO_NOT_WRITE',
                'python_description': 'Specifies how to handle basic TEDS data in the bitstream.',
                'python_type_annotation': 'Optional[nidaqmx.constants.WriteBasicTEDSOptions]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'PhysicalChannel',
        'python_description': 'Writes data from a 1D list of 8-bit unsigned integers to the TEDS sensor.',
        'returns': 'int32'
    },
    'WriteToTEDSFromFile': {
        'calling_convention': 'StdCall',
        'handle_parameter': {
            'ctypes_data_type': 'ctypes.c_char_p',
            'cvi_name': 'physicalChannel',
            'python_accessor': 'self._name'
        },
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'physicalChannel',
                'python_data_type': 'str',
                'python_description': '',
                'python_type_annotation': 'str',
                'type': 'const char[]',
                'use_in_python_api': False
            },
            {
                'ctypes_data_type': 'ctypes.c_char_p',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'filePath',
                'python_data_type': 'str',
                'python_default_value': '""',
                'python_description': 'Specifies the filename of a virtual TEDS file that contains the bitstream to write.',
                'python_type_annotation': 'Optional[str]',
                'type': 'const char[]'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'WriteBasicTEDSOptions',
                'is_optional_in_python': True,
                'name': 'basicTEDSOptions',
                'python_data_type': 'WriteBasicTEDSOptions',
                'python_default_value': 'WriteBasicTEDSOptions.DO_NOT_WRITE',
                'python_description': 'Specifies how to handle basic TEDS data in the bitstream.',
                'python_type_annotation': 'Optional[nidaqmx.constants.WriteBasicTEDSOptions]',
                'type': 'int32'
            }
        ],
        'python_class_name': 'PhysicalChannel',
        'python_description': 'Writes data from a virtual TEDS file to the TEDS sensor.',
        'returns': 'int32'
    }
}
