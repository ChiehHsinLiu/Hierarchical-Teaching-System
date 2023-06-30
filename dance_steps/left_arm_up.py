def left_arm_up(motion):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.8])
    keys.append([-0.168118])

    names.append("HeadYaw")
    times.append([0.8])
    keys.append([0.00770484])

    names.append("LAnklePitch")
    times.append([0.8])
    keys.append([0.085665])

    names.append("LAnkleRoll")
    times.append([0.8])
    keys.append([-0.124029])

    names.append("LElbowRoll")
    times.append([0.8])
    keys.append([-1.35055])

    names.append("LElbowYaw")
    times.append([0.8])
    keys.append([-1.90059])

    names.append("LHand")
    times.append([0.8])
    keys.append([0.303278])

    names.append("LHipPitch")
    times.append([0.8])
    keys.append([0.13])

    names.append("LHipRoll")
    times.append([0.8])
    keys.append([0.0934102])

    names.append("LHipYawPitch")
    times.append([0.8])
    keys.append([-0.17213])

    names.append("LKneePitch")
    times.append([0.8])
    keys.append([-0.0825253])

    names.append("LShoulderPitch")
    times.append([0.8])
    keys.append([0.384789])

    names.append("LShoulderRoll")
    times.append([0.8])
    keys.append([0.578389])

    names.append("LWristYaw")
    times.append([0.8])
    keys.append([-0.0996257])

    names.append("RAnklePitch")
    times.append([0.8])
    keys.append([0.0886427])

    names.append("RAnkleRoll")
    times.append([0.8])
    keys.append([0.125724])

    names.append("RElbowRoll")
    times.append([0.8])
    keys.append([0.416509])

    names.append("RElbowYaw")
    times.append([0.8])
    keys.append([1.12139])

    names.append("RHand")
    times.append([0.8])
    keys.append([0.295296])

    names.append("RHipPitch")
    times.append([0.8])
    keys.append([0.124676])

    names.append("RHipRoll")
    times.append([0.8])
    keys.append([-0.0948827])

    names.append("RHipYawPitch")
    times.append([0.8])
    keys.append([-0.17213])

    names.append("RKneePitch")
    times.append([0.8])
    keys.append([-0.0865441])

    names.append("RShoulderPitch")
    times.append([0.8])
    keys.append([1.47328])

    names.append("RShoulderRoll")
    times.append([0.8])
    keys.append([-0.484379])

    names.append("RWristYaw")
    times.append([0.8])
    keys.append([-0.103386])

    motion.angleInterpolation(names, keys, times, True)