# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/workflow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from proto.clarifai.api import common_pb2 as proto_dot_clarifai_dot_api_dot_common__pb2
from proto.clarifai.api import input_pb2 as proto_dot_clarifai_dot_api_dot_input__pb2
from proto.clarifai.api import model_pb2 as proto_dot_clarifai_dot_api_dot_model__pb2
from proto.clarifai.api import output_pb2 as proto_dot_clarifai_dot_api_dot_output__pb2
from proto.clarifai.api.status import status_pb2 as proto_dot_clarifai_dot_api_dot_status_dot_status__pb2
from proto.clarifai.api.utils import extensions_pb2 as proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/clarifai/api/workflow.proto',
  package='clarifai.api',
  syntax='proto3',
  serialized_pb=_b('\n!proto/clarifai/api/workflow.proto\x12\x0c\x63larifai.api\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fproto/clarifai/api/common.proto\x1a\x1eproto/clarifai/api/input.proto\x1a\x1eproto/clarifai/api/model.proto\x1a\x1fproto/clarifai/api/output.proto\x1a&proto/clarifai/api/status/status.proto\x1a)proto/clarifai/api/utils/extensions.proto\"\x81\x01\n\x08Workflow\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x05nodes\x18\x04 \x03(\x0b\x32\x1a.clarifai.api.WorkflowNode\">\n\x0cWorkflowNode\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x05model\x18\x02 \x01(\x0b\x32\x13.clarifai.api.Model\"Z\n\x12GetWorkflowRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x13\n\x0bworkflow_id\x18\x02 \x01(\t\"g\n\x14ListWorkflowsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\x10\n\x08per_page\x18\x03 \x01(\r\"<\n\x1aListPublicWorkflowsRequest\x12\x0c\n\x04page\x18\x01 \x01(\r\x12\x10\n\x08per_page\x18\x02 \x01(\r\"r\n\x14PostWorkflowsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12)\n\tworkflows\x18\x02 \x03(\x0b\x32\x16.clarifai.api.Workflow\"\x83\x01\n\x15PatchWorkflowsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12)\n\tworkflows\x18\x02 \x03(\x0b\x32\x16.clarifai.api.Workflow\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\"]\n\x15\x44\x65leteWorkflowRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x13\n\x0bworkflow_id\x18\x02 \x01(\t\"j\n\x16\x44\x65leteWorkflowsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x0b\n\x03ids\x18\x02 \x03(\t\x12\x12\n\ndelete_all\x18\x03 \x01(\x08\"o\n\x16SingleWorkflowResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12(\n\x08workflow\x18\x02 \x01(\x0b\x32\x16.clarifai.api.Workflow\"u\n\x15MultiWorkflowResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12/\n\tworkflows\x18\x02 \x03(\x0b\x32\x16.clarifai.api.WorkflowB\x04\x80\xb5\x18\x01\"\xba\x01\n\x1aPostWorkflowResultsRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x13\n\x0bworkflow_id\x18\x02 \x01(\t\x12#\n\x06inputs\x18\x03 \x03(\x0b\x32\x13.clarifai.api.Input\x12\x31\n\routput_config\x18\x04 \x01(\x0b\x32\x1a.clarifai.api.OutputConfig\"\xa3\x01\n\x1bPostWorkflowResultsResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12(\n\x08workflow\x18\x02 \x01(\x0b\x32\x16.clarifai.api.Workflow\x12-\n\x07results\x18\x03 \x03(\x0b\x32\x1c.clarifai.api.WorkflowResult\"\xe8\x01\n\x0eWorkflowResult\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\x06status\x18\x02 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x05model\x18\x04 \x01(\x0b\x32\x13.clarifai.api.Model\x12\"\n\x05input\x18\x05 \x01(\x0b\x32\x13.clarifai.api.Input\x12%\n\x07outputs\x18\x06 \x03(\x0b\x32\x14.clarifai.api.OutputB$Z\x03\x61pi\xa2\x02\x04\x43\x41IP\xc2\x02\x01_\xca\x02\x11\x43larifai\\Internalb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_common__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_input__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_model__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_output__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_status_dot_status__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2.DESCRIPTOR,])




_WORKFLOW = _descriptor.Descriptor(
  name='Workflow',
  full_name='clarifai.api.Workflow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='clarifai.api.Workflow.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='clarifai.api.Workflow.app_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='clarifai.api.Workflow.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='clarifai.api.Workflow.nodes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=427,
)


_WORKFLOWNODE = _descriptor.Descriptor(
  name='WorkflowNode',
  full_name='clarifai.api.WorkflowNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='clarifai.api.WorkflowNode.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='clarifai.api.WorkflowNode.model', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=429,
  serialized_end=491,
)


_GETWORKFLOWREQUEST = _descriptor.Descriptor(
  name='GetWorkflowRequest',
  full_name='clarifai.api.GetWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.GetWorkflowRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='clarifai.api.GetWorkflowRequest.workflow_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=583,
)


_LISTWORKFLOWSREQUEST = _descriptor.Descriptor(
  name='ListWorkflowsRequest',
  full_name='clarifai.api.ListWorkflowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.ListWorkflowsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='clarifai.api.ListWorkflowsRequest.page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='clarifai.api.ListWorkflowsRequest.per_page', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=688,
)


_LISTPUBLICWORKFLOWSREQUEST = _descriptor.Descriptor(
  name='ListPublicWorkflowsRequest',
  full_name='clarifai.api.ListPublicWorkflowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='clarifai.api.ListPublicWorkflowsRequest.page', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='clarifai.api.ListPublicWorkflowsRequest.per_page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=690,
  serialized_end=750,
)


_POSTWORKFLOWSREQUEST = _descriptor.Descriptor(
  name='PostWorkflowsRequest',
  full_name='clarifai.api.PostWorkflowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PostWorkflowsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflows', full_name='clarifai.api.PostWorkflowsRequest.workflows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=866,
)


_PATCHWORKFLOWSREQUEST = _descriptor.Descriptor(
  name='PatchWorkflowsRequest',
  full_name='clarifai.api.PatchWorkflowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PatchWorkflowsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflows', full_name='clarifai.api.PatchWorkflowsRequest.workflows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='clarifai.api.PatchWorkflowsRequest.action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=869,
  serialized_end=1000,
)


_DELETEWORKFLOWREQUEST = _descriptor.Descriptor(
  name='DeleteWorkflowRequest',
  full_name='clarifai.api.DeleteWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.DeleteWorkflowRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='clarifai.api.DeleteWorkflowRequest.workflow_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1002,
  serialized_end=1095,
)


_DELETEWORKFLOWSREQUEST = _descriptor.Descriptor(
  name='DeleteWorkflowsRequest',
  full_name='clarifai.api.DeleteWorkflowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.DeleteWorkflowsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ids', full_name='clarifai.api.DeleteWorkflowsRequest.ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete_all', full_name='clarifai.api.DeleteWorkflowsRequest.delete_all', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1097,
  serialized_end=1203,
)


_SINGLEWORKFLOWRESPONSE = _descriptor.Descriptor(
  name='SingleWorkflowResponse',
  full_name='clarifai.api.SingleWorkflowResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.SingleWorkflowResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow', full_name='clarifai.api.SingleWorkflowResponse.workflow', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1205,
  serialized_end=1316,
)


_MULTIWORKFLOWRESPONSE = _descriptor.Descriptor(
  name='MultiWorkflowResponse',
  full_name='clarifai.api.MultiWorkflowResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.MultiWorkflowResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflows', full_name='clarifai.api.MultiWorkflowResponse.workflows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1318,
  serialized_end=1435,
)


_POSTWORKFLOWRESULTSREQUEST = _descriptor.Descriptor(
  name='PostWorkflowResultsRequest',
  full_name='clarifai.api.PostWorkflowResultsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PostWorkflowResultsRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='clarifai.api.PostWorkflowResultsRequest.workflow_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='clarifai.api.PostWorkflowResultsRequest.inputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_config', full_name='clarifai.api.PostWorkflowResultsRequest.output_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1438,
  serialized_end=1624,
)


_POSTWORKFLOWRESULTSRESPONSE = _descriptor.Descriptor(
  name='PostWorkflowResultsResponse',
  full_name='clarifai.api.PostWorkflowResultsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.PostWorkflowResultsResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow', full_name='clarifai.api.PostWorkflowResultsResponse.workflow', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='clarifai.api.PostWorkflowResultsResponse.results', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1627,
  serialized_end=1790,
)


_WORKFLOWRESULT = _descriptor.Descriptor(
  name='WorkflowResult',
  full_name='clarifai.api.WorkflowResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='clarifai.api.WorkflowResult.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.WorkflowResult.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='clarifai.api.WorkflowResult.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='clarifai.api.WorkflowResult.model', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input', full_name='clarifai.api.WorkflowResult.input', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='clarifai.api.WorkflowResult.outputs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1793,
  serialized_end=2025,
)

_WORKFLOW.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WORKFLOW.fields_by_name['nodes'].message_type = _WORKFLOWNODE
_WORKFLOWNODE.fields_by_name['model'].message_type = proto_dot_clarifai_dot_api_dot_model__pb2._MODEL
_GETWORKFLOWREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_LISTWORKFLOWSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTWORKFLOWSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTWORKFLOWSREQUEST.fields_by_name['workflows'].message_type = _WORKFLOW
_PATCHWORKFLOWSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_PATCHWORKFLOWSREQUEST.fields_by_name['workflows'].message_type = _WORKFLOW
_DELETEWORKFLOWREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_DELETEWORKFLOWSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_SINGLEWORKFLOWRESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_SINGLEWORKFLOWRESPONSE.fields_by_name['workflow'].message_type = _WORKFLOW
_MULTIWORKFLOWRESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_MULTIWORKFLOWRESPONSE.fields_by_name['workflows'].message_type = _WORKFLOW
_POSTWORKFLOWRESULTSREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTWORKFLOWRESULTSREQUEST.fields_by_name['inputs'].message_type = proto_dot_clarifai_dot_api_dot_input__pb2._INPUT
_POSTWORKFLOWRESULTSREQUEST.fields_by_name['output_config'].message_type = proto_dot_clarifai_dot_api_dot_model__pb2._OUTPUTCONFIG
_POSTWORKFLOWRESULTSRESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_POSTWORKFLOWRESULTSRESPONSE.fields_by_name['workflow'].message_type = _WORKFLOW
_POSTWORKFLOWRESULTSRESPONSE.fields_by_name['results'].message_type = _WORKFLOWRESULT
_WORKFLOWRESULT.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_WORKFLOWRESULT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WORKFLOWRESULT.fields_by_name['model'].message_type = proto_dot_clarifai_dot_api_dot_model__pb2._MODEL
_WORKFLOWRESULT.fields_by_name['input'].message_type = proto_dot_clarifai_dot_api_dot_input__pb2._INPUT
_WORKFLOWRESULT.fields_by_name['outputs'].message_type = proto_dot_clarifai_dot_api_dot_output__pb2._OUTPUT
DESCRIPTOR.message_types_by_name['Workflow'] = _WORKFLOW
DESCRIPTOR.message_types_by_name['WorkflowNode'] = _WORKFLOWNODE
DESCRIPTOR.message_types_by_name['GetWorkflowRequest'] = _GETWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['ListWorkflowsRequest'] = _LISTWORKFLOWSREQUEST
DESCRIPTOR.message_types_by_name['ListPublicWorkflowsRequest'] = _LISTPUBLICWORKFLOWSREQUEST
DESCRIPTOR.message_types_by_name['PostWorkflowsRequest'] = _POSTWORKFLOWSREQUEST
DESCRIPTOR.message_types_by_name['PatchWorkflowsRequest'] = _PATCHWORKFLOWSREQUEST
DESCRIPTOR.message_types_by_name['DeleteWorkflowRequest'] = _DELETEWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['DeleteWorkflowsRequest'] = _DELETEWORKFLOWSREQUEST
DESCRIPTOR.message_types_by_name['SingleWorkflowResponse'] = _SINGLEWORKFLOWRESPONSE
DESCRIPTOR.message_types_by_name['MultiWorkflowResponse'] = _MULTIWORKFLOWRESPONSE
DESCRIPTOR.message_types_by_name['PostWorkflowResultsRequest'] = _POSTWORKFLOWRESULTSREQUEST
DESCRIPTOR.message_types_by_name['PostWorkflowResultsResponse'] = _POSTWORKFLOWRESULTSRESPONSE
DESCRIPTOR.message_types_by_name['WorkflowResult'] = _WORKFLOWRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Workflow = _reflection.GeneratedProtocolMessageType('Workflow', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOW,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.Workflow)
  ))
