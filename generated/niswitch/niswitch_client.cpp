
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// EXPERIMENTAL Client convenience wrapper for NI-SWITCH.
//---------------------------------------------------------------------
#include "niswitch_client.h"

#include <grpcpp/grpcpp.h>

#include <niswitch.grpc.pb.h>

#include <cstdint>
#include <memory>
#include <stdexcept>
#include <vector>

namespace niswitch_grpc::experimental::client {

AbortScanResponse
abort_scan(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = AbortScanRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = AbortScanResponse{};

  raise_if_error(
      stub->AbortScan(&context, request, &response));

  return response;
}

CanConnectResponse
can_connect(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel1, const pb::string& channel2)
{
  ::grpc::ClientContext context;

  auto request = CanConnectRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel1(channel1);
  request.set_channel2(channel2);

  auto response = CanConnectResponse{};

  raise_if_error(
      stub->CanConnect(&context, request, &response));

  return response;
}

CheckAttributeViBooleanResponse
check_attribute_vi_boolean(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id, const bool& attribute_value)
{
  ::grpc::ClientContext context;

  auto request = CheckAttributeViBooleanRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);
  request.set_attribute_value(attribute_value);

  auto response = CheckAttributeViBooleanResponse{};

  raise_if_error(
      stub->CheckAttributeViBoolean(&context, request, &response));

  return response;
}

CheckAttributeViInt32Response
check_attribute_vi_int32(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id, const simple_variant<NiSwitchInt32AttributeValues, pb::int32>& attribute_value)
{
  ::grpc::ClientContext context;

  auto request = CheckAttributeViInt32Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);
  const auto attribute_value_ptr = attribute_value.get_if<NiSwitchInt32AttributeValues>();
  const auto attribute_value_raw_ptr = attribute_value.get_if<pb::int32>();
  if (attribute_value_ptr) {
    request.set_attribute_value(*attribute_value_ptr);
  }
  else if (attribute_value_raw_ptr) {
    request.set_attribute_value_raw(*attribute_value_raw_ptr);
  }

  auto response = CheckAttributeViInt32Response{};

  raise_if_error(
      stub->CheckAttributeViInt32(&context, request, &response));

  return response;
}

CheckAttributeViReal64Response
check_attribute_vi_real64(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id, const double& attribute_value_raw)
{
  ::grpc::ClientContext context;

  auto request = CheckAttributeViReal64Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);
  request.set_attribute_value_raw(attribute_value_raw);

  auto response = CheckAttributeViReal64Response{};

  raise_if_error(
      stub->CheckAttributeViReal64(&context, request, &response));

  return response;
}

CheckAttributeViStringResponse
check_attribute_vi_string(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id, const pb::string& attribute_value_raw)
{
  ::grpc::ClientContext context;

  auto request = CheckAttributeViStringRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);
  request.set_attribute_value_raw(attribute_value_raw);

  auto response = CheckAttributeViStringResponse{};

  raise_if_error(
      stub->CheckAttributeViString(&context, request, &response));

  return response;
}

CheckAttributeViSessionResponse
check_attribute_vi_session(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id, const nidevice_grpc::Session& attribute_value)
{
  ::grpc::ClientContext context;

  auto request = CheckAttributeViSessionRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);
  request.mutable_attribute_value()->CopyFrom(attribute_value);

  auto response = CheckAttributeViSessionResponse{};

  raise_if_error(
      stub->CheckAttributeViSession(&context, request, &response));

  return response;
}

ClearErrorResponse
clear_error(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = ClearErrorRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = ClearErrorResponse{};

  raise_if_error(
      stub->ClearError(&context, request, &response));

  return response;
}

ClearInterchangeWarningsResponse
clear_interchange_warnings(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = ClearInterchangeWarningsRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = ClearInterchangeWarningsResponse{};

  raise_if_error(
      stub->ClearInterchangeWarnings(&context, request, &response));

  return response;
}

CloseResponse
close(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = CloseRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = CloseResponse{};

  raise_if_error(
      stub->Close(&context, request, &response));

  return response;
}

