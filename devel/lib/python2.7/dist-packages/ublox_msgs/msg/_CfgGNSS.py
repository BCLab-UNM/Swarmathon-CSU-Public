# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ublox_msgs/CfgGNSS.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CfgGNSS(genpy.Message):
  _md5sum = "b7f92af0b44aa7c047fd14c5926fb0fc"
  _type = "ublox_msgs/CfgGNSS"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# CFG-GNSS (0x06 0x3E)
# GNSS Configuration
# Gets or sets the GNSS system channel sharing configuration.

uint8 CLASS_ID = 6
uint8 MESSAGE_ID = 62

uint8 msgVer            # Message version (= 0 for this version)
uint8 numTrkChHw        # Number of tracking channels in hardware (read only)
uint8 numTrkChUse       # Number of tracking channels to use (<= numTrkChHw)
uint8 numConfigBlocks   # Number of configuration blocks following (set to 1)

uint8 gnssId            # GNSS identifier (select from following list)

uint8 GNSS_ID_GPS = 0
uint8 GNSS_ID_SBAS = 1
uint8 GNSS_ID_GALILEO = 2
uint8 GNSS_ID_BEIDOU = 3
uint8 GNSS_ID_QZSS = 5
uint8 GNSS_ID_GLONASS = 6

uint8 resTrkCh          # Number of reserved (minimum) tracking channels for this GNSS system
uint8 maxTrkCh          # Maximum number of tracking channels (>=resTrkChn)
uint8 reserved1         # Reserved
uint32 flags            # Bitfield of flags (bit 0 = enable/disable)"""
  # Pseudo-constants
  CLASS_ID = 6
  MESSAGE_ID = 62
  GNSS_ID_GPS = 0
  GNSS_ID_SBAS = 1
  GNSS_ID_GALILEO = 2
  GNSS_ID_BEIDOU = 3
  GNSS_ID_QZSS = 5
  GNSS_ID_GLONASS = 6

  __slots__ = ['msgVer','numTrkChHw','numTrkChUse','numConfigBlocks','gnssId','resTrkCh','maxTrkCh','reserved1','flags']
  _slot_types = ['uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       msgVer,numTrkChHw,numTrkChUse,numConfigBlocks,gnssId,resTrkCh,maxTrkCh,reserved1,flags

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CfgGNSS, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.msgVer is None:
        self.msgVer = 0
      if self.numTrkChHw is None:
        self.numTrkChHw = 0
      if self.numTrkChUse is None:
        self.numTrkChUse = 0
      if self.numConfigBlocks is None:
        self.numConfigBlocks = 0
      if self.gnssId is None:
        self.gnssId = 0
      if self.resTrkCh is None:
        self.resTrkCh = 0
      if self.maxTrkCh is None:
        self.maxTrkCh = 0
      if self.reserved1 is None:
        self.reserved1 = 0
      if self.flags is None:
        self.flags = 0
    else:
      self.msgVer = 0
      self.numTrkChHw = 0
      self.numTrkChUse = 0
      self.numConfigBlocks = 0
      self.gnssId = 0
      self.resTrkCh = 0
      self.maxTrkCh = 0
      self.reserved1 = 0
      self.flags = 0

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
      buff.write(_struct_8BI.pack(_x.msgVer, _x.numTrkChHw, _x.numTrkChUse, _x.numConfigBlocks, _x.gnssId, _x.resTrkCh, _x.maxTrkCh, _x.reserved1, _x.flags))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.msgVer, _x.numTrkChHw, _x.numTrkChUse, _x.numConfigBlocks, _x.gnssId, _x.resTrkCh, _x.maxTrkCh, _x.reserved1, _x.flags,) = _struct_8BI.unpack(str[start:end])
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
      buff.write(_struct_8BI.pack(_x.msgVer, _x.numTrkChHw, _x.numTrkChUse, _x.numConfigBlocks, _x.gnssId, _x.resTrkCh, _x.maxTrkCh, _x.reserved1, _x.flags))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.msgVer, _x.numTrkChHw, _x.numTrkChUse, _x.numConfigBlocks, _x.gnssId, _x.resTrkCh, _x.maxTrkCh, _x.reserved1, _x.flags,) = _struct_8BI.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_8BI = struct.Struct("<8BI")
