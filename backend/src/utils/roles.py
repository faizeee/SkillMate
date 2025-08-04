from enum import Enum


class Roles(Enum):
    """The Class represents the User Roles.

    An enumeration for the different user roles in the application.
    Using an Enum provides type safety and prevents "magic strings".
    """

    SUPER_ADMIN = 1
    ADMIN = 2
    USER = 3