_sym_db.RegisterMessage(Workflow)

WorkflowNode = _reflection.GeneratedProtocolMessageType('WorkflowNode', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOWNODE,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.WorkflowNode)
  ))
_sym_db.RegisterMessage(WorkflowNode)

GetWorkflowRequest = _reflection.GeneratedProtocolMessageType('GetWorkflowRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETWORKFLOWREQUEST,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GetWorkflowRequest)
  ))
_sym_db.RegisterMessage(GetWorkflowRequest)

ListWorkflowsRequest = _reflection.GeneratedProtocolMessageType('ListWorkflowsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTWORKFLOWSREQUEST,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ListWorkflowsRequest)
  ))
_sym_db.RegisterMessage(ListWorkflowsRequest)

ListPublicWorkflowsRequest = _reflection.GeneratedProtocolMessageType('ListPublicWorkflowsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPUBLICWORKFLOWSREQUEST,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ListPublicWorkflowsRequest)
  ))
_sym_db.RegisterMessage(ListPublicWorkflowsRequest)

PostWorkflowsRequest = _reflection.GeneratedProtocolMessageType('PostWorkflowsRequest', (_message.Message,), dict(
  DESCRIPTOR = _POSTWORKFLOWSREQUEST,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PostWorkflowsRequest)
  ))
