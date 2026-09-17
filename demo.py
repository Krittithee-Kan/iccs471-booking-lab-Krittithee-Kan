"""Direct behavior check: run with `uv run python demo.py`."""

from booking_app.booking import BookingService


def main() -> None:
    service = BookingService()
    service.create_booking("A", 540, 600, "Narin")  # 09:00-10:00
    print("First booking in room A: accepted")

    try:
        service.create_booking("A", 570, 630, "Mali")  # 09:30-10:30
    except ValueError as error:
        print(f"Overlapping booking in room A: rejected ({error})")
    else:
        print("Overlapping booking in room A: accepted (BUG)")

    service.create_booking("A", 600, 660, "Mali")  # 10:00-11:00
    print("Adjacent booking in room A: accepted")
    service.create_booking("B", 570, 630, "Pim")  # same time, other room
    print("Overlapping time in room B: accepted")
    print(f"Stored bookings: {len(service.list_bookings())}")


if __name__ == "__main__":
    main()
