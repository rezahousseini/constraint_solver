import numpy as np

# longest side is always c
# angle alpha lies opposite to side a
# angle beta lies opposite to side b
# angle gamma lies opposite to side c
# side a connects points B and C
# side b connects points A and C
# side c connects points A and B
# sum of all angles is always equals 180°
# sum of the two shorter side lengths cannot be shorter then the longest side length
def calcTriangle(a=None, b=None, c=None, alpha=None, beta=None, gamma=None):
    # 6 elements defined
    if a is not None and b is not None and c is not None and \
       alpha is not None and beta is not None and gamma is not None:
        # fully defined triangle

    # 5 elements defined
    if a is not None and b is not None and c is not None and \
       alpha is not None and beta is not None and gamma is None:
        # angle gamma missing
        gamma = None
    elif a is not None and b is not None and c is not None and \
         alpha is not None and beta is None and gamma is not None:
        # angle beta missing
        beta = None
    elif a is not None and b is not None and c is not None and \
         alpha is None and beta is not None and gamma is not None:
        # angle alpha missing
        alpha = None
    elif a is not None and b is not None and c is None and \
         alpha is not None and beta is not None and gamma is not None:
        # side c missing
        c = None
    elif a is not None and b is None and c is not None and \
         alpha is not None and beta is not None and gamma is not None:
        # side b missing
        b = None
    elif a is None and b is not None and c is not None and \
         alpha is not None and beta is not None and gamma is not None:
        # side a missing
        a = None

    # 4 elements defined
    if a is None and b is None and c is not None and \
       alpha is not None and beta is not None and gamma is not None:
        # side a and side b missing
        a = None
        b = None
    elif a is None and b is not None and c is None and \
         alpha is not None and beta is not None and gamma is not None:
        # side a and side c missing
        a = None
        c = None
    elif a is None and b is not None and c is not None and \
         alpha is None and beta is not None and gamma is not None:
        # side a and angle alpha missing
        a = None
        alpha = None
    elif a is None and b is not None and c is not None and \
         alpha is not None and beta is None and gamma is not None:
        # side a and angle beta missing
        a = None
        beta = None
    elif a is None and b is not None and c is not None and \
         alpha is not None and beta is not None and gamma is None:
        # side a and angle gamma missing
        a = None
        gamma = None
    elif a is not None and b is None and c is None and \
         alpha is not None and beta is not None and gamma is not None:
        # side b and side c missing
        b = None
        c = None
    elif a is not None and b is None and c is not None and \
         alpha is None and beta is not None and gamma is not None:
        # side b and angle alpha missing
        b = None
        alpha = None
    elif a is not None and b is None and c is not None and \
         alpha is not None and beta is None and gamma is not None:
        # side b and angle beta missing
        b = None
        beta = None
    elif a is not None and b is None and c is not None and \
         alpha is not None and beta is not None and gamma is None:
        # side b and angle gamma missing
        b = None
        gamma = None
    elif a is not None and b is not None and c is None and \
         alpha is None and beta is not None and gamma is not None:
        # side c and angle alpha missing
        c = None
        alpha = None
    elif a is not None and b is not None and c is None and \
         alpha is not None and beta is None and gamma is not None:
        # side c and angle beta missing
        c = None
        beta = None
    elif a is not None and b is not None and c is None and \
         alpha is not None and beta is not None and gamma is None:
        # side c and angle gamma missing
        c = None
        gamma = None
    elif a is not None and b is not None and c is not None and \
         alpha is None and beta is None and gamma is not None:
        # angle alpha and angle beta missing
        alpha = None
        beta = None
    elif a is not None and b is not None and c is not None and \
         alpha is None and beta is not None and gamma is None:
        # angle alpha and angle gamma missing
        alpha = None
        gamma = None
    elif a is not None and b is not None and c is not None and \
         alpha is not None and beta is None and gamma is None:
        # angle beta and angle gamma missing
        beta = None
        gamma = None

    # 3 elements defined
    if a is None and b is None and c is None and \
       alpha is not None and beta is not None and gamma is not None:
        # side a, side b and side c missing
        a = None
        b = None
        c = None
    elif a is None and b is None and c is not None and \
         alpha is None and beta is not None and gamma is not None:
        # side a, side b and angle alpha missing
        a = None
        b = None
        alpha = None
    elif a is None and b is None and c is not None and \
         alpha is not None and beta is None and gamma is not None:
        # side a, side b and angle beta missing
        a = None
        b = None
        beta = None
    elif a is None and b is None and c is not None and \
         alpha is not None and beta is not None and gamma is None:
        # side a, side b and angle gamma missing
        a = None
        b = None
        gamma = None
    elif a is None and b is not None and c is None and \
         alpha is None and beta is not None and gamma is not None:
        # side a, side c and angle alpha missing
        a = None
        c = None
        alpha = None
    elif a is None and b is not None and c is None and \
         alpha is not None and beta is None and gamma is not None:
        # side a, side c and angle beta missing
        a = None
        c = None
        beta = None
    elif a is None and b is not None and c is None and \
         alpha is not None and beta is not None and gamma is None:
        # side a, side c and angle gamma missing
        a = None
        c = None
        gamma = None
    elif a is None and b is not None and c is not None and \
         alpha is None and beta is None and gamma is not None:
        # side a, angle alpha and angle beta missing
        a = None
        alpha = None
        beta = None
    elif a is None and b is not None and c is not None and \
         alpha is None and beta is not None and gamma is None:
        # side a, angle alpha and angle gamma missing
        a = None
        alpha = None
        gamma = None
    elif a is None and b is not None and c is not None and \
         alpha is not None and beta is None and gamma is None:
        # side a, angle beta and angle gamma missing
        a = None
        beta = None
        gamma = None
    elif a is not None and b is None and c is None and \
         alpha is None and beta is not None and gamma is not None:
        # side b, side c and angle alpha missing
        b = None
        c = None
        alpha = None
    elif a is not None and b is None and c is None and \
         alpha is not None and beta is None and gamma is not None:
        # side b, side c and angle beta missing
        b = None
        c = None
        beta = None
    elif a is not None and b is None and c is None and \
         alpha is not None and beta is not None and gamma is None:
        # side b, side c and angle gamma missing
        b = None
        c = None
        gamma = None
    elif a is not None and b is None and c is not None and \
         alpha is None and beta is None and gamma is not None:
        # side b, angle alpha and angle beta missing
        b = None
        alpha = None
        beta = None
    elif a is not None and b is None and c is not None and \
         alpha is None and beta is not None and gamma is None:
        # side b, angle alpha and angle gamma missing
        b = None
        alpha = None
        gamma = None
    elif a is not None and b is None and c is not None and \
         alpha is not None and beta is None and gamma is None:
        # side b, angle beta and angle gamma missing
        b = None
        beta = None
        gamma = None
    elif a is not None and b is not None and c is None and \
         alpha is None and beta is None and gamma is not None:
        # side c, angle alpha and angle beta missing
        c = None
        alpha = None
        beta = None
    elif a is not None and b is not None and c is None and \
         alpha is None and beta is not None and gamma is None:
        # side c, angle alpha and angle gamma missing
        c = None
        alpha = None
        gamma = None
    elif a is not None and b is not None and c is None and \
         alpha is not None and beta is None and gamma is None:
        # side c, angle beta and angle gamma missing
        c = None
        beta = None
        gamma = None
    elif a is not None and b is not None and c is not None and \
         alpha is None and beta is None and gamma is None:
        # angle alpha, angle beta and angle gamma missing
        alpha = None
        beta = None
        gamma = None