_sym_db.RegisterMessage(PostWorkflowsRequest)

PatchWorkflowsRequest = _reflection.GeneratedProtocolMessageType('PatchWorkflowsRequest', (_message.Message,), dict(
  DESCRIPTOR = _PATCHWORKFLOWSREQUEST,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PatchWorkflowsRequest)
  ))
_sym_db.RegisterMessage(PatchWorkflowsRequest)

DeleteWorkflowRequest = _reflection.GeneratedProtocolMessageType('DeleteWorkflowRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEWORKFLOWREQUEST,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.DeleteWorkflowRequest)
  ))
_sym_db.RegisterMessage(DeleteWorkflowRequest)

DeleteWorkflowsRequest = _reflection.GeneratedProtocolMessageType('DeleteWorkflowsRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEWORKFLOWSREQUEST,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.DeleteWorkflowsRequest)
  ))
_sym_db.RegisterMessage(DeleteWorkflowsRequest)

SingleWorkflowResponse = _reflection.GeneratedProtocolMessageType('SingleWorkflowResponse', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEWORKFLOWRESPONSE,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.SingleWorkflowResponse)
  ))
_sym_db.RegisterMessage(SingleWorkflowResponse)

MultiWorkflowResponse = _reflection.GeneratedProtocolMessageType('MultiWorkflowResponse', (_message.Message,), dict(
  DESCRIPTOR = _MULTIWORKFLOWRESPONSE,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.MultiWorkflowResponse)
  ))