CommitResponse
commit(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = CommitRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = CommitResponse{};

  raise_if_error(
      stub->Commit(&context, request, &response));

  return response;
}

ConfigureScanListResponse
configure_scan_list(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& scanlist, const simple_variant<ScanMode, pb::int32>& scan_mode)
{
  ::grpc::ClientContext context;

  auto request = ConfigureScanListRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_scanlist(scanlist);
  const auto scan_mode_ptr = scan_mode.get_if<ScanMode>();
  const auto scan_mode_raw_ptr = scan_mode.get_if<pb::int32>();
  if (scan_mode_ptr) {
    request.set_scan_mode(*scan_mode_ptr);
  }
  else if (scan_mode_raw_ptr) {
    request.set_scan_mode_raw(*scan_mode_raw_ptr);
  }

  auto response = ConfigureScanListResponse{};

  raise_if_error(
      stub->ConfigureScanList(&context, request, &response));

  return response;
}

ConfigureScanTriggerResponse
configure_scan_trigger(const StubPtr& stub, const nidevice_grpc::Session& vi, const double& scan_delay, const simple_variant<TriggerInput, pb::int32>& trigger_input, const simple_variant<ScanAdvancedOutput, pb::int32>& scan_advanced_output)
{
  ::grpc::ClientContext context;

  auto request = ConfigureScanTriggerRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_scan_delay(scan_delay);
  const auto trigger_input_ptr = trigger_input.get_if<TriggerInput>();
  const auto trigger_input_raw_ptr = trigger_input.get_if<pb::int32>();
  if (trigger_input_ptr) {
    request.set_trigger_input(*trigger_input_ptr);
  }
  else if (trigger_input_raw_ptr) {
    request.set_trigger_input_raw(*trigger_input_raw_ptr);
  }
  const auto scan_advanced_output_ptr = scan_advanced_output.get_if<ScanAdvancedOutput>();
  const auto scan_advanced_output_raw_ptr = scan_advanced_output.get_if<pb::int32>();
  if (scan_advanced_output_ptr) {
    request.set_scan_advanced_output(*scan_advanced_output_ptr);
  }
  else if (scan_advanced_output_raw_ptr) {
    request.set_scan_advanced_output_raw(*scan_advanced_output_raw_ptr);
  }

  auto response = ConfigureScanTriggerResponse{};

  raise_if_error(
      stub->ConfigureScanTrigger(&context, request, &response));

  return response;
}

ConnectResponse
connect(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel1, const pb::string& channel2)
{
  ::grpc::ClientContext context;

  auto request = ConnectRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel1(channel1);
  request.set_channel2(channel2);

  auto response = ConnectResponse{};

  raise_if_error(
      stub->Connect(&context, request, &response));

  return response;
}

ConnectMultipleResponse
connect_multiple(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& connection_list)
{
  ::grpc::ClientContext context;

  auto request = ConnectMultipleRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_connection_list(connection_list);

  auto response = ConnectMultipleResponse{};

  raise_if_error(
      stub->ConnectMultiple(&context, request, &response));

  return response;
}

DisableResponse
disable(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = DisableRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = DisableResponse{};

  raise_if_error(
      stub->Disable(&context, request, &response));

  return response;
}

DisconnectResponse
disconnect(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel1, const pb::string& channel2)
{
  ::grpc::ClientContext context;

  auto request = DisconnectRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel1(channel1);
  request.set_channel2(channel2);

  auto response = DisconnectResponse{};

  raise_if_error(
      stub->Disconnect(&context, request, &response));

  return response;
}

DisconnectAllResponse
disconnect_all(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = DisconnectAllRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = DisconnectAllResponse{};

  raise_if_error(
      stub->DisconnectAll(&context, request, &response));

  return response;
}

DisconnectMultipleResponse
disconnect_multiple(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& disconnection_list)
{
  ::grpc::ClientContext context;

  auto request = DisconnectMultipleRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_disconnection_list(disconnection_list);

  auto response = DisconnectMultipleResponse{};

  raise_if_error(
      stub->DisconnectMultiple(&context, request, &response));

  return response;
}

