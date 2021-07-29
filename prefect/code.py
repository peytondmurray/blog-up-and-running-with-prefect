import prefect as pf
import pandas as pd
import numpy as np


@pf.task
def split(df: pd.DataFrame, fraction: float = 0.7):
    n_train = int(fraction*len(df))
    return df.iloc[:n_train], df.iloc[n_train:]


@pf.task
def make_random_df(nrows=20):
    return pd.DataFrame(
        {
            'a': np.random.randint(low=0, high=100, size=nrows),
            'b': np.random.randint(low=0, high=100, size=nrows),
        }
    )


def generate_flow():

    # Set the flow up
    with pf.Flow('My Flow') as flow:
        random_df = make_random_df(nrows=100)
        train, test = split(df=random_df, fraction=0.7)

    # Enforce constraints

    return flow
