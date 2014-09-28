# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openxc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='openxc.proto',
  package='openxc',
  serialized_pb='\n\x0copenxc.proto\x12\x06openxc\"\x94\x03\n\x0eVehicleMessage\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.openxc.VehicleMessage.Type\x12\'\n\x0braw_message\x18\x02 \x01(\x0b\x32\x12.openxc.RawMessage\x12\x35\n\x12translated_message\x18\x03 \x01(\x0b\x32\x19.openxc.TranslatedMessage\x12\x37\n\x13\x64iagnostic_response\x18\x04 \x01(\x0b\x32\x1a.openxc.DiagnosticResponse\x12/\n\x0f\x63ontrol_command\x18\x05 \x01(\x0b\x32\x16.openxc.ControlCommand\x12\x31\n\x10\x63ommand_response\x18\x06 \x01(\x0b\x32\x17.openxc.CommandResponse\"Z\n\x04Type\x12\x07\n\x03RAW\x10\x01\x12\x0e\n\nTRANSLATED\x10\x02\x12\x0e\n\nDIAGNOSTIC\x10\x03\x12\x13\n\x0f\x43ONTROL_COMMAND\x10\x04\x12\x14\n\x10\x43OMMAND_RESPONSE\x10\x05\";\n\nRawMessage\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x12\n\nmessage_id\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\xc8\x03\n\x0e\x43ontrolCommand\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.openxc.ControlCommand.Type\x12<\n\x12\x64iagnostic_request\x18\x02 \x01(\x0b\x32 .openxc.DiagnosticControlCommand\x12G\n\x18passthrough_mode_request\x18\x03 \x01(\x0b\x32%.openxc.PassthroughModeControlCommand\x12O\n acceptance_filter_bypass_command\x18\x04 \x01(\x0b\x32%.openxc.AcceptanceFilterBypassCommand\x12<\n\x16message_format_command\x18\x05 \x01(\x0b\x32\x1c.openxc.PayloadFormatCommand\"u\n\x04Type\x12\x0b\n\x07VERSION\x10\x01\x12\r\n\tDEVICE_ID\x10\x02\x12\x0e\n\nDIAGNOSTIC\x10\x03\x12\x0f\n\x0bPASSTHROUGH\x10\x04\x12\x1c\n\x18\x41\x43\x43\x45PTANCE_FILTER_BYPASS\x10\x05\x12\x12\n\x0eMESSAGE_FORMAT\x10\x06\"\x9e\x01\n\x18\x44iagnosticControlCommand\x12*\n\x07request\x18\x01 \x01(\x0b\x32\x19.openxc.DiagnosticRequest\x12\x37\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\'.openxc.DiagnosticControlCommand.Action\"\x1d\n\x06\x41\x63tion\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06\x43\x41NCEL\x10\x02\"=\n\x1dPassthroughModeControlCommand\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"<\n\x1d\x41\x63\x63\x65ptanceFilterBypassCommand\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x0e\n\x06\x62ypass\x18\x02 \x01(\x08\"{\n\x14PayloadFormatCommand\x12:\n\x06\x66ormat\x18\x01 \x01(\x0e\x32*.openxc.PayloadFormatCommand.PayloadFormat\"\'\n\rPayloadFormat\x12\x08\n\x04JSON\x10\x01\x12\x0c\n\x08PROTOBUF\x10\x02\"]\n\x0f\x43ommandResponse\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.openxc.ControlCommand.Type\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x08\"\xfd\x01\n\x11\x44iagnosticRequest\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x12\n\nmessage_id\x18\x02 \x01(\r\x12\x0c\n\x04mode\x18\x03 \x01(\r\x12\x0b\n\x03pid\x18\x04 \x01(\r\x12\x0f\n\x07payload\x18\x05 \x01(\x0c\x12\x1a\n\x12multiple_responses\x18\x06 \x01(\x08\x12\x11\n\tfrequency\x18\x07 \x01(\x01\x12\x0c\n\x04name\x18\x08 \x01(\t\x12;\n\x0c\x64\x65\x63oded_type\x18\t \x01(\x0e\x32%.openxc.DiagnosticRequest.DecodedType\"!\n\x0b\x44\x65\x63odedType\x12\x08\n\x04NONE\x10\x01\x12\x08\n\x04OBD2\x10\x02\"\xa1\x01\n\x12\x44iagnosticResponse\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x12\n\nmessage_id\x18\x02 \x01(\r\x12\x0c\n\x04mode\x18\x03 \x01(\r\x12\x0b\n\x03pid\x18\x04 \x01(\r\x12\x0f\n\x07success\x18\x05 \x01(\x08\x12\x1e\n\x16negative_response_code\x18\x06 \x01(\r\x12\x0f\n\x07payload\x18\x07 \x01(\x0c\x12\r\n\x05value\x18\x08 \x01(\x01\"\xa2\x01\n\x0c\x44ynamicField\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.openxc.DynamicField.Type\x12\x14\n\x0cstring_value\x18\x02 \x01(\t\x12\x15\n\rnumeric_value\x18\x03 \x01(\x01\x12\x15\n\rboolean_value\x18\x04 \x01(\x08\"%\n\x04Type\x12\n\n\x06STRING\x10\x01\x12\x07\n\x03NUM\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\"\xf7\x01\n\x11TranslatedMessage\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.openxc.TranslatedMessage.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12#\n\x05value\x18\x03 \x01(\x0b\x32\x14.openxc.DynamicField\x12#\n\x05\x65vent\x18\x04 \x01(\x0b\x32\x14.openxc.DynamicField\"\\\n\x04Type\x12\n\n\x06STRING\x10\x01\x12\x07\n\x03NUM\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x12\x12\n\x0e\x45VENTED_STRING\x10\x04\x12\x0f\n\x0b\x45VENTED_NUM\x10\x05\x12\x10\n\x0c\x45VENTED_BOOL\x10\x06\x42\x1c\n\ncom.openxcB\x0e\x42inaryMessages')



_VEHICLEMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='openxc.VehicleMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAW', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSLATED', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIAGNOSTIC', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_COMMAND', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_RESPONSE', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=339,
  serialized_end=429,
)

_CONTROLCOMMAND_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='openxc.ControlCommand.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VERSION', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_ID', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIAGNOSTIC', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSTHROUGH', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCEPTANCE_FILTER_BYPASS', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_FORMAT', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=832,
  serialized_end=949,
)

_DIAGNOSTICCONTROLCOMMAND_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='openxc.DiagnosticControlCommand.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1081,
  serialized_end=1110,
)

_PAYLOADFORMATCOMMAND_PAYLOADFORMAT = _descriptor.EnumDescriptor(
  name='PayloadFormat',
  full_name='openxc.PayloadFormatCommand.PayloadFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JSON', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTOBUF', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1321,
  serialized_end=1360,
)

_DIAGNOSTICREQUEST_DECODEDTYPE = _descriptor.EnumDescriptor(
  name='DecodedType',
  full_name='openxc.DiagnosticRequest.DecodedType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OBD2', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1678,
  serialized_end=1711,
)

_DYNAMICFIELD_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='openxc.DynamicField.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUM', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2003,
  serialized_end=2040,
)

_TRANSLATEDMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='openxc.TranslatedMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUM', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENTED_STRING', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENTED_NUM', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENTED_BOOL', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2198,
  serialized_end=2290,
)


_VEHICLEMESSAGE = _descriptor.Descriptor(
  name='VehicleMessage',
  full_name='openxc.VehicleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.VehicleMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_message', full_name='openxc.VehicleMessage.raw_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='translated_message', full_name='openxc.VehicleMessage.translated_message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diagnostic_response', full_name='openxc.VehicleMessage.diagnostic_response', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='control_command', full_name='openxc.VehicleMessage.control_command', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command_response', full_name='openxc.VehicleMessage.command_response', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VEHICLEMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=25,
  serialized_end=429,
)


_RAWMESSAGE = _descriptor.Descriptor(
  name='RawMessage',
  full_name='openxc.RawMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.RawMessage.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='openxc.RawMessage.message_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='openxc.RawMessage.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=431,
  serialized_end=490,
)


_CONTROLCOMMAND = _descriptor.Descriptor(
  name='ControlCommand',
  full_name='openxc.ControlCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.ControlCommand.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diagnostic_request', full_name='openxc.ControlCommand.diagnostic_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passthrough_mode_request', full_name='openxc.ControlCommand.passthrough_mode_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acceptance_filter_bypass_command', full_name='openxc.ControlCommand.acceptance_filter_bypass_command', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_format_command', full_name='openxc.ControlCommand.message_format_command', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTROLCOMMAND_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=493,
  serialized_end=949,
)


_DIAGNOSTICCONTROLCOMMAND = _descriptor.Descriptor(
  name='DiagnosticControlCommand',
  full_name='openxc.DiagnosticControlCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='openxc.DiagnosticControlCommand.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='openxc.DiagnosticControlCommand.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DIAGNOSTICCONTROLCOMMAND_ACTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=952,
  serialized_end=1110,
)


_PASSTHROUGHMODECONTROLCOMMAND = _descriptor.Descriptor(
  name='PassthroughModeControlCommand',
  full_name='openxc.PassthroughModeControlCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.PassthroughModeControlCommand.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='openxc.PassthroughModeControlCommand.enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1112,
  serialized_end=1173,
)


