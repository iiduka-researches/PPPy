import re


def header_decomposition(header: list[str]) -> list[dict]:
    '''
    Decompose the header and return the List of the dictionaries.
    The decomposition is::

        string<key1=value1><key2=value2>
        -> {'label': 'string', 'key1': 'value1', 'key2': 'value2'}
    
    The key of the string not in <> is 'label'.
    Meanwhile the string inside <>, the part before '=' is the key,
    and the part after '=' is the value.
    
    Parameters
    ----------
    header : list[str]
        Header to decompose.
    
    Returns
    -------
    info : list[dict]
        List of the decomposed header.

    Examples
    --------
    >>> h = [AAA<V=W><X=Y>,BBB<X=Z>]
    >>> info = header_decomposition(h)
    >>> info
    [{'label': 'AAA', 'V': 'W', 'X': 'Y'}, {'label': 'BBB', 'X': 'Z'}]
    '''
    info : list[dict] = []
    for name in header:
        d = dict()
        label = re.findall('\A[^<]+', name)[0]
        d['label'] = label
        params = re.findall('<[a-z]+=[a-z]+>', name)
        for param in params:
            p = re.findall('[a-z]+', param)
            d[p[0]] = p[1]
    
        info.append(d)

    return info
