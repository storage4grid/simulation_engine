# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.capacitor import Capacitor  # noqa: F401,E501
from swagger_server.models.charging_station import ChargingStation  # noqa: F401,E501
from swagger_server.models.linecode import Linecode  # noqa: F401,E501
from swagger_server.models.load import Load  # noqa: F401,E501
from swagger_server.models.photovoltaic import Photovoltaic  # noqa: F401,E501
from swagger_server.models.power_profile import PowerProfile  # noqa: F401,E501
from swagger_server.models.powerline import Powerline  # noqa: F401,E501
from swagger_server.models.reg_control import RegControl  # noqa: F401,E501
from swagger_server.models.storage import Storage  # noqa: F401,E501
from swagger_server.models.transformer import Transformer  # noqa: F401,E501
from swagger_server.models.tshape import Tshape  # noqa: F401,E501
from swagger_server.models.xy_curve import XYCurve  # noqa: F401,E501
from swagger_server import util


class Radial(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, radial_id: str=None, transformer: List[Transformer]=None, loads: List[Load]=None, power_profiles: List[PowerProfile]=None, power_lines: List[Powerline]=None, photovoltaics: List[Photovoltaic]=None, storage_units: List[Storage]=None, charging_stations: List[ChargingStation]=None, linecode: List[Linecode]=None, capacitor: List[Capacitor]=None, regcontrol: List[RegControl]=None, xycurves: List[XYCurve]=None, tshapes: List[Tshape]=None):  # noqa: E501
        """Radial - a model defined in Swagger

        :param radial_id: The radial_id of this Radial.  # noqa: E501
        :type radial_id: str
        :param transformer: The transformer of this Radial.  # noqa: E501
        :type transformer: List[Transformer]
        :param loads: The loads of this Radial.  # noqa: E501
        :type loads: List[Load]
        :param power_profiles: The power_profiles of this Radial.  # noqa: E501
        :type power_profiles: List[PowerProfile]
        :param power_lines: The power_lines of this Radial.  # noqa: E501
        :type power_lines: List[Powerline]
        :param photovoltaics: The photovoltaics of this Radial.  # noqa: E501
        :type photovoltaics: List[Photovoltaic]
        :param storage_units: The storage_units of this Radial.  # noqa: E501
        :type storage_units: List[Storage]
        :param charging_stations: The charging_stations of this Radial.  # noqa: E501
        :type charging_stations: List[ChargingStation]
        :param linecode: The linecode of this Radial.  # noqa: E501
        :type linecode: List[Linecode]
        :param capacitor: The capacitor of this Radial.  # noqa: E501
        :type capacitor: List[Capacitor]
        :param regcontrol: The regcontrol of this Radial.  # noqa: E501
        :type regcontrol: List[RegControl]
        :param xycurves: The xycurves of this Radial.  # noqa: E501
        :type xycurves: List[XYCurve]
        :param tshapes: The tshapes of this Radial.  # noqa: E501
        :type tshapes: List[Tshape]
        """
        self.swagger_types = {
            'radial_id': str,
            'transformer': List[Transformer],
            'loads': List[Load],
            'power_profiles': List[PowerProfile],
            'power_lines': List[Powerline],
            'photovoltaics': List[Photovoltaic],
            'storage_units': List[Storage],
            'charging_stations': List[ChargingStation],
            'linecode': List[Linecode],
            'capacitor': List[Capacitor],
            'regcontrol': List[RegControl],
            'xycurves': List[XYCurve],
            'tshapes': List[Tshape]
        }

        self.attribute_map = {
            'radial_id': 'radialId',
            'transformer': 'transformer',
            'loads': 'loads',
            'power_profiles': 'powerProfiles',
            'power_lines': 'powerLines',
            'photovoltaics': 'photovoltaics',
            'storage_units': 'storageUnits',
            'charging_stations': 'chargingStations',
            'linecode': 'linecode',
            'capacitor': 'capacitor',
            'regcontrol': 'regcontrol',
            'xycurves': 'xycurves',
            'tshapes': 'tshapes'
        }

        self._radial_id = radial_id
        self._transformer = transformer
        self._loads = loads
        self._power_profiles = power_profiles
        self._power_lines = power_lines
        self._photovoltaics = photovoltaics
        self._storage_units = storage_units
        self._charging_stations = charging_stations
        self._linecode = linecode
        self._capacitor = capacitor
        self._regcontrol = regcontrol
        self._xycurves = xycurves
        self._tshapes = tshapes

    @classmethod
    def from_dict(cls, dikt) -> 'Radial':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Radial of this Radial.  # noqa: E501
        :rtype: Radial
        """
        return util.deserialize_model(dikt, cls)

    @property
    def radial_id(self) -> str:
        """Gets the radial_id of this Radial.


        :return: The radial_id of this Radial.
        :rtype: str
        """
        return self._radial_id

    @radial_id.setter
    def radial_id(self, radial_id: str):
        """Sets the radial_id of this Radial.


        :param radial_id: The radial_id of this Radial.
        :type radial_id: str
        """

        self._radial_id = radial_id

    @property
    def transformer(self) -> List[Transformer]:
        """Gets the transformer of this Radial.


        :return: The transformer of this Radial.
        :rtype: List[Transformer]
        """
        return self._transformer

    @transformer.setter
    def transformer(self, transformer: List[Transformer]):
        """Sets the transformer of this Radial.


        :param transformer: The transformer of this Radial.
        :type transformer: List[Transformer]
        """

        self._transformer = transformer

    @property
    def loads(self) -> List[Load]:
        """Gets the loads of this Radial.


        :return: The loads of this Radial.
        :rtype: List[Load]
        """
        return self._loads

    @loads.setter
    def loads(self, loads: List[Load]):
        """Sets the loads of this Radial.


        :param loads: The loads of this Radial.
        :type loads: List[Load]
        """

        self._loads = loads

    @property
    def power_profiles(self) -> List[PowerProfile]:
        """Gets the power_profiles of this Radial.


        :return: The power_profiles of this Radial.
        :rtype: List[PowerProfile]
        """
        return self._power_profiles

    @power_profiles.setter
    def power_profiles(self, power_profiles: List[PowerProfile]):
        """Sets the power_profiles of this Radial.


        :param power_profiles: The power_profiles of this Radial.
        :type power_profiles: List[PowerProfile]
        """

        self._power_profiles = power_profiles

    @property
    def power_lines(self) -> List[Powerline]:
        """Gets the power_lines of this Radial.


        :return: The power_lines of this Radial.
        :rtype: List[Powerline]
        """
        return self._power_lines

    @power_lines.setter
    def power_lines(self, power_lines: List[Powerline]):
        """Sets the power_lines of this Radial.


        :param power_lines: The power_lines of this Radial.
        :type power_lines: List[Powerline]
        """

        self._power_lines = power_lines

    @property
    def photovoltaics(self) -> List[Photovoltaic]:
        """Gets the photovoltaics of this Radial.


        :return: The photovoltaics of this Radial.
        :rtype: List[Photovoltaic]
        """
        return self._photovoltaics

    @photovoltaics.setter
    def photovoltaics(self, photovoltaics: List[Photovoltaic]):
        """Sets the photovoltaics of this Radial.


        :param photovoltaics: The photovoltaics of this Radial.
        :type photovoltaics: List[Photovoltaic]
        """

        self._photovoltaics = photovoltaics

    @property
    def storage_units(self) -> List[Storage]:
        """Gets the storage_units of this Radial.


        :return: The storage_units of this Radial.
        :rtype: List[Storage]
        """
        return self._storage_units

    @storage_units.setter
    def storage_units(self, storage_units: List[Storage]):
        """Sets the storage_units of this Radial.


        :param storage_units: The storage_units of this Radial.
        :type storage_units: List[Storage]
        """

        self._storage_units = storage_units

    @property
    def charging_stations(self) -> List[ChargingStation]:
        """Gets the charging_stations of this Radial.


        :return: The charging_stations of this Radial.
        :rtype: List[ChargingStation]
        """
        return self._charging_stations

    @charging_stations.setter
    def charging_stations(self, charging_stations: List[ChargingStation]):
        """Sets the charging_stations of this Radial.


        :param charging_stations: The charging_stations of this Radial.
        :type charging_stations: List[ChargingStation]
        """

        self._charging_stations = charging_stations

    @property
    def linecode(self) -> List[Linecode]:
        """Gets the linecode of this Radial.


        :return: The linecode of this Radial.
        :rtype: List[Linecode]
        """
        return self._linecode

    @linecode.setter
    def linecode(self, linecode: List[Linecode]):
        """Sets the linecode of this Radial.


        :param linecode: The linecode of this Radial.
        :type linecode: List[Linecode]
        """

        self._linecode = linecode

    @property
    def capacitor(self) -> List[Capacitor]:
        """Gets the capacitor of this Radial.


        :return: The capacitor of this Radial.
        :rtype: List[Capacitor]
        """
        return self._capacitor

    @capacitor.setter
    def capacitor(self, capacitor: List[Capacitor]):
        """Sets the capacitor of this Radial.


        :param capacitor: The capacitor of this Radial.
        :type capacitor: List[Capacitor]
        """

        self._capacitor = capacitor

    @property
    def regcontrol(self) -> List[RegControl]:
        """Gets the regcontrol of this Radial.


        :return: The regcontrol of this Radial.
        :rtype: List[RegControl]
        """
        return self._regcontrol

    @regcontrol.setter
    def regcontrol(self, regcontrol: List[RegControl]):
        """Sets the regcontrol of this Radial.


        :param regcontrol: The regcontrol of this Radial.
        :type regcontrol: List[RegControl]
        """

        self._regcontrol = regcontrol

    @property
    def xycurves(self) -> List[XYCurve]:
        """Gets the xycurves of this Radial.


        :return: The xycurves of this Radial.
        :rtype: List[XYCurve]
        """
        return self._xycurves

    @xycurves.setter
    def xycurves(self, xycurves: List[XYCurve]):
        """Sets the xycurves of this Radial.


        :param xycurves: The xycurves of this Radial.
        :type xycurves: List[XYCurve]
        """

        self._xycurves = xycurves

    @property
    def tshapes(self) -> List[Tshape]:
        """Gets the tshapes of this Radial.


        :return: The tshapes of this Radial.
        :rtype: List[Tshape]
        """
        return self._tshapes

    @tshapes.setter
    def tshapes(self, tshapes: List[Tshape]):
        """Sets the tshapes of this Radial.


        :param tshapes: The tshapes of this Radial.
        :type tshapes: List[Tshape]
        """

        self._tshapes = tshapes