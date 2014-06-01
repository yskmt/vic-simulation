U = ['0',
 '0',
 'Z0 - (Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)',
 '(X0*Y0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100']

V = ['0',
 '0',
 '(X0*Y0*Z0*exp(t/20))/20 - (X0*Y0*Z0*exp(t/20))/(20*(X0*Y0*(exp(t/20) - 1) + 1)) + (X0*Y0*exp(t/20)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(20*(X0*Y0*(exp(t/20) - 1) + 1)^2)']

source = '(X0*Y0*exp(t/20))/20 - k*((Y0*sin((pi*t)/10)*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100 - (X0*Y0*sin((pi*t)/10)*(Y0 - Y0*exp(t/20)))/100)*(Y0*Z0 - Y0*Z0*exp(t/20)) - k*((X0*sin((pi*t)/10)*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100 - (X0*Y0*sin((pi*t)/10)*(X0 - X0*exp(t/20)))/100)*(X0*Z0 - X0*Z0*exp(t/20)) - (X0*Y0*exp(t/20))/(20*(X0*Y0*(exp(t/20) - 1) + 1)) + (X0*k*sin((pi*t)/10)*(X0*Z0 - X0*Z0*exp(t/20))*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100 + (Y0*k*sin((pi*t)/10)*(Y0*Z0 - Y0*Z0*exp(t/20))*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100 - (X0*Y0*sin((pi*t)/10)*((2*k*(X0 - X0*exp(t/20))*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) + (2*k*(Y0 - Y0*exp(t/20))*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100 + (X0*Y0*exp(t/20)*(X0*Y0*exp(t/20) - X0*Y0 + 1))/(20*(X0*Y0*(exp(t/20) - 1) + 1)^2) + (X0*Y0*k*sin((pi*t)/10)*(X0 - X0*exp(t/20))*(X0*Z0 - X0*Z0*exp(t/20)))/100 + (X0*Y0*k*sin((pi*t)/10)*(Y0 - Y0*exp(t/20))*(Y0*Z0 - Y0*Z0*exp(t/20)))/100'

bf = ['(lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Y0 - Y0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (mu*(Y0 - Y0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*(Y0 - Y0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (Y0*sin((pi*t)/10)*(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100', '(lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0 - X0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (mu*(X0 - X0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*(X0 - X0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (X0*sin((pi*t)/10)*(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100', '((lm*(Y0 - Y0*exp(t/20))*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1)^2 + (mu*(Y0 - Y0*exp(t/20))*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1)^2 - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Y0 - Y0*exp(t/20))*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1)^2)*(X0*Y0 + (X0*Y0*exp(t/20) - X0*Y0 + 1)/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Y0*exp(t/20) - 2) - 2*((mu*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*((X0 - X0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - X0 + X0*exp(t/20) + (X0*(exp(t/20) - 1)*(X0*Y0*exp(t/20) - X0*Y0 + 1))/(X0*Y0*(exp(t/20) - 1) + 1)^2) - 2*((mu*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*((Y0 - Y0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - Y0 + Y0*exp(t/20) + (Y0*(exp(t/20) - 1)*(X0*Y0*exp(t/20) - X0*Y0 + 1))/(X0*Y0*(exp(t/20) - 1) + 1)^2) + ((mu*(2*X0^2*Z0 + 2*Y0^2*Z0 + 2*X0^2*Z0*exp(t/10) - 4*X0^2*Z0*exp(t/20) + 2*Y0^2*Z0*exp(t/10) - 4*Y0^2*Z0*exp(t/20)))/(X0^2*Y0^2 - 2*X0*Y0 + X0^2*Y0^2*exp(t/10) - 2*X0^2*Y0^2*exp(t/20) + 2*X0*Y0*exp(t/20) + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(2*X0^2*Z0 + 2*Y0^2*Z0 + 2*X0^2*Z0*exp(t/10) - 4*X0^2*Z0*exp(t/20) + 2*Y0^2*Z0*exp(t/10) - 4*Y0^2*Z0*exp(t/20)))/(X0^2*Y0^2 - 2*X0*Y0 + X0^2*Y0^2*exp(t/10) - 2*X0^2*Y0^2*exp(t/20) + 2*X0*Y0*exp(t/20) + 1))*(X0*Y0 + (X0*Y0*exp(t/20) - X0*Y0 + 1)/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Y0*exp(t/20) - 2) - ((mu*(X0 - X0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0 - X0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*((X0*Z0 - X0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Z0 + X0*Z0*exp(t/20) + (X0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2) - ((mu*(Y0 - Y0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Y0 - Y0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*((Y0*Z0 - Y0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - Y0*Z0 + Y0*Z0*exp(t/20) + (Y0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2) + ((lm*(X0 - X0*exp(t/20))*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1)^2 + (mu*(X0 - X0*exp(t/20))*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1)^2 - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0 - X0*exp(t/20))*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1)^2)*(X0*Y0 + (X0*Y0*exp(t/20) - X0*Y0 + 1)/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Y0*exp(t/20) - 2) - lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*((2*X0^2*(exp(t/20) - 1)^2*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^3 + (2*X0*(exp(t/20) - 1)*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2) - lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*((2*Y0^2*(exp(t/20) - 1)^2*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^3 + (2*Y0*(exp(t/20) - 1)*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2) - (lm*(X0 - X0*exp(t/20))*((X0*Z0 - X0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Z0 + X0*Z0*exp(t/20) + (X0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*(Y0 - Y0*exp(t/20))*((Y0*Z0 - Y0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - Y0*Z0 + Y0*Z0*exp(t/20) + (Y0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (X0*Y0*sin((pi*t)/10)*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100']

