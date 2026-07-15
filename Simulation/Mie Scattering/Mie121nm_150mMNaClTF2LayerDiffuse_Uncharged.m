
clear, clc, close all

% ========================================================================
% FILE DESCRIPTION
% ========================================================================
%{ 
Solutions to the Mie model based on a 121 nm diameter gold sphere
immersed in a 150 mM NaCl solutions using the following layers:
- bulk gold
- thomas-fermi screening layer
- 2-part diffuse layer
- bulk electrolyte
The concentration gradient of the diffuse layer gives a change in
refractive index determined by the ions molar refractivity. Different
charges create different gradients and therefore different refractive
indices. The Thomas-Fermi screening layer describes a sub-nanometer outer
layer that encapsulates the sphere and acts to mitigate the effects of an
external electric field on the bulk material.
%}
% =========================================================================
load('121nm_150mMNaClTF2LayerDiffuse_Uncharged.mat')
% =========================================================================
% PARAMETER DEFINITIONS
% =========================================================================
%{
c           - Concentration of the electrolyte [mMol/L]
diameter    - Sphere diameter [m]
dndcCl      - Molar refractive index of Chloride ions [1/mol]
dndcNa      - Molar refractive index of Sodium ions [1/mol]
qabs        - Absorption cross-section wrt w [m^2]
qext        - Extinction cross-section wrt w [m^2]
qscat       - Scattering cross-section wrt w[m^2]
res_mag     - Scattering amplitude at the resonance peak [m^2]
res_pos     - Resonance wavelength [nm]
t           - Thickness of each layer in the model from inside to outside [m]
w           - Wavelength vector used in the Mie simulations [m]
%}
% =========================================================================
% Define the scattering gradient
yfine = qscat;
dx = w(2)-w(1);
dy = zeros(size(yfine));
dy(2:end-1) = (yfine(3:end) - yfine(1:end-2)) / (2*dx); % central difference
dy(1) = (yfine(2) - yfine(1)) / dx;                     % forward for first point
dy(end) = (yfine(end) - yfine(end-1)) / dx;             % backward for last point
% =========================================================================
%% PLOT GENERATION
% =========================================================================
% Plot scattering cross-section and its gradient
fig = figure(1);
axes1 = axes('Parent',fig);
hold(axes1,'on');
grid on

fsaxis = 10;
fstitle = 12;
lw = 2;

yyaxis left
plot(w*1e9, yfine, 'LineWidth', lw)
ylabel('$\sigma_{Scat}$ [m$^2$]','FontSize',fsaxis,'Interpreter','latex')
yyaxis right
plot(w*1e9, abs(dy), 'LineWidth', lw)
ylabel('$\frac{d\sigma_{Scat}}{d\lambda}$ [m]','FontSize',fsaxis,'Interpreter','latex')
xlabel('Wavelength [nm]','FontSize',fsaxis,'Interpreter','latex')
xline(660,'-.','LineWidth',lw)
text(670,max(abs(dy)),'$\lambda_{660nm}$','VerticalAlignment', 'top', 'HorizontalAlignment','left', 'FontSize',12,'Interpreter','latex', 'Color', 'red');
xlim([400,800])
