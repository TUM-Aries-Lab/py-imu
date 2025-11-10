"""Test the modules in py-imu."""

import numpy as np
import pytest
from loguru import logger

from py_imu.fusion.madgwick import Madgwick
from py_imu.fusion.quaternion import Vector3D


@pytest.mark.parametrize("gain", [0.033, 0.041])
def test_madgwick(gain: float):
    """Test the filter prediction module."""
    madgwick = Madgwick(frequency=100.0, gain=gain)

    sample_data = 10 * [np.array([5.0, 2.0, 0.0, 0.0, 0.0, 9.81])]
    # provide time increment dt based on time expired between each sensor reading
    for data in sample_data:
        gyr = Vector3D(data[0:3])
        acc = Vector3D(data[3:6])
        madgwick.update(gyr=gyr, acc=acc, dt=0.01)

        # access the quaternion
        logger.info(madgwick.q)
