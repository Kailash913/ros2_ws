import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subsrciption")
        self.pose_subscriber_=self.create_subscription(
            Pose,'/turtle1/pose',self.pose_callback,10)
    
    def pose_callback(self,msg:Pose):
        self.get_logger().info(f"Pose received: x={msg.x}, y={msg.y}, theta={msg.theta}")
def main(args=None):
    rclpy.init(args=args)
    node=PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()