# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: servicelayer/rpc/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='servicelayer/rpc/common.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dservicelayer/rpc/common.proto\":\n\x04Text\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x11\n\tlanguages\x18\x02 \x03(\t\x12\x11\n\tcountries\x18\x03 \x03(\tb\x06proto3')
)




_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Text.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='languages', full_name='Text.languages', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='countries', full_name='Text.countries', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=91,
)

DESCRIPTOR.message_types_by_name['Text'] = _TEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), dict(
  DESCRIPTOR = _TEXT,
  __module__ = 'servicelayer.rpc.common_pb2'
  # @@protoc_insertion_point(class_scope:Text)
  ))
_sym_db.RegisterMessage(Text)


# @@protoc_insertion_point(module_scope)