_ACCEPTANCEFILTERBYPASSCOMMAND = _descriptor.Descriptor(
  name='AcceptanceFilterBypassCommand',
  full_name='openxc.AcceptanceFilterBypassCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.AcceptanceFilterBypassCommand.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bypass', full_name='openxc.AcceptanceFilterBypassCommand.bypass', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1175,
  serialized_end=1235,
)


_PAYLOADFORMATCOMMAND = _descriptor.Descriptor(
  name='PayloadFormatCommand',
  full_name='openxc.PayloadFormatCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='openxc.PayloadFormatCommand.format', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PAYLOADFORMATCOMMAND_PAYLOADFORMAT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1237,
  serialized_end=1360,
)


_COMMANDRESPONSE = _descriptor.Descriptor(
  name='CommandResponse',
  full_name='openxc.CommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.CommandResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='openxc.CommandResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='openxc.CommandResponse.status', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1362,
  serialized_end=1455,
)


_DIAGNOSTICREQUEST = _descriptor.Descriptor(
  name='DiagnosticRequest',
  full_name='openxc.DiagnosticRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.DiagnosticRequest.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='openxc.DiagnosticRequest.message_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='openxc.DiagnosticRequest.mode', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pid', full_name='openxc.DiagnosticRequest.pid', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='openxc.DiagnosticRequest.payload', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiple_responses', full_name='openxc.DiagnosticRequest.multiple_responses', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='openxc.DiagnosticRequest.frequency', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.DiagnosticRequest.name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decoded_type', full_name='openxc.DiagnosticRequest.decoded_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DIAGNOSTICREQUEST_DECODEDTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1458,
  serialized_end=1711,
)


_DIAGNOSTICRESPONSE = _descriptor.Descriptor(
  name='DiagnosticResponse',
  full_name='openxc.DiagnosticResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.DiagnosticResponse.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='openxc.DiagnosticResponse.message_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='openxc.DiagnosticResponse.mode', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pid', full_name='openxc.DiagnosticResponse.pid', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='success', full_name='openxc.DiagnosticResponse.success', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negative_response_code', full_name='openxc.DiagnosticResponse.negative_response_code', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='openxc.DiagnosticResponse.payload', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openxc.DiagnosticResponse.value', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1714,
  serialized_end=1875,
)


_DYNAMICFIELD = _descriptor.Descriptor(
  name='DynamicField',
  full_name='openxc.DynamicField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.DynamicField.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='openxc.DynamicField.string_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numeric_value', full_name='openxc.DynamicField.numeric_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boolean_value', full_name='openxc.DynamicField.boolean_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DYNAMICFIELD_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1878,
  serialized_end=2040,
)


_TRANSLATEDMESSAGE = _descriptor.Descriptor(
  name='TranslatedMessage',
  full_name='openxc.TranslatedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.TranslatedMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.TranslatedMessage.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openxc.TranslatedMessage.value', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='openxc.TranslatedMessage.event', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSLATEDMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=2043,
  serialized_end=2290,
)

