# Room booking starter

This is a small, in-memory booking service for ICCS471. It already creates and lists bookings and rejects blank fields or invalid time ranges. **Known missing rule:** it currently accepts two bookings whose times overlap in the same room. That is the assigned change.

## Files

- `booking_app/booking.py`: `Booking` and `BookingService`.
- `tests/test_booking.py`: baseline tests using Python's standard `unittest` library.
- `demo.py`: a direct behavior check with overlap, adjacency, and a different room.
- `pyproject.toml`, `.python-version`, `uv.lock`: Python 3.12 project information.

Time values are **integer minutes after midnight**: `540` is 09:00, `600` is 10:00. A booking covers `[start, end)`, so 09:00–10:00 and 10:00–11:00 are adjacent, not overlapping. Rooms are compared as exact strings; do not add name normalization in this assignment. The service stores bookings only for the lifetime of the Python process. There is no database, web app, login, or date handling.

From the repository root in PowerShell:

```powershell
uv sync
uv run python --version
uv run python -m unittest discover -s tests -v
uv run python demo.py
```

The baseline tests pass. Before the fix, the demo explicitly prints `Overlapping booking in room A: accepted (BUG)` and shows four stored bookings. After a correct fix, it reports rejection and three stored bookings. The starter deliberately contains no overlap-specific regression test; add one as part of the assignment.
