"""Test the modules in py-imu."""

import numpy as np
from loguru import logger

from py_imu.madgwick import Madgwick
from py_imu.motion import Motion
from py_imu.quaternion import Vector3D


def test_madgwick():
    """Test the filter prediction module."""
    madgwick = Madgwick(frequency=100.0, gain=0.033)

    sample_data = 10 * [np.array([5.0, 2.0, 0.0, 0.0, 0.0, 9.81])]
    # provide time increment dt based on time expired between each sensor reading
    for data in sample_data:
        gyr = Vector3D(data[0:3])
        acc = Vector3D(data[3:6])
        madgwick.update(gyr=gyr, acc=acc, dt=0.01)

        # access the quaternion
        logger.info(madgwick.q)


def test_motion_moving_true():
    """Test the motion prediction module with moving turned on."""
    madgwick = Madgwick(frequency=100.0, gain=0.033)

    estimator = Motion(
        declination=9.27, latitude=32.253460, altitude=730, magfield=47392.3
    )

    sample_data = 10 * [np.array([5.0, 2.0, 0.0, 0.0, 0.0, 9.81])]
    # provide time increment dt based on time expired between each sensor reading
    for data in sample_data:
        gyr = Vector3D(data[0:3])
        acc = Vector3D(data[3:6])

        madgwick.update(gyr=gyr, acc=acc, dt=0.01)

        estimator.update(q=madgwick.q, acc=acc, timestamp=0.01, moving=True)
        logger.info(estimator)


def test_motion_moving_false():
    """Test the motion prediction module with moving turned off."""
    madgwick = Madgwick(frequency=100.0, gain=0.033)

    estimator = Motion(
        declination=9.27, latitude=32.253460, altitude=730, magfield=47392.3
    )

    sample_data = 10 * [np.array([5.0, 2.0, 0.0, 0.0, 0.0, 9.81])]
    # provide time increment dt based on time expired between each sensor reading
    for data in sample_data:
        gyr = Vector3D(data[0:3])
        acc = Vector3D(data[3:6])

        madgwick.update(gyr=gyr, acc=acc, dt=0.01)

        estimator.update(q=madgwick.q, acc=acc, timestamp=0.01, moving=False)
        logger.info(estimator)
