The optical properties of metallic nanostructures are complex and are driven by a variety of material and morphological properties. In some instances optical properties can be determined analytically for an exact solution, while in others they require numerical solutions based on iterative error minimisation. Mie theory is employed to determine the absorption and scattering of spherical particles, while finite element models (COMSOL Multiphysics) have been used for complex morphologies / scenarios

## Mie Scattering


Pending

### Refractive Index

The behaviour of light as it interacts with different materials is determined by the permittivity of those material, intrinsically linked to refractive index by it square root. Accurately defining the refractive index of these materials is imperative to correctly describing the absorption and scattering of light by plasmonic nanostructures. The bulk refractive index of several important materials can be obtained from the *find_nk.m* function, specifying `double(wavelength)` [m] and material, `string(material)`.
