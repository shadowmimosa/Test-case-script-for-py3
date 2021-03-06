#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def getRoomManagerGuardVO(self, roomOwnerKugoudId, managerKugouId):
    """
    Parameters:
     - roomOwnerKugoudId
     - managerKugouId
    """
    pass

  def getSendStarAndFollowVO(self, userKugouId, starKugouId):
    """
    Parameters:
     - userKugouId
     - starKugouId
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def getRoomManagerGuardVO(self, roomOwnerKugoudId, managerKugouId):
    """
    Parameters:
     - roomOwnerKugoudId
     - managerKugouId
    """
    self.send_getRoomManagerGuardVO(roomOwnerKugoudId, managerKugouId)
    return self.recv_getRoomManagerGuardVO()

  def send_getRoomManagerGuardVO(self, roomOwnerKugoudId, managerKugouId):
    self._oprot.writeMessageBegin('getRoomManagerGuardVO', TMessageType.CALL, self._seqid)
    args = getRoomManagerGuardVO_args()
    args.roomOwnerKugoudId = roomOwnerKugoudId
    args.managerKugouId = managerKugouId
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getRoomManagerGuardVO(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = getRoomManagerGuardVO_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getRoomManagerGuardVO failed: unknown result");

  def getSendStarAndFollowVO(self, userKugouId, starKugouId):
    """
    Parameters:
     - userKugouId
     - starKugouId
    """
    self.send_getSendStarAndFollowVO(userKugouId, starKugouId)
    return self.recv_getSendStarAndFollowVO()

  def send_getSendStarAndFollowVO(self, userKugouId, starKugouId):
    self._oprot.writeMessageBegin('getSendStarAndFollowVO', TMessageType.CALL, self._seqid)
    args = getSendStarAndFollowVO_args()
    args.userKugouId = userKugouId
    args.starKugouId = starKugouId
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getSendStarAndFollowVO(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = getSendStarAndFollowVO_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getSendStarAndFollowVO failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["getRoomManagerGuardVO"] = Processor.process_getRoomManagerGuardVO
    self._processMap["getSendStarAndFollowVO"] = Processor.process_getSendStarAndFollowVO

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_getRoomManagerGuardVO(self, seqid, iprot, oprot):
    args = getRoomManagerGuardVO_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getRoomManagerGuardVO_result()
    result.success = self._handler.getRoomManagerGuardVO(args.roomOwnerKugoudId, args.managerKugouId)
    oprot.writeMessageBegin("getRoomManagerGuardVO", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getSendStarAndFollowVO(self, seqid, iprot, oprot):
    args = getSendStarAndFollowVO_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getSendStarAndFollowVO_result()
    result.success = self._handler.getSendStarAndFollowVO(args.userKugouId, args.starKugouId)
    oprot.writeMessageBegin("getSendStarAndFollowVO", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class getRoomManagerGuardVO_args:
  """
  Attributes:
   - roomOwnerKugoudId
   - managerKugouId
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'roomOwnerKugoudId', None, None, ), # 1
    (2, TType.I64, 'managerKugouId', None, None, ), # 2
  )

  def __init__(self, roomOwnerKugoudId=None, managerKugouId=None,):
    self.roomOwnerKugoudId = roomOwnerKugoudId
    self.managerKugouId = managerKugouId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.roomOwnerKugoudId = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.managerKugouId = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getRoomManagerGuardVO_args')
    if self.roomOwnerKugoudId is not None:
      oprot.writeFieldBegin('roomOwnerKugoudId', TType.I64, 1)
      oprot.writeI64(self.roomOwnerKugoudId)
      oprot.writeFieldEnd()
    if self.managerKugouId is not None:
      oprot.writeFieldBegin('managerKugouId', TType.I64, 2)
      oprot.writeI64(self.managerKugouId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.roomOwnerKugoudId)
    value = (value * 31) ^ hash(self.managerKugouId)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getRoomManagerGuardVO_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Services.roomtype.ttypes.RoomManagerGuardVO, Services.roomtype.ttypes.RoomManagerGuardVO.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Services.roomtype.ttypes.RoomManagerGuardVO()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getRoomManagerGuardVO_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getSendStarAndFollowVO_args:
  """
  Attributes:
   - userKugouId
   - starKugouId
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'userKugouId', None, None, ), # 1
    (2, TType.I64, 'starKugouId', None, None, ), # 2
  )

  def __init__(self, userKugouId=None, starKugouId=None,):
    self.userKugouId = userKugouId
    self.starKugouId = starKugouId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.userKugouId = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.starKugouId = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getSendStarAndFollowVO_args')
    if self.userKugouId is not None:
      oprot.writeFieldBegin('userKugouId', TType.I64, 1)
      oprot.writeI64(self.userKugouId)
      oprot.writeFieldEnd()
    if self.starKugouId is not None:
      oprot.writeFieldBegin('starKugouId', TType.I64, 2)
      oprot.writeI64(self.starKugouId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.userKugouId)
    value = (value * 31) ^ hash(self.starKugouId)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getSendStarAndFollowVO_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Services.roomtype.ttypes.SendStarAndFollowVO, Services.roomtype.ttypes.SendStarAndFollowVO.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Services.roomtype.ttypes.SendStarAndFollowVO()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getSendStarAndFollowVO_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
