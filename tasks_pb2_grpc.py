# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tasks_pb2 as tasks__pb2


class TasksStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createTask = channel.unary_unary(
                '/grpcPackage1.Tasks/createTask',
                request_serializer=tasks__pb2.Task.SerializeToString,
                response_deserializer=tasks__pb2.Task.FromString,
                )
        self.returnTask = channel.unary_unary(
                '/grpcPackage1.Tasks/returnTask',
                request_serializer=tasks__pb2.voidNoParam.SerializeToString,
                response_deserializer=tasks__pb2.voidNoParam.FromString,
                )
        self.getTask = channel.unary_unary(
                '/grpcPackage1.Tasks/getTask',
                request_serializer=tasks__pb2.getTaskRequest.SerializeToString,
                response_deserializer=tasks__pb2.TasksList.FromString,
                )
        self.getTasks = channel.unary_unary(
                '/grpcPackage1.Tasks/getTasks',
                request_serializer=tasks__pb2.getAllTasksByUser.SerializeToString,
                response_deserializer=tasks__pb2.TasksList.FromString,
                )
        self.getTasksByUser = channel.unary_unary(
                '/grpcPackage1.Tasks/getTasksByUser',
                request_serializer=tasks__pb2.getAllTasksByUser.SerializeToString,
                response_deserializer=tasks__pb2.TasksList.FromString,
                )
        self.updateTask = channel.unary_unary(
                '/grpcPackage1.Tasks/updateTask',
                request_serializer=tasks__pb2.UpdateTaskRequest.SerializeToString,
                response_deserializer=tasks__pb2.Task.FromString,
                )
        self.deleteSpecificTask = channel.unary_unary(
                '/grpcPackage1.Tasks/deleteSpecificTask',
                request_serializer=tasks__pb2.getTaskRequest.SerializeToString,
                response_deserializer=tasks__pb2.voidNoParam.FromString,
                )
        self.deleteallTasksByUser = channel.unary_unary(
                '/grpcPackage1.Tasks/deleteallTasksByUser',
                request_serializer=tasks__pb2.getAllTasksByUser.SerializeToString,
                response_deserializer=tasks__pb2.voidNoParam.FromString,
                )
        self.flushTaskContent = channel.unary_unary(
                '/grpcPackage1.Tasks/flushTaskContent',
                request_serializer=tasks__pb2.voidNoParam.SerializeToString,
                response_deserializer=tasks__pb2.voidNoParam.FromString,
                )
        self.returnError = channel.unary_unary(
                '/grpcPackage1.Tasks/returnError',
                request_serializer=tasks__pb2.voidNoParam.SerializeToString,
                response_deserializer=tasks__pb2.voidNoParam.FromString,
                )


class TasksServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def returnTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTasksByUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteSpecificTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteallTasksByUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def flushTaskContent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def returnError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TasksServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createTask': grpc.unary_unary_rpc_method_handler(
                    servicer.createTask,
                    request_deserializer=tasks__pb2.Task.FromString,
                    response_serializer=tasks__pb2.Task.SerializeToString,
            ),
            'returnTask': grpc.unary_unary_rpc_method_handler(
                    servicer.returnTask,
                    request_deserializer=tasks__pb2.voidNoParam.FromString,
                    response_serializer=tasks__pb2.voidNoParam.SerializeToString,
            ),
            'getTask': grpc.unary_unary_rpc_method_handler(
                    servicer.getTask,
                    request_deserializer=tasks__pb2.getTaskRequest.FromString,
                    response_serializer=tasks__pb2.TasksList.SerializeToString,
            ),
            'getTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.getTasks,
                    request_deserializer=tasks__pb2.getAllTasksByUser.FromString,
                    response_serializer=tasks__pb2.TasksList.SerializeToString,
            ),
            'getTasksByUser': grpc.unary_unary_rpc_method_handler(
                    servicer.getTasksByUser,
                    request_deserializer=tasks__pb2.getAllTasksByUser.FromString,
                    response_serializer=tasks__pb2.TasksList.SerializeToString,
            ),
            'updateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.updateTask,
                    request_deserializer=tasks__pb2.UpdateTaskRequest.FromString,
                    response_serializer=tasks__pb2.Task.SerializeToString,
            ),
            'deleteSpecificTask': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteSpecificTask,
                    request_deserializer=tasks__pb2.getTaskRequest.FromString,
                    response_serializer=tasks__pb2.voidNoParam.SerializeToString,
            ),
            'deleteallTasksByUser': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteallTasksByUser,
                    request_deserializer=tasks__pb2.getAllTasksByUser.FromString,
                    response_serializer=tasks__pb2.voidNoParam.SerializeToString,
            ),
            'flushTaskContent': grpc.unary_unary_rpc_method_handler(
                    servicer.flushTaskContent,
                    request_deserializer=tasks__pb2.voidNoParam.FromString,
                    response_serializer=tasks__pb2.voidNoParam.SerializeToString,
            ),
            'returnError': grpc.unary_unary_rpc_method_handler(
                    servicer.returnError,
                    request_deserializer=tasks__pb2.voidNoParam.FromString,
                    response_serializer=tasks__pb2.voidNoParam.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcPackage1.Tasks', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Tasks(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcPackage1.Tasks/createTask',
            tasks__pb2.Task.SerializeToString,
            tasks__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def returnTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcPackage1.Tasks/returnTask',
            tasks__pb2.voidNoParam.SerializeToString,
            tasks__pb2.voidNoParam.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcPackage1.Tasks/getTask',
            tasks__pb2.getTaskRequest.SerializeToString,
            tasks__pb2.TasksList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcPackage1.Tasks/getTasks',
            tasks__pb2.getAllTasksByUser.SerializeToString,
            tasks__pb2.TasksList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTasksByUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcPackage1.Tasks/getTasksByUser',
            tasks__pb2.getAllTasksByUser.SerializeToString,
            tasks__pb2.TasksList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcPackage1.Tasks/updateTask',
            tasks__pb2.UpdateTaskRequest.SerializeToString,
            tasks__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteSpecificTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcPackage1.Tasks/deleteSpecificTask',
            tasks__pb2.getTaskRequest.SerializeToString,
            tasks__pb2.voidNoParam.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteallTasksByUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcPackage1.Tasks/deleteallTasksByUser',
            tasks__pb2.getAllTasksByUser.SerializeToString,
            tasks__pb2.voidNoParam.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def flushTaskContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcPackage1.Tasks/flushTaskContent',
            tasks__pb2.voidNoParam.SerializeToString,
            tasks__pb2.voidNoParam.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def returnError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcPackage1.Tasks/returnError',
            tasks__pb2.voidNoParam.SerializeToString,
            tasks__pb2.voidNoParam.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
