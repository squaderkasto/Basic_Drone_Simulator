class Drone:
    def __init__(self):
        self.x, self.y, self.z = 0, 0, 0
        self.flying = False
        self.yaw = 0  # rotation angle

    def takeoff(self):
        if not self.flying:
            self.z = 1
            self.flying = True
            print("Drone took off.")
        else:
            print("Already flying.")

    def land(self):
        if self.flying:
            self.z = 0
            self.flying = False
            print("Drone landed.")
        else:
            print("Already on ground.")

    def move_forward(self):
        if self.flying:
            self.y += 1
            print("Moved forward.")
        else:
            print("Takeoff first.")

    def move_up(self):
        if self.flying:
            self.z += 1
            print("Moved up.")
        else:
            print("Takeoff first.")

    def move_down(self):
        if self.flying and self.z > 0:
            self.z -= 1
            print("Moved down.")
        else:
            print("Cannot move down.")

    def rotate_left(self):
        self.yaw -= 15
        print("Rotated left.")

    def rotate_right(self):
        self.yaw += 15
        print("Rotated right.")

    def status(self):
        print(f"Position: ({self.x}, {self.y}, {self.z}), Yaw: {self.yaw}, Flying: {self.flying}")


# Example simulation
if __name__ == "__main__":
    drone = Drone()
    drone.takeoff()
    drone.move_forward()
    drone.move_up()
    drone.rotate_left()
    drone.status()
    drone.move_down()
    drone.land()
