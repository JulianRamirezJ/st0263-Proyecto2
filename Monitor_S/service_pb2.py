# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\"\x16\n\x05\x41live\x12\r\n\x05\x61live\x18\x01 \x01(\t\"\x1a\n\x06Metric\x12\x10\n\x08\x64\x65livery\x18\x01 \x01(\x03\"\x06\n\x04Nulo2B\n\x07Monitor\x12\x1c\n\nget_metric\x12\x05.Nulo\x1a\x07.Metric\x12\x19\n\x08is_alive\x12\x05.Nulo\x1a\x06.Aliveb\x06proto3'
)




_ALIVE = _descriptor.Descriptor(
  name='Alive',
  full_name='Alive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alive', full_name='Alive.alive', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=17,
  serialized_end=39,
)


_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='delivery', full_name='Metric.delivery', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=41,
  serialized_end=67,
)


_NULO = _descriptor.Descriptor(
  name='Nulo',
  full_name='Nulo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=69,
  serialized_end=75,
)

DESCRIPTOR.message_types_by_name['Alive'] = _ALIVE
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['Nulo'] = _NULO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Alive = _reflection.GeneratedProtocolMessageType('Alive', (_message.Message,), {
  'DESCRIPTOR' : _ALIVE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Alive)
  })
_sym_db.RegisterMessage(Alive)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Metric)
  })
_sym_db.RegisterMessage(Metric)

Nulo = _reflection.GeneratedProtocolMessageType('Nulo', (_message.Message,), {
  'DESCRIPTOR' : _NULO,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Nulo)
  })
_sym_db.RegisterMessage(Nulo)



_MONITOR = _descriptor.ServiceDescriptor(
  name='Monitor',
  full_name='Monitor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=77,
  serialized_end=143,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_metric',
    full_name='Monitor.get_metric',
    index=0,
    containing_service=None,
    input_type=_NULO,
    output_type=_METRIC,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='is_alive',
    full_name='Monitor.is_alive',
    index=1,
    containing_service=None,
    input_type=_NULO,
    output_type=_ALIVE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MONITOR)

DESCRIPTOR.services_by_name['Monitor'] = _MONITOR

# @@protoc_insertion_point(module_scope)
