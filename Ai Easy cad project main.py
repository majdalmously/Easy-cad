import matplotlib.pyplot as plt

def generate_floor_plan(width, height, rooms):
    """
    Simple AI-inspired floor plan generator (MVP version)
    """

    fig, ax = plt.subplots()

    # Draw outer boundary of the land
    ax.plot([0, width, width, 0, 0], [0, 0, height, height, 0])

    # Grid layout calculation
    num_rooms = len(rooms)
    cols = int(num_rooms ** 0.5) + 1
    rows = (num_rooms // cols) + 1

    room_width = width / cols
    room_height = height / rows

    index = 0

    # Place rooms in grid
    for r in range(rows):
        for c in range(cols):
            if index >= num_rooms:
                break

            x = c * room_width
            y = r * room_height

            # Draw room rectangle
            rect = plt.Rectangle(
                (x, y),
                room_width,
                room_height,
                fill=False,
                edgecolor="black"
            )
            ax.add_patch(rect)

            # Add room label
            ax.text(
                x + room_width / 2,
                y + room_height / 2,
                rooms[index],
                ha='center',
                va='center'
            )

            index += 1

    # Formatting
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.set_title("AI-Based Simple Floor Plan Generator")

    plt.show()


# =========================
# Example Usage
# =========================
if __name__ == "__main__":
    width = 20   # land width
    height = 15  # land height

    rooms = [
        "Living Room",
        "Kitchen",
        "Bedroom 1",
        "Bedroom 2",
        "Bathroom"
    ]

    generate_floor_plan(width, height, rooms)
