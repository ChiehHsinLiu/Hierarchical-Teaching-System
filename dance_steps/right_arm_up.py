def right_arm_up(motion):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.8])
    keys.append([-0.169883])

    names.append("HeadYaw")
    times.append([0.8])
    keys.append([-0.00938009])

    names.append("LAnklePitch")
    times.append([0.8])
    keys.append([0.0824927])

    names.append("LAnkleRoll")
    times.append([0.8])
    keys.append([-0.121131])

    names.append("LElbowRoll")
    times.append([0.8])
    keys.append([-0.407087])

    names.append("LElbowYaw")
    times.append([0.8])
    keys.append([-1.11353])

    names.append("LHand")
    times.append([0.8])
    keys.append([0.3])

    names.append("LHipPitch")
    times.append([0.8])
    keys.append([0.12425])

    names.append("LHipRoll")
    times.append([0.8])
    keys.append([0.0905925])

    names.append("LHipYawPitch")
    times.append([0.8])
    keys.append([-0.170826])

    names.append("LKneePitch")
    times.append([0.8])
    keys.append([-0.0891712])

    names.append("LShoulderPitch")
    times.append([0.8])
    keys.append([1.47368])

    names.append("LShoulderRoll")
    times.append([0.8])
    keys.append([0.479003])

    names.append("LWristYaw")
    times.append([0.8])
    keys.append([0.103774])

    names.append("RAnklePitch")
    times.append([0.8])
    keys.append([0.080422])

    names.append("RAnkleRoll")
    times.append([0.8])
    keys.append([0.126533])

    names.append("RElbowRoll")
    times.append([0.8])
    keys.append([1.35997])

    names.append("RElbowYaw")
    times.append([0.8])
    keys.append([1.90845])

    names.append("RHand")
    times.append([0.8])
    keys.append([0.304497])

    names.append("RHipPitch")
    times.append([0.8])
    keys.append([0.123769])

    names.append("RHipRoll")
    times.append([0.8])
    keys.append([-0.099173])

    names.append("RHipYawPitch")
    times.append([0.8])
    keys.append([-0.170826])

    names.append("RKneePitch")
    times.append([0.8])
    keys.append([-0.0889415])

    names.append("RShoulderPitch")
    times.append([0.8])
    keys.append([0.38439])

    names.append("RShoulderRoll")
    times.append([0.8])
    keys.append([-0.583764])

    names.append("RWristYaw")
    times.append([0.8])
    keys.append([0.100014])

    motion.angleInterpolation(names, keys, times, True)