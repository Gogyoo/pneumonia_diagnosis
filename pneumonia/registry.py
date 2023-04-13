# I keep it in the project, like model notebooks whose results
# were too low, but we never had to use that file.

from pneumonia.params import *

def save_results():
    """Takes a model's results (its parameters and metrics, from history)
    and dumps them separately in a timestamped pickle file.
    Locally: TODO: in which subfolder?
    Remotely: one bucket for params, another for metrics.
    Each pickle goes to a blob."""

    if MODEL_TARGET == "local":
        print("THIS IS A TEST: Saving results locally...")

    elif MODEL_TARGET == "gcs":
        print("THIS IS A TEST: Saving results on the cloud...")

    else:
        print ("Locale for results should be\
            either \'local\' or \'\gcs'.\
            Please check in .env.")



def save_model():
    """Takes a model's weights and dumps them in a timestamped pickle file.
    Locally: TODO: in which subfolder?
    Remotely: Each pickle goes to a blob."""

    if MODEL_TARGET == "local":
        print("THIS IS A TEST: Saving model weights locally...")
    elif MODEL_TARGET == "gcs":
        print("THIS IS A TEST: Saving model weights on the cloud...")
    else:
        print ("Locale to export a model should be\
            either \'local\' or \'\gcs'.\
            Please check in .env.")



def load_model():
    """Loads a model's weights saved locally or in a blob."""

    if MODEL_TARGET == "local":
        print("THIS IS A TEST: Loading model weights locally...")
    elif MODEL_TARGET == "gcs":
        print("THIS IS A TEST: Loading model weights on the cloud...")
    else:
        print ("Locale to load a model should be\
            either \'local\' or \'\gcs'.\
             Please check in .env.")