_sym_db.RegisterMessage(MultiWorkflowResponse)

PostWorkflowResultsRequest = _reflection.GeneratedProtocolMessageType('PostWorkflowResultsRequest', (_message.Message,), dict(
  DESCRIPTOR = _POSTWORKFLOWRESULTSREQUEST,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PostWorkflowResultsRequest)
  ))
_sym_db.RegisterMessage(PostWorkflowResultsRequest)

PostWorkflowResultsResponse = _reflection.GeneratedProtocolMessageType('PostWorkflowResultsResponse', (_message.Message,), dict(
  DESCRIPTOR = _POSTWORKFLOWRESULTSRESPONSE,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PostWorkflowResultsResponse)
  ))
_sym_db.RegisterMessage(PostWorkflowResultsResponse)

WorkflowResult = _reflection.GeneratedProtocolMessageType('WorkflowResult', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOWRESULT,
  __module__ = 'proto.clarifai.api.workflow_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.WorkflowResult)
  ))
_sym_db.RegisterMessage(WorkflowResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\003api\242\002\004CAIP\302\002\001_\312\002\021Clarifai\\Internal'))
_MULTIWORKFLOWRESPONSE.fields_by_name['workflows'].has_options = True
_MULTIWORKFLOWRESPONSE.fields_by_name['workflows']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001'))
# @@protoc_insertion_point(module_scope)
