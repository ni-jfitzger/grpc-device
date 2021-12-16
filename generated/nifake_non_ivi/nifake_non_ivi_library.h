//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Real implementation of LibraryInterface for NI-FAKE-NON-IVI
//---------------------------------------------------------------------
#ifndef NIFAKE_NON_IVI_GRPC_LIBRARY_H
#define NIFAKE_NON_IVI_GRPC_LIBRARY_H

#include "nifake_non_ivi_library_interface.h"

#include <server/shared_library.h>

namespace nifake_non_ivi_grpc {

class NiFakeNonIviLibrary : public nifake_non_ivi_grpc::NiFakeNonIviLibraryInterface {
 public:
  NiFakeNonIviLibrary();
  virtual ~NiFakeNonIviLibrary();

  ::grpc::Status check_function_exists(std::string functionName);
  int32 Close(FakeHandle handle);
  int32 GetCrossDriverSession(FakeHandle handle, int32* crossDriverSession);
  int32 GetMarbleAttributeDouble(FakeHandle handle, int32 attribute, double* value);
  int32 GetMarbleAttributeInt32(FakeHandle handle, int32 attribute, int32* value);
  int32 GetMarbleAttributeInt32Array(FakeHandle handle, int32 attribute, int32 value[]);
  int32 Init(const char sessionName[], FakeHandle* handle);
  int32 InitFromCrossDriverSession(int32 crossDriverSession, FakeHandle* handle);
  int32 InitWithHandleNameAsSessionName(const char handleName[], FakeHandle* handle);
  int32 InputArraysWithNarrowIntegerTypes(const myUInt16 u16Array[], const myInt16 i16Array[], const myInt8 i8Array[]);
  int32 IotaWithCustomSize(int32 sizeOne, int32 sizeTwo, int32 data[]);
  int32 OutputArraysWithNarrowIntegerTypes(int32 numberOfU16Samples, myUInt16 u16Data[], int32 numberOfI16Samples, myInt16 i16Data[], int32 numberOfI8Samples, myInt8 i8Data[]);
  int32 InputArrayOfBytes(const myUInt8 u8Array[]);
  int32 OutputArrayOfBytes(int32 numberOfU8Samples, myUInt8 u8Data[]);
  int32 OutputArraysWithPassedInByPtrMechanism(int32 i32Data[], myUInt16 u16Data[], int32* arraySize);
  int32 RegisterCallback(myInt16 inputData, CallbackPtr callbackFunction, void* callbackData);
  int32 ReadStream(int32 start, int32 stop, int32* value);
  int32 InputTimestamp(CVIAbsoluteTime when);
  int32 OutputTimestamp(CVIAbsoluteTime* when);
  int32 InputVarArgs(const char inputName[], const char channelName[], int32 color, double powerUpState, const char channelName0[], int32 color0, double powerUpState0, const char channelName1[], int32 color1, double powerUpState1, const char channelName2[], int32 color2, double powerUpState2);
  int32 OutputVarArgs(const char inputName[], const char channelName[], int32* color, const char channelName0[], int32* color0, const char channelName1[], int32* color1, const char channelName2[], int32* color2);
  int32 ResetMarbleAttribute(FakeHandle handle, int32 attribute);
  int32 ScalarsWithNarrowIntegerTypes(myUInt16 u16, myInt16 i16, myInt8 i8);
  int32 SetMarbleAttributeDouble(FakeHandle handle, int32 attribute, double value);
  int32 SetMarbleAttributeInt32(FakeHandle handle, int32 attribute, int32 value);
  int32 SetColors(int32 colors[3], int32 size);
  int32 GetStructsWithCoercion(int32 numberOfStructs, StructWithCoercion_struct structs[]);
  int32 SetStructsWithCoercion(StructWithCoercion_struct structs[3]);
  int32 InputStringValuedEnum(char aName[]);
  int32 WriteBooleanArray(int32 bools[], int32 size);

