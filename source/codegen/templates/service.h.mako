<%
import common_helpers
import service_helpers

enums = data['enums']
config = data['config']
functions = data['functions']

function_enums = common_helpers.get_function_enums(functions)
enums_to_map = service_helpers.get_enums_to_map(functions, enums)
service_class_prefix = config["service_class_prefix"]
driver_library_interface = common_helpers.get_library_interface_type_name(config)
include_guard_name = service_helpers.get_include_guard_name(config, "_SERVICE_H")
namespace_prefix = config["namespace_component"] + "_grpc::"
custom_types = common_helpers.get_custom_types(config)
(input_custom_types, output_custom_types) = common_helpers.get_input_and_output_custom_types(functions)
resource_repository_ptr = service_helpers.get_driver_shared_resource_repository_ptr_type(config)

async_functions = service_helpers.get_async_functions(functions)
has_async_functions = any(async_functions)
base_class_name = f"{service_class_prefix}::Service"
for async_function in async_functions.keys():
  base_class_name = f"{service_class_prefix}::WithCallbackMethod_{async_function}<{base_class_name}>"

cross_driver_session_deps = service_helpers.get_cross_driver_session_dependencies(functions)
%>\

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service header for the ${config["driver_name"]} Metadata
//---------------------------------------------------------------------
#ifndef ${include_guard_name}
#define ${include_guard_name}

#include <${config["module_name"]}.grpc.pb.h>
#include <condition_variable>
#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>
#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <map>
#include <server/converters.h>
#include <server/feature_toggles.h>
#include <server/session_resource_repository.h>
#include <server/shared_library.h>
#include <server/exceptions.h>

#include "${config["module_name"]}_library_interface.h"

namespace ${config["namespace_component"]}_grpc {

struct ${service_class_prefix}FeatureToggles
{
  using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;
  ${service_class_prefix}FeatureToggles(const nidevice_grpc::FeatureToggles& feature_toggles = {});

  bool is_enabled;
% for toggle in service_helpers.get_feature_toggles(config):
  bool ${service_helpers.get_toggle_member_name(toggle)};
% endfor
};

class ${service_class_prefix}Service final : public ${base_class_name} {
public:
  using ResourceRepositorySharedPtr = ${resource_repository_ptr};
% for cross_driver_dep in cross_driver_session_deps:
  using ${cross_driver_dep.resource_repository_alias} = ${cross_driver_dep.resource_repository_type};
% endfor

  ${service_class_prefix}Service(
    ${service_class_prefix}LibraryInterface* library,
    ResourceRepositorySharedPtr session_repository,
% for cross_driver_dep in cross_driver_session_deps:
    ${cross_driver_dep.resource_repository_alias} ${cross_driver_dep.local_name},
% endfor
    const ${service_class_prefix}FeatureToggles& feature_toggles = {});
  virtual ~${service_class_prefix}Service();
  
% for function in common_helpers.filter_proto_rpc_functions(functions):
<%
  f = functions[function]
  method_name = common_helpers.snake_to_pascal(function)
  request_type = service_helpers.get_request_type(method_name)
  response_type = service_helpers.get_response_type(method_name)
%>\
% if function in async_functions:
  ::grpc::ServerWriteReactor<${response_type}>* ${method_name}(::grpc::CallbackServerContext* context, const ${request_type}* request) override;
% else:
  ::grpc::Status ${method_name}(::grpc::ServerContext* context, const ${request_type}* request, ${response_type}* response) override;
% endif
% endfor
private:
  ${driver_library_interface}* library_;
  ResourceRepositorySharedPtr session_repository_;
% for cross_driver_dep in cross_driver_session_deps:
  ${cross_driver_dep.resource_repository_alias} ${cross_driver_dep.field_name};
% endfor
% if common_helpers.has_viboolean_array_param(functions):
  void Copy(const std::vector<ViBoolean>& input, google::protobuf::RepeatedField<bool>* output);
% endif
% if common_helpers.has_enum_array_string_out_param(functions):
  template <typename TEnum>
  void CopyBytesToEnums(const std::string& input, google::protobuf::RepeatedField<TEnum>* output);
% endif
% for enum in enums_to_map:
<%
  enum_value = common_helpers.get_enum_value_cpp_type(enums[enum])
%>\
  std::map<std::int32_t, ${enum_value}> ${enum.lower()}_input_map_ { ${service_helpers.get_input_lookup_values(enums[enum])} };
  std::map<${enum_value}, std::int32_t> ${enum.lower()}_output_map_ { ${service_helpers.get_output_lookup_values(enums[enum])} };
% endfor

  ${service_class_prefix}FeatureToggles feature_toggles_;
};

} // namespace ${config["namespace_component"]}_grpc

% if any(input_custom_types) or any(output_custom_types):
namespace nidevice_grpc {
namespace converters {
%   for custom_type in custom_types:
	% if custom_type["name"] in output_custom_types:
template <>
void convert_to_grpc(const ${custom_type["name"]}& input, ${namespace_prefix}${custom_type["grpc_name"]}* output);
	% endif
	% if custom_type["name"] in input_custom_types:
template <>
${custom_type["name"]} convert_from_grpc(const ${namespace_prefix}${custom_type["grpc_name"]}& input);
	%endif
%   endfor
} // namespace converters
} // namespace nidevice_grpc

% endif
#endif  // ${include_guard_name}