u_initial = ['0', '0', '0']

p_initial = '0'

v_initial = ['0', '0', '(X0*Y0*Z0)/20']

gbars = \
['- k*(X0*Z0 - X0*Z0*exp(t/20))*((X0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100 - (X0*Y0*sin((pi*t)/10)*(X0*Z0 - X0*Z0*exp(t/20)))/100) - k*(Y0*Z0 - Y0*Z0*exp(t/20))*((Y0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100 - (X0*Y0*sin((pi*t)/10)*(Y0*Z0 - Y0*Z0*exp(t/20)))/100) - (X0*Y0*sin((pi*t)/10)*(k/(X0*Y0*exp(t/20) - X0*Y0 + 1) + (k*(X0*Z0 - X0*Z0*exp(t/20))^2)/(X0*Y0*exp(t/20) - X0*Y0 + 1) + (k*(Y0*Z0 - Y0*Z0*exp(t/20))^2)/(X0*Y0*exp(t/20) - X0*Y0 + 1))*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100',
'k*(X0*Z0 - X0*Z0*exp(t/20))*((X0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100 - (X0*Y0*sin((pi*t)/10)*(X0*Z0 - X0*Z0*exp(t/20)))/100) + k*(Y0*Z0 - Y0*Z0*exp(t/20))*((Y0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100 - (X0*Y0*sin((pi*t)/10)*(Y0*Z0 - Y0*Z0*exp(t/20)))/100) + (X0*Y0*sin((pi*t)/10)*(k/(X0*Y0*exp(t/20) - X0*Y0 + 1) + (k*(X0*Z0 - X0*Z0*exp(t/20))^2)/(X0*Y0*exp(t/20) - X0*Y0 + 1) + (k*(Y0*Z0 - Y0*Z0*exp(t/20))^2)/(X0*Y0*exp(t/20) - X0*Y0 + 1))*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100',
'- k*((Y0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100 - (X0*Y0*sin((pi*t)/10)*(Y0*Z0 - Y0*Z0*exp(t/20)))/100)*(X0*Y0*exp(t/20) - X0*Y0 + 1) - (X0*Y0*k*sin((pi*t)/10)*(Y0*Z0 - Y0*Z0*exp(t/20))*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100',
'k*((Y0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100 - (X0*Y0*sin((pi*t)/10)*(Y0*Z0 - Y0*Z0*exp(t/20)))/100)*(X0*Y0*exp(t/20) - X0*Y0 + 1) + (X0*Y0*k*sin((pi*t)/10)*(Y0*Z0 - Y0*Z0*exp(t/20))*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100',
'- k*((X0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100 - (X0*Y0*sin((pi*t)/10)*(X0*Z0 - X0*Z0*exp(t/20)))/100)*(X0*Y0*exp(t/20) - X0*Y0 + 1) - (X0*Y0*k*sin((pi*t)/10)*(X0*Z0 - X0*Z0*exp(t/20))*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100',
'k*((X0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100 - (X0*Y0*sin((pi*t)/10)*(X0*Z0 - X0*Z0*exp(t/20)))/100)*(X0*Y0*exp(t/20) - X0*Y0 + 1) + (X0*Y0*k*sin((pi*t)/10)*(X0*Z0 - X0*Z0*exp(t/20))*(X0*Y0*exp(t/20) - X0*Y0 + 1))/100']

