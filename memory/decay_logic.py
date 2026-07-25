"""
ULOS Memory Lifecycle Manager

Illustrative pseudocode demonstrating how memory items
can transition between HOT, COLD, and ARCHIVE states.

This file is intended for research discussion and does
not represent the complete production implementation.
"""

from datetime import datetime


class MemoryLifecycle:
    """
    Example memory decay model.

    HOT:
        Frequently accessed memories.

    COLD:
        Lower-priority memories retained for future retrieval.

    ARCHIVE:
        Long-term storage for historical context.
    """

    COLD_THRESHOLD_DAYS = 30
    ARCHIVE_THRESHOLD_DAYS = 180

    def evaluate_memory(self, memory):
        days_since_access = (
            datetime.now() - memory.last_accessed
        ).days

        if days_since_access > self.ARCHIVE_THRESHOLD_DAYS:
            return "ARCHIVE"

        if days_since_access > self.COLD_THRESHOLD_DAYS:
            return "COLD"

        return "HOT"

    def update_memory_state(self, memory):
        memory.tier = self.evaluate_memory(memory)
        return memory
