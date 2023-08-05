img = imread("Your File Path"); %open Image
grayImg = rgb2gray(img); %turn the RGB image to Gray Scale Image
% img2 = rgb2gray(img);
origGray = grayImg;

imshow(img); %Show Image

grayImg = im2double(grayImg);%Turn the unit8 Gray Image data to floating data Gray Image
% NgrayImg = imnoise (grayImg, 'salt & pepper');
NgrayImg = imnoise (grayImg, 'gaussian'); %Add Gaussian Nosie to the Image 
imshow(NgrayImg); %Show Image

%imshow(NgI);
sigma = 1;
kernel = zeros(3,3);
w = 0;
for i = 1:3
    for j = 1:3
        sq_dis = (i-2)^2 + (j-2)^2;
        kernel(i,j) = exp((-1*sq_dis)/ 2*(sigma^2));
        w = w + kernel(i,j);
    end
end
kernel = kernel/w;
[m,n] = size(NgrayImg);
NgI = padarray(NgrayImg, [1 1], 0, 'both'); %imaging pading with 0
for i=1:m
    for j=1:n
        temp = NgI(i:i+2, j:j+2);
        convolution = temp.*kernel;
        output(i,j)=sum(convolution(:));
    end
end
subplot(2,2,1)
imshow(NgI);
title("Noisy Image");
subplot(2,2,2)
imshow(output);
title("Noise Reduced Image");
subplot(2,2,3)
imshow(img);
title("RGB Image");
subplot(2,2,4)
imshow(origGray);
title("orignal Image");