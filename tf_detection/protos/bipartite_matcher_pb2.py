# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tf_detection/protos/bipartite_matcher.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tf_detection/protos/bipartite_matcher.proto',
  package='tf_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n/tf_detection/protos/bipartite_matcher.proto\x12\x17tf_detection.protos\"\x12\n\x10\x42ipartiteMatcher')
)




_BIPARTITEMATCHER = _descriptor.Descriptor(
  name='BipartiteMatcher',
  full_name='tf_detection.protos.BipartiteMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['BipartiteMatcher'] = _BIPARTITEMATCHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BipartiteMatcher = _reflection.GeneratedProtocolMessageType('BipartiteMatcher', (_message.Message,), dict(
  DESCRIPTOR = _BIPARTITEMATCHER,
  __module__ = 'tf_detection.protos.bipartite_matcher_pb2'
  # @@protoc_insertion_point(class_scope:tf_detection.protos.BipartiteMatcher)
  ))
_sym_db.RegisterMessage(BipartiteMatcher)


# @@protoc_insertion_point(module_scope)