ErrorMessageResponse
error_message(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& error_code)
{
  ::grpc::ClientContext context;

  auto request = ErrorMessageRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_error_code(error_code);

  auto response = ErrorMessageResponse{};

  raise_if_error(
      stub->ErrorMessage(&context, request, &response));

  return response;
}

ErrorQueryResponse
error_query(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = ErrorQueryRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = ErrorQueryResponse{};

  raise_if_error(
      stub->ErrorQuery(&context, request, &response));

  return response;
}

GetAttributeViBooleanResponse
get_attribute_vi_boolean(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeViBooleanRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeViBooleanResponse{};

  raise_if_error(
      stub->GetAttributeViBoolean(&context, request, &response));

  return response;
}

GetAttributeViInt32Response
get_attribute_vi_int32(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeViInt32Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeViInt32Response{};

  raise_if_error(
      stub->GetAttributeViInt32(&context, request, &response));

  return response;
}

GetAttributeViReal64Response
get_attribute_vi_real64(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeViReal64Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeViReal64Response{};

  raise_if_error(
      stub->GetAttributeViReal64(&context, request, &response));

  return response;
}

GetAttributeViStringResponse
get_attribute_vi_string(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeViStringRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeViStringResponse{};

  raise_if_error(
      stub->GetAttributeViString(&context, request, &response));

  return response;
}

GetAttributeViSessionResponse
get_attribute_vi_session(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeViSessionRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeViSessionResponse{};

  raise_if_error(
      stub->GetAttributeViSession(&context, request, &response));

  return response;
}

GetChannelNameResponse
get_channel_name(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& index)
{
  ::grpc::ClientContext context;

  auto request = GetChannelNameRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_index(index);

  auto response = GetChannelNameResponse{};

  raise_if_error(
      stub->GetChannelName(&context, request, &response));

  return response;
}

GetErrorResponse
get_error(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = GetErrorRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = GetErrorResponse{};

  raise_if_error(
      stub->GetError(&context, request, &response));

  return response;
}

GetNextCoercionRecordResponse
get_next_coercion_record(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = GetNextCoercionRecordRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = GetNextCoercionRecordResponse{};

  raise_if_error(
      stub->GetNextCoercionRecord(&context, request, &response));

  return response;
}

GetNextInterchangeWarningResponse
get_next_interchange_warning(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = GetNextInterchangeWarningRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = GetNextInterchangeWarningResponse{};

  raise_if_error(
      stub->GetNextInterchangeWarning(&context, request, &response));

  return response;
}

GetPathResponse
get_path(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel1, const pb::string& channel2)
{
  ::grpc::ClientContext context;

  auto request = GetPathRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel1(channel1);
  request.set_channel2(channel2);

  auto response = GetPathResponse{};

  raise_if_error(
      stub->GetPath(&context, request, &response));

  return response;
}

GetRelayCountResponse
get_relay_count(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& relay_name)
{
  ::grpc::ClientContext context;

  auto request = GetRelayCountRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_relay_name(relay_name);

  auto response = GetRelayCountResponse{};

  raise_if_error(
      stub->GetRelayCount(&context, request, &response));

  return response;
}

GetRelayNameResponse
get_relay_name(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& index)
{
  ::grpc::ClientContext context;

  auto request = GetRelayNameRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_index(index);

  auto response = GetRelayNameResponse{};

  raise_if_error(
      stub->GetRelayName(&context, request, &response));

  return response;
}

GetRelayPositionResponse
get_relay_position(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& relay_name)
{
  ::grpc::ClientContext context;

  auto request = GetRelayPositionRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_relay_name(relay_name);

  auto response = GetRelayPositionResponse{};

  raise_if_error(
      stub->GetRelayPosition(&context, request, &response));

  return response;
}

InitResponse
init(const StubPtr& stub, const pb::string& resource_name, const bool& id_query, const bool& reset_device)
{
  ::grpc::ClientContext context;

  auto request = InitRequest{};
  request.set_resource_name(resource_name);
  request.set_id_query(id_query);
  request.set_reset_device(reset_device);

  auto response = InitResponse{};

  raise_if_error(
      stub->Init(&context, request, &response));

  return response;
}

