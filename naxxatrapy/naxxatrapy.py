G=6.67384*10**(-11)
from numpy import *

def velocity(displacement, time):
    """
        Calculate velocity given displacement and time
        Parameters
        ----------
        displacement : float
        time: float

        Returns
        -------
        float
    """
    pass


def displacement(velocity, time, acceleration):
    """
        Calculate displacement given velocity and time
        Parameters
        ----------
        velocity : float
        time: float

        Returns
        -------
        float
    """
    pass


def average_velocity(velocity_list):
    """
        Calculate the average velocity given multiple velocities
        Parameters
        ----------
        velocity_list : list

        Returns
        -------
        float
    """
    pass


def acceleration(velocity, time):
    """
        Calculate the acceleration given velocity and time
        Parameters
        ----------
        velocity : float
        time: float

        Returns
        -------
        float
    """
    pass


def initial_velocity():
    pass


def final_velocity():
    pass


def momentum():
    pass


def force(mass, acceleration=None, velocity=None, time=None):
    pass

def gravitational_force(m1, m2, r):
    
    """ 
       Calculates the gravitational force 
       between two objects of mass m1 and m2 
       seperated by a distance of r
       
       Parameters
       ----------
       m1 : float
       m2 : float 
       r : float
       
       Returns
       -------
       float
    """
    return G * m1 * m2 / r**2


def work(force, displacement, theta):
    
    """
       Calculates the work done by 
       the force while displacing
       an object at an angle theta
       
       Parameters
       ----------
       force : float
       displcement : float 
       theta : float
       
       Returns
       -------
       float
    """
    return force * displacement * cos(theta)


def power(work, time):
    
    """
       Power is the rate at which the work is done.
       Calculates the amountof work done divided by 
       the time it takes to do the work
       
       Parameters
       ----------
       work : float
       time : float
       
       Returns
       -------
       float
    """
    return work / time


def kinetic_energy(mass, velocity):
    
    """
       Calculates the energy associated 
       with an object with mass moving
       at a given velocity 
       
       Parameters
       ----------
       mass : float
       velocity : float
       
       Returns
       -------
       float
    """
    return (1/2) * mass * velocity**2


def total_energy(T, V):
    
    """
       Total energy of an object is 
       the sum of its kinetic energy 
       'T' and potential energy 'V'
       
       Parameters
       ----------
       T : float
       V : float
       
       Returns
       -------
       float
    """
    return T + V

def angular_displacement(l, r):
    
    """
       Calculates the angular displacement of
       an object whose linear displacement is 
       'l' and radius of the path traced is 'r'
       
       Parameters
       ----------
       l : float
       r : float
       
       Returns
       -------
       float
    """
    return l / r

def angular_velocity(v, r):
    
    """
       Calculates the angular velocity of an
       object whose linear velocity is 'v'
       and radius of the path traced is 'r'
       
       Parameters
       ----------
       v : float
       r : float
       
       Returns
       -------
       float
    """
    return v / r

def angular_acceleration(a, r):
    
    """
       Calculates the angular acceleration of an
       object whose linear acceelration is 'a' and 
       radius of the path traced by the object is 'r'
      
       Parameters
       ----------
       a : float
       r : float
       
       Returns
       -------
       float
    """
    return a / r

def moment_of_inertia(m, k):
    
    """
       Calculates the moment of inertia of an object
       of mass 'm' with radius of gyration 'k'
      
       Parameters
       ----------
       m : float
       k : float
       
       Returns
       -------
       float
    """
    return m * k**2

def angular_momentum(m, v, r, theta):
    
    """
       Calculates the angular momentum of an object 
       of mass 'm' whose linear velocity is 'v' and 
       radius of the path traced by the object is 'r',
       angle between velocity and radius is 'theta'
      
       Parameters
       ----------
       m : float
       v : float
       r : float
       theta : float
       
       Returns
       -------
       float
    """
    return m * v * r * sin(theta) 

def centripetal_acceleration(v, r):
    
    """
       Calculates the centripetal acceleration of
       an object whose linear velocity is 'v' and 
       radius of the path traced by the object is 'r'
      
       Parameters
       ----------
       v : float
       r : float
       
       Returns
       -------
       float
    """
    return v**2 / r
    
def centripetal_force(m, v, r):
    
    """
       Centripetal force is the net force
       that acts on an object with mass 'm' to 
       keep it moving with a velocity 'v' along
       a circular path of radius 'r'
       
       Parameters
       ----------
       m : float
       v : float 
       r : float
       
       Returns
       -------
       float
    """
    return m * v**2 / r

def angular_kinetic_energy(I, w):
    
    """
       Calculates the angular kinetic energy
       of an object with moment of inertia 'I'
       and angular velocity 'w'
       
       Parameters
       ----------
       I : float
       w: float 
       
       Returns
       -------
       float
    """
    return (1/2) * I * w**2

def torque(r, F, theta):
    
    """
       Calculates the torque acting on an object
       where 'r' is the radius, 'F' is the force 
       and 'theta' is the angle between 'r' and 'F'
      
       Parameters
       ----------
       m : float
       v : float
       r : float
       theta : float
       
       Returns
       -------
       float
    """
    return  r * F * sin(theta) 

def friction():
    pass


def normal_force():
    pass


