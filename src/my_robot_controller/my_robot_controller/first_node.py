import rclpy                    
from rclpy.node import Node  # Node class
class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")     
        self.counter_=0
        self.create_timer(1.0,self.timer_callback) # Create timer with 1 second period
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info(f"Timer called {self.counter_} times")
def main(args=None):
    rclpy.init(args=args) # Start ROS 2
    node = MyNode() # Create node object
    rclpy.spin(node) # Keep node running
    rclpy.shutdown() # Stop ROS 2
if __name__ == "__main__":
    main()            