# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngrpc.proto\x12\x0bgrpcPackage\"\r\n\x0bvoidNoParam\"0\n\x11UpdateUserRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07payload\x18\x02 \x01(\t\"\x1c\n\x0egetUserRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"#\n\x12returnErrorRequest\x12\r\n\x05\x45rror\x18\x01 \x01(\t\"#\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07payload\x18\x02 \x01(\t\"$\n\x05Items\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07payload\x18\x02 \x01(\t\"-\n\tItemsList\x12 \n\x05items\x18\x01 \x03(\x0b\x32\x11.grpcPackage.Item2\xc8\x03\n\x04Todo\x12\x35\n\ncreateItem\x12\x11.grpcPackage.Item\x1a\x12.grpcPackage.Items\"\x00\x12\x41\n\x0breturnItems\x12\x18.grpcPackage.voidNoParam\x1a\x16.grpcPackage.ItemsList\"\x00\x12<\n\x07getUser\x12\x1b.grpcPackage.getUserRequest\x1a\x12.grpcPackage.Items\"\x00\x12\x42\n\nupdateUser\x12\x1e.grpcPackage.UpdateUserRequest\x1a\x12.grpcPackage.Items\"\x00\x12\x35\n\ndeleteUser\x12\x11.grpcPackage.Item\x1a\x12.grpcPackage.Items\"\x00\x12\x43\n\x0breturnError\x12\x18.grpcPackage.voidNoParam\x1a\x18.grpcPackage.voidNoParam\"\x00\x12H\n\x10\x66lushUserContent\x12\x18.grpcPackage.voidNoParam\x1a\x18.grpcPackage.voidNoParam\"\x00\x62\x06proto3')



_VOIDNOPARAM = DESCRIPTOR.message_types_by_name['voidNoParam']
_UPDATEUSERREQUEST = DESCRIPTOR.message_types_by_name['UpdateUserRequest']
_GETUSERREQUEST = DESCRIPTOR.message_types_by_name['getUserRequest']
_RETURNERRORREQUEST = DESCRIPTOR.message_types_by_name['returnErrorRequest']
_ITEM = DESCRIPTOR.message_types_by_name['Item']
_ITEMS = DESCRIPTOR.message_types_by_name['Items']
_ITEMSLIST = DESCRIPTOR.message_types_by_name['ItemsList']
voidNoParam = _reflection.GeneratedProtocolMessageType('voidNoParam', (_message.Message,), {
  'DESCRIPTOR' : _VOIDNOPARAM,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpcPackage.voidNoParam)
  })
_sym_db.RegisterMessage(voidNoParam)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERREQUEST,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpcPackage.UpdateUserRequest)
  })
_sym_db.RegisterMessage(UpdateUserRequest)

getUserRequest = _reflection.GeneratedProtocolMessageType('getUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpcPackage.getUserRequest)
  })
_sym_db.RegisterMessage(getUserRequest)

returnErrorRequest = _reflection.GeneratedProtocolMessageType('returnErrorRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETURNERRORREQUEST,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpcPackage.returnErrorRequest)
  })
_sym_db.RegisterMessage(returnErrorRequest)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpcPackage.Item)
  })
_sym_db.RegisterMessage(Item)

Items = _reflection.GeneratedProtocolMessageType('Items', (_message.Message,), {
  'DESCRIPTOR' : _ITEMS,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpcPackage.Items)
  })
_sym_db.RegisterMessage(Items)

ItemsList = _reflection.GeneratedProtocolMessageType('ItemsList', (_message.Message,), {
  'DESCRIPTOR' : _ITEMSLIST,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:grpcPackage.ItemsList)
  })
_sym_db.RegisterMessage(ItemsList)

_TODO = DESCRIPTOR.services_by_name['Todo']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VOIDNOPARAM._serialized_start=27
  _VOIDNOPARAM._serialized_end=40
  _UPDATEUSERREQUEST._serialized_start=42
  _UPDATEUSERREQUEST._serialized_end=90
  _GETUSERREQUEST._serialized_start=92
  _GETUSERREQUEST._serialized_end=120
  _RETURNERRORREQUEST._serialized_start=122
  _RETURNERRORREQUEST._serialized_end=157
  _ITEM._serialized_start=159
  _ITEM._serialized_end=194
  _ITEMS._serialized_start=196
  _ITEMS._serialized_end=232
  _ITEMSLIST._serialized_start=234
  _ITEMSLIST._serialized_end=279
  _TODO._serialized_start=282
  _TODO._serialized_end=738
# @@protoc_insertion_point(module_scope)