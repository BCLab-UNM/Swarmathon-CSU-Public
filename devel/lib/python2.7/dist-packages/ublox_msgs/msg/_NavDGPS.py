# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ublox_msgs/NavDGPS.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ublox_msgs.msg

class NavDGPS(genpy.Message):
  _md5sum = "b0aba8454084620f2a8eb7ff6445368c"
  _type = "ublox_msgs/NavDGPS"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# NAV-DGPS (0x01 0x31)
# DGPS Data Used for NAV
#
# This message outputs the Correction data as it has been applied to the current NAV
# Solution. See also the notes on the RTCM protocol.
#

uint8 CLASS_ID = 1
uint8 MESSAGE_ID = 31

uint32 iTOW             # GPS Millisecond time of week [ms]

int32 age               # Age of newest correction data [ms]
int16 baseId            # DGPS Base Station ID
int16 baseHealth        # DGPS Base Station Health Status
int8 numCh              # Number of channels for which correction data is following

uint8 status            # DGPS Correction Type Status
uint8 DGPS_CORRECTION_NONE = 0
uint8 DGPS_CORRECTION_PR_PRR = 1

uint16 reserved1        # Reserved

NavDGPS_SV[] sv

================================================================================
MSG: ublox_msgs/NavDGPS_SV
# see message NavDGPS

uint8 svid              # Satellite ID

uint8 flags             # Bitmask / Channel Number
uint8 CHANNEL1 = 1
uint8 CHANNEL2 = 2
uint8 CHANNEL3 = 3
uint8 CHANNEL4 = 4
uint8 CHANNEL5 = 5
uint8 CHANNEL6 = 6
uint8 CHANNEL7 = 7
uint8 CHANNEL8 = 8
uint8 DGPS = 16

uint16 ageC             # Age of latest correction data [ms]
float32 prc             # Pseudo Range Correction [m]
float32 prrc            # Pseudo Range Rate Correction [m/s]

"""
  # Pseudo-constants
  CLASS_ID = 1
  MESSAGE_ID = 31
  DGPS_CORRECTION_NONE = 0
  DGPS_CORRECTION_PR_PRR = 1

  __slots__ = ['iTOW','age','baseId','baseHealth','numCh','status','reserved1','sv']
  _slot_types = ['uint32','int32','int16','int16','int8','uint8','uint16','ublox_msgs/NavDGPS_SV[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       iTOW,age,baseId,baseHealth,numCh,status,reserved1,sv

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(NavDGPS, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.iTOW is None:
        self.iTOW = 0
      if self.age is None:
        self.age = 0
      if self.baseId is None:
        self.baseId = 0
      if self.baseHealth is None:
        self.baseHealth = 0
      if self.numCh is None:
        self.numCh = 0
      if self.status is None:
        self.status = 0
      if self.reserved1 is None:
        self.reserved1 = 0
      if self.sv is None:
        self.sv = []
    else:
      self.iTOW = 0
      self.age = 0
      self.baseId = 0
      self.baseHealth = 0
      self.numCh = 0
      self.status = 0
      self.reserved1 = 0
      self.sv = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_Ii2hbBH.pack(_x.iTOW, _x.age, _x.baseId, _x.baseHealth, _x.numCh, _x.status, _x.reserved1))
      length = len(self.sv)
      buff.write(_struct_I.pack(length))
      for val1 in self.sv:
        _x = val1
        buff.write(_struct_2BH2f.pack(_x.svid, _x.flags, _x.ageC, _x.prc, _x.prrc))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.sv is None:
        self.sv = None
      end = 0
      _x = self
      start = end
      end += 16
      (_x.iTOW, _x.age, _x.baseId, _x.baseHealth, _x.numCh, _x.status, _x.reserved1,) = _struct_Ii2hbBH.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.sv = []
      for i in range(0, length):
        val1 = ublox_msgs.msg.NavDGPS_SV()
        _x = val1
        start = end
        end += 12
        (_x.svid, _x.flags, _x.ageC, _x.prc, _x.prrc,) = _struct_2BH2f.unpack(str[start:end])
        self.sv.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_Ii2hbBH.pack(_x.iTOW, _x.age, _x.baseId, _x.baseHealth, _x.numCh, _x.status, _x.reserved1))
      length = len(self.sv)
      buff.write(_struct_I.pack(length))
      for val1 in self.sv:
        _x = val1
        buff.write(_struct_2BH2f.pack(_x.svid, _x.flags, _x.ageC, _x.prc, _x.prrc))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.sv is None:
        self.sv = None
      end = 0
      _x = self
      start = end
      end += 16
      (_x.iTOW, _x.age, _x.baseId, _x.baseHealth, _x.numCh, _x.status, _x.reserved1,) = _struct_Ii2hbBH.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.sv = []
      for i in range(0, length):
        val1 = ublox_msgs.msg.NavDGPS_SV()
        _x = val1
        start = end
        end += 12
        (_x.svid, _x.flags, _x.ageC, _x.prc, _x.prrc,) = _struct_2BH2f.unpack(str[start:end])
        self.sv.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2BH2f = struct.Struct("<2BH2f")
_struct_Ii2hbBH = struct.Struct("<Ii2hbBH")