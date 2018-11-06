#!/usr/bin/env python

# Copyright (c) 2018 Christoph Pilz
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import abc

from support.singleton import Singleton

class SimulatorControl:
  __metaclass__ = Singleton

  def __init__(self, simName):
    self.__simName = simName
    self.__isConnected = False
    self.__isRunning = False
    self.__stateEvents = None

  def getIsConnected(self):
    raise NotImplementedError("implement getIsConnected")

  def getIsRunning(self):
    raise NotImplementedError("implement getIsRunning")

  @abc.abstractmethod
  def connect(self):
    pass

  @abc.abstractmethod
  def disconnect(self):
    pass

  @abc.abstractmethod
  def loadScene(self, sceneDescription):
    pass

  @abc.abstractmethod
  def run(self):
    pass


class CarlaSimulatorControl(SimulatorControl):
  def __init__(self):
    SimulatorControl.__init__(self, "Carla")

  def connect(self):
    raise NotImplementedError("implement connect")

  def disconnect(self):
    raise NotImplementedError("implement disconnect")

  def loadScene(self, sceneDescription):
    raise NotImplementedError("implement loadScene")

  def run(self):
    raise NotImplementedError("implement run")