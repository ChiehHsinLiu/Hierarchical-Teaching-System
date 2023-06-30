def rolling(motion):
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.6, 1.2, 1.8, 2.4])
    keys.append([-1.15809, -0.849998, -1.15633, -1.53707])

    names.append("LElbowYaw")
    times.append([0.6, 1.8])
    keys.append([-0.117541, 0.0614977])

    names.append("LHand")
    times.append([0.6, 1.2])
    keys.append([0.303278, 0])

    names.append("LShoulderPitch")
    times.append([0.6, 1.2, 1.8, 2.4])
    keys.append([0.328214, 0.387519, 0.826742, 0.554413])

    names.append("LShoulderRoll")
    times.append([0.6, 1.8])
    keys.append([0.124689, 0.0140896])

    names.append("LWristYaw")
    times.append([0.6])
    keys.append([0.266929])

    names.append("RElbowRoll")
    times.append([0.6, 1.2, 1.8, 2.4])
    keys.append([1.17026, 1.53707, 1.43737, 0.849998])

    names.append("RElbowYaw")
    times.append([0.6])
    keys.append([0.265807])

    names.append("RHand")
    times.append([0.6, 2.4])
    keys.append([0.295296, 0])

    names.append("RShoulderPitch")
    times.append([0.6, 1.2, 1.8, 2.4])
    keys.append([0.762669, 0.554413, 0.491549, 0.387519])

    names.append("RShoulderRoll")
    times.append([0.6, 1.8])
    keys.append([-0.0580825, -0.00341842])

    names.append("RWristYaw")
    times.append([0.6])
    keys.append([0.0977692])

    motion.angleInterpolation(names, keys, times, True)