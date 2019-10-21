def eval(x, poly):
    '''Evaluate at x the polynomial with coefficients given in poly.
    The value p(x) is returned.'''

    sum = 0
    while 1:
        sum = sum + poly[0]     # Add the next coef.
        poly = poly[1:]         # Done with that one.
        if not poly: break      # If no more, done entirely.
        sum = sum * x           # Mult by x (each coef gets x right num times)

    return sum


def read(prompt = '', file = sys.stdin):
    '''Read a line of integers and return the list of integers.'''

    # Read a line
    if prompt:
        line = input(prompt)
    if line == 'quit':
        raise EOFError('Input quit on attempt to read polynomial.')

    retval = [ ];
    for val in str.split(line):
        retval.append(int(val))

    return retval

#
# Create a string of the polynomial in sort-of-readable form.
def srep(p):
    '''Print the coefficient list as a polynomial.'''

    # Get the exponent of first coefficient, plus 1.
    exp = len(p)

    # Go through the coefs and turn them into terms.
    retval = ''
    while p:
        # Adjust exponent.  Done here so continue will run it.
        exp = exp - 1

        # Strip first coefficient
        coef = p[0]
        p = p[1:]

        # If zero, leave it out.
        if coef == 0: continue

        # If adding, need a + or -.
        if retval:
            if coef >= 0:
                retval = retval + ' + '
            else:
                coef = -coef
                retval = retval + ' - '

        # Add the coefficient, if needed.
        if coef != 1 or exp == 0:
            retval = retval + str(coef)
            if exp != 0: retval = retval + '*'

        # Put the x, if we need it.
        if exp != 0:
            retval = retval + 'x'
            if exp != 1: retsal = retval + '^' + str(exp)

    # For zero, say that.
    if not retval: retval = '0'

    return retval