InitWithOptionsResponse
init_with_options(const StubPtr& stub, const pb::string& resource_name, const bool& id_query, const bool& reset_device, const pb::string& option_string)
{
  ::grpc::ClientContext context;

  auto request = InitWithOptionsRequest{};
  request.set_resource_name(resource_name);
  request.set_id_query(id_query);
  request.set_reset_device(reset_device);
  request.set_option_string(option_string);

  auto response = InitWithOptionsResponse{};

  raise_if_error(
      stub->InitWithOptions(&context, request, &response));

  return response;
}

InitWithTopologyResponse
init_with_topology(const StubPtr& stub, const pb::string& resource_name, const pb::string& topology, const bool& simulate, const bool& reset_device)
{
  ::grpc::ClientContext context;

  auto request = InitWithTopologyRequest{};
  request.set_resource_name(resource_name);
  request.set_topology(topology);
  request.set_simulate(simulate);
  request.set_reset_device(reset_device);

  auto response = InitWithTopologyResponse{};

  raise_if_error(
      stub->InitWithTopology(&context, request, &response));

  return response;
}

InitiateScanResponse
initiate_scan(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = InitiateScanRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = InitiateScanResponse{};

  raise_if_error(
      stub->InitiateScan(&context, request, &response));

  return response;
}

InvalidateAllAttributesResponse
invalidate_all_attributes(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = InvalidateAllAttributesRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = InvalidateAllAttributesResponse{};

  raise_if_error(
      stub->InvalidateAllAttributes(&context, request, &response));

  return response;
}

IsDebouncedResponse
is_debounced(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = IsDebouncedRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = IsDebouncedResponse{};

  raise_if_error(
      stub->IsDebounced(&context, request, &response));

  return response;
}

IsScanningResponse
is_scanning(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = IsScanningRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = IsScanningResponse{};

  raise_if_error(
      stub->IsScanning(&context, request, &response));

  return response;
}

RelayControlResponse
relay_control(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& relay_name, const simple_variant<RelayAction, pb::int32>& relay_action)
{
  ::grpc::ClientContext context;

  auto request = RelayControlRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_relay_name(relay_name);
  const auto relay_action_ptr = relay_action.get_if<RelayAction>();
  const auto relay_action_raw_ptr = relay_action.get_if<pb::int32>();
  if (relay_action_ptr) {
    request.set_relay_action(*relay_action_ptr);
  }
  else if (relay_action_raw_ptr) {
    request.set_relay_action_raw(*relay_action_raw_ptr);
  }

  auto response = RelayControlResponse{};

  raise_if_error(
      stub->RelayControl(&context, request, &response));

  return response;
}

ResetResponse
reset(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = ResetRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = ResetResponse{};

  raise_if_error(
      stub->Reset(&context, request, &response));

  return response;
}

ResetInterchangeCheckResponse
reset_interchange_check(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = ResetInterchangeCheckRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = ResetInterchangeCheckResponse{};

  raise_if_error(
      stub->ResetInterchangeCheck(&context, request, &response));

  return response;
}

ResetWithDefaultsResponse
reset_with_defaults(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = ResetWithDefaultsRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = ResetWithDefaultsResponse{};

  raise_if_error(
      stub->ResetWithDefaults(&context, request, &response));

  return response;
}

RevisionQueryResponse
revision_query(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = RevisionQueryRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = RevisionQueryResponse{};

  raise_if_error(
      stub->RevisionQuery(&context, request, &response));

  return response;
}

