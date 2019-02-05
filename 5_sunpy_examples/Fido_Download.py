def fido_down(out_path='/unsafe/ddp/Fits_files/AIA/193/', start_endtime=["2016-11-10 00:00:00", "2016-11-10 06:00:00"],
              wvlnth=193, Inst='aia', samplerate=1):
    """
    :param out_path: Path to save fits files to
    :param start_endtime: First number gives startpoint, second gives endpoint
    :param wvlnth: Chosen Wavelength to download
    :param Inst: Chosen Instrument - can be any from http://sdac.virtualsolar.org/cgi/show_details?keyword=INSTRUMENT
    :param samplerate: In hours
    :return: Downloads the selected files after confirming with enter
    """
    from sunpy.net import Fido, attrs as a
    import astropy.units as u
    from os import makedirs as newdir

    start_time = start_endtime[0]  # YYYY-MM-DD HH:MM:SS
    end_time = start_endtime[1]
    lambda_ang = (wvlnth * u.Angstrom)  # Convert the Wavelength to Angstroms
    samplerate_hours = samplerate * u.hour  # Convert samplerate to temporal units

    fido = Fido.search(a.Time(start=start_time, end=end_time),  # Search the VSO site with the selected parameters
                       a.Instrument(Inst),
                       a.Wavelength(lambda_ang),
                       a.vso.Sample(samplerate_hours))

    print(fido)

    input('Press enter to download the selected files')  # Allows to look at file list before downloading

    newdir(out_path, exist_ok=True)  # Check if the directory already exists: if it does not, create it
    Fido.fetch(fido, path=f'{out_path}/')


    print(f'Done Downloading {len(fido)} files to {out_path}')


