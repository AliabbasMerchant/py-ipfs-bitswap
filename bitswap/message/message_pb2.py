# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message/message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message/message.proto',
  package='bitswap',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x15message/message.proto\x12\x07\x62itswap\"\x9d\x02\n\x07Message\x12+\n\x08wantlist\x18\x01 \x01(\x0b\x32\x19.bitswap.Message.Wantlist\x12\x0e\n\x06\x62locks\x18\x02 \x03(\x0c\x12\'\n\x07payload\x18\x03 \x03(\x0b\x32\x16.bitswap.Message.Block\x1a\x84\x01\n\x08Wantlist\x12\x30\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1f.bitswap.Message.Wantlist.Entry\x12\x0c\n\x04\x66ull\x18\x02 \x01(\x08\x1a\x38\n\x05\x45ntry\x12\r\n\x05\x62lock\x18\x01 \x01(\x0c\x12\x10\n\x08priority\x18\x02 \x01(\x05\x12\x0e\n\x06\x63\x61ncel\x18\x03 \x01(\x08\x1a%\n\x05\x42lock\x12\x0e\n\x06prefix\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c')
)




_MESSAGE_WANTLIST_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='bitswap.Message.Wantlist.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block', full_name='bitswap.Message.Wantlist.Entry.block', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='bitswap.Message.Wantlist.Entry.priority', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cancel', full_name='bitswap.Message.Wantlist.Entry.cancel', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=281,
)

_MESSAGE_WANTLIST = _descriptor.Descriptor(
  name='Wantlist',
  full_name='bitswap.Message.Wantlist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='bitswap.Message.Wantlist.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full', full_name='bitswap.Message.Wantlist.full', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGE_WANTLIST_ENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=281,
)

_MESSAGE_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='bitswap.Message.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prefix', full_name='bitswap.Message.Block.prefix', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='bitswap.Message.Block.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=320,
)

_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='bitswap.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wantlist', full_name='bitswap.Message.wantlist', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocks', full_name='bitswap.Message.blocks', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='bitswap.Message.payload', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGE_WANTLIST, _MESSAGE_BLOCK, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=320,
)

_MESSAGE_WANTLIST_ENTRY.containing_type = _MESSAGE_WANTLIST
_MESSAGE_WANTLIST.fields_by_name['entries'].message_type = _MESSAGE_WANTLIST_ENTRY
_MESSAGE_WANTLIST.containing_type = _MESSAGE
_MESSAGE_BLOCK.containing_type = _MESSAGE
_MESSAGE.fields_by_name['wantlist'].message_type = _MESSAGE_WANTLIST
_MESSAGE.fields_by_name['payload'].message_type = _MESSAGE_BLOCK
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(

  Wantlist = _reflection.GeneratedProtocolMessageType('Wantlist', (_message.Message,), dict(

    Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), dict(
      DESCRIPTOR = _MESSAGE_WANTLIST_ENTRY,
      __module__ = 'message.message_pb2'
      # @@protoc_insertion_point(class_scope:bitswap.Message.Wantlist.Entry)
      ))
    ,
    DESCRIPTOR = _MESSAGE_WANTLIST,
    __module__ = 'message.message_pb2'
    # @@protoc_insertion_point(class_scope:bitswap.Message.Wantlist)
    ))
  ,

  Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
    DESCRIPTOR = _MESSAGE_BLOCK,
    __module__ = 'message.message_pb2'
    # @@protoc_insertion_point(class_scope:bitswap.Message.Block)
    ))
  ,
  DESCRIPTOR = _MESSAGE,
  __module__ = 'message.message_pb2'
  # @@protoc_insertion_point(class_scope:bitswap.Message)
  ))
_sym_db.RegisterMessage(Message)
_sym_db.RegisterMessage(Message.Wantlist)
_sym_db.RegisterMessage(Message.Wantlist.Entry)
_sym_db.RegisterMessage(Message.Block)


# @@protoc_insertion_point(module_scope)