RouteScanAdvancedOutputResponse
route_scan_advanced_output(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<ScanAdvancedOutput, pb::int32>& scan_advanced_output_connector, const simple_variant<ScanAdvancedOutput, pb::int32>& scan_advanced_output_bus_line, const bool& invert)
{
  ::grpc::ClientContext context;

  auto request = RouteScanAdvancedOutputRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto scan_advanced_output_connector_ptr = scan_advanced_output_connector.get_if<ScanAdvancedOutput>();
  const auto scan_advanced_output_connector_raw_ptr = scan_advanced_output_connector.get_if<pb::int32>();
  if (scan_advanced_output_connector_ptr) {
    request.set_scan_advanced_output_connector(*scan_advanced_output_connector_ptr);
  }
  else if (scan_advanced_output_connector_raw_ptr) {
    request.set_scan_advanced_output_connector_raw(*scan_advanced_output_connector_raw_ptr);
  }
  const auto scan_advanced_output_bus_line_ptr = scan_advanced_output_bus_line.get_if<ScanAdvancedOutput>();
  const auto scan_advanced_output_bus_line_raw_ptr = scan_advanced_output_bus_line.get_if<pb::int32>();
  if (scan_advanced_output_bus_line_ptr) {
    request.set_scan_advanced_output_bus_line(*scan_advanced_output_bus_line_ptr);
  }
  else if (scan_advanced_output_bus_line_raw_ptr) {
    request.set_scan_advanced_output_bus_line_raw(*scan_advanced_output_bus_line_raw_ptr);
  }
  request.set_invert(invert);

  auto response = RouteScanAdvancedOutputResponse{};

  raise_if_error(
      stub->RouteScanAdvancedOutput(&context, request, &response));

  return response;
}

RouteTriggerInputResponse
route_trigger_input(const StubPtr& stub, const nidevice_grpc::Session& vi, const simple_variant<TriggerInput, pb::int32>& trigger_input_connector, const simple_variant<TriggerInput, pb::int32>& trigger_input_bus_line, const bool& invert)
{
  ::grpc::ClientContext context;

  auto request = RouteTriggerInputRequest{};
  request.mutable_vi()->CopyFrom(vi);
  const auto trigger_input_connector_ptr = trigger_input_connector.get_if<TriggerInput>();
  const auto trigger_input_connector_raw_ptr = trigger_input_connector.get_if<pb::int32>();
  if (trigger_input_connector_ptr) {
    request.set_trigger_input_connector(*trigger_input_connector_ptr);
  }
  else if (trigger_input_connector_raw_ptr) {
    request.set_trigger_input_connector_raw(*trigger_input_connector_raw_ptr);
  }
  const auto trigger_input_bus_line_ptr = trigger_input_bus_line.get_if<TriggerInput>();
  const auto trigger_input_bus_line_raw_ptr = trigger_input_bus_line.get_if<pb::int32>();
  if (trigger_input_bus_line_ptr) {
    request.set_trigger_input_bus_line(*trigger_input_bus_line_ptr);
  }
  else if (trigger_input_bus_line_raw_ptr) {
    request.set_trigger_input_bus_line_raw(*trigger_input_bus_line_raw_ptr);
  }
  request.set_invert(invert);

  auto response = RouteTriggerInputResponse{};

  raise_if_error(
      stub->RouteTriggerInput(&context, request, &response));

  return response;
}

ScanResponse
scan(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& scanlist, const simple_variant<HandshakingInitiation, pb::int32>& initiation)
{
  ::grpc::ClientContext context;

  auto request = ScanRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_scanlist(scanlist);
  const auto initiation_ptr = initiation.get_if<HandshakingInitiation>();
  const auto initiation_raw_ptr = initiation.get_if<pb::int32>();
  if (initiation_ptr) {
    request.set_initiation(*initiation_ptr);
  }
  else if (initiation_raw_ptr) {
    request.set_initiation_raw(*initiation_raw_ptr);
  }

  auto response = ScanResponse{};

  raise_if_error(
      stub->Scan(&context, request, &response));

  return response;
}

SelfTestResponse
self_test(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = SelfTestRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = SelfTestResponse{};

  raise_if_error(
      stub->SelfTest(&context, request, &response));

  return response;
}

