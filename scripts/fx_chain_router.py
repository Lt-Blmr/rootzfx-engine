import json
import logging

# Optional future expansion: This could be loaded from JSON instead
FX_PRESETS = {
    'dub': ['analog_delay', 'spring_reverb', 'low_pass_filter'],
    'roots reggae': ['tape_echo', 'chorus', 'reverb'],
    'ska': ['compressor', 'plate_reverb'],
    'rocksteady': ['tremolo', 'delay'],
    'dancehall': ['flanger', 'bitcrusher']
}

def apply_fx_chain(metadata, preview=False):
    """
    Given a metadata dict, return a suggested FX chain.
    :param metadata: dict with keys like 'style', 'bpm', 'instrument'
    :param preview: if True, prints out the logic instead of returning
    :return: list of FX modules (ordered)
    """
    style = metadata.get('style', '').lower()
    bpm = metadata.get('bpm', 90)
    instrument = metadata.get('instrument', 'guitar').lower()

    fx_chain = FX_PRESETS.get(style, ['reverb'])

    # Optional adjustments based on tempo or instrument
    if bpm < 75 and 'delay' not in fx_chain:
        fx_chain.append('delay')
    if instrument == 'bass':
        fx_chain.insert(0, 'subharmonic_boost')
        if 'reverb' in fx_chain:
            fx_chain.remove('reverb')

    if preview:
        print(f"Selected FX Chain for {style} @ {bpm} BPM on {instrument}:")
        print(" → ".join(fx_chain))
    return fx_chain

# CLI Test
if __name__ == "__main__":
    test_meta = {
        'style': 'Dub',
        'bpm': 68,
        'instrument': 'guitar'
    }
    apply_fx_chain(test_meta, preview=True)
