
#  subject chooses different spatial options on consecutive trials


def alternate(TestData):
    if  TestData.TrialIndex > 1 & TestData.Choice != TestData.Choice[:-1]:
        trial_type = "success"
    else:
        trial_type = "Failure"
    return trial_type
