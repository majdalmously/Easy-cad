import matplotlib.pyplot as plt

class AICadGenerator:
    def __init__(self, width, height, rooms):
        self.width = width
        self.height = height
        self.rooms = rooms

    def generate(self):
        fig, ax = plt.subplots()

        # Draw boundary
        ax.plot(
            [0, self.width, self.width, 0, 0],
            [0, 0, self.height, self.height, 0]
        )

        num_rooms = len(self.rooms)

        # Better grid calculation
        cols = int(num_rooms ** 0.5)
        if cols == 0:
            cols = 1
        rows = (num_rooms // cols) + (num_rooms % cols > 0)

        room_w = self.width / cols
        room_h = self.height / rows

        index = 0

        for r in range(rows):
            for c in range(cols):
                if index >= num_rooms:
                    break

                x = c * room_w
                y = r * room_h

                # Draw room
                ax.add_patch(
                    plt.Rectangle(
                        (x, y),
                        room_w,
                        room_h,
                        fill=False,
                        edgecolor="black",
                        linewidth=2
                    )
                )

                # Label room
                ax.text(
                    x + room_w / 2,
                    y + room_h / 2,
                    self.rooms[index],
                    ha='center',
                    va='center',
                    fontsize=10
                )

                index += 1

        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.set_title("AI CAD Generator - Pro Version")

        plt.show()


def get_user_input():
    print("=== AI CAD Generator ===")

    width = float(input("Enter land width: "))
    height = float(input("Enter land height: "))

    rooms = []
    n = int(input("How many rooms? "))

    for i in range(n):
        name = input(f"Enter name of room {i+1}: ")
        rooms.append(name)

    return width, height, rooms


if __name__ == "__main__":
    w, h, rooms = get_user_input()

    cad = AICadGenerator(w, h, rooms)
    cad.generate()
