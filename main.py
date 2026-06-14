import ezdxf

class DXFCadGenerator:
    def __init__(self, width, height, rooms):
        self.width = width
        self.height = height
        self.rooms = rooms

    def create_dxf(self, filename="floor_plan.dxf"):
        doc = ezdxf.new()
        msp = doc.modelspace()

        # Draw outer boundary
        msp.add_lwpolyline([
            (0, 0),
            (self.width, 0),
            (self.width, self.height),
            (0, self.height),
            (0, 0)
        ])

        num_rooms = len(self.rooms)
        cols = max(1, int(num_rooms ** 0.5))
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

                # Room rectangle
                msp.add_lwpolyline([
                    (x, y),
                    (x + room_w, y),
                    (x + room_w, y + room_h),
                    (x, y + room_h),
                    (x, y)
                ])

                # Room label
                msp.add_text(
                    self.rooms[index],
                    dxfattribs={'height': 0.5}
                ).set_placement((x + room_w/2, y + room_h/2))

                index += 1

        doc.saveas(filename)
        print(f"DXF file created: {filename}")


def get_user_input():
    print("=== AI DXF CAD Generator ===")

    width = float(input("Enter land width: "))
    height = float(input("Enter land height: "))

    rooms = []
    n = int(input("How many rooms? "))

    for i in range(n):
        rooms.append(input(f"Room {i+1} name: "))

    return width, height, rooms


if __name__ == "__main__":
    w, h, rooms = get_user_input()

    cad = DXFCadGenerator(w, h, rooms)
    cad.create_dxf()
