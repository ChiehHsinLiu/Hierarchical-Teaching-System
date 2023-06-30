def disco_left(motion):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.8, 3.2, 3.4, 4.56])
    keys.append([-0.167185, -0.375246, -0.375246, -0.167185])

    names.append("HeadYaw")
    times.append([0.8, 3.2, 3.4, 4.56])
    keys.append([0.00490394, -0.371755, -0.371755, 0.00523515])

    names.append("LElbowRoll")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([-0.412615, -0.0447104, -0.0447104, -0.33895, -0.33895, -0.409943])

    names.append("LElbowYaw")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([-1.18897, 0.233169, 0.233169, -0.667812, -0.667812, -1.18731])

    names.append("LHand")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([0.30632, 1, 1, 0.988457, 0.988457, 0.301063])

    names.append("LShoulderPitch")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([1.4323, -1.48218, -1.48218, 0.804258, 0.804258, 1.46989])

    names.append("LShoulderRoll")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([0.221144, 0.731949, 0.731949, -0.103681, -0.103681, 0.181755])

    names.append("LWristYaw")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([0.108217, 0.494764, 0.494764, 0.530945, 0.530945, 0.10298])

    names.append("RElbowRoll")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([0.404459, 0.117268, 0.117268, 0.415367, 0.415367, 0.407302])

    names.append("RElbowYaw")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([1.19741, -0.235356, -0.235356, 0.629833, 0.629833, 1.18929])

    names.append("RHand")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([0.291165, 0, 0, 0.0236453, 0.0236453, 0.293224])

    names.append("RShoulderPitch")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([1.45012, 1.28608, 1.28608, 1.31831, 1.31831, 1.47351])

    names.append("RShoulderRoll")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([-0.231823, -0.252415, -0.252415, -0.325371, -0.325371, -0.189771])

    names.append("RWristYaw")
    times.append([0.8, 1.8, 2, 3.2, 3.4, 4.56])
    keys.append([0.103736, 0.935763, 0.935763, 0.918464, 0.918464, 0.102782])

    motion.angleInterpolation(names, keys, times, True)