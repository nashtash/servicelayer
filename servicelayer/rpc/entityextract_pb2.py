# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: servicelayer/rpc/entityextract.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from servicelayer.rpc import common_pb2 as servicelayer_dot_rpc_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='servicelayer/rpc/entityextract.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$servicelayer/rpc/entityextract.proto\x1a\x1dservicelayer/rpc/common.proto\"\xf7\x01\n\x0f\x45xtractedEntity\x12\x0c\n\x04text\x18\x01 \x01(\t\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.ExtractedEntity.Type\x12\r\n\x05start\x18\x03 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x04\"\x94\x01\n\x04Type\x12\t\n\x05OTHER\x10\x00\x12\n\n\x06PERSON\x10\x01\x12\x10\n\x0cORGANIZATION\x10\x02\x12\x0b\n\x07\x43OMPANY\x10\x03\x12\x0c\n\x08LOCATION\x10\x04\x12\x0b\n\x07\x43OUNTRY\x10\x05\x12\x0c\n\x08LANGUAGE\x10\x06\x12\r\n\tIPADDRESS\x10\x07\x12\t\n\x05PHONE\x10\x08\x12\t\n\x05\x45MAIL\x10\t\x12\x08\n\x04IBAN\x10\n25\n\rEntityExtract\x12$\n\x07\x45xtract\x12\x05.Text\x1a\x10.ExtractedEntity0\x01\x62\x06proto3')
  ,
  dependencies=[servicelayer_dot_rpc_dot_common__pb2.DESCRIPTOR,])



_EXTRACTEDENTITY_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ExtractedEntity.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERSON', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORGANIZATION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPANY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUNTRY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LANGUAGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IPADDRESS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMAIL', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IBAN', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=171,
  serialized_end=319,
)
_sym_db.RegisterEnumDescriptor(_EXTRACTEDENTITY_TYPE)


_EXTRACTEDENTITY = _descriptor.Descriptor(
  name='ExtractedEntity',
  full_name='ExtractedEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='ExtractedEntity.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ExtractedEntity.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='ExtractedEntity.start', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='ExtractedEntity.end', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTRACTEDENTITY_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=319,
)

_EXTRACTEDENTITY.fields_by_name['type'].enum_type = _EXTRACTEDENTITY_TYPE
_EXTRACTEDENTITY_TYPE.containing_type = _EXTRACTEDENTITY
DESCRIPTOR.message_types_by_name['ExtractedEntity'] = _EXTRACTEDENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtractedEntity = _reflection.GeneratedProtocolMessageType('ExtractedEntity', (_message.Message,), dict(
  DESCRIPTOR = _EXTRACTEDENTITY,
  __module__ = 'servicelayer.rpc.entityextract_pb2'
  # @@protoc_insertion_point(class_scope:ExtractedEntity)
  ))
_sym_db.RegisterMessage(ExtractedEntity)



_ENTITYEXTRACT = _descriptor.ServiceDescriptor(
  name='EntityExtract',
  full_name='EntityExtract',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=321,
  serialized_end=374,
  methods=[
  _descriptor.MethodDescriptor(
    name='Extract',
    full_name='EntityExtract.Extract',
    index=0,
    containing_service=None,
    input_type=servicelayer_dot_rpc_dot_common__pb2._TEXT,
    output_type=_EXTRACTEDENTITY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENTITYEXTRACT)

DESCRIPTOR.services_by_name['EntityExtract'] = _ENTITYEXTRACT

# @@protoc_insertion_point(module_scope)
