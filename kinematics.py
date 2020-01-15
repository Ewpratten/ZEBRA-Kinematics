from math import atan2


class Twist(object):
    """
    A difference in 2D space with heading
    """

    # Locals
    dx: float
    dy: float
    dTheta: float
    
    # Constants
    DEFAULT_TRACK_WIDTH: float = 28.0
    TRACK_SCRUB: float = 1.0469745223 # From 254's 2019 bot

    def __init__(self, dx: float, dy: float, dTheta: float) -> None:
        """
        Create a Twist

        :param dx:     X difference
        :param dy:     Y difference
        :param dTheta: Theta difference
        """

        # Set locals
        self.dx = dx
        self.dy = dy
        self.dTheta = dTheta

    @classmethod
    def fromTranslation(self, prevX: float, prevY: float, x: float, y: float) -> None:
        """
        Create a Twist from last and current points in space

        :param prevX: Previous X position
        :param prevY: Previous Y position
        :param x:     Current X position
        :param y:     Current Y position
        """

        # Calculate dx and dy
        dx: float = x - prevX
        dy: float = y - prevY

        # Calculate dTheta
        dTheta: float = atan2(dx, dy)

        # Create a new Twist
        return self(dx, dy, dTheta)

    def toWheelSpeeds(self) -> (float, float):
        """
        Calculate differential wheel velocities from Twist
        """
        
        # Handle tiny changes in space
        if abs(self.dTheta) < 1E-9:
            return (dx, dy)
        
        # Handle chassis kinematics
        deltaV: float = self.DEFAULT_TRACK_WIDTH * self.dTheta / (2 * self.TRACK_SCRUB)
        return (self.dx - deltaV, self.dx + deltaV)
        