 private:
  using ClosePtr = decltype(&niFakeNonIvi_Close);
  using GetCrossDriverSessionPtr = decltype(&niFakeNonIvi_GetCrossDriverSession);
  using GetMarbleAttributeDoublePtr = decltype(&niFakeNonIvi_GetMarbleAttributeDouble);
  using GetMarbleAttributeInt32Ptr = decltype(&niFakeNonIvi_GetMarbleAttributeInt32);
  using GetMarbleAttributeInt32ArrayPtr = decltype(&niFakeNonIvi_GetMarbleAttributeInt32Array);
  using InitPtr = decltype(&niFakeNonIvi_Init);
  using InitFromCrossDriverSessionPtr = decltype(&niFakeNonIvi_InitFromCrossDriverSession);
  using InitWithHandleNameAsSessionNamePtr = decltype(&niFakeNonIvi_InitWithHandleNameAsSessionName);
  using InputArraysWithNarrowIntegerTypesPtr = decltype(&niFakeNonIvi_InputArraysWithNarrowIntegerTypes);
  using IotaWithCustomSizePtr = decltype(&niFakeNonIvi_IotaWithCustomSize);
  using OutputArraysWithNarrowIntegerTypesPtr = decltype(&niFakeNonIvi_OutputArraysWithNarrowIntegerTypes);
  using InputArrayOfBytesPtr = decltype(&niFakeNonIvi_InputArrayOfBytes);
  using OutputArrayOfBytesPtr = decltype(&niFakeNonIvi_OutputArrayOfBytes);
  using OutputArraysWithPassedInByPtrMechanismPtr = decltype(&niFakeNonIvi_OutputArraysWithPassedInByPtrMechanism);
  using RegisterCallbackPtr = decltype(&niFakeNonIvi_RegisterCallback);
  using ReadStreamPtr = decltype(&niFakeNonIvi_ReadStream);
  using InputTimestampPtr = decltype(&niFakeNonIvi_InputTimestamp);
  using OutputTimestampPtr = decltype(&niFakeNonIvi_OutputTimestamp);
  using InputVarArgsPtr = decltype(&niFakeNonIvi_InputVarArgs);
  using OutputVarArgsPtr = decltype(&niFakeNonIvi_OutputVarArgs);
  using ResetMarbleAttributePtr = decltype(&niFakeNonIvi_ResetMarbleAttribute);
  using ScalarsWithNarrowIntegerTypesPtr = decltype(&niFakeNonIvi_ScalarsWithNarrowIntegerTypes);
  using SetMarbleAttributeDoublePtr = decltype(&niFakeNonIvi_SetMarbleAttributeDouble);
  using SetMarbleAttributeInt32Ptr = decltype(&niFakeNonIvi_SetMarbleAttributeInt32);
  using SetColorsPtr = decltype(&niFakeNonIvi_SetColors);
  using GetStructsWithCoercionPtr = decltype(&niFakeNonIvi_GetStructsWithCoercion);
  using SetStructsWithCoercionPtr = decltype(&niFakeNonIvi_SetStructsWithCoercion);
  using InputStringValuedEnumPtr = decltype(&niFakeNonIvi_InputStringValuedEnum);
  using WriteBooleanArrayPtr = decltype(&niFakeNonIvi_WriteBooleanArray);

  typedef struct FunctionPointers {
    ClosePtr Close;
    GetCrossDriverSessionPtr GetCrossDriverSession;
    GetMarbleAttributeDoublePtr GetMarbleAttributeDouble;
    GetMarbleAttributeInt32Ptr GetMarbleAttributeInt32;
    GetMarbleAttributeInt32ArrayPtr GetMarbleAttributeInt32Array;
    InitPtr Init;
    InitFromCrossDriverSessionPtr InitFromCrossDriverSession;
    InitWithHandleNameAsSessionNamePtr InitWithHandleNameAsSessionName;
    InputArraysWithNarrowIntegerTypesPtr InputArraysWithNarrowIntegerTypes;
    IotaWithCustomSizePtr IotaWithCustomSize;
    OutputArraysWithNarrowIntegerTypesPtr OutputArraysWithNarrowIntegerTypes;
    InputArrayOfBytesPtr InputArrayOfBytes;
    OutputArrayOfBytesPtr OutputArrayOfBytes;
    OutputArraysWithPassedInByPtrMechanismPtr OutputArraysWithPassedInByPtrMechanism;
    RegisterCallbackPtr RegisterCallback;
    ReadStreamPtr ReadStream;
    InputTimestampPtr InputTimestamp;
    OutputTimestampPtr OutputTimestamp;
    InputVarArgsPtr InputVarArgs;
    OutputVarArgsPtr OutputVarArgs;
    ResetMarbleAttributePtr ResetMarbleAttribute;
    ScalarsWithNarrowIntegerTypesPtr ScalarsWithNarrowIntegerTypes;
    SetMarbleAttributeDoublePtr SetMarbleAttributeDouble;
    SetMarbleAttributeInt32Ptr SetMarbleAttributeInt32;
    SetColorsPtr SetColors;
    GetStructsWithCoercionPtr GetStructsWithCoercion;
    SetStructsWithCoercionPtr SetStructsWithCoercion;
    InputStringValuedEnumPtr InputStringValuedEnum;
    WriteBooleanArrayPtr WriteBooleanArray;
  } FunctionLoadStatus;

  nidevice_grpc::SharedLibrary shared_library_;
  FunctionPointers function_pointers_;
};

}  // namespace nifake_non_ivi_grpc

#endif  // NIFAKE_NON_IVI_GRPC_LIBRARY_H
