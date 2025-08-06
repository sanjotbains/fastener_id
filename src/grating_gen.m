% grating_gen.m
% Generates an MxN image of a black and white grating with frequency f and angle theta

M = 256;      % Image height
N = 256;      % Image width
f = 40;       % Grating frequency (cycles per image, f > M,N)
theta = 0; % Grating angle in radians

% Create coordinate grid centered at image center
[x, y] = meshgrid(1:N, 1:M);
x = x - N/2;
y = y - M/2;

% Compute grating pattern
grating = sin(2 * pi * f * (x * cos(theta) + y * sin(theta)) / max(M, N));

% Threshold to get black and white pixels
bw_grating = grating > 0;

% Display the image
imshow(bw_grating, []);
title('Black and White Grating');
% Save the image
imwrite(bw_grating, 'bw_grating.png');