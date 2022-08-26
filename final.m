A_cond = 0.01*0.08;
A_conv = 2*(0.01+0.09)*01;
p = 2*(0.01+0.09);
T = zeros(11,201);      % temp matrix
K = 200;                % thermal conductivity
rho = 3000;             % density
h = 2.5;                
T_a = 25.8;             % ambient temp
T_f = 20;               % fin tip temp at t=0
T_b = 50;               % base temp
c_p = 200;
m = rho*0.01*1*0.08;    % mass
c0 = -K*A_cond/(rho*A_cond*c_p);
c1 = h*p/(rho*A_cond*c_p);
del_t = 0.1;

del_x = 0.1;
t=200;             % total time 

for i = 2:11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
       T(i,1) = 50*exp(-del_x*i)+ 1.6*(del_x*i);    % equation at t=0;
end
for i=1:t
    T(1,i) = T_b;
end
p = 2;                  %  time
while(p<=t)
    for k = 2:11        %  node
        if(k==11)
            T(k,p) = T(k,p-1) + del_t*(c0/(del_x^2))*(T(k,p-1)-2*T(k-1,p-1)+T(k-2,p-1)) + del_t*c1*(T(k,p-1)-T_a);
        else
            T(k,p) = T(k,p-1) + del_t*(c0/(del_x^2))*(T(k-1,p-1)-2*T(k,p-1)+T(k+1,p-1)) + del_t*c1*(T(k,p-1)-T_a);
        end
    end
    p = p+1;
end

opm_len = 0;
error = 0.003;
for i=150:201
    for j = 1:11
        if(abs(T(j,i)-T_a) < error)
            opm_len = del_x*(j-1) ;
        end
    end
end

x = linspace(0,1,11);
 for i=1:t
    plot(x,T(:,i));
    hold on
 end
 legend('t=1','t=2','t=3','t=4','t=5','t=6')
 figure(2)
 plot(x,T(:,1));
 hold on
 plot(x,T(:,20));
 plot(x,T(:,50));
 plot(x,T(:,100));
 plot(x,T(:,150));
 plot(x,T(:,200));
 legend('t=0.1','t=2','t=5','t=10','t=15','t=20');