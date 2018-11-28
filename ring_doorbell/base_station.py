# coding: utf-8
# vim:sw=4:ts=4:et:
"""Python Ring RingGeneric wrapper."""
import logging

from ring_doorbell.generic import RingGeneric
from ring_doorbell.const import (
    API_URI, CHIMES_ENDPOINT, CHIME_VOL_MIN, CHIME_VOL_MAX,
    LINKED_CHIMES_ENDPOINT, MSG_VOL_OUTBOUND, TESTSOUND_CHIME_ENDPOINT,
    CHIME_TEST_SOUND_KINDS, KIND_DING)

_LOGGER = logging.getLogger(__name__)

class RingBaseStation(RingGeneric):
    """Implementation for Ring Base Station."""

    @property
    def family(self):
        """Return Ring device family type."""
        return 'base_stations'

    @property
    def battery_life(self):
        """Return battery life."""
        return int(self._health_attrs.get('battery_percentage'))