tbars = \
[['(lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (mu*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (X0*Y0*sin((pi*t)/10)*(Y0*Z0 - Y0*Z0*exp(t/20))*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100',
'(lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (mu*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (X0*Y0*sin((pi*t)/10)*(X0*Z0 - X0*Z0*exp(t/20))*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100',
'(mu*((X0^2*Z0^2 + Y0^2*Z0^2 + X0^2*Z0^2*exp(t/10) - 2*X0^2*Z0^2*exp(t/20) + Y0^2*Z0^2*exp(t/10) - 2*Y0^2*Z0^2*exp(t/20) + 1)/(X0^2*Y0^2 - 2*X0*Y0 + X0^2*Y0^2*exp(t/10) - 2*X0^2*Y0^2*exp(t/20) + 2*X0*Y0*exp(t/20) + 1) - 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0^2*Z0^2 + Y0^2*Z0^2 + X0^2*Z0^2*exp(t/10) - 2*X0^2*Z0^2*exp(t/20) + Y0^2*Z0^2*exp(t/10) - 2*Y0^2*Z0^2*exp(t/20) + 1))/(X0^2*Y0^2 - 2*X0*Y0 + X0^2*Y0^2*exp(t/10) - 2*X0^2*Y0^2*exp(t/20) + 2*X0*Y0*exp(t/20) + 1))*(X0*Y0 + (X0*Y0*exp(t/20) - X0*Y0 + 1)/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Y0*exp(t/20) - 2) - ((mu*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*((X0*Z0 - X0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Z0 + X0*Z0*exp(t/20) + (X0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2) - ((mu*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*((Y0*Z0 - Y0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - Y0*Z0 + Y0*Z0*exp(t/20) + (Y0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2) - (X0*Y0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100'], 
['(mu*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) + (X0*Y0*sin((pi*t)/10)*(Y0*Z0 - Y0*Z0*exp(t/20))*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100',
'(mu*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) + (X0*Y0*sin((pi*t)/10)*(X0*Z0 - X0*Z0*exp(t/20))*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100',
'((mu*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*((X0*Z0 - X0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Z0 + X0*Z0*exp(t/20) + (X0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2) - (mu*((X0^2*Z0^2 + Y0^2*Z0^2 + X0^2*Z0^2*exp(t/10) - 2*X0^2*Z0^2*exp(t/20) + Y0^2*Z0^2*exp(t/10) - 2*Y0^2*Z0^2*exp(t/20) + 1)/(X0^2*Y0^2 - 2*X0*Y0 + X0^2*Y0^2*exp(t/10) - 2*X0^2*Y0^2*exp(t/20) + 2*X0*Y0*exp(t/20) + 1) - 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0^2*Z0^2 + Y0^2*Z0^2 + X0^2*Z0^2*exp(t/10) - 2*X0^2*Z0^2*exp(t/20) + Y0^2*Z0^2*exp(t/10) - 2*Y0^2*Z0^2*exp(t/20) + 1))/(X0^2*Y0^2 - 2*X0*Y0 + X0^2*Y0^2*exp(t/10) - 2*X0^2*Y0^2*exp(t/20) + 2*X0*Y0*exp(t/20) + 1))*(X0*Y0 + (X0*Y0*exp(t/20) - X0*Y0 + 1)/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Y0*exp(t/20) - 2) + ((mu*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*((Y0*Z0 - Y0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - Y0*Z0 + Y0*Z0*exp(t/20) + (Y0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2) + (X0*Y0*sin((pi*t)/10)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100'], 
['lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1) - (X0*Y0*sin((pi*t)/10)*(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100',
'0',
'((mu*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*(X0*Y0 + (X0*Y0*exp(t/20) - X0*Y0 + 1)/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Y0*exp(t/20) - 2) + lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*((Y0*Z0 - Y0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - Y0*Z0 + Y0*Z0*exp(t/20) + (Y0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2)'], 
['(X0*Y0*sin((pi*t)/10)*(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100 - lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)',
'0',
'- ((mu*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Y0*Z0 - Y0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*(X0*Y0 + (X0*Y0*exp(t/20) - X0*Y0 + 1)/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Y0*exp(t/20) - 2) - lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*((Y0*Z0 - Y0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - Y0*Z0 + Y0*Z0*exp(t/20) + (Y0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2)'], 
['0',
'lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1) - (X0*Y0*sin((pi*t)/10)*(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100',
'((mu*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*(X0*Y0 + (X0*Y0*exp(t/20) - X0*Y0 + 1)/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Y0*exp(t/20) - 2) + lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*((X0*Z0 - X0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Z0 + X0*Z0*exp(t/20) + (X0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2)'], 
['0',
'(X0*Y0*sin((pi*t)/10)*(X0*Y0*exp(t/20) - X0*Y0 + 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/100 - lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)',
'- ((mu*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1) - (lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*(X0*Z0 - X0*Z0*exp(t/20)))/(X0*Y0*exp(t/20) - X0*Y0 + 1))*(X0*Y0 + (X0*Y0*exp(t/20) - X0*Y0 + 1)/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Y0*exp(t/20) - 2) - lm*log(X0*Y0*exp(t/20) - X0*Y0 + 1)*((X0*Z0 - X0*Z0*exp(t/20))/(X0*Y0*(exp(t/20) - 1) + 1) - X0*Z0 + X0*Z0*exp(t/20) + (X0*(exp(t/20) - 1)*(Z0 - X0*Y0*Z0 + X0*Y0*Z0*exp(t/20)))/(X0*Y0*(exp(t/20) - 1) + 1)^2)']]
