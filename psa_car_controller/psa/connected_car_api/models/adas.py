# coding: utf-8

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Adas(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'abs': 'bool',
        'accr': 'str',
        'aebs': 'str',
        'afil': 'str',
        'artiv': 'str',
        'bsm': 'str',
        'esp': 'bool',
        'fse': 'bool',
        'lrka': 'str',
        'lvv': 'bool',
        'park_assist': 'AdasParkAssist',
        'rlka': 'str',
        'rvv': 'str',
        'sli': 'int'
    }

    attribute_map = {
        'abs': 'abs',
        'accr': 'accr',
        'aebs': 'aebs',
        'afil': 'afil',
        'artiv': 'artiv',
        'bsm': 'bsm',
        'esp': 'esp',
        'fse': 'fse',
        'lrka': 'lrka',
        'lvv': 'lvv',
        'park_assist': 'parkAssist',
        'rlka': 'rlka',
        'rvv': 'rvv',
        'sli': 'sli'
    }

    def __init__(self, abs=None, accr=None, aebs=None, afil=None, artiv='unavailable', bsm=None, esp=None, fse=None, lrka=None, lvv=None, park_assist=None, rlka=None, rvv=None, sli=None):  # noqa: E501
        """Adas - a model defined in Swagger"""  # noqa: E501

        self._abs = None
        self._accr = None
        self._aebs = None
        self._afil = None
        self._artiv = None
        self._bsm = None
        self._esp = None
        self._fse = None
        self._lrka = None
        self._lvv = None
        self._park_assist = None
        self._rlka = None
        self._rvv = None
        self._sli = None
        self.discriminator = None

        if abs is not None:
            self.abs = abs
        if accr is not None:
            self.accr = accr
        if aebs is not None:
            self.aebs = aebs
        if afil is not None:
            self.afil = afil
        if artiv is not None:
            self.artiv = artiv
        if bsm is not None:
            self.bsm = bsm
        if esp is not None:
            self.esp = esp
        if fse is not None:
            self.fse = fse
        if lrka is not None:
            self.lrka = lrka
        if lvv is not None:
            self.lvv = lvv
        if park_assist is not None:
            self.park_assist = park_assist
        if rlka is not None:
            self.rlka = rlka
        if rvv is not None:
            self.rvv = rvv
        if sli is not None:
            self.sli = sli

    @property
    def abs(self):
        """Gets the abs of this Adas.  # noqa: E501

        Anti-lock braking system  # noqa: E501

        :return: The abs of this Adas.  # noqa: E501
        :rtype: bool
        """
        return self._abs

    @abs.setter
    def abs(self, abs):
        """Sets the abs of this Adas.

        Anti-lock braking system  # noqa: E501

        :param abs: The abs of this Adas.  # noqa: E501
        :type: bool
        """

        self._abs = abs

    @property
    def accr(self):
        """Gets the accr of this Adas.  # noqa: E501

        Adaptive Cruise Control Regulation  # noqa: E501

        :return: The accr of this Adas.  # noqa: E501
        :rtype: str
        """
        return self._accr

    @accr.setter
    def accr(self, accr):
        """Sets the accr of this Adas.

        Adaptive Cruise Control Regulation  # noqa: E501

        :param accr: The accr of this Adas.  # noqa: E501
        :type: str
        """
        allowed_values = ["Activated", "Fault", "Hold", "HoldWithOverSpeeding", "Off"]  # noqa: E501
        if accr not in allowed_values:
            raise ValueError(
                "Invalid value for `accr` ({0}), must be one of {1}"  # noqa: E501
                .format(accr, allowed_values)
            )

        self._accr = accr

    @property
    def aebs(self):
        """Gets the aebs of this Adas.  # noqa: E501

        Advanced Emergency Braking System  # noqa: E501

        :return: The aebs of this Adas.  # noqa: E501
        :rtype: str
        """
        return self._aebs

    @aebs.setter
    def aebs(self, aebs):
        """Sets the aebs of this Adas.

        Advanced Emergency Braking System  # noqa: E501

        :param aebs: The aebs of this Adas.  # noqa: E501
        :type: str
        """
        allowed_values = ["off", "Fixed", "OnFlashing"]  # noqa: E501
        if aebs not in allowed_values:
            raise ValueError(
                "Invalid value for `aebs` ({0}), must be one of {1}"  # noqa: E501
                .format(aebs, allowed_values)
            )

        self._aebs = aebs

    @property
    def afil(self):
        """Gets the afil of this Adas.  # noqa: E501

        Lane Departure Warning System  # noqa: E501

        :return: The afil of this Adas.  # noqa: E501
        :rtype: str
        """
        return self._afil

    @afil.setter
    def afil(self, afil):
        """Sets the afil of this Adas.

        Lane Departure Warning System  # noqa: E501

        :param afil: The afil of this Adas.  # noqa: E501
        :type: str
        """
        allowed_values = ["FlashingFault", "FlashingWarning", "Off", "OnFixed"]  # noqa: E501
        if afil not in allowed_values:
            raise ValueError(
                "Invalid value for `afil` ({0}), must be one of {1}"  # noqa: E501
                .format(afil, allowed_values)
            )

        self._afil = afil

    @property
    def artiv(self):
        """Gets the artiv of this Adas.  # noqa: E501

        Respect of inter vehicle time assist (ARTIV)  # noqa: E501

        :return: The artiv of this Adas.  # noqa: E501
        :rtype: str
        """
        return self._artiv

    @artiv.setter
    def artiv(self, artiv):
        """Sets the artiv of this Adas.

        Respect of inter vehicle time assist (ARTIV)  # noqa: E501

        :param artiv: The artiv of this Adas.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSelected", "Selected", "Unavailable"]  # noqa: E501
        if artiv not in allowed_values:
            raise ValueError(
                "Invalid value for `artiv` ({0}), must be one of {1}"  # noqa: E501
                .format(artiv, allowed_values)
            )

        self._artiv = artiv

    @property
    def bsm(self):
        """Gets the bsm of this Adas.  # noqa: E501

        Blink SpotMonitoring  # noqa: E501

        :return: The bsm of this Adas.  # noqa: E501
        :rtype: str
        """
        return self._bsm

    @bsm.setter
    def bsm(self, bsm):
        """Sets the bsm of this Adas.

        Blink SpotMonitoring  # noqa: E501

        :param bsm: The bsm of this Adas.  # noqa: E501
        :type: str
        """
        allowed_values = ["Active", "Inactive", "Disabled"]  # noqa: E501
        if bsm not in allowed_values:
            raise ValueError(
                "Invalid value for `bsm` ({0}), must be one of {1}"  # noqa: E501
                .format(bsm, allowed_values)
            )

        self._bsm = bsm

    @property
    def esp(self):
        """Gets the esp of this Adas.  # noqa: E501

        Electronic Stability Programme  # noqa: E501

        :return: The esp of this Adas.  # noqa: E501
        :rtype: bool
        """
        return self._esp

    @esp.setter
    def esp(self, esp):
        """Sets the esp of this Adas.

        Electronic Stability Programme  # noqa: E501

        :param esp: The esp of this Adas.  # noqa: E501
        :type: bool
        """

        self._esp = esp

    @property
    def fse(self):
        """Gets the fse of this Adas.  # noqa: E501

        Electric brake application  # noqa: E501

        :return: The fse of this Adas.  # noqa: E501
        :rtype: bool
        """
        return self._fse

    @fse.setter
    def fse(self, fse):
        """Sets the fse of this Adas.

        Electric brake application  # noqa: E501

        :param fse: The fse of this Adas.  # noqa: E501
        :type: bool
        """

        self._fse = fse

    @property
    def lrka(self):
        """Gets the lrka of this Adas.  # noqa: E501

        Lane Keeping Assist left  # noqa: E501

        :return: The lrka of this Adas.  # noqa: E501
        :rtype: str
        """
        return self._lrka

    @lrka.setter
    def lrka(self, lrka):
        """Sets the lrka of this Adas.

        Lane Keeping Assist left  # noqa: E501

        :param lrka: The lrka of this Adas.  # noqa: E501
        :type: str
        """
        allowed_values = ["Authorized", "CorrectionInProgress", "NotAuthorized", "NotSelected"]  # noqa: E501
        if lrka not in allowed_values:
            raise ValueError(
                "Invalid value for `lrka` ({0}), must be one of {1}"  # noqa: E501
                .format(lrka, allowed_values)
            )

        self._lrka = lrka

    @property
    def lvv(self):
        """Gets the lvv of this Adas.  # noqa: E501


        :return: The lvv of this Adas.  # noqa: E501
        :rtype: bool
        """
        return self._lvv

    @lvv.setter
    def lvv(self, lvv):
        """Sets the lvv of this Adas.


        :param lvv: The lvv of this Adas.  # noqa: E501
        :type: bool
        """

        self._lvv = lvv

    @property
    def park_assist(self):
        """Gets the park_assist of this Adas.  # noqa: E501


        :return: The park_assist of this Adas.  # noqa: E501
        :rtype: AdasParkAssist
        """
        return self._park_assist

    @park_assist.setter
    def park_assist(self, park_assist):
        """Sets the park_assist of this Adas.


        :param park_assist: The park_assist of this Adas.  # noqa: E501
        :type: AdasParkAssist
        """

        self._park_assist = park_assist

    @property
    def rlka(self):
        """Gets the rlka of this Adas.  # noqa: E501

        Lane Keeping Assist right  # noqa: E501

        :return: The rlka of this Adas.  # noqa: E501
        :rtype: str
        """
        return self._rlka

    @rlka.setter
    def rlka(self, rlka):
        """Sets the rlka of this Adas.

        Lane Keeping Assist right  # noqa: E501

        :param rlka: The rlka of this Adas.  # noqa: E501
        :type: str
        """
        allowed_values = ["Authorized", "CorrectionInProgress", "NotAuthorized", "NotSelected"]  # noqa: E501
        if rlka not in allowed_values:
            raise ValueError(
                "Invalid value for `rlka` ({0}), must be one of {1}"  # noqa: E501
                .format(rlka, allowed_values)
            )

        self._rlka = rlka

    @property
    def rvv(self):
        """Gets the rvv of this Adas.  # noqa: E501


        :return: The rvv of this Adas.  # noqa: E501
        :rtype: str
        """
        return self._rvv

    @rvv.setter
    def rvv(self, rvv):
        """Sets the rvv of this Adas.


        :param rvv: The rvv of this Adas.  # noqa: E501
        :type: str
        """
        allowed_values = ["off", "Inactive", "Active", "SpeedExceeded", "Disabled", "DisabledBySystem", "MaxSpeedExceed", "SpeedDeltaExceed", "ReducedVisibility", "Learning"]  # noqa: E501
        if rvv not in allowed_values:
            raise ValueError(
                "Invalid value for `rvv` ({0}), must be one of {1}"  # noqa: E501
                .format(rvv, allowed_values)
            )

        self._rvv = rvv

    @property
    def sli(self):
        """Gets the sli of this Adas.  # noqa: E501

        Speed Limit Information  # noqa: E501

        :return: The sli of this Adas.  # noqa: E501
        :rtype: int
        """
        return self._sli

    @sli.setter
    def sli(self, sli):
        """Sets the sli of this Adas.

        Speed Limit Information  # noqa: E501

        :param sli: The sli of this Adas.  # noqa: E501
        :type: int
        """

        self._sli = sli

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Adas, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Adas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