_VEHICLEMESSAGE.fields_by_name['type'].enum_type = _VEHICLEMESSAGE_TYPE
_VEHICLEMESSAGE.fields_by_name['raw_message'].message_type = _RAWMESSAGE
_VEHICLEMESSAGE.fields_by_name['translated_message'].message_type = _TRANSLATEDMESSAGE
_VEHICLEMESSAGE.fields_by_name['diagnostic_response'].message_type = _DIAGNOSTICRESPONSE
_VEHICLEMESSAGE.fields_by_name['control_command'].message_type = _CONTROLCOMMAND
_VEHICLEMESSAGE.fields_by_name['command_response'].message_type = _COMMANDRESPONSE
_VEHICLEMESSAGE_TYPE.containing_type = _VEHICLEMESSAGE;
_CONTROLCOMMAND.fields_by_name['type'].enum_type = _CONTROLCOMMAND_TYPE
_CONTROLCOMMAND.fields_by_name['diagnostic_request'].message_type = _DIAGNOSTICCONTROLCOMMAND
_CONTROLCOMMAND.fields_by_name['passthrough_mode_request'].message_type = _PASSTHROUGHMODECONTROLCOMMAND
_CONTROLCOMMAND.fields_by_name['acceptance_filter_bypass_command'].message_type = _ACCEPTANCEFILTERBYPASSCOMMAND
_CONTROLCOMMAND.fields_by_name['message_format_command'].message_type = _PAYLOADFORMATCOMMAND
_CONTROLCOMMAND_TYPE.containing_type = _CONTROLCOMMAND;
_DIAGNOSTICCONTROLCOMMAND.fields_by_name['request'].message_type = _DIAGNOSTICREQUEST
_DIAGNOSTICCONTROLCOMMAND.fields_by_name['action'].enum_type = _DIAGNOSTICCONTROLCOMMAND_ACTION
_DIAGNOSTICCONTROLCOMMAND_ACTION.containing_type = _DIAGNOSTICCONTROLCOMMAND;
_PAYLOADFORMATCOMMAND.fields_by_name['format'].enum_type = _PAYLOADFORMATCOMMAND_PAYLOADFORMAT
_PAYLOADFORMATCOMMAND_PAYLOADFORMAT.containing_type = _PAYLOADFORMATCOMMAND;
_COMMANDRESPONSE.fields_by_name['type'].enum_type = _CONTROLCOMMAND_TYPE
_DIAGNOSTICREQUEST.fields_by_name['decoded_type'].enum_type = _DIAGNOSTICREQUEST_DECODEDTYPE
_DIAGNOSTICREQUEST_DECODEDTYPE.containing_type = _DIAGNOSTICREQUEST;
_DYNAMICFIELD.fields_by_name['type'].enum_type = _DYNAMICFIELD_TYPE
_DYNAMICFIELD_TYPE.containing_type = _DYNAMICFIELD;
_TRANSLATEDMESSAGE.fields_by_name['type'].enum_type = _TRANSLATEDMESSAGE_TYPE
_TRANSLATEDMESSAGE.fields_by_name['value'].message_type = _DYNAMICFIELD
_TRANSLATEDMESSAGE.fields_by_name['event'].message_type = _DYNAMICFIELD
_TRANSLATEDMESSAGE_TYPE.containing_type = _TRANSLATEDMESSAGE;
DESCRIPTOR.message_types_by_name['VehicleMessage'] = _VEHICLEMESSAGE
DESCRIPTOR.message_types_by_name['RawMessage'] = _RAWMESSAGE
DESCRIPTOR.message_types_by_name['ControlCommand'] = _CONTROLCOMMAND
DESCRIPTOR.message_types_by_name['DiagnosticControlCommand'] = _DIAGNOSTICCONTROLCOMMAND
DESCRIPTOR.message_types_by_name['PassthroughModeControlCommand'] = _PASSTHROUGHMODECONTROLCOMMAND
DESCRIPTOR.message_types_by_name['AcceptanceFilterBypassCommand'] = _ACCEPTANCEFILTERBYPASSCOMMAND
DESCRIPTOR.message_types_by_name['PayloadFormatCommand'] = _PAYLOADFORMATCOMMAND
DESCRIPTOR.message_types_by_name['CommandResponse'] = _COMMANDRESPONSE
DESCRIPTOR.message_types_by_name['DiagnosticRequest'] = _DIAGNOSTICREQUEST
DESCRIPTOR.message_types_by_name['DiagnosticResponse'] = _DIAGNOSTICRESPONSE
DESCRIPTOR.message_types_by_name['DynamicField'] = _DYNAMICFIELD
DESCRIPTOR.message_types_by_name['TranslatedMessage'] = _TRANSLATEDMESSAGE

class VehicleMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VEHICLEMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.VehicleMessage)

class RawMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RAWMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.RawMessage)

class ControlCommand(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTROLCOMMAND

  # @@protoc_insertion_point(class_scope:openxc.ControlCommand)

class DiagnosticControlCommand(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIAGNOSTICCONTROLCOMMAND

  # @@protoc_insertion_point(class_scope:openxc.DiagnosticControlCommand)

class PassthroughModeControlCommand(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PASSTHROUGHMODECONTROLCOMMAND

  # @@protoc_insertion_point(class_scope:openxc.PassthroughModeControlCommand)

class AcceptanceFilterBypassCommand(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACCEPTANCEFILTERBYPASSCOMMAND

  # @@protoc_insertion_point(class_scope:openxc.AcceptanceFilterBypassCommand)

class PayloadFormatCommand(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PAYLOADFORMATCOMMAND

  # @@protoc_insertion_point(class_scope:openxc.PayloadFormatCommand)

class CommandResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMANDRESPONSE

  # @@protoc_insertion_point(class_scope:openxc.CommandResponse)

class DiagnosticRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIAGNOSTICREQUEST

  # @@protoc_insertion_point(class_scope:openxc.DiagnosticRequest)

class DiagnosticResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIAGNOSTICRESPONSE

  # @@protoc_insertion_point(class_scope:openxc.DiagnosticResponse)

class DynamicField(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DYNAMICFIELD

  # @@protoc_insertion_point(class_scope:openxc.DynamicField)

class TranslatedMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSLATEDMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.TranslatedMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\ncom.openxcB\016BinaryMessages')
# @@protoc_insertion_point(module_scope)
