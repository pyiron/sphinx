import numpy as np
from typing import Optional
from stinx.toolkit import fill_values


class sphinx:
    @staticmethod
    def create(
        structure: Optional[dict] = None,
        basis: Optional[dict] = None,
        pawPot: Optional[dict] = None,
        PAWHamiltonian: Optional[dict] = None,
        spinConstraint: Optional[dict] = None,
        initialGuess: Optional[dict] = None,
        pseudoPot: Optional[dict] = None,
        PWHamiltonian: Optional[dict] = None,
        main: Optional[dict] = None,
    ):
        """
        Args:
            structure (dict): (Optional)
            basis (dict): (Optional)
            pawPot (dict): The pawPot group defines the PAW potentials, by a sequence of species groups. The order of species must agree with the structure group. (Optional)
            PAWHamiltonian (dict): (Optional)
            spinConstraint (dict): (Optional)
            initialGuess (dict): In order to start a DFT calculations, one must set up an initial guess for the density and for the wave functions. The initialGuess group defines how this is done, as well as a few other settings (such as keeping the waves on disk to save RAM). The default is to set up the density from a superposition of atomic densities, and the wave-functions from a single-step LCAO calculation, using the atomic valence orbitals. This works exceptionally well. If you want to finetune the behavior, the initialGuess group must contain a waves or a rho group. Otherwise, you may omit the waves and rho groups to get the default behavior. Additionally, the initialGuess group may contain an occupations group to set up initial occupations (notably when keeping them fixed), and an exchange group for hybrid functionals. (Optional)
            pseudoPot (dict): The pseudoPot group defines the norm-conserving pseudopotentials by a sequence of species groups. The order of species must agree with the structure group.

Note: PAW and norm-conserving pseudopotentials cannot be mixed. Using pseudoPot requires to use PWHamiltonian to define the Hamiltonian. (Optional)
            PWHamiltonian (dict): (Optional)
            main (dict): (Optional)
        """
        return fill_values(
            structure=structure,
            basis=basis,
            pawPot=pawPot,
            PAWHamiltonian=PAWHamiltonian,
            spinConstraint=spinConstraint,
            initialGuess=initialGuess,
            pseudoPot=pseudoPot,
            PWHamiltonian=PWHamiltonian,
            main=main,
        )

    class structure:
        @staticmethod
        def create(
            cell: list,
            movable: Optional[bool] = None,
            movableX: Optional[bool] = None,
            movableY: Optional[bool] = None,
            movableZ: Optional[bool] = None,
            species: Optional[dict] = None,
            symmetry: Optional[dict] = None,
        ):
            """
            Args:
                cell (list): Cell matrix.
                movable (bool): Allow atoms to move. Default: True. (Optional)
                movableX (bool): Allow atoms to move in the x direction. Default: True. (Optional)
                movableY (bool): Allow atoms to move in the y direction. Default: True. (Optional)
                movableZ (bool): Allow atoms to move in the z direction. Default: True. (Optional)
                species (dict): (Optional)
                symmetry (dict): (Optional)
            """
            return fill_values(
                cell=cell,
                movable=movable,
                movableX=movableX,
                movableY=movableY,
                movableZ=movableZ,
                species=species,
                symmetry=symmetry,
            )

        class species:
            @staticmethod
            def create(
                element: Optional[str] = None,
                atom: Optional[dict] = None,
            ):
                """
                Args:
                    element (str): Element. (Optional)
                    atom (dict): (Optional)
                """
                return fill_values(
                    element=element,
                    atom=atom,
                )

            class atom:
                @staticmethod
                def create(
                    coords: Optional[np.ndarray] = None,
                    relative: Optional[bool] = None,
                    movableLine: Optional[list] = None,
                    label: Optional[str] = None,
                    movable: Optional[bool] = None,
                    movableX: Optional[bool] = None,
                    movableY: Optional[bool] = None,
                    movableZ: Optional[bool] = None,
                ):
                    """
                    Args:
                        coords (np.ndarray): Atomic coordinates. (Optional)
                        relative (bool): The coordinates are given relative to the unit cell vectors. (Optional)
                        movableLine (list): The movement of the atom is restricted to a line. The value gives the direction of the line as a 3-vector. (Optional)
                        label (str): Assign a label (or rather a tag) to this atom. If labels are used, atoms with different labels are considered inequivalent. Think of spin configurations for a use-case. (Optional)
                        movable (bool): Allow atoms to move. Default: True. (Optional)
                        movableX (bool): Allow atoms to move in the x direction. Default: True. (Optional)
                        movableY (bool): Allow atoms to move in the y direction. Default: True. (Optional)
                        movableZ (bool): Allow atoms to move in the z direction. Default: True. (Optional)
                    """
                    return fill_values(
                        coords=coords,
                        relative=relative,
                        movableLine=movableLine,
                        label=label,
                        movable=movable,
                        movableX=movableX,
                        movableY=movableY,
                        movableZ=movableZ,
                    )

        class symmetry:
            @staticmethod
            def create(
                operator: list,
            ):
                """
                Args:
                    operator (list): Symmetry operator.
                """
                return fill_values(
                    operator=operator,
                )

    class basis:
        @staticmethod
        def create(
            eCut: float,
            gCut: Optional[float] = None,
            folding: Optional[int] = None,
            mesh: Optional[list] = None,
            meshAccuracy: Optional[float] = None,
            saveMemory: Optional[bool] = None,
            kPoint: Optional[dict] = None,
            kPoints: Optional[dict] = None,
        ):
            """
            Args:
                eCut (float): Energy cutoff.
                gCut (float): Gradient cutoff. (Optional)
                folding (int): Folding. (Optional)
                mesh (list): Mesh. (Optional)
                meshAccuracy (float): Mesh accuracy. (Optional)
                saveMemory (bool): Save memory. (Optional)
                kPoint (dict): (Optional)
                kPoints (dict): (Optional)
            """
            return fill_values(
                eCut=eCut,
                gCut=gCut,
                folding=folding,
                mesh=mesh,
                meshAccuracy=meshAccuracy,
                saveMemory=saveMemory,
                kPoint=kPoint,
                kPoints=kPoints,
            )

        class kPoint:
            @staticmethod
            def create(
                coords: np.ndarray,
                relative: Optional[bool] = None,
                weight: Optional[float] = None,
            ):
                """
                Args:
                    coords (np.ndarray): The k-point coordinates as a 3-vector. Unless the relative tag is employed, the coordinates are Cartesian.
                    relative (bool): The coordinates are given relative to the unit cell vectors. (Optional)
                    weight (float): The weight of the k-point in the sampling. (Optional)
                """
                return fill_values(
                    coords=coords,
                    relative=relative,
                    weight=weight,
                )

        class kPoints:
            @staticmethod
            def create(
                relative: Optional[bool] = None,
                dK: Optional[float] = None,
                from_: Optional[dict] = None,
                to: Optional[dict] = None,
            ):
                """
                Args:
                    relative (bool): The coordinates are given relative to the unit cell vectors. (Optional)
                    dK (float): Set the number of intermediate k-points such that the distance is at most dK. (Optional)
                    from_ (dict): The from group (within the kPoints group) adds a single k-point at the desired position. It may be used multiple times. (Optional)
                    to (dict): The to group (within the kPoints group) adds a line of k-points from the previous one to a new position. The number of points is set directly with nPoints or indirectly via dK. (Optional)
                """
                return fill_values(
                    relative=relative,
                    dK=dK,
                    from_=from_,
                    to=to,
                )

            class from_:
                @staticmethod
                def create(
                    coords: np.ndarray,
                    relative: Optional[bool] = None,
                    label: Optional[str] = None,
                ):
                    """
                    The from group (within the kPoints group) adds a single k-point at the desired position. It may be used multiple times.

                    Args:
                        coords (np.ndarray): The k-point coordinates as a 3-vector. If the relative flag is not given.
                        relative (bool): The coordinates are given relative to the unit cell vectors. (Optional)
                        label (str): Assign a label (or rather a tag) to this k-point. If labels are used, k-points with different labels are considered inequivalent. (Optional)
                    """
                    return fill_values(
                        coords=coords,
                        relative=relative,
                        label=label,
                    )

            class to:
                @staticmethod
                def create(
                    coords: np.ndarray,
                    relative: Optional[bool] = None,
                    label: Optional[str] = None,
                    dK: Optional[float] = None,
                    nPoints: Optional[int] = None,
                ):
                    """
                    The to group (within the kPoints group) adds a line of k-points from the previous one to a new position. The number of points is set directly with nPoints or indirectly via dK.

                    Args:
                        coords (np.ndarray): The k-point coordinates as a 3-vector. If the relative flag is not given, the units are 1/bohr.
                        relative (bool): The coordinates are given relative to the unit cell vectors. (Optional)
                        label (str): Assign a label (or rather a tag) to this k-point. If labels are used, k-points with different labels are considered inequivalent. (Optional)
                        dK (float): Set the number of intermediate k-points such that the distance is at most dK. (Optional)
                        nPoints (int): Specify number of points to add. The final one will be at coords. (Optional)
                    """
                    return fill_values(
                        coords=coords,
                        relative=relative,
                        label=label,
                        dK=dK,
                        nPoints=nPoints,
                    )

    class pawPot:
        @staticmethod
        def create(
            species: Optional[dict] = None,
        ):
            """
            The pawPot group defines the PAW potentials, by a sequence of species groups. The order of species must agree with the structure group.

            Args:
                species (dict): (Optional)
            """
            return fill_values(
                species=species,
            )

        class species:
            @staticmethod
            def create(
                potential: str,
                potType: str,
                name: Optional[str] = None,
                element: Optional[str] = None,
                lMaxRho: Optional[int] = None,
                angularGrid: Optional[int] = None,
                nRadGrid: Optional[int] = None,
                checkOverlap: Optional[bool] = None,
                rPAW: Optional[float] = None,
            ):
                """
                Args:
                    potential (str): Name of the potential file.
                    potType (str): Type of the potential file.
                    name (str): English name of the element. (Optional)
                    element (str): Chemical symbol of the element. (Optional)
                    lMaxRho (int): Truncate the spherical expansion of densities (and compensation charges) at this l. (Optional)
                    angularGrid (int): Choose a different angular grid for xc calculation in the PAW sphere. Larger is finer. Default: 7 (110 points). (Optional)
                    nRadGrid (int): Interpolate to a different radial grid. (Optional)
                    checkOverlap (bool): Check that PAW norm is garantueed to be positive definite in the limit of large cutoffs. Some problematic PAW potentials may fail the check, but work normally in some circumstances, so you can switch off the check here. Default: True. (Optional)
                    rPAW (float): Change the PAW radius used for atomic quantities "inside the PAW sphere". (Optional)
                """
                return fill_values(
                    potential=potential,
                    potType=potType,
                    name=name,
                    element=element,
                    lMaxRho=lMaxRho,
                    angularGrid=angularGrid,
                    nRadGrid=nRadGrid,
                    checkOverlap=checkOverlap,
                    rPAW=rPAW,
                )

    class PAWHamiltonian:
        @staticmethod
        def create(
            xc: str,
            ekt: Optional[float] = None,
            MethfesselPaxton: Optional[float] = None,
            FermiDirac: Optional[int] = None,
            nEmptyStates: Optional[int] = None,
            nExcessElectrons: Optional[int] = None,
            spinPolarized: Optional[bool] = None,
            dipoleCorrection: Optional[bool] = None,
            zField: Optional[float] = None,
            vExt: Optional[dict] = None,
            xcMesh: Optional[dict] = None,
            vdwCorrection: Optional[dict] = None,
            HubbardU: Optional[dict] = None,
        ):
            """
            Args:
                xc (str): The exchange-correlation functional to use.
                ekt (float): The electronic temperature. (Optional)
                MethfesselPaxton (float): If ≥0, use Methfessel-Paxton smearing of indicated order. Order 0 is same as Gaussian smearing. (Optional)
                FermiDirac (int): If ≥0, use FermiDirac smearing of indicated order. Order 1 corresponds to first-order corrections. Higher orders are not yet implemented. Default: 0. (Optional)
                nEmptyStates (int): The number of empty states to include in the calculation. (Optional)
                nExcessElectrons (int): The number of excess electrons to include in the calculation. (Optional)
                spinPolarized (bool): Whether to perform a spin-polarized calculation. (Optional)
                dipoleCorrection (bool): Use the dipole correction for slab systems. The in-plane lattice must be perpendicular to the z- axis, and the third basis vector must be aligned with the z-axis. For charged calculation, this requests the generalized dipole correction, which may need some care for initializing the charge (see charged in the initialGuess group). (Optional)
                zField (float): Use an additional electric field along z when using the dipole correction (eV/bohr). (Optional)
                vExt (dict): External potential. (Optional)
                xcMesh (dict): Mesh for the exchange-correlation potential. (Optional)
                vdwCorrection (dict): Van der Waals correction. (Optional)
                HubbardU (dict): Hubbard U. (Optional)
            """
            return fill_values(
                xc=xc,
                ekt=ekt,
                MethfesselPaxton=MethfesselPaxton,
                FermiDirac=FermiDirac,
                nEmptyStates=nEmptyStates,
                nExcessElectrons=nExcessElectrons,
                spinPolarized=spinPolarized,
                dipoleCorrection=dipoleCorrection,
                zField=zField,
                vExt=vExt,
                xcMesh=xcMesh,
                vdwCorrection=vdwCorrection,
                HubbardU=HubbardU,
            )

        class vExt:
            @staticmethod
            def create(
                file: str,
            ):
                """
                External potential

                Args:
                    file (str): The file containing the external potential.
                """
                return fill_values(
                    file=file,
                )

        class xcMesh:
            @staticmethod
            def create(
                eCut: float,
                mesh: Optional[list] = None,
                meshAccuracy: Optional[float] = None,
            ):
                """
                Mesh for the exchange-correlation potential

                Args:
                    eCut (float): The energy cutoff for the mesh.
                    mesh (list): The mesh for the exchange-correlation potential. (Optional)
                    meshAccuracy (float): The accuracy of the mesh. (Optional)
                """
                return fill_values(
                    eCut=eCut,
                    mesh=mesh,
                    meshAccuracy=meshAccuracy,
                )

        class vdwCorrection:
            @staticmethod
            def create(
                method: str,
                combinationRule: Optional[str] = None,
            ):
                """
                Van der Waals correction

                Args:
                    method (str): The method to use for the van der Waals correction.
                    combinationRule (str): The combination rule to use for the van der Waals correction. (Optional)
                """
                return fill_values(
                    method=method,
                    combinationRule=combinationRule,
                )

        class HubbardU:
            @staticmethod
            def create(
                verbose: Optional[bool] = None,
                AO: Optional[dict] = None,
                MO: Optional[dict] = None,
            ):
                """
                Hubbard U

                Args:
                    verbose (bool): Verbose output. (Optional)
                    AO (dict): AO. (Optional)
                    MO (dict): The MO group within the HubbardU group defines on-site correlation corrections using MO orbital projectors. The molecular orbitals (MOs) are constructed from atomic orbitals (AOs) of given radial shape. This shape is defined in the orbital group. The MO projectors are constructed from AO projectors such that a normalized MO is projected to unity. The AO projectors include also the atomic PAW normalization. (Optional)
                """
                return fill_values(
                    verbose=verbose,
                    AO=AO,
                    MO=MO,
                )

            class AO:
                @staticmethod
                def create(
                    orbital: Optional[dict] = None,
                ):
                    """
                    AO

                    Args:
                        orbital (dict): Orbital. (Optional)
                    """
                    return fill_values(
                        orbital=orbital,
                    )

                class orbital:
                    @staticmethod
                    def create(
                        file: str,
                        iot: int,
                        fromPotential: Optional[bool] = None,
                        is_: Optional[int] = None,
                    ):
                        """
                        Orbital

                        Args:
                            file (str): Get orbital shape from this quamol-data_type sxb file.
                            iot (int): Which orbital to take. Starts at 0.
                            fromPotential (bool): Get orbital shape from potential. This is not recommended. (Optional)
                            is_ (int): species id within file (starts at 0). If not given, assumes same species ordering in sxb file as in input file. (Optional)
                        """
                        return fill_values(
                            file=file,
                            iot=iot,
                            fromPotential=fromPotential,
                            is_=is_,
                        )

            class MO:
                @staticmethod
                def create(
                    element: str,
                    orbital: Optional[dict] = None,
                    species: Optional[int] = None,
                    label: Optional[str] = None,
                    maxDist: Optional[float] = None,
                    minDist: Optional[float] = None,
                    nInterpolate: Optional[int] = None,
                    nRadGrid: Optional[int] = None,
                    rCut: Optional[float] = None,
                    cutWidth: Optional[float] = None,
                    mMO: Optional[int] = None,
                    sign: Optional[int] = None,
                    U: Optional[float] = None,
                    shift: Optional[float] = None,
                ):
                    """
                    The MO group within the HubbardU group defines on-site correlation corrections using MO orbital projectors. The molecular orbitals (MOs) are constructed from atomic orbitals (AOs) of given radial shape. This shape is defined in the orbital group. The MO projectors are constructed from AO projectors such that a normalized MO is projected to unity. The AO projectors include also the atomic PAW normalization.

                    Args:
                        element (str): defines the element via its name.
                        orbital (dict): Orbital. (Optional)
                        species (int): defines the element via its species number (1,2,3...) within the input file. (Optional)
                        label (str): defines the relevant atoms via their label. All atoms must belong to the same species. See also label in the atom group. (Optional)
                        maxDist (float): maximum distance of two atoms to be considered a molecule. Default: 10.0. (Optional)
                        minDist (float): minimum distance of two atoms to be considered a molecule. Default value is half the maximum distance. Default: 5.0. (Optional)
                        nInterpolate (int): number of distance points used to interpolate orbital normalization. Default: 100. (Optional)
                        nRadGrid (int): number of radial points to represent atomic orbital projector. Default: 200. (Optional)
                        rCut (float): The cutoff radius for the atomic orbital. (Optional)
                        cutWidth (float): The width of the cutoff region. Default: 0.7. (Optional)
                        mMO (int): rotational constant of orbital symmetry (σ=0, π=1). (Optional)
                        sign (int): relative sign of orbitals on both atoms. Can be +1 or -1. (Optional)
                        U (float): The Hubbard U value. (Optional)
                        shift (float): An additional energy shift of the. (Optional)
                    """
                    return fill_values(
                        element=element,
                        orbital=orbital,
                        species=species,
                        label=label,
                        maxDist=maxDist,
                        minDist=minDist,
                        nInterpolate=nInterpolate,
                        nRadGrid=nRadGrid,
                        rCut=rCut,
                        cutWidth=cutWidth,
                        mMO=mMO,
                        sign=sign,
                        U=U,
                        shift=shift,
                    )

                class orbital:
                    @staticmethod
                    def create(
                        file: str,
                        iot: int,
                        fromPotential: Optional[bool] = None,
                        is_: Optional[int] = None,
                    ):
                        """
                        Orbital

                        Args:
                            file (str): Get orbital shape from this quamol-data_type sxb file.
                            iot (int): Which orbital to take. Starts at 0.
                            fromPotential (bool): Get orbital shape from potential. This is not recommended. (Optional)
                            is_ (int): species id within file (starts at 0). If not given, assumes same species ordering in sxb file as in input file. (Optional)
                        """
                        return fill_values(
                            file=file,
                            iot=iot,
                            fromPotential=fromPotential,
                            is_=is_,
                        )

    class spinConstraint:
        @staticmethod
        def create(
            label: Optional[str] = None,
            constraint: Optional[float] = None,
            file: Optional[str] = None,
        ):
            """
            Args:
                label (str): The present constraint applies to atoms with the given label. (Optional)
                constraint (float): Value of the desired atomic spin. (Optional)
                file (str): Read all spin constraints from this file. (Optional)
            """
            return fill_values(
                label=label,
                constraint=constraint,
                file=file,
            )

    class initialGuess:
        @staticmethod
        def create(
            noWavesStorage: Optional[bool] = None,
            noRhoStorage: Optional[bool] = None,
            waves: Optional[dict] = None,
            rho: Optional[dict] = None,
            occupations: Optional[dict] = None,
            exchange: Optional[dict] = None,
        ):
            """
            In order to start a DFT calculations, one must set up an initial guess for the density and for the wave functions. The initialGuess group defines how this is done, as well as a few other settings (such as keeping the waves on disk to save RAM). The default is to set up the density from a superposition of atomic densities, and the wave-functions from a single-step LCAO calculation, using the atomic valence orbitals. This works exceptionally well. If you want to finetune the behavior, the initialGuess group must contain a waves or a rho group. Otherwise, you may omit the waves and rho groups to get the default behavior. Additionally, the initialGuess group may contain an occupations group to set up initial occupations (notably when keeping them fixed), and an exchange group for hybrid functionals.

            Args:
                noWavesStorage (bool): Do not save wavefunctions after the initial guess. (Optional)
                noRhoStorage (bool): Do not save the density after the initial guess. (Optional)
                waves (dict): (Optional)
                rho (dict): (Optional)
                occupations (dict): The occupations group within the initialGuess group defines the initial occupations. This makes sense if the density is computed from wave functions, or if the occupations are going to be fixed at these values. (Optional)
                exchange (dict): Note: hybrid functionals are experimental and slow. The exchange group allows to set waves for the non-local exchange operator at the initialization stage. This is necessary if you want to initialize the waves from an LCAO calculation. The exchange group contains a single parameter, file, which contains the filename of the waves file to be used. (Optional)
            """
            return fill_values(
                noWavesStorage=noWavesStorage,
                noRhoStorage=noRhoStorage,
                waves=waves,
                rho=rho,
                occupations=occupations,
                exchange=exchange,
            )

        class waves:
            @staticmethod
            def create(
                file: Optional[str] = None,
                random: Optional[bool] = None,
                keepWavesOnDisk: Optional[bool] = None,
                lcao: Optional[dict] = None,
            ):
                """
                Args:
                    file (str): Read wave functions from this file. (Optional)
                    random (bool): Initialize wave functions randomly. (Optional)
                    keepWavesOnDisk (bool): Keep waves on disk, load only a single k-point at each time. May save a lot of RAM, but can be quite a bottleneck on small systems. (Optional)
                    lcao (dict): (Optional)
                """
                return fill_values(
                    file=file,
                    random=random,
                    keepWavesOnDisk=keepWavesOnDisk,
                    lcao=lcao,
                )

            class lcao:
                @staticmethod
                def create(
                    maxSteps: Optional[int] = None,
                    dEnergy: Optional[float] = None,
                ):
                    """
                    Args:
                        maxSteps (int): Maximum number of SCF steps. (Optional)
                        dEnergy (float): Energy convergence criterion. (Optional)
                    """
                    return fill_values(
                        maxSteps=maxSteps,
                        dEnergy=dEnergy,
                    )

        class rho:
            @staticmethod
            def create(
                file: Optional[str] = None,
                fromWave: Optional[bool] = None,
                random: Optional[bool] = None,
                atomicOrbitals: Optional[bool] = None,
                spinMoment: Optional[bool] = None,
                atomicSpin: Optional[dict] = None,
                charged: Optional[dict] = None,
            ):
                """
                Args:
                    file (str): Read density from this file. (Optional)
                    fromWave (bool): Compute from the wave functions (which must be from file in this case). (Optional)
                    random (bool): Initialize density randomly. (Optional)
                    atomicOrbitals (bool): Initialize density from atomic orbitals. (Optional)
                    spinMoment (bool): When from atomic densities, apply a global spin polarization. (Optional)
                    atomicSpin (dict): Atomic spin. (Optional)
                    charged (dict): (Optional)
                """
                return fill_values(
                    file=file,
                    fromWave=fromWave,
                    random=random,
                    atomicOrbitals=atomicOrbitals,
                    spinMoment=spinMoment,
                    atomicSpin=atomicSpin,
                    charged=charged,
                )

            class atomicSpin:
                @staticmethod
                def create(
                    spin: Optional[float] = None,
                    label: Optional[str] = None,
                    file: Optional[str] = None,
                ):
                    """
                    Atomic spin

                    Args:
                        spin (float): The spin of the atom. (Optional)
                        label (str): For which atoms to apply this spin. (Optional)
                        file (str): Read atomic spins from this file (one spin per line), one per atom, in sequential order. (Optional)
                    """
                    return fill_values(
                        spin=spin,
                        label=label,
                        file=file,
                    )

            class charged:
                @staticmethod
                def create(
                    charge: float,
                    beta: Optional[float] = None,
                    z: Optional[float] = None,
                    coords: Optional[np.ndarray] = None,
                ):
                    """
                    Args:
                        charge (float): The classical charge (i.e. -nExcessElectrons from the PAWHamiltonian or PWHamiltonian group).
                        beta (float): Gaussian broadening. (Optional)
                        z (float): Request a sheet charge at this z. (Optional)
                        coords (np.ndarray): Request a Gaussian charge at this position. (Optional)
                    """
                    return fill_values(
                        charge=charge,
                        beta=beta,
                        z=z,
                        coords=coords,
                    )

        class occupations:
            @staticmethod
            def create(
                kPoints: Optional[dict] = None,
                spin: Optional[dict] = None,
                bands: Optional[dict] = None,
            ):
                """
                The occupations group within the initialGuess group defines the initial occupations. This makes sense if the density is computed from wave functions, or if the occupations are going to be fixed at these values.

                Args:
                    kPoints (dict): (Optional)
                    spin (dict): (Optional)
                    bands (dict): (Optional)
                """
                return fill_values(
                    kPoints=kPoints,
                    spin=spin,
                    bands=bands,
                )

            class kPoints:
                @staticmethod
                def create(
                    spin: Optional[dict] = None,
                    bands: Optional[dict] = None,
                ):
                    """
                    Args:
                        spin (dict): (Optional)
                        bands (dict): (Optional)
                    """
                    return fill_values(
                        spin=spin,
                        bands=bands,
                    )

                class spin:
                    @staticmethod
                    def create(
                        bands: Optional[dict] = None,
                    ):
                        """
                        Args:
                            bands (dict): (Optional)
                        """
                        return fill_values(
                            bands=bands,
                        )

                    class bands:
                        @staticmethod
                        def create(
                            value: list,
                            range: list,
                            focc: int,
                        ):
                            """
                            Args:
                                value (list): Specifically list the indices affected.
                                range (list): Specify start and end index.
                                focc (int): The occupation value.
                            """
                            return fill_values(
                                value=value,
                                range=range,
                                focc=focc,
                            )

                class bands:
                    @staticmethod
                    def create(
                        value: list,
                        range: list,
                        focc: int,
                    ):
                        """
                        Args:
                            value (list): Specifically list the indices affected.
                            range (list): Specify start and end index.
                            focc (int): The occupation value.
                        """
                        return fill_values(
                            value=value,
                            range=range,
                            focc=focc,
                        )

            class spin:
                @staticmethod
                def create(
                    bands: Optional[dict] = None,
                ):
                    """
                    Args:
                        bands (dict): (Optional)
                    """
                    return fill_values(
                        bands=bands,
                    )

                class bands:
                    @staticmethod
                    def create(
                        value: list,
                        range: list,
                        focc: int,
                    ):
                        """
                        Args:
                            value (list): Specifically list the indices affected.
                            range (list): Specify start and end index.
                            focc (int): The occupation value.
                        """
                        return fill_values(
                            value=value,
                            range=range,
                            focc=focc,
                        )

            class bands:
                @staticmethod
                def create(
                    value: list,
                    range: list,
                    focc: int,
                ):
                    """
                    Args:
                        value (list): Specifically list the indices affected.
                        range (list): Specify start and end index.
                        focc (int): The occupation value.
                    """
                    return fill_values(
                        value=value,
                        range=range,
                        focc=focc,
                    )

        class exchange:
            @staticmethod
            def create(
                file: Optional[str] = None,
            ):
                """
                Note: hybrid functionals are experimental and slow. The exchange group allows to set waves for the non-local exchange operator at the initialization stage. This is necessary if you want to initialize the waves from an LCAO calculation. The exchange group contains a single parameter, file, which contains the filename of the waves file to be used.

                Args:
                    file (str): Read exchange-correlation potential from this file. (Optional)
                """
                return fill_values(
                    file=file,
                )

    class pseudoPot:
        @staticmethod
        def create(
            species: Optional[dict] = None,
        ):
            """
            The pseudoPot group defines the norm-conserving pseudopotentials by a sequence of species groups. The order of species must agree with the structure group.

Note: PAW and norm-conserving pseudopotentials cannot be mixed. Using pseudoPot requires to use PWHamiltonian to define the Hamiltonian.

            Args:
                species (dict): (Optional)
            """
            return fill_values(
                species=species,
            )

        class species:
            @staticmethod
            def create(
                name: str,
                potential: str,
                valenceCharge: float,
                lMax: int,
                lLoc: int,
                rGauss: float,
                atomicRhoOcc: float,
                reciprocalMass: float,
                dampingMass: float,
                ionicMass: float,
                element: Optional[str] = None,
                lcaoOrbital: Optional[int] = None,
            ):
                """
                Args:
                    name (str): English name of the element.
                    potential (str): Name of the potential file.
                    valenceCharge (float): The valence charge of the atom.
                    lMax (int): The maximum l value to include in the pseudopotential.
                    lLoc (int): The l value to use for the local part of the pseudopotential.
                    rGauss (float): Broadening of compensation charge, usually 1.
                    atomicRhoOcc (float): Occupation numbers for charge initialization.
                    reciprocalMass (float): Mass of the ion.
                    dampingMass (float): Damping for damped-Newton geometry optimization. (curretly not used).
                    ionicMass (float): Mass of the ion.
                    element (str): Element. (Optional)
                    lcaoOrbital (int): Which orbitals should be used for lcao initialization. Note: s,p,d, and f are predefined constants in parameters.sx. (Optional)
                """
                return fill_values(
                    name=name,
                    potential=potential,
                    valenceCharge=valenceCharge,
                    lMax=lMax,
                    lLoc=lLoc,
                    rGauss=rGauss,
                    atomicRhoOcc=atomicRhoOcc,
                    reciprocalMass=reciprocalMass,
                    dampingMass=dampingMass,
                    ionicMass=ionicMass,
                    element=element,
                    lcaoOrbital=lcaoOrbital,
                )

    class PWHamiltonian:
        @staticmethod
        def create(
            xc: str,
            ekt: Optional[float] = None,
            MethfesselPaxton: Optional[float] = None,
            FermiDirac: Optional[float] = None,
            nEmptyStates: Optional[int] = None,
            nExcessElectrons: Optional[int] = None,
            spinPolarized: Optional[bool] = None,
            dipoleCorrection: Optional[bool] = None,
            zField: Optional[float] = None,
        ):
            """
            Args:
                xc (str): The exchange-correlation functional to use.
                ekt (float): The electronic temperature. (Optional)
                MethfesselPaxton (float): If ≥0, use Methfessel-Paxton smearing of indicated order. Order 0 is same as Gaussian smearing. (Optional)
                FermiDirac (float): If ≥0, use FermiDirac smearing of indicated order. Order 1 corresponds to first-order corrections. Higher orders are not yet implemented. Default: 0. (Optional)
                nEmptyStates (int): The number of empty states to include in the calculation. (Optional)
                nExcessElectrons (int): The number of excess electrons to include in the calculation. (Optional)
                spinPolarized (bool): Whether to perform a spin-polarized calculation. (Optional)
                dipoleCorrection (bool): Use the dipole correction for slab systems. The in-plane lattice must be perpendicular to the z- axis, and the third basis vector must be aligned with the z-axis. For charged calculation, this requests the generalized dipole correction, which may need some care for initializing the charge (see charged in the initialGuess group). (Optional)
                zField (float): Use an additional electric field along z when using the dipole correction. (Optional)
            """
            return fill_values(
                xc=xc,
                ekt=ekt,
                MethfesselPaxton=MethfesselPaxton,
                FermiDirac=FermiDirac,
                nEmptyStates=nEmptyStates,
                nExcessElectrons=nExcessElectrons,
                spinPolarized=spinPolarized,
                dipoleCorrection=dipoleCorrection,
                zField=zField,
            )

    class main:
        @staticmethod
        def create(
            **kwargs
        ):
            """
            Args:
                scfDiag (dict): The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                QN (dict): The QN group selects and controls the geometry optimization via quasi-Newton scheme with BFGS updates. Note: In general, ricQN is the faster algorithm. (Optional)
                linQN (dict): The linQN group selects and controls the geometry optimization via linear quasi-Newton scheme with BFGS updates. Note: In general, ricQN is the faster algorithm. (Optional)
                ricQN (dict): (Optional)
                ric (dict): The ric group defines the parameters for internal coordinate generation. (Optional)
                ricTS (dict): The ricTS group requests a quasi-Newton optimization for 1st-order saddle points (transition states) using updates [11] of an on-the-fly optimized internal-coordinate based initial guess for the Hessian [10]. An initial guess for the reaction coordinate must be known. Note: This is an experimental feature. The optimization should be started within the saddle point region (one negative eigenvalue of the Hesse matrix), otherwise, the algorithm may converge to a different stationary point (a minimum, or a higher-order saddle point). (Optional)
            """
            return fill_values(
                **kwargs
            )

        class scfDiag:
            @staticmethod
            def create(
                dEnergy: Optional[float] = None,
                maxSteps: Optional[int] = None,
                maxResidue: Optional[float] = None,
                printSteps: Optional[int] = None,
                mixingMethod: Optional[str] = None,
                nPulaySteps: Optional[int] = None,
                rhoMixing: Optional[float] = None,
                spinMixing: Optional[float] = None,
                keepRhoFixed: Optional[bool] = None,
                keepOccFixed: Optional[bool] = None,
                keepSpinFixed: Optional[bool] = None,
                spinMoment: Optional[float] = None,
                ekt: Optional[float] = None,
                dipoleCorrection: Optional[bool] = None,
                dSpinMoment: Optional[float] = None,
                noRhoStorage: Optional[bool] = None,
                noWavesStorage: Optional[bool] = None,
                CCG: Optional[dict] = None,
                blockCCG: Optional[dict] = None,
                preconditioner: Optional[dict] = None,
            ):
                """
                The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations.

                Args:
                    dEnergy (float): Free energy convergence criterium. Default: 1e-8. (Optional)
                    maxSteps (int): Max. number of steps (density updates). (Optional)
                    maxResidue (float): Additional requirement for convergence; density residue must fall below this threshold. (Optional)
                    printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                    mixingMethod (str): Method for the density mixing. Constants defined in parameters.sx. Can be PULAY (2) or LINEAR (0). Default: 2. (Optional)
                    nPulaySteps (int): Number of previous steps (densities) to use in Pulay mixing. Default: 7. (Optional)
                    rhoMixing (float): Additional linear mixing factor for density updates (1=full update, 0=no change). Low values may lead to a more stable convergence, but will slow down the calculation if set too low. Default: 1. (Optional)
                    spinMixing (float): Linear mixing parameter for spin densities. (Optional)
                    keepRhoFixed (bool): Do not update the density (for band structures). (Optional)
                    keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                    keepSpinFixed (bool): Do not update the spin density. (Optional)
                    spinMoment (float): Keep the spin moment at this value. (Optional)
                    ekt (float): The electronic temperature. (Optional)
                    dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                    dSpinMoment (float): accuracy of iterative enforcement of spin constraints. Default: 1e-8. (Optional)
                    noRhoStorage (bool): Do not write rho.sxb. (Optional)
                    noWavesStorage (bool): Do not write waves.sxb. (Optional)
                    CCG (dict): The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                    blockCCG (dict): The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states). (Optional)
                    preconditioner (dict): The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result. (Optional)
                """
                return fill_values(
                    dEnergy=dEnergy,
                    maxSteps=maxSteps,
                    maxResidue=maxResidue,
                    printSteps=printSteps,
                    mixingMethod=mixingMethod,
                    nPulaySteps=nPulaySteps,
                    rhoMixing=rhoMixing,
                    spinMixing=spinMixing,
                    keepRhoFixed=keepRhoFixed,
                    keepOccFixed=keepOccFixed,
                    keepSpinFixed=keepSpinFixed,
                    spinMoment=spinMoment,
                    ekt=ekt,
                    dipoleCorrection=dipoleCorrection,
                    dSpinMoment=dSpinMoment,
                    noRhoStorage=noRhoStorage,
                    noWavesStorage=noWavesStorage,
                    CCG=CCG,
                    blockCCG=blockCCG,
                    preconditioner=preconditioner,
                )

            class CCG:
                @staticmethod
                def create(
                    dEnergy: Optional[float] = None,
                    maxSteps: Optional[int] = None,
                    printSteps: Optional[int] = None,
                    initialDiag: Optional[bool] = None,
                    finalDiag: Optional[bool] = None,
                    kappa: Optional[float] = None,
                    keepOccFixed: Optional[bool] = None,
                    ekt: Optional[float] = None,
                    dipoleCorrection: Optional[bool] = None,
                    noRhoStorage: Optional[bool] = None,
                    noWavesStorage: Optional[bool] = None,
                ):
                    """
                    The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations

                    Args:
                        dEnergy (float): Use these settings until energy change fall below this threshold. Default: 1e-8. (Optional)
                        maxSteps (int): Max. number of steps to perform. (Optional)
                        printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                        initialDiag (bool): Perform iterative wave-function optimization based on the initial density. Default: True. (Optional)
                        finalDiag (bool): Perform iterative wave-function optimization based on the final density. (Optional)
                        kappa (float): Perform subspace diagonalization at the end. (optional) Initial mixing between subspace Hamiltonian and wave-function updates. If set to a negative value, the value of κ will be fixed at the absolute value. Otherwise, κ is adapted on the fly. (Optional)
                        keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                        ekt (float): Override electronic temperature setting in the Hamiltonian group. (Optional)
                        dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                        noRhoStorage (bool): Do not write rho.sxb. (Optional)
                        noWavesStorage (bool): Do not write waves.sxb. (Optional)
                    """
                    return fill_values(
                        dEnergy=dEnergy,
                        maxSteps=maxSteps,
                        printSteps=printSteps,
                        initialDiag=initialDiag,
                        finalDiag=finalDiag,
                        kappa=kappa,
                        keepOccFixed=keepOccFixed,
                        ekt=ekt,
                        dipoleCorrection=dipoleCorrection,
                        noRhoStorage=noRhoStorage,
                        noWavesStorage=noWavesStorage,
                    )

            class blockCCG:
                @staticmethod
                def create(
                    dRelEps: Optional[float] = None,
                    maxStepsCCG: Optional[int] = None,
                    blockSize: Optional[int] = None,
                    nSloppy: Optional[int] = None,
                    dEnergy: Optional[float] = None,
                    verbose: Optional[bool] = None,
                    numericalLimit: Optional[float] = None,
                ):
                    """
                    The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states).

                    Args:
                        dRelEps (float): Stop iterating when the change in eigenvalue falls below this fraction of the change in the first (steepest-descent) step. (Optional)
                        maxStepsCCG (int): Max. number of steps to perform. Default: 5. (Optional)
                        blockSize (int): Block size. Default: 64. (Optional)
                        nSloppy (int): Number of sloppy steps. (Optional)
                        dEnergy (float): Use these settings until energy change fall below this threshold. (Optional)
                        verbose (bool): Verbose output. (Optional)
                        numericalLimit (float): Stop iterating when approaching the numerical limit. (Optional)
                    """
                    return fill_values(
                        dRelEps=dRelEps,
                        maxStepsCCG=maxStepsCCG,
                        blockSize=blockSize,
                        nSloppy=nSloppy,
                        dEnergy=dEnergy,
                        verbose=verbose,
                        numericalLimit=numericalLimit,
                    )

            class preconditioner:
                @staticmethod
                def create(
                    type: str,
                    scaling: Optional[float] = None,
                    spinScaling: Optional[float] = None,
                    dielecConstant: Optional[float] = None,
                ):
                    """
                    The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result.

                    Args:
                        type (str): NONE (0). No preconditioning. Ideal for atoms/molecules in vacuum; KERKER (1). Kerker preconditioner. Ideal for metals; CSRB (3). Preconditioner for semiconductors based on the Cappellini-del- Sole-Reining-Bechstedt model dielectric function. Requires dielecConstant; ELLIPTIC (5). An explicit-solver preconditioner. No screening in vacuum region, Thomas-Fermi screening (Kerker-like) elsewhere. Ideal for metallic.
                        scaling (float): Scaling factor for the preconditioner. Default: 1.0. (Optional)
                        spinScaling (float): Scaling factor for the spin part of the preconditioner. Default: 1.0. (Optional)
                        dielecConstant (float): Dielectric constant for the CSRB preconditioner. (Optional)
                    """
                    return fill_values(
                        type=type,
                        scaling=scaling,
                        spinScaling=spinScaling,
                        dielecConstant=dielecConstant,
                    )

        class QN:
            @staticmethod
            def create(
                maxSteps: Optional[int] = None,
                dX: Optional[float] = None,
                dF: Optional[float] = None,
                dEnergy: Optional[float] = None,
                maxStepLength: Optional[float] = None,
                hessian: Optional[str] = None,
                driftFilter: Optional[bool] = None,
                bornOppenheimer: Optional[dict] = None,
            ):
                """
                The QN group selects and controls the geometry optimization via quasi-Newton scheme with BFGS updates. Note: In general, ricQN is the faster algorithm.

                Args:
                    maxSteps (int): Max. number of steps to perform. Default: 50. (Optional)
                    dX (float): Stop iterating when the change in geometry falls below this threshold. Default: 0.01. (Optional)
                    dF (float): Stop iterating when the change in forces falls below this threshold. Default: 0.01. (Optional)
                    dEnergy (float): Use these settings until energy change fall below this threshold. Default: 1e-4. (Optional)
                    maxStepLength (float): maximum allowed displacement (length of displacement vector for a single atom). Larger steps are reduced by scaling. Default: 0.3. (Optional)
                    hessian (str): Initialize Hessian from file. (Optional)
                    driftFilter (bool): Project out the average force and displacement. Default: True. (Optional)
                    bornOppenheimer (dict): The bornOppenheimer group defines the electronic loop within a geometry optimization. It contains one or more of the electronic loop groups. If more than one minimizer is used, the complete electronic loop sequence is executed at each ionic step. (Optional)
                """
                return fill_values(
                    maxSteps=maxSteps,
                    dX=dX,
                    dF=dF,
                    dEnergy=dEnergy,
                    maxStepLength=maxStepLength,
                    hessian=hessian,
                    driftFilter=driftFilter,
                    bornOppenheimer=bornOppenheimer,
                )

            class bornOppenheimer:
                @staticmethod
                def create(
                    scfDiag: Optional[dict] = None,
                ):
                    """
                    The bornOppenheimer group defines the electronic loop within a geometry optimization. It contains one or more of the electronic loop groups. If more than one minimizer is used, the complete electronic loop sequence is executed at each ionic step.

                    Args:
                        scfDiag (dict): The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                    """
                    return fill_values(
                        scfDiag=scfDiag,
                    )

                class scfDiag:
                    @staticmethod
                    def create(
                        dEnergy: Optional[float] = None,
                        maxSteps: Optional[int] = None,
                        maxResidue: Optional[float] = None,
                        printSteps: Optional[int] = None,
                        mixingMethod: Optional[str] = None,
                        nPulaySteps: Optional[int] = None,
                        rhoMixing: Optional[float] = None,
                        spinMixing: Optional[float] = None,
                        keepRhoFixed: Optional[bool] = None,
                        keepOccFixed: Optional[bool] = None,
                        keepSpinFixed: Optional[bool] = None,
                        spinMoment: Optional[float] = None,
                        ekt: Optional[float] = None,
                        dipoleCorrection: Optional[bool] = None,
                        dSpinMoment: Optional[float] = None,
                        noRhoStorage: Optional[bool] = None,
                        noWavesStorage: Optional[bool] = None,
                        CCG: Optional[dict] = None,
                        blockCCG: Optional[dict] = None,
                        preconditioner: Optional[dict] = None,
                    ):
                        """
                        The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations.

                        Args:
                            dEnergy (float): Free energy convergence criterium. Default: 1e-8. (Optional)
                            maxSteps (int): Max. number of steps (density updates). (Optional)
                            maxResidue (float): Additional requirement for convergence; density residue must fall below this threshold. (Optional)
                            printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                            mixingMethod (str): Method for the density mixing. Constants defined in parameters.sx. Can be PULAY (2) or LINEAR (0). Default: 2. (Optional)
                            nPulaySteps (int): Number of previous steps (densities) to use in Pulay mixing. Default: 7. (Optional)
                            rhoMixing (float): Additional linear mixing factor for density updates (1=full update, 0=no change). Low values may lead to a more stable convergence, but will slow down the calculation if set too low. Default: 1. (Optional)
                            spinMixing (float): Linear mixing parameter for spin densities. (Optional)
                            keepRhoFixed (bool): Do not update the density (for band structures). (Optional)
                            keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                            keepSpinFixed (bool): Do not update the spin density. (Optional)
                            spinMoment (float): Keep the spin moment at this value. (Optional)
                            ekt (float): The electronic temperature. (Optional)
                            dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                            dSpinMoment (float): accuracy of iterative enforcement of spin constraints. Default: 1e-8. (Optional)
                            noRhoStorage (bool): Do not write rho.sxb. (Optional)
                            noWavesStorage (bool): Do not write waves.sxb. (Optional)
                            CCG (dict): The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                            blockCCG (dict): The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states). (Optional)
                            preconditioner (dict): The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result. (Optional)
                        """
                        return fill_values(
                            dEnergy=dEnergy,
                            maxSteps=maxSteps,
                            maxResidue=maxResidue,
                            printSteps=printSteps,
                            mixingMethod=mixingMethod,
                            nPulaySteps=nPulaySteps,
                            rhoMixing=rhoMixing,
                            spinMixing=spinMixing,
                            keepRhoFixed=keepRhoFixed,
                            keepOccFixed=keepOccFixed,
                            keepSpinFixed=keepSpinFixed,
                            spinMoment=spinMoment,
                            ekt=ekt,
                            dipoleCorrection=dipoleCorrection,
                            dSpinMoment=dSpinMoment,
                            noRhoStorage=noRhoStorage,
                            noWavesStorage=noWavesStorage,
                            CCG=CCG,
                            blockCCG=blockCCG,
                            preconditioner=preconditioner,
                        )

                    class CCG:
                        @staticmethod
                        def create(
                            dEnergy: Optional[float] = None,
                            maxSteps: Optional[int] = None,
                            printSteps: Optional[int] = None,
                            initialDiag: Optional[bool] = None,
                            finalDiag: Optional[bool] = None,
                            kappa: Optional[float] = None,
                            keepOccFixed: Optional[bool] = None,
                            ekt: Optional[float] = None,
                            dipoleCorrection: Optional[bool] = None,
                            noRhoStorage: Optional[bool] = None,
                            noWavesStorage: Optional[bool] = None,
                        ):
                            """
                            The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations

                            Args:
                                dEnergy (float): Use these settings until energy change fall below this threshold. Default: 1e-8. (Optional)
                                maxSteps (int): Max. number of steps to perform. (Optional)
                                printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                                initialDiag (bool): Perform iterative wave-function optimization based on the initial density. Default: True. (Optional)
                                finalDiag (bool): Perform iterative wave-function optimization based on the final density. (Optional)
                                kappa (float): Perform subspace diagonalization at the end. (optional) Initial mixing between subspace Hamiltonian and wave-function updates. If set to a negative value, the value of κ will be fixed at the absolute value. Otherwise, κ is adapted on the fly. (Optional)
                                keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                                ekt (float): Override electronic temperature setting in the Hamiltonian group. (Optional)
                                dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                                noRhoStorage (bool): Do not write rho.sxb. (Optional)
                                noWavesStorage (bool): Do not write waves.sxb. (Optional)
                            """
                            return fill_values(
                                dEnergy=dEnergy,
                                maxSteps=maxSteps,
                                printSteps=printSteps,
                                initialDiag=initialDiag,
                                finalDiag=finalDiag,
                                kappa=kappa,
                                keepOccFixed=keepOccFixed,
                                ekt=ekt,
                                dipoleCorrection=dipoleCorrection,
                                noRhoStorage=noRhoStorage,
                                noWavesStorage=noWavesStorage,
                            )

                    class blockCCG:
                        @staticmethod
                        def create(
                            dRelEps: Optional[float] = None,
                            maxStepsCCG: Optional[int] = None,
                            blockSize: Optional[int] = None,
                            nSloppy: Optional[int] = None,
                            dEnergy: Optional[float] = None,
                            verbose: Optional[bool] = None,
                            numericalLimit: Optional[float] = None,
                        ):
                            """
                            The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states).

                            Args:
                                dRelEps (float): Stop iterating when the change in eigenvalue falls below this fraction of the change in the first (steepest-descent) step. (Optional)
                                maxStepsCCG (int): Max. number of steps to perform. Default: 5. (Optional)
                                blockSize (int): Block size. Default: 64. (Optional)
                                nSloppy (int): Number of sloppy steps. (Optional)
                                dEnergy (float): Use these settings until energy change fall below this threshold. (Optional)
                                verbose (bool): Verbose output. (Optional)
                                numericalLimit (float): Stop iterating when approaching the numerical limit. (Optional)
                            """
                            return fill_values(
                                dRelEps=dRelEps,
                                maxStepsCCG=maxStepsCCG,
                                blockSize=blockSize,
                                nSloppy=nSloppy,
                                dEnergy=dEnergy,
                                verbose=verbose,
                                numericalLimit=numericalLimit,
                            )

                    class preconditioner:
                        @staticmethod
                        def create(
                            type: str,
                            scaling: Optional[float] = None,
                            spinScaling: Optional[float] = None,
                            dielecConstant: Optional[float] = None,
                        ):
                            """
                            The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result.

                            Args:
                                type (str): NONE (0). No preconditioning. Ideal for atoms/molecules in vacuum; KERKER (1). Kerker preconditioner. Ideal for metals; CSRB (3). Preconditioner for semiconductors based on the Cappellini-del- Sole-Reining-Bechstedt model dielectric function. Requires dielecConstant; ELLIPTIC (5). An explicit-solver preconditioner. No screening in vacuum region, Thomas-Fermi screening (Kerker-like) elsewhere. Ideal for metallic.
                                scaling (float): Scaling factor for the preconditioner. Default: 1.0. (Optional)
                                spinScaling (float): Scaling factor for the spin part of the preconditioner. Default: 1.0. (Optional)
                                dielecConstant (float): Dielectric constant for the CSRB preconditioner. (Optional)
                            """
                            return fill_values(
                                type=type,
                                scaling=scaling,
                                spinScaling=spinScaling,
                                dielecConstant=dielecConstant,
                            )

        class linQN:
            @staticmethod
            def create(
                maxSteps: Optional[int] = None,
                dX: Optional[float] = None,
                dF: Optional[float] = None,
                dEnergy: Optional[float] = None,
                maxStepLength: Optional[float] = None,
                nProjectors: Optional[int] = None,
                hessian: Optional[str] = None,
                driftFilter: Optional[bool] = None,
                bornOppenheimer: Optional[dict] = None,
            ):
                """
                The linQN group selects and controls the geometry optimization via linear quasi-Newton scheme with BFGS updates. Note: In general, ricQN is the faster algorithm.

                Args:
                    maxSteps (int): Max. number of steps to perform. Default: 50. (Optional)
                    dX (float): Stop iterating when the change in geometry falls below this threshold. Default: 0.01. (Optional)
                    dF (float): Stop iterating when the change in forces falls below this threshold. Default: 0.001. (Optional)
                    dEnergy (float): Use these settings until energy change fall below this threshold. Default: 1e-4. (Optional)
                    maxStepLength (float): maximum allowed displacement (length of displacement vector for a single atom). Larger steps are reduced by scaling. Default: 0.3. (Optional)
                    nProjectors (int): Number of projectors. (Optional)
                    hessian (str): Initialize Hessian from file. (Optional)
                    driftFilter (bool): Project out the average force and displacement. Default: True. (Optional)
                    bornOppenheimer (dict): The bornOppenheimer group defines the electronic loop within a geometry optimization. It contains one or more of the electronic loop groups. If more than one minimizer is used, the complete electronic loop sequence is executed at each ionic step. (Optional)
                """
                return fill_values(
                    maxSteps=maxSteps,
                    dX=dX,
                    dF=dF,
                    dEnergy=dEnergy,
                    maxStepLength=maxStepLength,
                    nProjectors=nProjectors,
                    hessian=hessian,
                    driftFilter=driftFilter,
                    bornOppenheimer=bornOppenheimer,
                )

            class bornOppenheimer:
                @staticmethod
                def create(
                    scfDiag: Optional[dict] = None,
                ):
                    """
                    The bornOppenheimer group defines the electronic loop within a geometry optimization. It contains one or more of the electronic loop groups. If more than one minimizer is used, the complete electronic loop sequence is executed at each ionic step.

                    Args:
                        scfDiag (dict): The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                    """
                    return fill_values(
                        scfDiag=scfDiag,
                    )

                class scfDiag:
                    @staticmethod
                    def create(
                        dEnergy: Optional[float] = None,
                        maxSteps: Optional[int] = None,
                        maxResidue: Optional[float] = None,
                        printSteps: Optional[int] = None,
                        mixingMethod: Optional[str] = None,
                        nPulaySteps: Optional[int] = None,
                        rhoMixing: Optional[float] = None,
                        spinMixing: Optional[float] = None,
                        keepRhoFixed: Optional[bool] = None,
                        keepOccFixed: Optional[bool] = None,
                        keepSpinFixed: Optional[bool] = None,
                        spinMoment: Optional[float] = None,
                        ekt: Optional[float] = None,
                        dipoleCorrection: Optional[bool] = None,
                        dSpinMoment: Optional[float] = None,
                        noRhoStorage: Optional[bool] = None,
                        noWavesStorage: Optional[bool] = None,
                        CCG: Optional[dict] = None,
                        blockCCG: Optional[dict] = None,
                        preconditioner: Optional[dict] = None,
                    ):
                        """
                        The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations.

                        Args:
                            dEnergy (float): Free energy convergence criterium. Default: 1e-8. (Optional)
                            maxSteps (int): Max. number of steps (density updates). (Optional)
                            maxResidue (float): Additional requirement for convergence; density residue must fall below this threshold. (Optional)
                            printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                            mixingMethod (str): Method for the density mixing. Constants defined in parameters.sx. Can be PULAY (2) or LINEAR (0). Default: 2. (Optional)
                            nPulaySteps (int): Number of previous steps (densities) to use in Pulay mixing. Default: 7. (Optional)
                            rhoMixing (float): Additional linear mixing factor for density updates (1=full update, 0=no change). Low values may lead to a more stable convergence, but will slow down the calculation if set too low. Default: 1. (Optional)
                            spinMixing (float): Linear mixing parameter for spin densities. (Optional)
                            keepRhoFixed (bool): Do not update the density (for band structures). (Optional)
                            keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                            keepSpinFixed (bool): Do not update the spin density. (Optional)
                            spinMoment (float): Keep the spin moment at this value. (Optional)
                            ekt (float): The electronic temperature. (Optional)
                            dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                            dSpinMoment (float): accuracy of iterative enforcement of spin constraints. Default: 1e-8. (Optional)
                            noRhoStorage (bool): Do not write rho.sxb. (Optional)
                            noWavesStorage (bool): Do not write waves.sxb. (Optional)
                            CCG (dict): The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                            blockCCG (dict): The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states). (Optional)
                            preconditioner (dict): The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result. (Optional)
                        """
                        return fill_values(
                            dEnergy=dEnergy,
                            maxSteps=maxSteps,
                            maxResidue=maxResidue,
                            printSteps=printSteps,
                            mixingMethod=mixingMethod,
                            nPulaySteps=nPulaySteps,
                            rhoMixing=rhoMixing,
                            spinMixing=spinMixing,
                            keepRhoFixed=keepRhoFixed,
                            keepOccFixed=keepOccFixed,
                            keepSpinFixed=keepSpinFixed,
                            spinMoment=spinMoment,
                            ekt=ekt,
                            dipoleCorrection=dipoleCorrection,
                            dSpinMoment=dSpinMoment,
                            noRhoStorage=noRhoStorage,
                            noWavesStorage=noWavesStorage,
                            CCG=CCG,
                            blockCCG=blockCCG,
                            preconditioner=preconditioner,
                        )

                    class CCG:
                        @staticmethod
                        def create(
                            dEnergy: Optional[float] = None,
                            maxSteps: Optional[int] = None,
                            printSteps: Optional[int] = None,
                            initialDiag: Optional[bool] = None,
                            finalDiag: Optional[bool] = None,
                            kappa: Optional[float] = None,
                            keepOccFixed: Optional[bool] = None,
                            ekt: Optional[float] = None,
                            dipoleCorrection: Optional[bool] = None,
                            noRhoStorage: Optional[bool] = None,
                            noWavesStorage: Optional[bool] = None,
                        ):
                            """
                            The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations

                            Args:
                                dEnergy (float): Use these settings until energy change fall below this threshold. Default: 1e-8. (Optional)
                                maxSteps (int): Max. number of steps to perform. (Optional)
                                printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                                initialDiag (bool): Perform iterative wave-function optimization based on the initial density. Default: True. (Optional)
                                finalDiag (bool): Perform iterative wave-function optimization based on the final density. (Optional)
                                kappa (float): Perform subspace diagonalization at the end. (optional) Initial mixing between subspace Hamiltonian and wave-function updates. If set to a negative value, the value of κ will be fixed at the absolute value. Otherwise, κ is adapted on the fly. (Optional)
                                keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                                ekt (float): Override electronic temperature setting in the Hamiltonian group. (Optional)
                                dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                                noRhoStorage (bool): Do not write rho.sxb. (Optional)
                                noWavesStorage (bool): Do not write waves.sxb. (Optional)
                            """
                            return fill_values(
                                dEnergy=dEnergy,
                                maxSteps=maxSteps,
                                printSteps=printSteps,
                                initialDiag=initialDiag,
                                finalDiag=finalDiag,
                                kappa=kappa,
                                keepOccFixed=keepOccFixed,
                                ekt=ekt,
                                dipoleCorrection=dipoleCorrection,
                                noRhoStorage=noRhoStorage,
                                noWavesStorage=noWavesStorage,
                            )

                    class blockCCG:
                        @staticmethod
                        def create(
                            dRelEps: Optional[float] = None,
                            maxStepsCCG: Optional[int] = None,
                            blockSize: Optional[int] = None,
                            nSloppy: Optional[int] = None,
                            dEnergy: Optional[float] = None,
                            verbose: Optional[bool] = None,
                            numericalLimit: Optional[float] = None,
                        ):
                            """
                            The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states).

                            Args:
                                dRelEps (float): Stop iterating when the change in eigenvalue falls below this fraction of the change in the first (steepest-descent) step. (Optional)
                                maxStepsCCG (int): Max. number of steps to perform. Default: 5. (Optional)
                                blockSize (int): Block size. Default: 64. (Optional)
                                nSloppy (int): Number of sloppy steps. (Optional)
                                dEnergy (float): Use these settings until energy change fall below this threshold. (Optional)
                                verbose (bool): Verbose output. (Optional)
                                numericalLimit (float): Stop iterating when approaching the numerical limit. (Optional)
                            """
                            return fill_values(
                                dRelEps=dRelEps,
                                maxStepsCCG=maxStepsCCG,
                                blockSize=blockSize,
                                nSloppy=nSloppy,
                                dEnergy=dEnergy,
                                verbose=verbose,
                                numericalLimit=numericalLimit,
                            )

                    class preconditioner:
                        @staticmethod
                        def create(
                            type: str,
                            scaling: Optional[float] = None,
                            spinScaling: Optional[float] = None,
                            dielecConstant: Optional[float] = None,
                        ):
                            """
                            The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result.

                            Args:
                                type (str): NONE (0). No preconditioning. Ideal for atoms/molecules in vacuum; KERKER (1). Kerker preconditioner. Ideal for metals; CSRB (3). Preconditioner for semiconductors based on the Cappellini-del- Sole-Reining-Bechstedt model dielectric function. Requires dielecConstant; ELLIPTIC (5). An explicit-solver preconditioner. No screening in vacuum region, Thomas-Fermi screening (Kerker-like) elsewhere. Ideal for metallic.
                                scaling (float): Scaling factor for the preconditioner. Default: 1.0. (Optional)
                                spinScaling (float): Scaling factor for the spin part of the preconditioner. Default: 1.0. (Optional)
                                dielecConstant (float): Dielectric constant for the CSRB preconditioner. (Optional)
                            """
                            return fill_values(
                                type=type,
                                scaling=scaling,
                                spinScaling=spinScaling,
                                dielecConstant=dielecConstant,
                            )

        class ricQN:
            @staticmethod
            def create(
                maxSteps: Optional[int] = None,
                dX: Optional[float] = None,
                dF: Optional[float] = None,
                dEnergy: Optional[float] = None,
                maxStepLength: Optional[float] = None,
                nProjectors: Optional[int] = None,
                softModeDamping: Optional[float] = None,
                driftFilter: Optional[bool] = None,
                bornOppenheimer: Optional[dict] = None,
            ):
                """
                Args:
                    maxSteps (int): Max. number of steps to perform. Default: 50. (Optional)
                    dX (float): Stop iterating when the change in geometry falls below this threshold. Default: 0.01. (Optional)
                    dF (float): Stop iterating when the change in forces falls below this threshold. Default: 0.001. (Optional)
                    dEnergy (float): Use these settings until energy change fall below this threshold. Default: 1e-4. (Optional)
                    maxStepLength (float): maximum allowed displacement (length of displacement vector for a single atom). Larger steps are reduced by scaling. Default: 0.3. (Optional)
                    nProjectors (int): Number of projectors. (Optional)
                    softModeDamping (float): Initial value for Hessian shift. This is overriden with the first successful fit of a positive shift parameter. Default: 0.01. (Optional)
                    driftFilter (bool): Project out the average force and displacement. Default: True. (Optional)
                    bornOppenheimer (dict): The bornOppenheimer group defines the electronic loop within a geometry optimization. It contains one or more of the electronic loop groups. If more than one minimizer is used, the complete electronic loop sequence is executed at each ionic step. (Optional)
                """
                return fill_values(
                    maxSteps=maxSteps,
                    dX=dX,
                    dF=dF,
                    dEnergy=dEnergy,
                    maxStepLength=maxStepLength,
                    nProjectors=nProjectors,
                    softModeDamping=softModeDamping,
                    driftFilter=driftFilter,
                    bornOppenheimer=bornOppenheimer,
                )

            class bornOppenheimer:
                @staticmethod
                def create(
                    scfDiag: Optional[dict] = None,
                ):
                    """
                    The bornOppenheimer group defines the electronic loop within a geometry optimization. It contains one or more of the electronic loop groups. If more than one minimizer is used, the complete electronic loop sequence is executed at each ionic step.

                    Args:
                        scfDiag (dict): The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                    """
                    return fill_values(
                        scfDiag=scfDiag,
                    )

                class scfDiag:
                    @staticmethod
                    def create(
                        dEnergy: Optional[float] = None,
                        maxSteps: Optional[int] = None,
                        maxResidue: Optional[float] = None,
                        printSteps: Optional[int] = None,
                        mixingMethod: Optional[str] = None,
                        nPulaySteps: Optional[int] = None,
                        rhoMixing: Optional[float] = None,
                        spinMixing: Optional[float] = None,
                        keepRhoFixed: Optional[bool] = None,
                        keepOccFixed: Optional[bool] = None,
                        keepSpinFixed: Optional[bool] = None,
                        spinMoment: Optional[float] = None,
                        ekt: Optional[float] = None,
                        dipoleCorrection: Optional[bool] = None,
                        dSpinMoment: Optional[float] = None,
                        noRhoStorage: Optional[bool] = None,
                        noWavesStorage: Optional[bool] = None,
                        CCG: Optional[dict] = None,
                        blockCCG: Optional[dict] = None,
                        preconditioner: Optional[dict] = None,
                    ):
                        """
                        The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations.

                        Args:
                            dEnergy (float): Free energy convergence criterium. Default: 1e-8. (Optional)
                            maxSteps (int): Max. number of steps (density updates). (Optional)
                            maxResidue (float): Additional requirement for convergence; density residue must fall below this threshold. (Optional)
                            printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                            mixingMethod (str): Method for the density mixing. Constants defined in parameters.sx. Can be PULAY (2) or LINEAR (0). Default: 2. (Optional)
                            nPulaySteps (int): Number of previous steps (densities) to use in Pulay mixing. Default: 7. (Optional)
                            rhoMixing (float): Additional linear mixing factor for density updates (1=full update, 0=no change). Low values may lead to a more stable convergence, but will slow down the calculation if set too low. Default: 1. (Optional)
                            spinMixing (float): Linear mixing parameter for spin densities. (Optional)
                            keepRhoFixed (bool): Do not update the density (for band structures). (Optional)
                            keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                            keepSpinFixed (bool): Do not update the spin density. (Optional)
                            spinMoment (float): Keep the spin moment at this value. (Optional)
                            ekt (float): The electronic temperature. (Optional)
                            dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                            dSpinMoment (float): accuracy of iterative enforcement of spin constraints. Default: 1e-8. (Optional)
                            noRhoStorage (bool): Do not write rho.sxb. (Optional)
                            noWavesStorage (bool): Do not write waves.sxb. (Optional)
                            CCG (dict): The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                            blockCCG (dict): The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states). (Optional)
                            preconditioner (dict): The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result. (Optional)
                        """
                        return fill_values(
                            dEnergy=dEnergy,
                            maxSteps=maxSteps,
                            maxResidue=maxResidue,
                            printSteps=printSteps,
                            mixingMethod=mixingMethod,
                            nPulaySteps=nPulaySteps,
                            rhoMixing=rhoMixing,
                            spinMixing=spinMixing,
                            keepRhoFixed=keepRhoFixed,
                            keepOccFixed=keepOccFixed,
                            keepSpinFixed=keepSpinFixed,
                            spinMoment=spinMoment,
                            ekt=ekt,
                            dipoleCorrection=dipoleCorrection,
                            dSpinMoment=dSpinMoment,
                            noRhoStorage=noRhoStorage,
                            noWavesStorage=noWavesStorage,
                            CCG=CCG,
                            blockCCG=blockCCG,
                            preconditioner=preconditioner,
                        )

                    class CCG:
                        @staticmethod
                        def create(
                            dEnergy: Optional[float] = None,
                            maxSteps: Optional[int] = None,
                            printSteps: Optional[int] = None,
                            initialDiag: Optional[bool] = None,
                            finalDiag: Optional[bool] = None,
                            kappa: Optional[float] = None,
                            keepOccFixed: Optional[bool] = None,
                            ekt: Optional[float] = None,
                            dipoleCorrection: Optional[bool] = None,
                            noRhoStorage: Optional[bool] = None,
                            noWavesStorage: Optional[bool] = None,
                        ):
                            """
                            The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations

                            Args:
                                dEnergy (float): Use these settings until energy change fall below this threshold. Default: 1e-8. (Optional)
                                maxSteps (int): Max. number of steps to perform. (Optional)
                                printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                                initialDiag (bool): Perform iterative wave-function optimization based on the initial density. Default: True. (Optional)
                                finalDiag (bool): Perform iterative wave-function optimization based on the final density. (Optional)
                                kappa (float): Perform subspace diagonalization at the end. (optional) Initial mixing between subspace Hamiltonian and wave-function updates. If set to a negative value, the value of κ will be fixed at the absolute value. Otherwise, κ is adapted on the fly. (Optional)
                                keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                                ekt (float): Override electronic temperature setting in the Hamiltonian group. (Optional)
                                dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                                noRhoStorage (bool): Do not write rho.sxb. (Optional)
                                noWavesStorage (bool): Do not write waves.sxb. (Optional)
                            """
                            return fill_values(
                                dEnergy=dEnergy,
                                maxSteps=maxSteps,
                                printSteps=printSteps,
                                initialDiag=initialDiag,
                                finalDiag=finalDiag,
                                kappa=kappa,
                                keepOccFixed=keepOccFixed,
                                ekt=ekt,
                                dipoleCorrection=dipoleCorrection,
                                noRhoStorage=noRhoStorage,
                                noWavesStorage=noWavesStorage,
                            )

                    class blockCCG:
                        @staticmethod
                        def create(
                            dRelEps: Optional[float] = None,
                            maxStepsCCG: Optional[int] = None,
                            blockSize: Optional[int] = None,
                            nSloppy: Optional[int] = None,
                            dEnergy: Optional[float] = None,
                            verbose: Optional[bool] = None,
                            numericalLimit: Optional[float] = None,
                        ):
                            """
                            The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states).

                            Args:
                                dRelEps (float): Stop iterating when the change in eigenvalue falls below this fraction of the change in the first (steepest-descent) step. (Optional)
                                maxStepsCCG (int): Max. number of steps to perform. Default: 5. (Optional)
                                blockSize (int): Block size. Default: 64. (Optional)
                                nSloppy (int): Number of sloppy steps. (Optional)
                                dEnergy (float): Use these settings until energy change fall below this threshold. (Optional)
                                verbose (bool): Verbose output. (Optional)
                                numericalLimit (float): Stop iterating when approaching the numerical limit. (Optional)
                            """
                            return fill_values(
                                dRelEps=dRelEps,
                                maxStepsCCG=maxStepsCCG,
                                blockSize=blockSize,
                                nSloppy=nSloppy,
                                dEnergy=dEnergy,
                                verbose=verbose,
                                numericalLimit=numericalLimit,
                            )

                    class preconditioner:
                        @staticmethod
                        def create(
                            type: str,
                            scaling: Optional[float] = None,
                            spinScaling: Optional[float] = None,
                            dielecConstant: Optional[float] = None,
                        ):
                            """
                            The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result.

                            Args:
                                type (str): NONE (0). No preconditioning. Ideal for atoms/molecules in vacuum; KERKER (1). Kerker preconditioner. Ideal for metals; CSRB (3). Preconditioner for semiconductors based on the Cappellini-del- Sole-Reining-Bechstedt model dielectric function. Requires dielecConstant; ELLIPTIC (5). An explicit-solver preconditioner. No screening in vacuum region, Thomas-Fermi screening (Kerker-like) elsewhere. Ideal for metallic.
                                scaling (float): Scaling factor for the preconditioner. Default: 1.0. (Optional)
                                spinScaling (float): Scaling factor for the spin part of the preconditioner. Default: 1.0. (Optional)
                                dielecConstant (float): Dielectric constant for the CSRB preconditioner. (Optional)
                            """
                            return fill_values(
                                type=type,
                                scaling=scaling,
                                spinScaling=spinScaling,
                                dielecConstant=dielecConstant,
                            )

        class ric:
            @staticmethod
            def create(
                maxDist: Optional[float] = None,
                typifyThreshold: Optional[float] = None,
                rmsThreshold: Optional[float] = None,
                planeCutLimit: Optional[float] = None,
                withAngles: Optional[bool] = None,
                bvkAtoms: Optional[str] = None,
                bornOppenheimer: Optional[dict] = None,
            ):
                """
                The ric group defines the parameters for internal coordinate generation.

                Args:
                    maxDist (float): maximum possible distance for considering neighbors. Default: 10. (Optional)
                    typifyThreshold (float): minimum bond length separation of distinct bond types (the f parameter in [10]). After sorting the bond lengthes, the logarithm of subsequent lengthes are compared. If they differ by less than the threshold, the two bonds are assigned the same bond type. Default: 0.05. (Optional)
                    rmsThreshold (float): minimum distance between two bond length clusters in units of their root-mean-square displacements (the R parameter of [10]). Default: 3. (Optional)
                    planeCutLimit (float): Relative size of coordination polyhedra to separate the nearest neighbors from further atoms (the P parameter of [10]). Larger values allow for more neighbors. Default: 0.95. (Optional)
                    withAngles (bool): add bond angle coordinates for all bonds. (Optional)
                    bvkAtoms (str): (experimental) List of atom ids (starting from 1) for which born-von-Karman transversal force constants are added. The comma-separated list must be enclosed by square brackets []. This adds a bond-directional coordinate to each bond of the atoms in the list. (Optional)
                    bornOppenheimer (dict): The bornOppenheimer group defines the electronic loop within a geometry optimization. It contains one or more of the electronic loop groups. If more than one minimizer is used, the complete electronic loop sequence is executed at each ionic step. (Optional)
                """
                return fill_values(
                    maxDist=maxDist,
                    typifyThreshold=typifyThreshold,
                    rmsThreshold=rmsThreshold,
                    planeCutLimit=planeCutLimit,
                    withAngles=withAngles,
                    bvkAtoms=bvkAtoms,
                    bornOppenheimer=bornOppenheimer,
                )

            class bornOppenheimer:
                @staticmethod
                def create(
                    scfDiag: Optional[dict] = None,
                ):
                    """
                    The bornOppenheimer group defines the electronic loop within a geometry optimization. It contains one or more of the electronic loop groups. If more than one minimizer is used, the complete electronic loop sequence is executed at each ionic step.

                    Args:
                        scfDiag (dict): The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                    """
                    return fill_values(
                        scfDiag=scfDiag,
                    )

                class scfDiag:
                    @staticmethod
                    def create(
                        dEnergy: Optional[float] = None,
                        maxSteps: Optional[int] = None,
                        maxResidue: Optional[float] = None,
                        printSteps: Optional[int] = None,
                        mixingMethod: Optional[str] = None,
                        nPulaySteps: Optional[int] = None,
                        rhoMixing: Optional[float] = None,
                        spinMixing: Optional[float] = None,
                        keepRhoFixed: Optional[bool] = None,
                        keepOccFixed: Optional[bool] = None,
                        keepSpinFixed: Optional[bool] = None,
                        spinMoment: Optional[float] = None,
                        ekt: Optional[float] = None,
                        dipoleCorrection: Optional[bool] = None,
                        dSpinMoment: Optional[float] = None,
                        noRhoStorage: Optional[bool] = None,
                        noWavesStorage: Optional[bool] = None,
                        CCG: Optional[dict] = None,
                        blockCCG: Optional[dict] = None,
                        preconditioner: Optional[dict] = None,
                    ):
                        """
                        The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations.

                        Args:
                            dEnergy (float): Free energy convergence criterium. Default: 1e-8. (Optional)
                            maxSteps (int): Max. number of steps (density updates). (Optional)
                            maxResidue (float): Additional requirement for convergence; density residue must fall below this threshold. (Optional)
                            printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                            mixingMethod (str): Method for the density mixing. Constants defined in parameters.sx. Can be PULAY (2) or LINEAR (0). Default: 2. (Optional)
                            nPulaySteps (int): Number of previous steps (densities) to use in Pulay mixing. Default: 7. (Optional)
                            rhoMixing (float): Additional linear mixing factor for density updates (1=full update, 0=no change). Low values may lead to a more stable convergence, but will slow down the calculation if set too low. Default: 1. (Optional)
                            spinMixing (float): Linear mixing parameter for spin densities. (Optional)
                            keepRhoFixed (bool): Do not update the density (for band structures). (Optional)
                            keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                            keepSpinFixed (bool): Do not update the spin density. (Optional)
                            spinMoment (float): Keep the spin moment at this value. (Optional)
                            ekt (float): The electronic temperature. (Optional)
                            dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                            dSpinMoment (float): accuracy of iterative enforcement of spin constraints. Default: 1e-8. (Optional)
                            noRhoStorage (bool): Do not write rho.sxb. (Optional)
                            noWavesStorage (bool): Do not write waves.sxb. (Optional)
                            CCG (dict): The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                            blockCCG (dict): The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states). (Optional)
                            preconditioner (dict): The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result. (Optional)
                        """
                        return fill_values(
                            dEnergy=dEnergy,
                            maxSteps=maxSteps,
                            maxResidue=maxResidue,
                            printSteps=printSteps,
                            mixingMethod=mixingMethod,
                            nPulaySteps=nPulaySteps,
                            rhoMixing=rhoMixing,
                            spinMixing=spinMixing,
                            keepRhoFixed=keepRhoFixed,
                            keepOccFixed=keepOccFixed,
                            keepSpinFixed=keepSpinFixed,
                            spinMoment=spinMoment,
                            ekt=ekt,
                            dipoleCorrection=dipoleCorrection,
                            dSpinMoment=dSpinMoment,
                            noRhoStorage=noRhoStorage,
                            noWavesStorage=noWavesStorage,
                            CCG=CCG,
                            blockCCG=blockCCG,
                            preconditioner=preconditioner,
                        )

                    class CCG:
                        @staticmethod
                        def create(
                            dEnergy: Optional[float] = None,
                            maxSteps: Optional[int] = None,
                            printSteps: Optional[int] = None,
                            initialDiag: Optional[bool] = None,
                            finalDiag: Optional[bool] = None,
                            kappa: Optional[float] = None,
                            keepOccFixed: Optional[bool] = None,
                            ekt: Optional[float] = None,
                            dipoleCorrection: Optional[bool] = None,
                            noRhoStorage: Optional[bool] = None,
                            noWavesStorage: Optional[bool] = None,
                        ):
                            """
                            The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations

                            Args:
                                dEnergy (float): Use these settings until energy change fall below this threshold. Default: 1e-8. (Optional)
                                maxSteps (int): Max. number of steps to perform. (Optional)
                                printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                                initialDiag (bool): Perform iterative wave-function optimization based on the initial density. Default: True. (Optional)
                                finalDiag (bool): Perform iterative wave-function optimization based on the final density. (Optional)
                                kappa (float): Perform subspace diagonalization at the end. (optional) Initial mixing between subspace Hamiltonian and wave-function updates. If set to a negative value, the value of κ will be fixed at the absolute value. Otherwise, κ is adapted on the fly. (Optional)
                                keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                                ekt (float): Override electronic temperature setting in the Hamiltonian group. (Optional)
                                dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                                noRhoStorage (bool): Do not write rho.sxb. (Optional)
                                noWavesStorage (bool): Do not write waves.sxb. (Optional)
                            """
                            return fill_values(
                                dEnergy=dEnergy,
                                maxSteps=maxSteps,
                                printSteps=printSteps,
                                initialDiag=initialDiag,
                                finalDiag=finalDiag,
                                kappa=kappa,
                                keepOccFixed=keepOccFixed,
                                ekt=ekt,
                                dipoleCorrection=dipoleCorrection,
                                noRhoStorage=noRhoStorage,
                                noWavesStorage=noWavesStorage,
                            )

                    class blockCCG:
                        @staticmethod
                        def create(
                            dRelEps: Optional[float] = None,
                            maxStepsCCG: Optional[int] = None,
                            blockSize: Optional[int] = None,
                            nSloppy: Optional[int] = None,
                            dEnergy: Optional[float] = None,
                            verbose: Optional[bool] = None,
                            numericalLimit: Optional[float] = None,
                        ):
                            """
                            The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states).

                            Args:
                                dRelEps (float): Stop iterating when the change in eigenvalue falls below this fraction of the change in the first (steepest-descent) step. (Optional)
                                maxStepsCCG (int): Max. number of steps to perform. Default: 5. (Optional)
                                blockSize (int): Block size. Default: 64. (Optional)
                                nSloppy (int): Number of sloppy steps. (Optional)
                                dEnergy (float): Use these settings until energy change fall below this threshold. (Optional)
                                verbose (bool): Verbose output. (Optional)
                                numericalLimit (float): Stop iterating when approaching the numerical limit. (Optional)
                            """
                            return fill_values(
                                dRelEps=dRelEps,
                                maxStepsCCG=maxStepsCCG,
                                blockSize=blockSize,
                                nSloppy=nSloppy,
                                dEnergy=dEnergy,
                                verbose=verbose,
                                numericalLimit=numericalLimit,
                            )

                    class preconditioner:
                        @staticmethod
                        def create(
                            type: str,
                            scaling: Optional[float] = None,
                            spinScaling: Optional[float] = None,
                            dielecConstant: Optional[float] = None,
                        ):
                            """
                            The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result.

                            Args:
                                type (str): NONE (0). No preconditioning. Ideal for atoms/molecules in vacuum; KERKER (1). Kerker preconditioner. Ideal for metals; CSRB (3). Preconditioner for semiconductors based on the Cappellini-del- Sole-Reining-Bechstedt model dielectric function. Requires dielecConstant; ELLIPTIC (5). An explicit-solver preconditioner. No screening in vacuum region, Thomas-Fermi screening (Kerker-like) elsewhere. Ideal for metallic.
                                scaling (float): Scaling factor for the preconditioner. Default: 1.0. (Optional)
                                spinScaling (float): Scaling factor for the spin part of the preconditioner. Default: 1.0. (Optional)
                                dielecConstant (float): Dielectric constant for the CSRB preconditioner. (Optional)
                            """
                            return fill_values(
                                type=type,
                                scaling=scaling,
                                spinScaling=spinScaling,
                                dielecConstant=dielecConstant,
                            )

        class ricTS:
            @staticmethod
            def create(
                maxSteps: Optional[int] = None,
                dX: Optional[float] = None,
                dF: Optional[float] = None,
                dEnergy: Optional[float] = None,
                nProjectors: Optional[int] = None,
                maxStepLength: Optional[float] = None,
                transCurvature: Optional[float] = None,
                anyStationaryPoint: Optional[bool] = None,
                maxDirRot: Optional[float] = None,
                scheme: Optional[int] = None,
                driftFilter: Optional[bool] = None,
                bornOppenheimer: Optional[dict] = None,
            ):
                """
                The ricTS group requests a quasi-Newton optimization for 1st-order saddle points (transition states) using updates [11] of an on-the-fly optimized internal-coordinate based initial guess for the Hessian [10]. An initial guess for the reaction coordinate must be known. Note: This is an experimental feature. The optimization should be started within the saddle point region (one negative eigenvalue of the Hesse matrix), otherwise, the algorithm may converge to a different stationary point (a minimum, or a higher-order saddle point).

                Args:
                    maxSteps (int): Maximum number of steps. (Optional)
                    dX (float): Position convergence criterion. (Optional)
                    dF (float): Force convergence criterion. (Optional)
                    dEnergy (float): Energy convergence criterion. (Optional)
                    nProjectors (int): Number of projectors. (Optional)
                    maxStepLength (float): Maximum step length. (Optional)
                    transCurvature (float): Transversal curvature. (Optional)
                    anyStationaryPoint (bool): Any stationary point. (Optional)
                    maxDirRot (float): Control updates of transition direction. Parameter between 0 (no updates) and 1 (full updates). Default: 0.5. (Optional)
                    scheme (int): Hesse update scheme (0=Murtagh-Sargent, 1=Powell symmetric Broyden, 2=Borrell, 3=Farkas-Schlegel, see [11], Eqs. 6-10). Default: 1. (Optional)
                    driftFilter (bool): Drift filter. (Optional)
                    bornOppenheimer (dict): The bornOppenheimer group defines the electronic loop within a geometry optimization. It contains one or more of the electronic loop groups. If more than one minimizer is used, the complete electronic loop sequence is executed at each ionic step. (Optional)
                """
                return fill_values(
                    maxSteps=maxSteps,
                    dX=dX,
                    dF=dF,
                    dEnergy=dEnergy,
                    nProjectors=nProjectors,
                    maxStepLength=maxStepLength,
                    transCurvature=transCurvature,
                    anyStationaryPoint=anyStationaryPoint,
                    maxDirRot=maxDirRot,
                    scheme=scheme,
                    driftFilter=driftFilter,
                    bornOppenheimer=bornOppenheimer,
                )

            class bornOppenheimer:
                @staticmethod
                def create(
                    scfDiag: Optional[dict] = None,
                ):
                    """
                    The bornOppenheimer group defines the electronic loop within a geometry optimization. It contains one or more of the electronic loop groups. If more than one minimizer is used, the complete electronic loop sequence is executed at each ionic step.

                    Args:
                        scfDiag (dict): The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                    """
                    return fill_values(
                        scfDiag=scfDiag,
                    )

                class scfDiag:
                    @staticmethod
                    def create(
                        dEnergy: Optional[float] = None,
                        maxSteps: Optional[int] = None,
                        maxResidue: Optional[float] = None,
                        printSteps: Optional[int] = None,
                        mixingMethod: Optional[str] = None,
                        nPulaySteps: Optional[int] = None,
                        rhoMixing: Optional[float] = None,
                        spinMixing: Optional[float] = None,
                        keepRhoFixed: Optional[bool] = None,
                        keepOccFixed: Optional[bool] = None,
                        keepSpinFixed: Optional[bool] = None,
                        spinMoment: Optional[float] = None,
                        ekt: Optional[float] = None,
                        dipoleCorrection: Optional[bool] = None,
                        dSpinMoment: Optional[float] = None,
                        noRhoStorage: Optional[bool] = None,
                        noWavesStorage: Optional[bool] = None,
                        CCG: Optional[dict] = None,
                        blockCCG: Optional[dict] = None,
                        preconditioner: Optional[dict] = None,
                    ):
                        """
                        The scfDiag group selects and controls the iterative diagonalization + density mixing algorithm for the solution of the Kohn-Sham DFT equations.

                        Args:
                            dEnergy (float): Free energy convergence criterium. Default: 1e-8. (Optional)
                            maxSteps (int): Max. number of steps (density updates). (Optional)
                            maxResidue (float): Additional requirement for convergence; density residue must fall below this threshold. (Optional)
                            printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                            mixingMethod (str): Method for the density mixing. Constants defined in parameters.sx. Can be PULAY (2) or LINEAR (0). Default: 2. (Optional)
                            nPulaySteps (int): Number of previous steps (densities) to use in Pulay mixing. Default: 7. (Optional)
                            rhoMixing (float): Additional linear mixing factor for density updates (1=full update, 0=no change). Low values may lead to a more stable convergence, but will slow down the calculation if set too low. Default: 1. (Optional)
                            spinMixing (float): Linear mixing parameter for spin densities. (Optional)
                            keepRhoFixed (bool): Do not update the density (for band structures). (Optional)
                            keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                            keepSpinFixed (bool): Do not update the spin density. (Optional)
                            spinMoment (float): Keep the spin moment at this value. (Optional)
                            ekt (float): The electronic temperature. (Optional)
                            dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                            dSpinMoment (float): accuracy of iterative enforcement of spin constraints. Default: 1e-8. (Optional)
                            noRhoStorage (bool): Do not write rho.sxb. (Optional)
                            noWavesStorage (bool): Do not write waves.sxb. (Optional)
                            CCG (dict): The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations. (Optional)
                            blockCCG (dict): The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states). (Optional)
                            preconditioner (dict): The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result. (Optional)
                        """
                        return fill_values(
                            dEnergy=dEnergy,
                            maxSteps=maxSteps,
                            maxResidue=maxResidue,
                            printSteps=printSteps,
                            mixingMethod=mixingMethod,
                            nPulaySteps=nPulaySteps,
                            rhoMixing=rhoMixing,
                            spinMixing=spinMixing,
                            keepRhoFixed=keepRhoFixed,
                            keepOccFixed=keepOccFixed,
                            keepSpinFixed=keepSpinFixed,
                            spinMoment=spinMoment,
                            ekt=ekt,
                            dipoleCorrection=dipoleCorrection,
                            dSpinMoment=dSpinMoment,
                            noRhoStorage=noRhoStorage,
                            noWavesStorage=noWavesStorage,
                            CCG=CCG,
                            blockCCG=blockCCG,
                            preconditioner=preconditioner,
                        )

                    class CCG:
                        @staticmethod
                        def create(
                            dEnergy: Optional[float] = None,
                            maxSteps: Optional[int] = None,
                            printSteps: Optional[int] = None,
                            initialDiag: Optional[bool] = None,
                            finalDiag: Optional[bool] = None,
                            kappa: Optional[float] = None,
                            keepOccFixed: Optional[bool] = None,
                            ekt: Optional[float] = None,
                            dipoleCorrection: Optional[bool] = None,
                            noRhoStorage: Optional[bool] = None,
                            noWavesStorage: Optional[bool] = None,
                        ):
                            """
                            The CCG group selects and controls the direct minimization algorithm for the solution of the Kohn-Sham DFT equations

                            Args:
                                dEnergy (float): Use these settings until energy change fall below this threshold. Default: 1e-8. (Optional)
                                maxSteps (int): Max. number of steps to perform. (Optional)
                                printSteps (int): Print convergence status every n steps. Default: 10. (Optional)
                                initialDiag (bool): Perform iterative wave-function optimization based on the initial density. Default: True. (Optional)
                                finalDiag (bool): Perform iterative wave-function optimization based on the final density. (Optional)
                                kappa (float): Perform subspace diagonalization at the end. (optional) Initial mixing between subspace Hamiltonian and wave-function updates. If set to a negative value, the value of κ will be fixed at the absolute value. Otherwise, κ is adapted on the fly. (Optional)
                                keepOccFixed (bool): Do not update the occupation numbers. (Optional)
                                ekt (float): Override electronic temperature setting in the Hamiltonian group. (Optional)
                                dipoleCorrection (bool): Override the dipole correction setting in the Hamiltonian group. (Optional)
                                noRhoStorage (bool): Do not write rho.sxb. (Optional)
                                noWavesStorage (bool): Do not write waves.sxb. (Optional)
                            """
                            return fill_values(
                                dEnergy=dEnergy,
                                maxSteps=maxSteps,
                                printSteps=printSteps,
                                initialDiag=initialDiag,
                                finalDiag=finalDiag,
                                kappa=kappa,
                                keepOccFixed=keepOccFixed,
                                ekt=ekt,
                                dipoleCorrection=dipoleCorrection,
                                noRhoStorage=noRhoStorage,
                                noWavesStorage=noWavesStorage,
                            )

                    class blockCCG:
                        @staticmethod
                        def create(
                            dRelEps: Optional[float] = None,
                            maxStepsCCG: Optional[int] = None,
                            blockSize: Optional[int] = None,
                            nSloppy: Optional[int] = None,
                            dEnergy: Optional[float] = None,
                            verbose: Optional[bool] = None,
                            numericalLimit: Optional[float] = None,
                        ):
                            """
                            The blockCCG group (within the scfDiag group) selects the block-conjugate-gradient algorithm for (inner-loop) iterative diagonalization. After all states have been updated, a subspace diagonalization is performed. This algorithm works best for larger systems (> 5 states).

                            Args:
                                dRelEps (float): Stop iterating when the change in eigenvalue falls below this fraction of the change in the first (steepest-descent) step. (Optional)
                                maxStepsCCG (int): Max. number of steps to perform. Default: 5. (Optional)
                                blockSize (int): Block size. Default: 64. (Optional)
                                nSloppy (int): Number of sloppy steps. (Optional)
                                dEnergy (float): Use these settings until energy change fall below this threshold. (Optional)
                                verbose (bool): Verbose output. (Optional)
                                numericalLimit (float): Stop iterating when approaching the numerical limit. (Optional)
                            """
                            return fill_values(
                                dRelEps=dRelEps,
                                maxStepsCCG=maxStepsCCG,
                                blockSize=blockSize,
                                nSloppy=nSloppy,
                                dEnergy=dEnergy,
                                verbose=verbose,
                                numericalLimit=numericalLimit,
                            )

                    class preconditioner:
                        @staticmethod
                        def create(
                            type: str,
                            scaling: Optional[float] = None,
                            spinScaling: Optional[float] = None,
                            dielecConstant: Optional[float] = None,
                        ):
                            """
                            The preconditioner group defines the density preconditioner, i.e., a transformation of the observed (or predicted) difference between the input and output density to the applied changes to the input density. An ideal preconditioner models the screening behavior of the system and is able to include the expected screening response into the suggested density change. Selecting an appropriate preconditioner, that rejects the screening properties of the system at hand, is a key to an efficient (i.e. fast) convergence. The preconditioner does not affect the converged result.

                            Args:
                                type (str): NONE (0). No preconditioning. Ideal for atoms/molecules in vacuum; KERKER (1). Kerker preconditioner. Ideal for metals; CSRB (3). Preconditioner for semiconductors based on the Cappellini-del- Sole-Reining-Bechstedt model dielectric function. Requires dielecConstant; ELLIPTIC (5). An explicit-solver preconditioner. No screening in vacuum region, Thomas-Fermi screening (Kerker-like) elsewhere. Ideal for metallic.
                                scaling (float): Scaling factor for the preconditioner. Default: 1.0. (Optional)
                                spinScaling (float): Scaling factor for the spin part of the preconditioner. Default: 1.0. (Optional)
                                dielecConstant (float): Dielectric constant for the CSRB preconditioner. (Optional)
                            """
                            return fill_values(
                                type=type,
                                scaling=scaling,
                                spinScaling=spinScaling,
                                dielecConstant=dielecConstant,
                            )
