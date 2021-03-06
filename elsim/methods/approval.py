import random
import numpy as np
from ._common import _all_indices


def _order_tiebreak(winners):
    """
    Given an iterable of possibly tied `winners`, select the lowest numbered
    """
    return min(winners)


def _random_tiebreak(winners):
    """
    Given an iterable of possibly tied `winners`, select one at random
    """
    return random.choice(winners)


def _no_tiebreak(winners):
    """
    Given an iterable of possibly tied `winners`, return None if there is a tie
    """
    if len(winners) == 1:
        return winners[0]
    else:
        return None


_tiebreak_map = {'order': _order_tiebreak,
                 'random': _random_tiebreak,
                 None: _no_tiebreak}


def _get_tiebreak(tiebreaker):
    try:
        return _tiebreak_map[tiebreaker]
    except KeyError:
        raise ValueError('Tiebreaker not understood')


def approval(election, tiebreaker=None):
    """
    Finds the winner of an election using approval voting

    The candidate with the largest number of approvals wins.[1]_

    Parameters
    ----------
    election : array_like
        A 2D collection of approval ballots.

        Rows represent voters, and columns represent candidate IDs.
        A cell contains 1 if that voter approves of that candidate,
        otherwise 0.

    tiebreaker : {'random', 'order', None}, optional
        If there is a tie, and `tiebreaker` is ``'random'``, a random finalist
        is returned.
        If 'order', the lowest-ID tied candidate is returned.
        By default, ``None`` is returned for ties.

    Returns
    -------
    winner : int
        The ID number of the winner, or ``None`` for an unbroken tie.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Approval_voting

    Examples
    --------
    Voter 0 approves Candidate A (index 0) and B (index 1).
    Voter 1 approves B and C.
    Voter 2 approves B and C.

    >>> election = [[1, 1, 0],
                    [0, 1, 1],
                    [0, 1, 1],
                    ]

    Candidate B (1) gets the most approvals and wins the election:

    >>> approval(election)
    1

    """
    election = np.asarray(election, dtype=np.uint8)

    # Tally all approvals
    tallies = election.sum(0)

    # Find the set of candidates who have the highest score (usually only one)
    winners = _all_indices(tallies, max(tallies))

    # Break any ties using specified method
    tiebreak = _get_tiebreak(tiebreaker)
    return tiebreak(winners)
