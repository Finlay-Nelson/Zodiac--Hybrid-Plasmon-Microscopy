The optical properties of metallic nanostructures are complex and are driven by a variety of material and morphological properties. In some instances optical properties can be determined analytically for an exact solution, while in others they require numerical solutions based on iterative error minimisation. Mie theory is employed to determine the absorption and scattering of spherical particles, while finite element models (COMSOL Multiphysics) have been used for complex morphologies / scenarios

# Mie Scattering


Pending

## Refractive Index

The behaviour of light as it interacts with different materials is determined by the permittivity of those material, intrinsically linked to refractive index by it square root. Accurately defining the refractive index of these materials is imperative to correctly describing the absorption and scattering of light by plasmonic nanostructures. The bulk refractive index of several important materials can be obtained from the *find_nk.m* function, specifying `double(wavelength)` [m] and material, `string(material)`.

### Thomas-Fermi Screening Length

The free electrons at the surface of a charged metallic surface constitute a sub-Angstrom domain whose refractive index is distinctly different from that of the bulk material based on Drude interpretation of the free-electron model.
The index within the domain constrained by the Thomas-Fermi screening length depends on both the wavelength of light and surface charge density. The simulations considered here are primarily concerned with the electrc double layer formed between Au and a dilute electrolyte; more specifically a 150mM NaCl solution
Data in the *index_Au_ThomasFermi.mat* supplies the refractive index of wavelengths 400:1:800nm having applied potentials of -300:1:300mV. The corresponding surface charge densities are also noted, assuming immersion of Au in a 150mM solution of NaCl (see discussions of the electric double layer)

<img width="345" height="315" alt="index_nAu_ThomasFermi" src="https://github.com/user-attachments/assets/2f023fe1-a327-4ad1-b4a1-da55be976f72" />

<img width="345" height="315" alt="index_kAu_ThomasFermi" src="https://github.com/user-attachments/assets/12a8d0c0-8a43-40c3-8f0a-f959217a2cd2" />