SendSoftwareTriggerResponse
send_software_trigger(const StubPtr& stub, const nidevice_grpc::Session& vi)
{
  ::grpc::ClientContext context;

  auto request = SendSoftwareTriggerRequest{};
  request.mutable_vi()->CopyFrom(vi);

  auto response = SendSoftwareTriggerResponse{};

  raise_if_error(
      stub->SendSoftwareTrigger(&context, request, &response));

  return response;
}

SetAttributeViBooleanResponse
set_attribute_vi_boolean(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id, const bool& attribute_value)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeViBooleanRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);
  request.set_attribute_value(attribute_value);

  auto response = SetAttributeViBooleanResponse{};

  raise_if_error(
      stub->SetAttributeViBoolean(&context, request, &response));

  return response;
}

SetAttributeViInt32Response
set_attribute_vi_int32(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id, const simple_variant<NiSwitchInt32AttributeValues, pb::int32>& attribute_value)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeViInt32Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);
  const auto attribute_value_ptr = attribute_value.get_if<NiSwitchInt32AttributeValues>();
  const auto attribute_value_raw_ptr = attribute_value.get_if<pb::int32>();
  if (attribute_value_ptr) {
    request.set_attribute_value(*attribute_value_ptr);
  }
  else if (attribute_value_raw_ptr) {
    request.set_attribute_value_raw(*attribute_value_raw_ptr);
  }

  auto response = SetAttributeViInt32Response{};

  raise_if_error(
      stub->SetAttributeViInt32(&context, request, &response));

  return response;
}

SetAttributeViReal64Response
set_attribute_vi_real64(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id, const double& attribute_value_raw)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeViReal64Request{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);
  request.set_attribute_value_raw(attribute_value_raw);

  auto response = SetAttributeViReal64Response{};

  raise_if_error(
      stub->SetAttributeViReal64(&context, request, &response));

  return response;
}

SetAttributeViStringResponse
set_attribute_vi_string(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id, const pb::string& attribute_value_raw)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeViStringRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);
  request.set_attribute_value_raw(attribute_value_raw);

  auto response = SetAttributeViStringResponse{};

  raise_if_error(
      stub->SetAttributeViString(&context, request, &response));

  return response;
}

SetAttributeViSessionResponse
set_attribute_vi_session(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& channel_name, const NiSwitchAttribute& attribute_id, const nidevice_grpc::Session& attribute_value)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeViSessionRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_id);
  request.mutable_attribute_value()->CopyFrom(attribute_value);

  auto response = SetAttributeViSessionResponse{};

  raise_if_error(
      stub->SetAttributeViSession(&context, request, &response));

  return response;
}

SetContinuousScanResponse
set_continuous_scan(const StubPtr& stub, const nidevice_grpc::Session& vi, const bool& continuous_scan)
{
  ::grpc::ClientContext context;

  auto request = SetContinuousScanRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_continuous_scan(continuous_scan);

  auto response = SetContinuousScanResponse{};

  raise_if_error(
      stub->SetContinuousScan(&context, request, &response));

  return response;
}

SetPathResponse
set_path(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::string& path_list)
{
  ::grpc::ClientContext context;

  auto request = SetPathRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_path_list(path_list);

  auto response = SetPathResponse{};

  raise_if_error(
      stub->SetPath(&context, request, &response));

  return response;
}

WaitForDebounceResponse
wait_for_debounce(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& maximum_time_ms)
{
  ::grpc::ClientContext context;

  auto request = WaitForDebounceRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_maximum_time_ms(maximum_time_ms);

  auto response = WaitForDebounceResponse{};

  raise_if_error(
      stub->WaitForDebounce(&context, request, &response));

  return response;
}

WaitForScanCompleteResponse
wait_for_scan_complete(const StubPtr& stub, const nidevice_grpc::Session& vi, const pb::int32& maximum_time_ms)
{
  ::grpc::ClientContext context;

  auto request = WaitForScanCompleteRequest{};
  request.mutable_vi()->CopyFrom(vi);
  request.set_maximum_time_ms(maximum_time_ms);

  auto response = WaitForScanCompleteResponse{};

  raise_if_error(
      stub->WaitForScanComplete(&context, request, &response));

  return response;
}


} // namespace niswitch_grpc::experimental::client
